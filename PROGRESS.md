# Progres — Gakumas-Translation-Data-ID

Dokumen ini memantau status pengerjaan lokalisasi Bahasa Indonesia untuk seluruh komponen game Gakuen Idolm@ster.

---

## Ringkasan Progres Global

| Kategori | Volume | Estimasi Baris/Key | Status | Persentase |
|---|---|---|---|---|
| **Fase 1: UI & Sistem Inti** | 11 file | 11.024 key | Selesai | 100% |
| **Fase 2: Kartu Skill & Cerita Utama** | 118 file | 1.748 kartu + ~25K baris | Dalam Pengerjaan | 0% |
| **Fase 3: Cerita Idol & Relasi** | 851 file | ~40.000 baris | Belum Mulai | 0% |
| **Fase 4: Gameplay Dalam & Event** | 2.245 file | ~60.000 baris | Belum Mulai | 0% |
| **Lirik Lagu** | 64 file | ~15.000 baris | Di-skip | — |

---

## Keterangan Status

- `[ ]` **Belum Mulai**: Berkas belum disentuh.
- `[-]` **Dalam Pengerjaan**: Sedang dalam proses pembuatan draf terjemahan.
- `[?]` **Perlu Review**: Draf selesai, menunggu peninjauan kelancaran bahasa dan konsistensi.
- `[x]` **Selesai**: Sudah ditinjau, tervalidasi secara teknis, dan digabungkan.

---

## Fase 1 — UI & Sistem Inti (Prioritas Utama)

Target: Seluruh antarmuka game, menu, tombol, item, misi, tutorial, dan string UI umum berbahasa Indonesia. **Status: 100% SELESAI (11.024 / 11.024 key)**.

| Status | File Target | Deskripsi | Volume | Penerjemah / Reviewer | Catatan |
|---|---|---|---|---|---|
| `[x]` | `local-files/localization.json` | String UI utama, menu, label status | 6.958 key | User & Assistant | **100% Selesai**. Seluruh sistem UI, menu, kartu nama, pemotretan, hadiah, P-Book, live, pengaturan, dan dialog game tuntas. |
| `[x]` | `local-files/generic.json` | Kamus generik root sistem UI & fallback | 525 key | User & Assistant | **100% Selesai**. Alur produce, gacha, stamina, efek kartu, pencapaian, dan istilah umum game. |
| `[x]` | `local-files/genericTrans/index/tutorial.json` | Panduan tutorial gameplay | 299 key | User & Assistant | **100% Selesai**. Mekanik turn, kartu, Genki, buff status (Kondisi Prima, Fokus, Kesan Baik, Semangat), dan Anomaly. |
| `[x]` | `local-files/genericTrans/index/News.json` | Pengumuman dan berita in-game | 283 key | User & Assistant | **100% Selesai**. Judul pengumuman update game, banner gacha, event musim, dan laporan kendala bug. |
| `[x]` | `local-files/genericTrans/index/ProduceCardCustomize.json` | Teks kustom kartu | 43 key | User & Assistant | **100% Selesai**. Fragmen kustomisasi kartu skill, penyesuaian biaya, dan syarat aktivasi. |
| `[x]` | `local-files/genericTrans/index/Item.json` | Nama & deskripsi item | 27 key | User & Assistant | **100% Selesai**. Deskripsi item paket perayaan unduhan, sewa memory, dan hadiah login harian. |
| `[x]` | `local-files/genericTrans/index/flavor.json` | Flavor text umum & dialog teaser | 12 key | User & Assistant | **100% Selesai**. Dialog teaser unit (Re;IRIS, dll.) dan peringatan hukum. |
| `[x]` | `local-files/genericTrans/index/mission.json` | Teks misi harian & mingguan | 11 key | User & Assistant | **100% Selesai**. Misi Produce idol Sense/Anomaly, ranking, dan N.I.A. |
| `[x]` | `local-files/genericTrans/index/mission.fmt.json` | Format string misi dinamis | 22 key | User & Assistant | **100% Selesai**. Format string dinamis untuk misi SP Lesson, level keakraban, dan peningkatan kartu. |
| `[x]` | `local-files/genericTrans/index/EventBlurb.json` | Teks blurb dialog banner event | 334 key | User & Assistant | **100% Selesai**. Seluruh dialog blurb festival olahraga antarkelas dan interaksi karakter idol. |
| `[x]` | `local-files/genericTrans/index/trash.json` | Kamus string UI umum & fallback | 2.510 key | User & Assistant | **100% Selesai**. Seluruh kamus string UI umum, tombol aksi, item AP, P-Idol, achievement, dan label game. |

