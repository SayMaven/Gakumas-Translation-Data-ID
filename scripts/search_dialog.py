#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gakumas Translation & Dialog Inspector & In-Place Editor
=========================================================
Alat bantu pencari teks dialog, penampil cerita (Story Viewer),
editor langsung (in-place editor), smart auto-wrap (maksimal 40 karakter),
dan inspeksi file lokalisasi Gakumas.

Fitur Unggulan:
  1. Cari kata/kalimat cepat di seluruh file ADV (.txt) dan JSON.
  2. Story Viewer: Buka seluruh percakapan kronologis dari berkas adv_*.txt
     (dialog message, narasi, dan semua pilihan respon choice).
  3. Buka GUI Desktop: Edit langsung dialog di text box & klik "Simpan" tanpa buka VS Code.
  4. Tombol "Auto-Wrap (<= 40)": Memotong baris kepanjangan secara cerdas pada spasi terdekat.
  5. Pengecekan batas karakter real-time & multi-line tag indexing support.
  6. Auto-wrap massal (batch) untuk merapikan file sekaligus.

Penggunaan CLI:
  python scripts/search_dialog.py -q "Misuzu telat"
  python scripts/search_dialog.py --overflow
  python scripts/search_dialog.py --gui
  python scripts/search_dialog.py --overflow --auto-wrap --file adv_csprt-3-0098
