#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/update_translation.py
Memperbarui file terjemahan (seperti local-files/localization.json) secara presisi
berdasarkan batch terjemahan JSON tanpa mengubah urutan key, menambah/menghapus key,
atau merusak struktur formatting.
"""

import argparse
import json
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


def extract_placeholders(text):
    """Mengekstrak placeholder seperti {0}, {1}, {0:N0} dari teks."""
    return sorted(re.findall(r'\{[0-9a-zA-Z_:]+\}', text))


def update_translation(target_path, input_path, dry_run=False):
    if not os.path.exists(target_path):
        print(f"Error: Target file '{target_path}' tidak ditemukan.", file=sys.stderr)
        return False
    if not os.path.exists(input_path):
        print(f"Error: Input batch file '{input_path}' tidak ditemukan.", file=sys.stderr)
        return False
    with open(target_path, 'r', encoding='utf-8') as f:
        try:
            target_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Gagal mem-parse target JSON: {e}", file=sys.stderr)
            return False
    with open(input_path, 'r', encoding='utf-8') as f:
        try:
            batch_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Gagal mem-parse batch JSON: {e}", file=sys.stderr)
            return False
    if not isinstance(batch_data, dict):
        print("Error: Format batch JSON harus berupa objek { key: value }.", file=sys.stderr)
        return False

    updated_count = 0
    skipped_identical_count = 0
    unknown_keys = []
    placeholder_warnings = []

    for key, new_val in batch_data.items():
        if key not in target_data:
            unknown_keys.append(key)
            continue
        orig_val = target_data[key]

        if orig_val == new_val:
            skipped_identical_count += 1
            continue
        orig_ph = extract_placeholders(orig_val)
        new_ph = extract_placeholders(new_val)
        if orig_ph != new_ph:
            placeholder_warnings.append((key, orig_ph, new_ph))
        target_data[key] = new_val
        updated_count += 1
    print("=" * 60)
    print("LAPORAN UPDATE TERJEMAHAN")
    print("=" * 60)
    print(f"Target Berkas       : {target_path}")
    print(f"Batch Input         : {input_path}")
    print(f"Total Key di Batch  : {len(batch_data)}")
    print(f"Key Diperbarui      : {updated_count}")
    print(f"Key Dilewati (Sama) : {skipped_identical_count}")

    if unknown_keys:
        print(f"\n[PERINGATAN] {len(unknown_keys)} key tidak ditemukan di target (diabaikan):")
        for k in unknown_keys[:10]:
            print(f"  - {k}")
        if len(unknown_keys) > 10:
            print(f"  ... dan {len(unknown_keys) - 10} key lainnya.")

    if placeholder_warnings:
        print(f"\n[PERINGATAN PLACEHOLDER] {len(placeholder_warnings)} key memiliki perbedaan placeholder:")
        for k, o, n in placeholder_warnings[:10]:
            print(f"  - Key: {k}")
            print(f"    Asli : {o}")
            print(f"    Baru : {n}")

    if dry_run:
        print("\nMode DRY-RUN aktif: Berkas target tidak diubah.")
        return True

    if updated_count > 0:
        tmp_target = target_path + ".tmp"
        with open(tmp_target, 'w', encoding='utf-8') as f:
            json.dump(target_data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        with open(tmp_target, 'r', encoding='utf-8') as f:
            try:
                json.load(f)
            except Exception as e:
                print(f"Error fatal: File hasil sementara tidak valid ({e}). Pembatalan.", file=sys.stderr)
                if os.path.exists(tmp_target):
                    os.remove(tmp_target)
                return False
        os.replace(tmp_target, target_path)
        print(f"\n[SUKSES] Berhasil menyimpan pembaruan ke {target_path}.")
    else:
        print("\nTidak ada perubahan yang perlu disimpan.")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Perbarui berkas lokalisasi Gakumas secara aman dari batch terjemahan."
    )
    parser.add_argument("input", help="Path ke berkas JSON batch terjemahan")
    parser.add_argument(
        "--target",
        "-t",
        default="local-files/localization.json",
        help="Path ke berkas JSON target (default: local-files/localization.json)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulasikan pembaruan tanpa menulis perubahan ke file target"
    )

    args = parser.parse_args()
    success = update_translation(args.target, args.input, dry_run=args.dry_run)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