---

## Fase 2 — Kartu Skill (ProduceCard) & Cerita Utama

Target: Dimulai dengan menerjemahkan seluruh kartu skill (`masterTrans/ProduceCard.json`) agar interaksi utama saat sesi Produce (Lesson & Audition) langsung berbahasa Indonesia, lalu dilanjutkan dengan alur cerita prolog, tutorial interaktif, dan cerita unit utama.

| Status | Komponen | File / Folder | Volume | Status Detail |
|---|---|---|---|---|
| `[-]` | **Kartu Skill Produce (Prioritas 1)** | `masterTrans/ProduceCard.json` | 1.748 kartu (458 kartu unik, ~438K baris) | **Dalam Pengerjaan (50%)**. Seluruh 447 fragmen deskripsi efek kartu (11.340 entri) **100% Selesai**. Tahap berikutnya: Penerjemahan nama kartu. |
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

Target: Event produksi mendalam dan cerita pendukung kartu.

| Status | Komponen | File / Folder | Volume | Status Detail |
|---|---|---|---|---|
| `[ ]` | Cerita Story Produksi | `resource/adv_pstory_*.txt` | 611 file | Belum Mulai |
| `[ ]` | Cerita Support Card | `resource/adv_csprt_*.txt` | 529 file | Belum Mulai |
| `[ ]` | Event Produksi | `resource/adv_pevent_*.txt` | 1.105 file | Belum Mulai |

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
| 2026-10-15 | `localization.json` (Batch 6) | Terjemahan | Menerjemahkan adv.*, angya.*, app_tracking_transparency.*, character_detail.*, check.*, clear_cache_sheet.* (total 3.292 key / 47,3%). |
| 2026-10-15 | `localization.json` (Batch 7) | Terjemahan | Menerjemahkan card.* bagian 1 (card.common, card.detail, card.filter, card.idol, card.idol_card: 213 key, total 3.472 key / 49,9%). |
| 2026-10-15 | `localization.json` (Batch 8) | Terjemahan | Menerjemahkan card.* bagian 2 (support_card, sort, status, upgrade_status_list: 150 key, total 3.596 key / 51,7%). card.* 100% tuntas. |
| 2026-10-15 | `localization.json` (Batch 9) | Terjemahan | Menerjemahkan competition.*, contest.*, conversion.*, costume.* (508 key diperiksa, 426 diupdate, total 4.104 key / 59,0%). |
| 2026-10-15 | `localization.json` (Batch 10) | Terjemahan | Menerjemahkan data.*, dearness.*, dmm.*, download.*, exchange.*, friend.*, google.*, grade_mission.*, guild/Circle.*, high_score_event.* (530 key diperiksa, 477 diupdate, total 4.634 key / 66,6%). |
| 2026-10-15 | `localization.json` (Batch 11) | Terjemahan | Menerjemahkan home.*, idol_dearness.*, invite.*, item.*, jewel.*, last_login.*, legend_skill_card.*, limit.* (525 key diperiksa, 457 diupdate, total 5.159 key / 74,1%). |
| 2026-10-15 | `localization.json` (Batch 12) | Terjemahan | Menerjemahkan live.*, loading.*, login_bonus.*, main_task.*, maintenance.*, master.*, media.*, meishi/Kartu Nama.* (442 key diperiksa, 373 diupdate, total 5.601 key / 80,5%). |
| 2026-10-15 | `localization.json` (Batch 13) | Terjemahan | Menerjemahkan memory.*, mission.*, music.*, notice.*, octo.*, others.*, photo.* (503 key diperiksa, 451 diupdate, total 6.104 key / 87,7%). |
| 2026-10-15 | `localization.json` (Batch 14 & Final) | Terjemahan | Menerjemahkan photography.*, photopose.*, picturebook.* (P-Book), present.* (Kotak Hadiah), dan pembersihan teks sisa. **100% SELESAI (6.958 / 6.958 key)**. |
| 2026-10-15 | `genericTrans/index/Item.json` | Terjemahan | Menerjemahkan seluruh nama & deskripsi item login bonus dan paket perayaan unduhan. **100% SELESAI (27 key)**. |
| 2026-10-15 | `genericTrans/index/mission.json` | Terjemahan | Menerjemahkan misi Produce idol Sense/Anomaly, target ranking A/SS, dan N.I.A. **100% SELESAI (11 key)**. |
| 2026-10-15 | `genericTrans/index/flavor.json` | Terjemahan | Menerjemahkan dialog teaser unit Re;IRIS/Begrazia dan peringatan batas usia. **100% SELESAI (12 key)**. |
| 2026-10-15 | `genericTrans/index/tutorial.json` | Terjemahan | Menerjemahkan seluruh panduan tutorial gameplay, mekanik Genki, buff status, dan pendekatan Anomaly. **100% SELESAI (299 key)**. |
| 2026-10-15 | `genericTrans/index/ProduceCardCustomize.json` | Terjemahan | Menerjemahkan seluruh fragmen teks kustomisasi kartu skill, penyesuaian biaya, dan syarat aktivasi. **100% SELESAI (43 key)**. |
| 2026-10-15 | `genericTrans/index/News.json` | Terjemahan | Menerjemahkan seluruh judul pengumuman update game, banner gacha, event musim, dan laporan kendala bug. **100% SELESAI (283 key)**. |
| 2026-10-15 | `genericTrans/index/mission.fmt.json` | Terjemahan | Menerjemahkan seluruh template format string misi dinamis (SP Lesson, bond Lv, dll.). **100% SELESAI (22 key)**. |
| 2026-10-15 | `genericTrans/index/EventBlurb.json` | Terjemahan | Menerjemahkan seluruh dialog blurb festival olahraga antarkelas dan dialog interaksi idol. **100% SELESAI (334 key)**. |
| 2026-10-15 | `genericTrans/index/trash.json` (Batch 1-5) | Terjemahan | Menerjemahkan seluruh kamus string UI umum, tombol aksi, item AP, P-Idol, achievement, dan label game dalam 5 batch terukur. **100% SELESAI (2.510 key)**. |
| 2026-10-15 | `local-files/generic.json` | Terjemahan | Menerjemahkan seluruh kamus teks generik root, alur Produce, efek kartu, gacha, dan dialog sistem. **100% SELESAI (525 key)**. |
| 2026-10-15 | **Fase 1: UI & Sistem Inti** | Milestone | **11 File, 11.024 Key Tuntas 100%**. Seluruh antarmuka UI, menu, tombol, item, tutorial, kamus fallback, dan teks umum resmi berbahasa Indonesia. |
| 2026-10-15 | Perencanaan Tahap 2 (`ProduceCard.json`) | Roadmap | Menetapkan `masterTrans/ProduceCard.json` (1.748 kartu, 458 kartu unik) sebagai prioritas pertama Fase 2 sebelum naskah cerita. |
| 2026-10-15 | `masterTrans/ProduceCard.json` (Efek Kartu) | Terjemahan | Menerjemahkan seluruh 447 fragmen deskripsi efek kartu skill (11.340 entri diperbarui). Seluruh efek status, buff, giliran, stamina, dan mekanik lesson 100% berbahasa Indonesia. |
