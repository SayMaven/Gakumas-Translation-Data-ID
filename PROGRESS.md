# Progres — Gakumas-Translation-Data-ID

Dokumen ini memantau status pengerjaan lokalisasi Bahasa Indonesia untuk seluruh komponen game Gakuen Idolm@ster.

---

## Ringkasan Progres Global

| Kategori | Volume | Estimasi Baris/Key | Status | Persentase |
|---|---|---|---|---|
| **Fase 1: UI & Sistem Inti** | 5 file | ~4.500 key | Dalam Pengerjaan | 45% |
| **Fase 2: Cerita Utama & Tutorial** | 117 file | ~25.000 baris | Belum Mulai | 0% |
| **Fase 3: Cerita Idol & Relasi** | 851 file | ~40.000 baris | Belum Mulai | 0% |
| **Fase 4: Gameplay Dalam & Event** | 2.246 file | ~500.000 baris | Belum Mulai | 0% |
| **Lirik Lagu** | 64 file | ~15.000 baris | Di-skip | — |

---

## Keterangan Status

- `[ ]` **Belum Mulai**: Berkas belum disentuh.
- `[-]` **Dalam Pengerjaan**: Sedang dalam proses pembuatan draf terjemahan.
- `[?]` **Perlu Review**: Draf selesai, menunggu peninjauan kelancaran bahasa dan konsistensi.
- `[x]` **Selesai**: Sudah ditinjau, tervalidasi secara teknis, dan digabungkan.

---

## Fase 1 — UI & Sistem Inti (Prioritas Utama)

Target: Seluruh antarmuka game, menu, tombol, item, misi, dan pesan tutorial berbahasa Indonesia.

| Status | File Target | Deskripsi | Volume | Penerjemah / Reviewer | Catatan |
|---|---|---|---|---|---|
| `[-]` | `local-files/localization.json` | String UI, tombol menu, label status | ~6.958 key | User & Assistant | 3.154 key selesai (~45,3%). Mencakup produce, pvp, profile, shop, setting, tour, tower, tutorial, work, dll. |
| `[ ]` | `local-files/genericTrans/index/tutorial.json` | Panduan tutorial gameplay | ~200 baris | — | Prioritas 1 |
| `[ ]` | `local-files/genericTrans/index/Item.json` | Nama & deskripsi item | ~150 baris | — | Prioritas 2 |
| `[ ]` | `local-files/genericTrans/index/mission.json` | Teks misi harian & mingguan | ~300 baris | — | Prioritas 2 |
| `[ ]` | `local-files/genericTrans/index/News.json` | Pengumuman dan berita in-game | ~100 baris | — | Prioritas 2 |
| `[ ]` | `local-files/genericTrans/index/ProduceCardCustomize.json` | Teks kustom kartu | ~100 baris | — | Prioritas 3 |
| `[ ]` | `local-files/genericTrans/index/flavor.json` | Flavor text umum | ~150 baris | — | Prioritas 3 |

---

## Fase 2 — Cerita Utama (Main Story) & Pembuka

Target: Pemain dapat menikmati alur cerita prolog, tutorial interaktif, dan cerita unit utama.

| Status | Komponen | File / Folder | Volume | Status Detail |
|---|---|---|---|---|
| `[ ]` | Prolog / Opening | `resource/adv_startup_*.txt` | 33 file | Belum Mulai |
| `[ ]` | Tutorial Interaktif | `resource/adv_tutorial_*.txt` | 17 file | Belum Mulai |
| `[ ]` | Cerita Unit Utama | `resource/adv_unit_*.txt` | 66 file | Belum Mulai |
| `[ ]` | Judul Cerita Produksi | `masterTrans/ProduceStory.json` | ~18K baris | Belum Mulai |

---

## Fase 3 — Konten Cerita Idol & Relasi

Target: Cerita per karakter idol dan interaksi keakraban (Dearness/Bond).

| Status | Komponen | File / Folder | Volume | Status Detail |
|---|---|---|---|---|
| `[ ]` | Cerita Idol Kandidat | `resource/adv_cidol_*.txt` | 354 file | Belum Mulai |
| `[ ]` | Cerita Bond / Keakraban | `resource/adv_dear_*.txt` | 494 file | Belum Mulai |
| `[ ]` | Deskripsi Achievement | `masterTrans/Achievement.json` | ~6K baris | Belum Mulai |
| `[ ]` | Konten Bantuan (Help) | `masterTrans/HelpContent.json` | ~2K baris | Belum Mulai |
| `[ ]` | Flavor Support Card | `masterTrans/SupportCardFlavor.json` | ~3K baris | Belum Mulai |

---

## Fase 4 — Konten Gameplay Dalam & Event

Target: Event produksi mendalam dan deskripsi kartu skill lengkap.

| Status | Komponen | File / Folder | Volume | Status Detail |
|---|---|---|---|---|
| `[ ]` | Cerita Story Produksi | `resource/adv_pstory_*.txt` | 611 file | Belum Mulai |
| `[ ]` | Cerita Support Card | `resource/adv_csprt_*.txt` | 529 file | Belum Mulai |
| `[ ]` | Event Produksi | `resource/adv_pevent_*.txt` | 1.105 file | Belum Mulai |
| `[ ]` | Deskripsi Kartu Skill | `masterTrans/ProduceCard.json` | ~438K baris | Belum Mulai |
| `[ ]` | Blurb Event | `genericTrans/index/EventBlurb.json` | ~39 KB | Belum Mulai |

---

## Log Riwayat Pengerjaan

| Tanggal | Target Berkas / Bagian | Aktivitas | Keterangan |
|---|---|---|---|
| 2026-10-15 | Setup Project & Proposal | Persiapan | Proposal terjemahan, glosarium mekanik, README.md, dan PROGRESS.md dibuat. |
| 2026-10-15 | `localization.json` (Batch 1) | Terjemahan | Menerjemahkan account_delete, achievement, dan common UI (~220 key). |
| 2026-10-15 | `localization.json` (Batch 2) | Terjemahan | Menerjemahkan sisa common.* hingga 100% selesai (~346 key total). Total 435 key. |
| 2026-10-15 | `localization.json` (Batch 3) | Terjemahan | Menerjemahkan audition.*, badge.*, dan title.* layar judul (total 510 key selesai). |
| 2026-10-15 | `localization.json` (Batch 4) | Terjemahan | Menerjemahkan produce.*, pvp.*, profile.*, shop.*, setting.*, seminar.*, story.*, dll. (total 2.834 key). |
| 2026-10-15 | `localization.json` (Batch 5) | Terjemahan | Menerjemahkan tour.*, tower.*, trail_event.*, tutorial.*, voice.*, work.*, upload errors (total 3.154 key / 45,3%). |