"""

import os
import sys
import re
import json
import argparse
import subprocess
from pathlib import Path

# Pastikan UTF-8 encoding untuk Windows terminal
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCE_DIR = BASE_DIR / "local-files" / "resource"
GENERIC_DIR = BASE_DIR / "local-files" / "genericTrans"
MASTER_DIR = BASE_DIR / "local-files" / "masterTrans"
LOCALIZATION_FILE = BASE_DIR / "local-files" / "localization.json"

MAX_SAFE_LINE_LENGTH = 40
MAX_SAFE_CHOICE_LENGTH = 18

RE_ADV_TAG = re.compile(
    r'\[(message|narration|choice)\s+text=(.*?)(?=(?:\s+(?:name|isInner|clip|lip|target|voice|speaker|se|fontSize|fade|speed|setting|selectAction)=|\]))',
    re.DOTALL
)
RE_NAME = re.compile(r'\s+name=([^\s\]]+)')
RE_CLEAN_TAGS = re.compile(r'<[^>]+>')

def clean_rich_text(text: str) -> str:
    """Menghapus tag Unity rich-text seperti <color=...> atau <size=...> untuk hitung panjang asli."""
    return RE_CLEAN_TAGS.sub('', text)

def wrap_unit_dialog(text: str) -> str:
    """
    Merapikan dialog khusus berkas adv_unit_*.txt agar MAKSIMAL 2 BARIS.
    Jika kalimat panjang, dipecah menjadi 2 baris seimbang di titik tengah spasi.
    """
    normalized = text.replace(r'\n', ' ').replace('\r\n', ' ').replace('\n', ' ')
    words = normalized.split()
    if not words:
        return text

    total_len = sum(len(clean_rich_text(w)) for w in words) + len(words) - 1
    if total_len <= 40:
        return " ".join(words)

    half = total_len / 2
    best_split = 1
    best_diff = float('inf')
    cur = 0
    for i in range(len(words) - 1):
        cur += len(clean_rich_text(words[i])) + (1 if i > 0 else 0)
        diff = abs(cur - half)
        if diff < best_diff:
            best_diff = diff
            best_split = i + 1

    l1 = " ".join(words[:best_split])
    l2 = " ".join(words[best_split:])
    return f"{l1}\n{l2}"

def smart_wrap_text(text: str, max_len: int = MAX_SAFE_LINE_LENGTH, is_unit: bool = False) -> str:
    """
    Memecah baris teks dialog secara cerdas pada spasi terdekat.
    Melakukan reflow penuh pada aliran kata agar baris berikutnya diisi maksimal
    dan tidak terpotong nanggung menjadi baris baru yang kosong/pendek.
    Jika is_unit=True, membatasi teks dialog maksimal 2 baris seimbang.
    """
    if is_unit:
        return wrap_unit_dialog(text)

    # Bersihkan escape \n dan satukan newline menjadi paragraf
    normalized = text.replace(r'\n', '\n').replace('\r\n', '\n').replace('\r', '\n')
    paragraphs = normalized.split('\n\n')
    wrapped_paragraphs = []

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        words = para.split()
        if not words:
            continue

        lines = []
        current_words = []
        current_len = 0

        for w in words:
            w_clean = clean_rich_text(w)
            w_len = len(w_clean)
            space_len = 1 if current_words else 0

            if current_len + space_len + w_len <= max_len:
                current_words.append(w)
                current_len += space_len + w_len
            else:
                if current_words:
                    lines.append(" ".join(current_words))
                current_words = [w]
                current_len = w_len

        if current_words:
            lines.append(" ".join(current_words))

        wrapped_paragraphs.append("\n".join(lines))

    return "\n".join(wrapped_paragraphs)

def save_adv_line(abs_path: str, line_idx: int, new_text: str, tag_index: int = 0):
    """
    Menyimpan pembaruan teks dialog ke berkas ADV .txt dengan menjaga:
    - LF newline (\n) murni
    - Escape literal \n di dalam tag text=
    - Dukungan tag_index jika dalam 1 baris ada beberapa tag (misal: beberapa choice)
    - Semua tag clip Unity, voice, dan actorlayout tetap utuh 100%.
    """
    with open(abs_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if line_idx < 1 or line_idx > len(lines):
        raise IndexError(f"Nomor baris {line_idx} di luar rentang berkas.")

    target_line = lines[line_idx - 1]
    matches = list(RE_ADV_TAG.finditer(target_line))
    if not matches:
        raise ValueError("Tag dialog tidak ditemukan pada baris target.")

    if tag_index >= len(matches):
        tag_index = 0

    match = matches[tag_index]

    normalized_text = new_text.strip().replace("\r\n", "\n").replace("\r", "\n")
    text_segments = [seg.strip() for seg in normalized_text.split("\n") if seg.strip()]
    escaped_text = r"\n".join(text_segments)

    # Ganti hanya bagian text=... pada tag yang sesuai
    new_line = target_line[:match.start(2)] + escaped_text + target_line[match.end(2):]

    # Validasi sintaks kurung siku dan kurung kurawal
    if new_line.count('[') != new_line.count(']') or new_line.count('{') != new_line.count('}'):
        raise ValueError("Gagal validasi sintaks: kurung [] atau {} tidak seimbang.")

    lines[line_idx - 1] = new_line

    with open(abs_path, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(lines)

    return escaped_text

def save_json_entry(abs_path: str, key_tokens: list, new_value: str):
    """
    Menyimpan pembaruan nilai teks ke berkas JSON dengan aman:
    - Menjaga encoding UTF-8
    - Format indentasi 2 spasi
    - Menjaga placeholder dan hierarki asli JSON
    - Menggunakan berkas sementara (.tmp) dan validasi json.load sebelum atomic replace.
    """
    with open(abs_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Navigasi ke node target
    curr = data
    for token in key_tokens[:-1]:
        curr = curr[token]

    curr[key_tokens[-1]] = new_value

    tmp_path = abs_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # Verifikasi integritas JSON hasil penyimpanan
    with open(tmp_path, "r", encoding="utf-8") as f:
        json.load(f)

    # Timpa berkas asli secara aman
    os.replace(tmp_path, abs_path)
    return new_value

def scan_file_issues(abs_path: str, max_len: int = MAX_SAFE_LINE_LENGTH):
    """Memindai seluruh baris dialog pada 1 berkas fisik dan mendeteksi apakah ada masalah layout."""
    issue_lines = []
    is_unit = Path(abs_path).name.startswith("adv_unit_")
    try:
        with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
            for idx, line in enumerate(f, 1):
                for match in RE_ADV_TAG.finditer(line):
                    raw_text = match.group(2)
                    tag_type = match.group(1)
                    cur_limit = MAX_SAFE_CHOICE_LENGTH if tag_type == "choice" else max_len

                    lines_in_dialog = [s for s in raw_text.split(r'\n') if s.strip()]
                    has_overflow = any(len(clean_rich_text(seg)) > cur_limit for seg in lines_in_dialog)
                    wrapped_sim = smart_wrap_text(raw_text, cur_limit, is_unit=is_unit)
                    opt_lines = [l for l in wrapped_sim.split('\n') if l.strip()]
                    can_compact = (len(lines_in_dialog) > 1 and len(opt_lines) < len(lines_in_dialog))
                    unit_over = (is_unit and len(lines_in_dialog) > 2)
                    if has_overflow or can_compact or unit_over:
                        issue_lines.append(idx)
                        break
    except Exception:
        pass
    return issue_lines

def wrap_entire_file(abs_path: str, max_len: int = MAX_SAFE_LINE_LENGTH):
    """
    Memindai dan merapikan SELURUH baris dialog pada satu berkas ADV (.txt)
    dari baris 1 sampai baris terakhir secara otomatis.
    """
    is_unit = Path(abs_path).name.startswith("adv_unit_")
    with open(abs_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    modified_count = 0
    new_lines = []

    for line_idx, line in enumerate(lines, 1):
        matches = list(RE_ADV_TAG.finditer(line))
        if not matches:
            new_lines.append(line)
            continue

        updated_line = line
        line_modified = False

        # Proses tag dari kanan ke kiri agar offset span tetap valid
        for match in reversed(matches):
            raw_text = match.group(2)
            tag_type = match.group(1)
            cur_limit = MAX_SAFE_CHOICE_LENGTH if tag_type == "choice" else max_len

            lines_in_dialog = [s for s in raw_text.split(r'\n') if s.strip()]
            has_overflow = any(len(clean_rich_text(seg)) > cur_limit for seg in lines_in_dialog)
            wrapped_sim = smart_wrap_text(raw_text, cur_limit, is_unit=is_unit)
            opt_lines = [l for l in wrapped_sim.split('\n') if l.strip()]
            can_compact = (len(lines_in_dialog) > 1 and len(opt_lines) < len(lines_in_dialog))
            unit_over = (is_unit and len(lines_in_dialog) > 2)

            if has_overflow or can_compact or unit_over:
                escaped_text = r"\n".join(opt_lines)
                updated_line = updated_line[:match.start(2)] + escaped_text + updated_line[match.end(2):]
                line_modified = True

        if line_modified and updated_line.count('[') == updated_line.count(']') and updated_line.count('{') == updated_line.count('}'):
            new_lines.append(updated_line)
            modified_count += 1
        else:
            new_lines.append(line)

    if modified_count > 0:
        with open(abs_path, "w", encoding="utf-8", newline="\n") as f:
            f.writelines(new_lines)

    return modified_count

def load_file_dialogs(abs_path: str, max_len: int = MAX_SAFE_LINE_LENGTH):
    """
    Membaca seluruh dialog kronologis dari SATU berkas ADV (.txt)
    Termasuk message, narration, dan choice.
    """
    results = []
    file_path = Path(abs_path)
    if not file_path.is_file():
        return results

    is_unit = file_path.name.startswith("adv_unit_")

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_idx, line in enumerate(f, 1):
                matches = list(RE_ADV_TAG.finditer(line))
                if not matches:
                    continue

                name_match = RE_NAME.search(line)
                default_speaker = name_match.group(1) if name_match else None

                for tag_idx, match in enumerate(matches):
                    tag_type = match.group(1)
                    raw_text = match.group(2)

                    if tag_type == "message":
                        speaker = default_speaker if default_speaker else "{user}"
                    elif tag_type == "narration":
                        speaker = "(Narasi)"
                    elif tag_type == "choice":
                        speaker = f"[Pilihan #{tag_idx+1}]" if len(matches) > 1 else "[Pilihan]"
                    else:
                        speaker = tag_type

                    cur_limit = MAX_SAFE_CHOICE_LENGTH if tag_type == "choice" else max_len

                    lines_in_dialog = raw_text.split(r'\n')
                    max_char_in_dialog = 0
                    has_overflow = False
                    line_details = []

                    for seg in lines_in_dialog:
                        clean_seg = clean_rich_text(seg)
                        seg_len = len(clean_seg)
                        if seg_len > max_char_in_dialog:
                            max_char_in_dialog = seg_len
                        if seg_len > cur_limit:
                            has_overflow = True
                        line_details.append((clean_seg, seg_len))

                    cur_lines = [s for s in lines_in_dialog if s.strip()]
                    cur_line_cnt = len(cur_lines)
                    wrapped_sim = smart_wrap_text(raw_text, cur_limit, is_unit=is_unit)
                    opt_lines = [l for l in wrapped_sim.split('\n') if l.strip()]
                    opt_line_cnt = len(opt_lines)
                    can_compact = (cur_line_cnt > 1 and opt_line_cnt < cur_line_cnt)
                    compact_info = f"{cur_line_cnt}➔{opt_line_cnt} baris" if can_compact else ""

                    unit_over_lines = (is_unit and cur_line_cnt > 2)

                    if tag_type == "choice":
                        if has_overflow:
                            status_str = f"⚠️ PILIHAN > 18 ch ({max_char_in_dialog} ch)"
                        else:
                            status_str = "OK [Choice]"
                    elif unit_over_lines and has_overflow:
                        status_str = f"⚠️ UNIT > 2 BARIS & OVERFLOW ({cur_line_cnt} baris)"
                    elif unit_over_lines:
                        status_str = f"⚠️ UNIT > 2 BARIS ({cur_line_cnt} baris, bentrok nama)"
                    elif has_overflow and can_compact:
                        status_str = f"⚠️ OVERFLOW & RAPATKAN ({compact_info})"
                    elif has_overflow:
                        status_str = "⚠️ OVERFLOW"
                    elif can_compact:
                        status_str = f"ℹ️ BISA DIRAPATKAN ({compact_info})"
                    else:
                        status_str = "OK"

                    results.append({
                        "file": file_path.name,
                        "rel_path": os.path.relpath(file_path, BASE_DIR),
                        "abs_path": str(file_path),
                        "line": line_idx,
                        "tag_idx": tag_idx,
                        "type": tag_type,
                        "speaker": speaker,
                        "text": raw_text,
                        "max_line_len": max_char_in_dialog,
                        "is_overflow": has_overflow,
                        "can_compact": can_compact,
                        "compact_info": compact_info,
                        "status_str": status_str,
                        "line_details": line_details,
                        "is_json": False
                    })
    except Exception:
        pass

    return results

def search_adv_files(query: str = "", actor_filter: str = "", overflow_only: bool = False, issue_filter: str = "all", max_len: int = MAX_SAFE_LINE_LENGTH, file_filter: str = ""):
    """Mencari dialog di file ADV resource/*.txt dan mendeteksi overflow serta baris yang bisa dirapatkan."""
    results = []
    if not RESOURCE_DIR.is_dir():
        return results

    if overflow_only and issue_filter == "all":
        issue_filter = "overflow"

    query_lower = query.lower() if query else ""
    actor_lower = actor_filter.lower() if actor_filter else ""
    file_lower = file_filter.lower() if file_filter else ""

    for entry in os.scandir(RESOURCE_DIR):
        if not entry.name.endswith(".txt"):
            continue
        if file_lower and file_lower not in entry.name.lower():
            continue

        file_path = entry.path
        is_unit = entry.name.startswith("adv_unit_")

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line_idx, line in enumerate(f, 1):
                    matches = list(RE_ADV_TAG.finditer(line))
                    if not matches:
                        continue

                    name_match = RE_NAME.search(line)
                    default_speaker = name_match.group(1) if name_match else None

                    for tag_idx, match in enumerate(matches):
                        tag_type = match.group(1)
                        raw_text = match.group(2)

                        if tag_type == "message":
                            speaker = default_speaker if default_speaker else "{user}"
                        elif tag_type == "narration":
                            speaker = "(Narasi)"
                        elif tag_type == "choice":
                            speaker = f"[Pilihan #{tag_idx+1}]" if len(matches) > 1 else "[Pilihan]"
                        else:
                            speaker = tag_type

                        if actor_lower and actor_lower not in speaker.lower():
                            continue

                        cur_limit = MAX_SAFE_CHOICE_LENGTH if tag_type == "choice" else max_len

                        lines_in_dialog = raw_text.split(r'\n')
                        max_char_in_dialog = 0
                        has_overflow = False

                        line_details = []
                        for seg in lines_in_dialog:
                            clean_seg = clean_rich_text(seg)
                            seg_len = len(clean_seg)
                            if seg_len > max_char_in_dialog:
                                max_char_in_dialog = seg_len
                            if seg_len > cur_limit:
                                has_overflow = True
                            line_details.append((clean_seg, seg_len))

                        cur_lines = [s for s in lines_in_dialog if s.strip()]
                        cur_line_cnt = len(cur_lines)
                        wrapped_sim = smart_wrap_text(raw_text, cur_limit, is_unit=is_unit)
                        opt_lines = [l for l in wrapped_sim.split('\n') if l.strip()]
                        opt_line_cnt = len(opt_lines)
                        can_compact = (cur_line_cnt > 1 and opt_line_cnt < cur_line_cnt)
                        compact_info = f"{cur_line_cnt}➔{opt_line_cnt} baris" if can_compact else ""

                        unit_over_lines = (is_unit and cur_line_cnt > 2)

                        if tag_type == "choice":
                            if has_overflow:
                                status_str = f"⚠️ PILIHAN > 18 ch ({max_char_in_dialog} ch)"
                            else:
                                status_str = "OK [Choice]"
                        elif unit_over_lines and has_overflow:
                            status_str = f"⚠️ UNIT > 2 BARIS & OVERFLOW ({cur_line_cnt} baris)"
                        elif unit_over_lines:
                            status_str = f"⚠️ UNIT > 2 BARIS ({cur_line_cnt} baris, bentrok nama)"
                        elif has_overflow and can_compact:
                            status_str = f"⚠️ OVERFLOW & RAPATKAN ({compact_info})"
                        elif has_overflow:
                            status_str = "⚠️ OVERFLOW"
                        elif can_compact:
                            status_str = f"ℹ️ BISA DIRAPATKAN ({compact_info})"
                        else:
                            status_str = "OK"

                        has_any_issue = (has_overflow or can_compact or unit_over_lines)
                        if issue_filter == "overflow" and not (has_overflow or unit_over_lines):
                            continue
                        elif issue_filter == "compact" and not can_compact:
                            continue
                        elif issue_filter in ("issues", "all_issues") and not has_any_issue:
                            continue

                        if query_lower:
                            if query_lower not in raw_text.lower() and query_lower not in speaker.lower():
                                continue

                        results.append({
                            "file": entry.name,
                            "rel_path": os.path.relpath(file_path, BASE_DIR),
                            "abs_path": file_path,
                            "line": line_idx,
                            "tag_idx": tag_idx,
                            "type": tag_type,
                            "speaker": speaker,
                            "text": raw_text,
                            "max_line_len": max_char_in_dialog,
                            "is_overflow": has_overflow,
                            "can_compact": can_compact,
                            "compact_info": compact_info,
                            "status_str": status_str,
                            "line_details": line_details,
                            "is_json": False
                        })
        except Exception:
            continue

    return results

def search_json_file(file_path: Path, query_lower: str):
    """Mencari string di dalam satu file JSON secara rekursif dan mencatat path token key."""
    matches = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)

        def walk(obj, key_tokens):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    walk(v, key_tokens + [k])
            elif isinstance(obj, list):
                for idx, v in enumerate(obj):
                    walk(v, key_tokens + [idx])
            elif isinstance(obj, str):
                if query_lower in obj.lower():
                    matches.append((key_tokens, obj))

        walk(data, [])
    except Exception:
        pass
    return matches

def search_json_files(query: str, file_filter: str = ""):
    """Mencari kata di seluruh JSON lokalisasi, master, dan generic."""
    results = []
    if not query:
        return results

    query_lower = query.lower()
    file_lower = file_filter.lower() if file_filter else ""

    candidates = []
    if LOCALIZATION_FILE.is_file():
        candidates.append(LOCALIZATION_FILE)

    for d in (GENERIC_DIR, MASTER_DIR):
        if d.is_dir():
            for p in d.rglob("*.json"):
                candidates.append(p)

    for p in candidates:
        if file_lower and file_lower not in p.name.lower():
            continue

        raw_matches = search_json_file(p, query_lower)
        for key_tokens, val in raw_matches:
            key_str = " -> ".join(str(k) for k in key_tokens)
            results.append({
                "file": p.name,
                "rel_path": os.path.relpath(p, BASE_DIR),
                "abs_path": str(p),
                "line": 0,
                "tag_idx": 0,
                "speaker": f"JSON ({key_tokens[-1]})" if key_tokens else "JSON",
                "text": val,
                "max_line_len": len(val),
                "is_overflow": False,
                "can_compact": False,
                "compact_info": "",
                "status_str": "JSON",
                "line_details": [(val, len(val))],
                "is_json": True,
                "key_tokens": key_tokens,
                "json_key_str": key_str
            })

    return results

def print_results(results, limit=MAX_SAFE_LINE_LENGTH):
    """Menampilkan hasil pencarian di terminal dengan format yang jelas dan terbaca."""
    if not results:
        print("\n🔍 Tidak ada hasil yang ditemukan.")
        return

    print(f"\nMenampilkan {len(results)} dialog:\n" + "=" * 80)
    for idx, r in enumerate(results, 1):
        rel = r.get("rel_path", r["file"])
        speaker = r["speaker"]
        max_c = r.get("max_line_len", 0)
        status_lbl = f" ⚠️ [OVERFLOW: {max_c} char > {limit}]" if r.get("is_overflow") else f" [Max: {max_c} char]"

        if r.get("is_json"):
            print(f"{idx}. 📁 {rel} -> {r.get('json_key_str')}")
            print(f"   Nilai: {r['text']}")
        else:
            line_no = r["line"]
            print(f"{idx}. 📁 {rel}:{line_no} [{speaker}]{status_lbl}")
            for l_idx, (seg, length) in enumerate(r.get("line_details", []), 1):
                over_flag = " ⚠️ [OVERFLOW]" if length > limit else ""
                print(f"   Baris {l_idx} ({length:2d} ch): {seg}{over_flag}")
        print()
    print("=" * 80)

def open_file_at_line(abs_path: str, line_no: int):
    """Membuka berkas langsung pada nomor baris di VS Code atau editor default sistem."""
    try:
        subprocess.run(["code", "-g", f"{abs_path}:{line_no}"], check=True)
    except Exception:
        try:
            if sys.platform.startswith("win"):
                os.startfile(abs_path)
            elif sys.platform.startswith("darwin"):
                subprocess.run(["open", abs_path])
            else:
                subprocess.run(["xdg-open", abs_path])
        except Exception as e:
            print(f"Tidak dapat membuka file: {e}")

def launch_gui():
    """Membuka GUI Desktop Tkinter dengan antarmuka pencarian, Story Viewer (Sidebar List) & In-Place Editor."""
    try:
        import tkinter as tk
        from tkinter import ttk, messagebox
    except ImportError:
        print("Error: Tkinter tidak tersedia di instalasi Python ini.")
        return

    root = tk.Tk()
    root.title("Gakumas Translation & Dialog Inspector & Story Editor")
    root.geometry("1200x780")
    root.minsize(950, 600)

    style = ttk.Style(root)
    style.theme_use('clam')

    # Top Control Panel (Search, Filter Masalah, Batas)
    top_frame = ttk.LabelFrame(root, text=" 🔍 Pencarian & Filter Dialog ", padding=6)
    top_frame.pack(fill="x", padx=10, pady=4)

    # Row 1: Pencarian Kata & Karakter
    row1 = ttk.Frame(top_frame)
    row1.pack(fill="x", pady=2)
    ttk.Label(row1, text="Kata / Kalimat:", width=13).pack(side="left")
    query_var = tk.StringVar()
    query_entry = ttk.Entry(row1, textvariable=query_var, width=32)
    query_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

    ttk.Label(row1, text="Karakter:").pack(side="left")
    actor_var = tk.StringVar()
    actor_entry = ttk.Entry(row1, textvariable=actor_var, width=12)
    actor_entry.pack(side="left", padx=(4, 10))

    ttk.Label(row1, text="Cakupan:").pack(side="left")
    target_var = tk.StringVar(value="all")
    ttk.Radiobutton(row1, text="Semua", variable=target_var, value="all").pack(side="left", padx=3)
    ttk.Radiobutton(row1, text="ADV", variable=target_var, value="adv").pack(side="left", padx=3)
    ttk.Radiobutton(row1, text="JSON", variable=target_var, value="json").pack(side="left", padx=3)

    # Row 2: Filter Masalah, Batas, dan Tombol Cari
    row2 = ttk.Frame(top_frame)
    row2.pack(fill="x", pady=2)

    ttk.Label(row2, text="Filter Masalah:", width=13).pack(side="left")
    issue_var = tk.StringVar(value="Semua Dialog")
    issue_combo = ttk.Combobox(row2, textvariable=issue_var, values=[
        "Semua Dialog",
        "⚠️ Hanya Overflow (> 40 ch)",
        "ℹ️ Hanya Bisa Dirapatkan",
        "⚠️ & ℹ️ Semua Masalah Layout"
    ], state="readonly", width=22)
    issue_combo.pack(side="left", padx=(0, 10))

    ttk.Label(row2, text="Batas:").pack(side="left")
    limit_var = tk.IntVar(value=MAX_SAFE_LINE_LENGTH)
    limit_spin = ttk.Spinbox(row2, from_=10, to=100, width=5, textvariable=limit_var)
    limit_spin.pack(side="left", padx=(4, 12))

    btn_search = ttk.Button(row2, text="🔍 Cari Dialog", width=13)
    btn_search.pack(side="left", padx=3)

    btn_scan_all = ttk.Button(row2, text="⚠️ Pindai Masalah", width=15)
    btn_scan_all.pack(side="left", padx=3)

    btn_batch_wrap = ttk.Button(row2, text="⚡ Auto-Wrap Massal", width=18)
    btn_batch_wrap.pack(side="left", padx=3)

    # Status Bar Atas
    status_var = tk.StringVar(value="Siap. Klik berkas pada daftar kiri untuk membuka dialog cerita, atau gunakan pencarian.")
    status_lbl = ttk.Label(root, textvariable=status_var, font=("Segoe UI", 9, "italic"))
    status_lbl.pack(fill="x", padx=12, pady=(0, 2))

    # Main Split Body (PanedWindow: Kiri = Daftar Berkas, Kanan = Tabel Dialog)
    main_paned = ttk.PanedWindow(root, orient="horizontal")
    main_paned.pack(fill="both", expand=True, padx=10, pady=2)

    # ------------------ PANEL KIRI: DAFTAR BERKAS TERSUSUN RAPI ------------------
    sidebar_frame = ttk.LabelFrame(main_paned, text=" 📂 Daftar Berkas Cerita ADV ", padding=6)
    main_paned.add(sidebar_frame, weight=1)

    # Filter Kategori Dropdown
    cat_row = ttk.Frame(sidebar_frame)
    cat_row.pack(fill="x", pady=(0, 4))
    ttk.Label(cat_row, text="Kategori:").pack(side="left")
    cat_var = tk.StringVar(value="Cerita Unit (adv_unit_*)")
    cat_combo = ttk.Combobox(cat_row, textvariable=cat_var, values=[
        "Cerita Unit (adv_unit_*)",
        "Cerita Keakraban Bond (adv_dear_*)",
        "Support Card (adv_csprt_*)",
        "Produce Story (adv_pstory_*)",
        "Event Story (adv_event_*)",
        "Semua Berkas ADV"
    ], state="readonly", width=24)
    cat_combo.pack(side="left", fill="x", expand=True, padx=(5, 0))

    # Search Box untuk daftar berkas
    search_file_row = ttk.Frame(sidebar_frame)
    search_file_row.pack(fill="x", pady=(0, 4))
    ttk.Label(search_file_row, text="Filter:").pack(side="left")
    sidebar_filter_var = tk.StringVar()
    sidebar_filter_entry = ttk.Entry(search_file_row, textvariable=sidebar_filter_var)
    sidebar_filter_entry.pack(side="left", fill="x", expand=True, padx=(5, 0))

    # Listbox daftar berkas dengan scrollbar
    file_list_container = ttk.Frame(sidebar_frame)
    file_list_container.pack(fill="both", expand=True)

    file_listbox = tk.Listbox(file_list_container, selectmode="browse", font=("Consolas", 9), exportselection=False)
    file_scroll_y = ttk.Scrollbar(file_list_container, orient="vertical", command=file_listbox.yview)
    file_listbox.configure(yscrollcommand=file_scroll_y.set)

    file_listbox.pack(side="left", fill="both", expand=True)
    file_scroll_y.pack(side="right", fill="y")

    lbl_file_count = ttk.Label(sidebar_frame, text="", font=("Segoe UI", 8))
    lbl_file_count.pack(anchor="w", pady=(2, 0))

    # ------------------ PANEL KANAN: TABEL DIALOG CERITA ------------------
    content_frame = ttk.Frame(main_paned)
    main_paned.add(content_frame, weight=3)

    cols = ("file", "line", "speaker", "len", "status", "text")
    tree = ttk.Treeview(content_frame, columns=cols, show="headings", selectmode="browse")
    tree.heading("file", text="Nama Berkas")
    tree.heading("line", text="Baris")
    tree.heading("speaker", text="Karakter / Tipe")
    tree.heading("len", text="Max Karakter")
    tree.heading("status", text="Status Layout")
    tree.heading("text", text="Isi Dialog")

    tree.column("file", width=170, anchor="w")
    tree.column("line", width=50, anchor="center")
    tree.column("speaker", width=110, anchor="w")
    tree.column("len", width=90, anchor="center")
    tree.column("status", width=190, anchor="center")
    tree.column("text", width=360, anchor="w")

    tree_scroll_y = ttk.Scrollbar(content_frame, orient="vertical", command=tree.yview)
    tree_scroll_x = ttk.Scrollbar(content_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)

    tree.grid(row=0, column=0, sticky="nsew")
    tree_scroll_y.grid(row=0, column=1, sticky="ns")
    tree_scroll_x.grid(row=1, column=0, sticky="ew")
    content_frame.rowconfigure(0, weight=1)
    content_frame.columnconfigure(0, weight=1)

    # ------------------ IN-PLACE EDITOR DI BAWAH ------------------
    editor_frame = ttk.LabelFrame(root, text=" 📝 Editor Dialog Langsung (In-Place Editor) ", padding=8)
    editor_frame.pack(fill="x", padx=10, pady=(2, 8))

    info_row = ttk.Frame(editor_frame)
    info_row.pack(fill="x", pady=(0, 4))

    lbl_file_info = ttk.Label(info_row, text="Pilih dialog pada tabel untuk mulai mengedit.", font=("Segoe UI", 9, "bold"))
    lbl_file_info.pack(side="left")

    lbl_counter = ttk.Label(info_row, text="", font=("Segoe UI", 9))
    lbl_counter.pack(side="right")

    edit_box_row = ttk.Frame(editor_frame)
    edit_box_row.pack(fill="x")

    text_editor = tk.Text(edit_box_row, height=5, wrap="word", font=("Consolas", 10))
    text_editor.pack(side="left", fill="x", expand=True, padx=(0, 10))

    btn_box = ttk.Frame(edit_box_row)
    btn_box.pack(side="right", fill="y")

    btn_auto_wrap = ttk.Button(btn_box, text="⚡ Auto-Wrap Baris Ini", width=22)
    btn_auto_wrap.pack(fill="x", pady=2)

    btn_wrap_file = ttk.Button(btn_box, text="⚡ Auto-Wrap 1 Berkas Ini", width=22)
    btn_wrap_file.pack(fill="x", pady=2)

    btn_save = ttk.Button(btn_box, text="💾 Simpan (Save)", width=22)
    btn_save.pack(fill="x", pady=2)

    btn_open = ttk.Button(btn_box, text="📂 Buka di Editor", width=22)
    btn_open.pack(fill="x", pady=2)

    current_data = []
    all_adv_files = []
    if RESOURCE_DIR.is_dir():
        all_adv_files = sorted([f.name for f in RESOURCE_DIR.iterdir() if f.name.endswith(".txt")])

    displayed_files = []

    def refresh_file_list(*args):
        nonlocal displayed_files
        cat = cat_var.get()
        flt = sidebar_filter_var.get().strip().lower()

        filtered = []
        for fn in all_adv_files:
            if cat == "Cerita Unit (adv_unit_*)":
                if not fn.startswith("adv_unit_"):
                    continue
            elif cat == "Cerita Keakraban Bond (adv_dear_*)":
                if not fn.startswith("adv_dear_"):
                    continue
            elif cat == "Support Card (adv_csprt_*)":
                if not fn.startswith("adv_csprt-"):
                    continue
            elif cat == "Produce Story (adv_pstory_*)":
                if not fn.startswith("adv_pstory_"):
                    continue
            elif cat == "Event Story (adv_event_*)":
                if not (fn.startswith("adv_event_") or fn.startswith("adv_pevent_")):
                    continue

            if flt and flt not in fn.lower():
                continue

            filtered.append(fn)

        displayed_files = filtered
        file_listbox.delete(0, "end")
        for fn in displayed_files:
            file_listbox.insert("end", fn)

        lbl_file_count.config(text=f"Total: {len(displayed_files)} berkas")

    cat_combo.bind("<<ComboboxSelected>>", refresh_file_list)
    sidebar_filter_var.trace_add("write", refresh_file_list)

    def on_file_selected(event=None):
        sel = file_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        if idx >= len(displayed_files):
            return
        fn = displayed_files[idx]
        target_path = RESOURCE_DIR / fn
        if not target_path.is_file():
            return

        status_var.set(f"Memuat dialog dari {fn}...")
        root.update_idletasks()
        results = load_file_dialogs(str(target_path), limit_var.get())
        populate_tree(results)
        status_var.set(f"📖 Berkas aktif: {fn} ({len(results)} dialog & pilihan).")

    file_listbox.bind("<<ListboxSelect>>", on_file_selected)

    def update_char_counter(event=None):
        content = text_editor.get("1.0", "end-1c")
        if not content.strip():
            lbl_counter.config(text="")
            return

        lines = content.split('\n')
        counts = []
        has_over = False

        selected_items = tree.selection()
        is_choice = False
        is_unit_file = False
        if selected_items:
            s_idx = tree.index(selected_items[0])
            if s_idx < len(current_data):
                cur_item = current_data[s_idx]
                is_choice = (cur_item.get('type') == 'choice')
                is_unit_file = cur_item.get('file', '').startswith('adv_unit_')

        active_limit = MAX_SAFE_CHOICE_LENGTH if is_choice else limit_var.get()

        for idx, l in enumerate(lines, 1):
            cl = clean_rich_text(l.strip())
            c_len = len(cl)
            if c_len > active_limit:
                has_over = True
                counts.append(f"B{idx}:{c_len}⚠️")
            else:
                counts.append(f"B{idx}:{c_len}")
        summary = " | ".join(counts)

        cur_cnt = len([l for l in lines if l.strip()])
        wrapped = smart_wrap_text(content, active_limit, is_unit=is_unit_file)
        opt_cnt = len([l for l in wrapped.split('\n') if l.strip()])
        compact_note = f" | ℹ️ Bisa dirapatkan ({cur_cnt}➔{opt_cnt} baris)" if cur_cnt > 1 and opt_cnt < cur_cnt else ""

        unit_warn = ""
        if is_unit_file and cur_cnt > 2:
            has_over = True
            unit_warn = f" | ⚠️ UNIT MAKS 2 BARIS! ({cur_cnt} baris - bentrok nama)"

        choice_note = " (Pilihan: Maks 18 ch)" if is_choice else f" (Maks {active_limit} ch)"

        if has_over:
            lbl_counter.config(text=f"{summary}{choice_note}{compact_note}{unit_warn}", foreground="#B00020")
        elif compact_note:
            lbl_counter.config(text=f"{summary}{compact_note}{unit_warn}", foreground="#8A6D3B")
        else:
            lbl_counter.config(text=f"{summary} (Aman <= {active_limit}){unit_warn}", foreground="#007700")

    def populate_tree(results):
        nonlocal current_data
        current_data = results
        for row in tree.get_children():
            tree.delete(row)

        for idx, r in enumerate(results):
            status = r.get("status_str", "OK")
            display_text = r['text'].replace(r'\n', ' ↵ ')
            item_id = tree.insert("", "end", values=(
                r['file'],
                r['line'] if r['line'] else "-",
                r['speaker'],
                f"{r.get('max_line_len', 0)} ch",
                status,
                display_text
            ))
            if "UNIT > 2 BARIS" in status:
                tree.item(item_id, tags=("unit_overflow",))
            elif "PILIHAN > 18" in status or (r.get("is_overflow") and r.get("type") == "choice"):
                tree.item(item_id, tags=("choice_overflow",))
            elif r.get("is_overflow") and r.get("can_compact"):
                tree.item(item_id, tags=("both",))
            elif r.get("is_overflow"):
                tree.item(item_id, tags=("overflow",))
            elif r.get("can_compact"):
                tree.item(item_id, tags=("compact",))

        tree.tag_configure("unit_overflow", background="#FFE6E6", foreground="#CC0000")
        tree.tag_configure("choice_overflow", background="#FFEFEB", foreground="#B34700")
        tree.tag_configure("overflow", background="#FFF2F2", foreground="#B00020")
        tree.tag_configure("compact", background="#FFFBE6", foreground="#8A6D3B")
        tree.tag_configure("both", background="#FFE6E6", foreground="#990000")
        status_var.set(f"Selesai: Ditemukan {len(results)} entri.")

    def perform_search(overflow_mode=False):
        q = query_var.get().strip()
        act = actor_var.get().strip()
        t = target_var.get()
        lim = limit_var.get()

        iv = issue_var.get()
        if overflow_mode:
            issue_flt = "issues"
        elif "Overflow" in iv:
            issue_flt = "overflow"
        elif "Dirapatkan" in iv:
            issue_flt = "compact"
        elif "Semua Masalah" in iv:
            issue_flt = "issues"
        else:
            issue_flt = "all"

        if not q and issue_flt == "all" and not act:
            messagebox.showinfo("Petunjuk", "Masukkan kata pencarian, filter karakter, atau pilih Filter Masalah.")
            return

        status_var.set("Sedang memindai berkas, mohon tunggu...")
        root.update_idletasks()

        results = []
        if t in ("all", "adv"):
            results.extend(search_adv_files(query=q, actor_filter=act, issue_filter=issue_flt, max_len=lim))
        if t in ("all", "json") and issue_flt == "all":
            results.extend(search_json_files(query=q))

        populate_tree(results)

    def on_select(event):
        selected_items = tree.selection()
        if not selected_items:
            return
        idx = tree.index(selected_items[0])
        if idx < len(current_data):
            r = current_data[idx]
            if r.get('is_json'):
                lbl_file_info.config(text=f"📁 {r['rel_path']} — Key: {r.get('json_key_str', '-')} ({r['speaker']})")
            else:
                tag_label = f"[{r.get('type')}]" if r.get('type') != 'message' else ""
                lbl_file_info.config(text=f"📁 {r['rel_path']} (Baris {r['line']}) — Pembicara: {r['speaker']} {tag_label}")
            text_editor.delete("1.0", "end")
            multiline_text = r['text'].replace(r'\n', '\n')
            text_editor.insert("1.0", multiline_text)
            update_char_counter()

    def on_auto_wrap_single():
        selected_items = tree.selection()
        is_unit_file = False
        is_choice = False
        if selected_items:
            idx = tree.index(selected_items[0])
            if idx < len(current_data):
                r = current_data[idx]
                if r.get('is_json') or r.get('line', 0) == 0 or r.get('file', '').endswith('.json'):
                    messagebox.showinfo("Info", "Fitur auto-wrap dikhususkan untuk dialog cerita ADV (.txt).\nBerkas JSON UI/Master tidak menggunakan auto-wrap.")
                    return
                is_unit_file = r.get('file', '').startswith('adv_unit_')
                is_choice = (r.get('type') == 'choice')

        content = text_editor.get("1.0", "end-1c")
        if not content.strip():
            return

        cur_limit = MAX_SAFE_CHOICE_LENGTH if is_choice else limit_var.get()
        wrapped = smart_wrap_text(content, cur_limit, is_unit=is_unit_file)
        text_editor.delete("1.0", "end")
        text_editor.insert("1.0", wrapped)
        update_char_counter()
        status_var.set("Teks telah di-wrap otomatis. Klik 'Simpan' untuk memperbarui berkas.")

    def on_wrap_file_click():
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showwarning("Peringatan", "Pilih salah satu baris dari berkas yang ingin di-wrap terlebih dahulu.")
            return
        idx = tree.index(selected_items[0])
        if idx >= len(current_data):
            return
        r = current_data[idx]
        target_file = r['file']
        abs_path = r['abs_path']

        if r.get('is_json') or r.get('line', 0) == 0 or target_file.endswith('.json'):
            messagebox.showinfo("Info", f"Fitur auto-wrap 1 berkas dikhususkan untuk berkas cerita ADV (.txt).\nBerkas JSON ({target_file}) aman dan tidak menggunakan auto-wrap.")
            return

        issue_lines = scan_file_issues(abs_path, limit_var.get())
        if not issue_lines:
            messagebox.showinfo("Info", f"Seluruh baris dialog pada berkas {target_file} sudah rapi dan aman (tidak ada masalah layout)!")
            return

        confirm = messagebox.askyesno(
            "Konfirmasi Auto-Wrap Seluruh Berkas",
            f"Ditemukan {len(issue_lines)} dialog bermasalah di seluruh berkas:\n{target_file}\n\n"
            f"Apakah Anda ingin auto-wrap SEMUA {len(issue_lines)} dialog di berkas ini sekarang?"
        )
        if not confirm:
            return

        modified_count = wrap_entire_file(abs_path, limit_var.get())

        # Segarkan tabel dialog berkas aktif jika sesuai
        sel_list = file_listbox.curselection()
        if sel_list and displayed_files[sel_list[0]] == target_file:
            on_file_selected()
        else:
            try:
                with open(abs_path, "r", encoding="utf-8") as f:
                    all_file_lines = f.readlines()
                for item in current_data:
                    if item.get('file') == target_file and item.get('line', 0) > 0:
                        l_idx = item['line'] - 1
                        if 0 <= l_idx < len(all_file_lines):
                            matches = list(RE_ADV_TAG.finditer(all_file_lines[l_idx]))
                            t_idx = item.get('tag_idx', 0)
                            if t_idx < len(matches):
                                m = matches[t_idx]
                                new_t = m.group(2)
                                item['text'] = new_t
                                lines = new_t.split(r'\n')
                                max_c = max(len(clean_rich_text(l)) for l in lines) if lines else 0
                                item['max_line_len'] = max_c

                                c_lim = MAX_SAFE_CHOICE_LENGTH if item.get('type') == 'choice' else limit_var.get()
                                item['is_overflow'] = max_c > c_lim

                                cur_l = [l for l in lines if l.strip()]
                                cur_cnt = len(cur_l)
                                w_sim = smart_wrap_text(new_t, c_lim)
                                opt_cnt = len([l for l in w_sim.split('\n') if l.strip()])
                                can_comp = (cur_cnt > 1 and opt_cnt < cur_cnt)
                                comp_info = f"{cur_cnt}➔{opt_cnt} baris" if can_comp else ""
                                item['can_compact'] = can_comp
                                item['compact_info'] = comp_info

                                if item.get('type') == 'choice':
                                    st = f"⚠️ PILIHAN > 18 ch ({max_c} ch)" if item['is_overflow'] else "OK [Choice]"
                                elif item['is_overflow'] and can_comp:
                                    st = f"⚠️ OVERFLOW & RAPATKAN ({comp_info})"
                                elif item['is_overflow']:
                                    st = "⚠️ OVERFLOW"
                                elif can_comp:
                                    st = f"ℹ️ BISA DIRAPATKAN ({comp_info})"
                                else:
                                    st = "OK"
                                item['status_str'] = st
                populate_tree(current_data)
            except Exception:
                pass

        messagebox.showinfo("Selesai", f"Berhasil merapikan {modified_count} baris dialog pada {target_file}!")
        status_var.set(f"✅ Auto-wrap selesai: {modified_count} baris diperbarui pada {target_file}.")

    def on_save_click():
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Pilih baris pada tabel terlebih dahulu sebelum menyimpan.")
            return

        idx = tree.index(selected_items[0])
        if idx >= len(current_data):
            return

        r = current_data[idx]
        new_content = text_editor.get("1.0", "end-1c")

        if r.get("is_json"):
            if not r.get("key_tokens"):
                messagebox.showerror("Error", "Key JSON tidak dapat ditentukan untuk penyimpanan otomatis.")
                return
            try:
                save_json_entry(r['abs_path'], r['key_tokens'], new_content)
                r['text'] = new_content
                r['max_line_len'] = len(new_content)
                disp = new_content.replace('\n', ' ↵ ')
                tree.item(selected_items[0], values=(
                    r['file'],
                    "-",
                    r['speaker'],
                    f"{len(new_content)} ch",
                    "OK",
                    disp
                ))
                update_char_counter()
                messagebox.showinfo("Sukses", f"Perubahan berhasil disimpan ke berkas JSON:\n{r['file']}\n\nKey: {r.get('json_key_str')}")
                status_var.set(f"✅ Berkas JSON {r['file']} berhasil diperbarui!")
            except Exception as err:
                messagebox.showerror("Gagal Simpan JSON", f"Terjadi kesalahan saat menyimpan berkas JSON:\n{err}")
            return

        if r['line'] == 0:
            messagebox.showinfo("Info", "Penyuntingan langsung saat ini dikhususkan untuk berkas cerita ADV (.txt) dan JSON yang valid.")
            return

        try:
            t_idx = r.get('tag_idx', 0)
            escaped_text = save_adv_line(r['abs_path'], r['line'], new_content, tag_index=t_idx)
            r['text'] = escaped_text
            lines = escaped_text.split(r'\n')
            max_c = max(len(clean_rich_text(l)) for l in lines) if lines else 0
            r['max_line_len'] = max_c

            c_lim = MAX_SAFE_CHOICE_LENGTH if r.get('type') == 'choice' else limit_var.get()
            r['is_overflow'] = max_c > c_lim

            cur_l = [l for l in lines if l.strip()]
            cur_cnt = len(cur_l)
            w_sim = smart_wrap_text(escaped_text, c_lim)
            opt_cnt = len([l for l in w_sim.split('\n') if l.strip()])
            can_comp = (cur_cnt > 1 and opt_cnt < cur_cnt)
            comp_info = f"{cur_cnt}➔{opt_cnt} baris" if can_comp else ""
            r['can_compact'] = can_comp
            r['compact_info'] = comp_info

            if r.get('type') == 'choice':
                st = f"⚠️ PILIHAN > 18 ch ({max_c} ch)" if r['is_overflow'] else "OK [Choice]"
            elif r['is_overflow'] and can_comp:
                st = f"⚠️ OVERFLOW & RAPATKAN ({comp_info})"
            elif r['is_overflow']:
                st = "⚠️ OVERFLOW"
            elif can_comp:
                st = f"ℹ️ BISA DIRAPATKAN ({comp_info})"
            else:
                st = "OK"
            r['status_str'] = st

            disp = escaped_text.replace(r'\n', ' ↵ ')
            tree.item(selected_items[0], values=(
                r['file'],
                r['line'],
                r['speaker'],
                f"{max_c} ch",
                st,
                disp
            ))
            if r.get('type') == 'choice' and r['is_overflow']:
                tree.item(selected_items[0], tags=("choice_overflow",))
            elif r['is_overflow'] and can_comp:
                tree.item(selected_items[0], tags=("both",))
            elif r['is_overflow']:
                tree.item(selected_items[0], tags=("overflow",))
            elif can_comp:
                tree.item(selected_items[0], tags=("compact",))
            else:
                tree.item(selected_items[0], tags=())

            update_char_counter()
            status_var.set(f"✅ Berhasil disimpan ke {r['file']} (Baris {r['line']})!")
        except Exception as err:
            messagebox.showerror("Gagal Menyimpan", f"Terjadi kesalahan saat menyimpan: {err}")

    def on_batch_wrap():
        if not current_data:
            messagebox.showinfo("Info", "Tidak ada hasil pencarian untuk di-wrap.")
            return

        adv_items = [r for r in current_data if r.get('line', 0) > 0 and (r.get('is_overflow') or r.get('can_compact'))]
        if not adv_items:
            messagebox.showinfo("Info", "Tidak ada dialog ADV yang bermasalah pada daftar ini.")
            return

        confirm = messagebox.askyesno(
            "Konfirmasi Auto-Wrap Massal",
            f"Ditemukan {len(adv_items)} dialog yang bisa dirapikan (batas: {limit_var.get()} karakter).\n\n"
            "Apakah Anda yakin ingin melakukan auto-wrap dan menyimpan perubahannya sekarang?"
        )
        if not confirm:
            return

        success_count = 0
        status_var.set("Memproses auto-wrap massal...")
        root.update_idletasks()

        for r in adv_items:
            try:
                c_lim = MAX_SAFE_CHOICE_LENGTH if r.get('type') == 'choice' else limit_var.get()
                wrapped = smart_wrap_text(r['text'], c_lim)
                escaped = save_adv_line(r['abs_path'], r['line'], wrapped, tag_index=r.get('tag_idx', 0))
                r['text'] = escaped
                lines = escaped.split(r'\n')
                max_c = max(len(clean_rich_text(l)) for l in lines) if lines else 0
                r['max_line_len'] = max_c
                r['is_overflow'] = max_c > c_lim

                cur_l = [l for l in lines if l.strip()]
                cur_cnt = len(cur_l)
                w_sim = smart_wrap_text(escaped, c_lim)
                opt_cnt = len([l for l in w_sim.split('\n') if l.strip()])
                can_comp = (cur_cnt > 1 and opt_cnt < cur_cnt)
                comp_info = f"{cur_cnt}➔{opt_cnt} baris" if can_comp else ""
                r['can_compact'] = can_comp
                r['compact_info'] = comp_info

                if r.get('type') == 'choice':
                    st = f"⚠️ PILIHAN > 18 ch ({max_c} ch)" if r['is_overflow'] else "OK [Choice]"
                elif r['is_overflow'] and can_comp:
                    st = f"⚠️ OVERFLOW & RAPATKAN ({comp_info})"
                elif r['is_overflow']:
                    st = "⚠️ OVERFLOW"
                elif can_comp:
                    st = f"ℹ️ BISA DIRAPATKAN ({comp_info})"
                else:
                    st = "OK"
                r['status_str'] = st
                success_count += 1
            except Exception:
                continue

        populate_tree(current_data)
        messagebox.showinfo("Selesai", f"Berhasil melakukan auto-wrap pada {success_count} dialog!")
        status_var.set(f"Auto-wrap massal selesai ({success_count} dialog diperbarui).")

    def on_open_click():
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Pilih baris pada tabel terlebih dahulu.")
            return
        idx = tree.index(selected_items[0])
        if idx < len(current_data):
            r = current_data[idx]
            open_file_at_line(r['abs_path'], r['line'])

    btn_search.configure(command=lambda: perform_search(False))
    btn_scan_all.configure(command=lambda: perform_search(True))
    btn_batch_wrap.configure(command=on_batch_wrap)
    btn_auto_wrap.configure(command=on_auto_wrap_single)
    btn_wrap_file.configure(command=on_wrap_file_click)
    btn_save.configure(command=on_save_click)
    btn_open.configure(command=on_open_click)

    limit_var.trace_add("write", lambda *args: update_char_counter())

    tree.bind("<<TreeviewSelect>>", on_select)
    tree.bind("<Double-1>", lambda e: on_open_click())
    query_entry.bind("<Return>", lambda e: perform_search(False))
    text_editor.bind("<KeyRelease>", update_char_counter)

    # Inisialisasi daftar berkas pertama kali
    refresh_file_list()

    # Pilih berkas pertama secara otomatis agar langsung muncul dialognya
    if displayed_files:
        file_listbox.selection_set(0)
        on_file_selected()

    root.mainloop()


def batch_wrap_cli(results, limit=MAX_SAFE_LINE_LENGTH):
    """Menjalankan auto-wrap massal dari CLI."""
    adv_items = [r for r in results if r.get('line', 0) > 0 and r.get('is_overflow')]
    if not adv_items:
        print("Tidak ada dialog yang perlu di-wrap.")
        return

    print(f"\nMemulai auto-wrap massal pada {len(adv_items)} dialog (batas: {limit} karakter)...")
    success = 0
    for r in adv_items:
        try:
            c_lim = MAX_SAFE_CHOICE_LENGTH if r.get('type') == 'choice' else limit
            wrapped = smart_wrap_text(r['text'], c_lim)
            save_adv_line(r['abs_path'], r['line'], wrapped, tag_index=r.get('tag_idx', 0))
            success += 1
        except Exception as e:
            print(f"Error pada {r['file']}:{r['line']} -> {e}")

    print(f"✅ Berhasil meng-update {success} dari {len(adv_items)} dialog!")

def interactive_cli():
    """Mode prompt interaktif di terminal saat dijalankan tanpa argumen."""
    print("=" * 60)
    print("      Gakumas Translation & Dialog Inspector Tool")
    print("=" * 60)
    print("[1] Cari kata / kalimat spesifik")
    print("[2] Pindai dialog kepanjangan (> 40 karakter)")
    print("[3] Buka Tampilan Desktop (GUI dengan Story Viewer & Editor)")
    print("[0] Keluar")
    print("=" * 60)

    try:
        pilihan = input("Pilih menu [1-3, 0]: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nKeluar.")
        return

    if pilihan == "1":
        q = input("Ketik kata / kalimat yang dicari: ").strip()
        if not q:
            print("Kata kunci kosong.")
            return
        act = input("Filter karakter (opsional, tekan Enter untuk lewati): ").strip()
        print("\nSedang mencari...")
        res_adv = search_adv_files(query=q, actor_filter=act)
        res_json = search_json_files(query=q)
        print_results(res_adv + res_json)
    elif pilihan == "2":
        lim_str = input(f"Batas karakter [default {MAX_SAFE_LINE_LENGTH}]: ").strip()
        lim = int(lim_str) if lim_str.isdigit() else MAX_SAFE_LINE_LENGTH
        act = input("Filter karakter (opsional, tekan Enter untuk lewati): ").strip()
        print(f"\nMemindai seluruh berkas ADV untuk baris > {lim} karakter...")
        res = search_adv_files(actor_filter=act, overflow_only=True, max_len=lim)
        print_results(res, limit=lim)
        if res:
            wrap_confirm = input("\nApakah ingin auto-wrap semua dialog ini sekarang? (y/N): ").strip().lower()
            if wrap_confirm == 'y':
                batch_wrap_cli(res, limit=lim)
    elif pilihan == "3":
        print("Membuka tampilan GUI...")
        launch_gui()
    elif pilihan == "0":
        print("Sampai jumpa!")
    else:
        print("Pilihan tidak valid.")

def main():
    parser = argparse.ArgumentParser(
        description="Gakumas Translation Inspector, Search & In-Place Editor Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-q", "--query", type=str, default="", help="Kata atau kalimat yang ingin dicari")
    parser.add_argument("-a", "--actor", type=str, default="", help="Filter nama karakter (misal: Sena, Misuzu)")
    parser.add_argument("-t", "--target", choices=["all", "adv", "json"], default="all", help="Cakupan berkas (default: all)")
    parser.add_argument("-o", "--overflow", action="store_true", help="Hanya tampilkan dialog yang melebihi batas karakter")
    parser.add_argument("-l", "--limit", type=int, default=MAX_SAFE_LINE_LENGTH, help=f"Batas karakter per baris (default: {MAX_SAFE_LINE_LENGTH})")
    parser.add_argument("-f", "--file", type=str, default="", help="Filter nama berkas (misal: *csprt*)")
    parser.add_argument("--auto-wrap", action="store_true", help="Jalankan smart auto-wrap otomatis pada hasil")
    parser.add_argument("--gui", action="store_true", help="Jalankan dalam mode antarmuka grafis desktop (Tkinter)")

    args = parser.parse_args()

    if args.gui:
        launch_gui()
        return

    if len(sys.argv) == 1:
        interactive_cli()
        return

    results = []
    if args.target in ("all", "adv"):
        results.extend(search_adv_files(
            query=args.query,
            actor_filter=args.actor,
            overflow_only=args.overflow,
            max_len=args.limit,
            file_filter=args.file
        ))

    if args.target in ("all", "json") and not args.overflow:
        results.extend(search_json_files(query=args.query, file_filter=args.file))

    print_results(results, limit=args.limit)

    if args.auto_wrap and results:
        batch_wrap_cli(results, limit=args.limit)

if __name__ == "__main__":
    main()
