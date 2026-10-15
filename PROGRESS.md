# Progres — Gakumas-Translation-Data-ID

Dokumen ini memantau status pengerjaan lokalisasi Bahasa Indonesia untuk seluruh komponen game Gakuen Idolm@ster secara transparan dan terperinci.

---

## Ringkasan Progres Global

| Kategori | Cakupan File | Status Saat Ini | Detail Kemajuan |
|---|---|---|---|
| **Fase 1: UI & Sistem Inti** | 11 berkas JSON | **100% Selesai** | Seluruh UI, kamus generik, tutorial, teks item, event blurb, dan trash.json (11.024 key). |
| **Fase 2: Master Database Gameplay (`masterTrans`)** | 108 berkas JSON | **Dalam Pengerjaan (7/108 tuntas)** | Komponen utama Produce (kartu skill, P-item, P-drink, badge efek, label mekanik, support card, item tas) 100% selesai. Sisa 99 berkas sedang diproses bertahap. |
| **Fase 3: Cerita Prolog, Tutorial & Unit (`resource/`)** | 116 berkas TXT | Belum Mulai | Naskah cerita pembuka (33 file), tutorial visual novel (17 file), dan cerita unit utama (66 file). |
| **Fase 4: Cerita Karakter & Event (`resource/`)** | 3.093 berkas TXT | Belum Mulai | Cerita kandidat idol (354 file), commu bond (494 file), cerita support (529 file), p-story (611 file), pevent (1.105 file). |
| **Lirik Lagu (`lyrics/`)** | 64 berkas | Di-skip | Dibiarkan berbahasa asli Jepang sesuai standar resmi proyek. |

---

## Keterangan Status Simbol

- `[x]` **Selesai**: Terjemahan tuntas 100%, divalidasi sintaksis JSON, dan lolos uji konsistensi glosarium.
- `[-]` **Di-skip / Teknis**: Berkas konfigurasi engine internal tanpa teks tampilan pemain.
- `[ ]` **Belum Mulai**: Berkas database belum diterjemahkan dan siap dikerjakan.

---

## Fase 1 — UI & Sistem Inti (Status: 100% Selesai)

Target: Seluruh antarmuka game, menu, tombol, item, misi, tutorial, dan string UI umum berbahasa Indonesia. **Status: 11 / 11 Berkas Tuntas (11.024 Key)**.

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

## Fase 2 — Master Database Gameplay (`local-files/masterTrans/`)

Target: Menyelesaikan seluruh data gameplay di folder `local-files/masterTrans/` (total 108 berkas) agar fitur **MasterDB Localization** pada Localify bekerja 100% dalam Bahasa Indonesia tanpa ada teks sistem yang bocor.

Status Keseluruhan Fase 2: **8 Selesai** | **96 Belum Mulai** | **4 Di-skip (Nama Asli / Teknis)** (Total: 108 Berkas)

### 2.1 Inti Produce, Kartu Skill & Pertandingan (Lesson & Audition) — 37 Berkas

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Kartu Skill Produce** | `masterTrans/ProduceCard.json` | 1748 entri | **100% Selesai**. Seluruh 447 fragmen efek (11.340 entri) dan 1.748 nama kartu (457 nama unik) telah diterjemahkan. |
| `[x]` | **P-Item (Item Produce)** | `masterTrans/ProduceItem.json` | 1088 entri | **100% Selesai**. Seluruh 7.057 fragmen deskripsi efek dan 1.088 nama item Produce (534 nama unik) telah diterjemahkan. |
| `[x]` | **P-Drink (Minuman Produce)** | `masterTrans/ProduceDrink.json` | 29 entri | **100% Selesai**. Seluruh 29 nama minuman P-Drink dan seluruh efek deskripsinya telah diterjemahkan. |
| `[x]` | **Badge Status Efek Game** | `masterTrans/ProduceDescriptionExamEffect.json` | 89 entri | **100% Selesai**. Seluruh 89 badge efek status buff/debuff (Kesan Baik, Semangat, Genki, Pengurangan Biaya Stamina, dll.). |
| `[x]` | **Label & Tooltip Mekanik** | `masterTrans/ProduceDescriptionLabel.json` | 228 entri | **100% Selesai**. Seluruh 228 label mekanik gameplay dan seluruh fragmen deskripsi/tooltip penjelasannya. |
| `[ ]` | **Deskripsi Efek Produce** | `masterTrans/ProduceDescriptionProduceEffect.json` | 92 entri | Belum Mulai. Efek perolehan parameter (Vocal +, Dance +, Visual +, dll.) saat sesi Produce. |
| `[ ]` | **Efek Pertumbuhan Kartu** | `masterTrans/ProduceDescriptionProduceCardGrowEffect.json` | 53 entri | Belum Mulai. Deskripsi efek peningkatan/penurunan nilai parameter kartu skill. |
| `[ ]` | **Teks Pergantian Kartu** | `masterTrans/ProduceDescriptionSwap.json` | 78 entri | Belum Mulai. Teks instruksi pergantian dan penukaran kartu skill saat sesi lesson/audition. |
| `[ ]` | **Label Rencana Produce** | `masterTrans/ProduceDescriptionProducePlan.json` | 4 entri | Belum Mulai. Nama dan keterangan kategori rencana (Sense, Logic, Anomaly). |
| `[ ]` | **Label Tipe Produce** | `masterTrans/ProduceDescriptionProduceType.json` | 5 entri | Belum Mulai. Tipe rute dan pembagian jalur skenario Produce. |
| `[ ]` | **Label Tahapan Produce** | `masterTrans/ProduceDescriptionProduceStep.json` | 2 entri | Belum Mulai. Teks tahapan alur sesi Produce (Lesson, Istirahat, Audisi, dll.). |
| `[ ]` | **Kustomisasi Kartu Skill** | `masterTrans/ProduceCardCustomize.json` | 347 entri | Belum Mulai. Atribut efek modifikasi dan peningkatan skill kartu. |
| `[ ]` | **Pencarian Kartu Skill** | `masterTrans/ProduceCardSearch.json` | 283 entri | Belum Mulai. Filter dan kategori pencarian kartu skill di menu Produce. |
| `[ ]` | **Enchant Status Kartu** | `masterTrans/ProduceCardStatusEnchant.json` | 79 entri | Belum Mulai. Deskripsi status enchant tambahan pada kartu skill. |
| `[ ]` | **Database Efek Ujian/Audisi** | `masterTrans/ProduceExamEffect.json` | 2112 entri | Belum Mulai. Kumpulan formula dan efek aksi saat lesson/audition Produce. |
| `[ ]` | **Status Enchant Ujian** | `masterTrans/ProduceExamStatusEnchant.json` | 2054 entri | Belum Mulai. Efek status enchant khusus saat evaluasi audisi. |
| `[ ]` | **Grup Efek Gimmick Ujian** | `masterTrans/ProduceExamGimmickEffectGroup.json` | 3762 entri | Belum Mulai. Gimmick khusus rintangan dan mekanik panggung ujian. |
| `[ ]` | **Pemicu Aksi Ujian** | `masterTrans/ProduceExamTrigger.json` | 691 entri | Belum Mulai. Syarat aktivasi pemicu efek skill saat ujian berlangsung. |
| `[ ]` | **Nama NPC Rival Audisi** | `masterTrans/ProduceExamBattleNpcMob.json` | 62 entri | Belum Mulai. Nama karakter idol saingan (rival/mob) di panggung audisi. |
| `[ ]` | **Panel Pertumbuhan Idol** | `masterTrans/ProduceGrowthPanel.json` | 50 entri | Belum Mulai. Pilihan aksi dan peningkatan status idol pada panel perkembangan. |
| `[ ]` | **Kategori Panduan Kartu** | `masterTrans/ProduceGuideProduceCardCategory.json` | 67 entri | Belum Mulai. Label panduan kategori kartu rekomendasi untuk pemula. |
| `[ ]` | **Grup Panduan Kartu** | `masterTrans/ProduceGuideProduceCardCategoryGroup.json` | 16 entri | Belum Mulai. Deskripsi kelompok kartu panduan strategi Produce. |
| `[ ]` | **Sampel Deck Panduan** | `masterTrans/ProduceGuideProduceCardSampleDeckCategory.json` | 65 entri | Belum Mulai. Label panduan contoh susunan deck kartu untuk idol. |
| `[ ]` | **Sesi Lesson Produce** | `masterTrans/ProduceStepLesson.json` | 955 entri | Belum Mulai. Nama dan detail sesi latihan (Vocal, Dance, Visual Lesson). |
| `[ ]` | **Detail Event Langkah Produce** | `masterTrans/ProduceStepEventDetail.json` | 6921 entri | Belum Mulai. Teks pilihan aksi dan opsi respon saat event Produce berlangsung. |
| `[ ]` | **Saran Pilihan Event** | `masterTrans/ProduceStepEventSuggestion.json` | 3066 entri | Belum Mulai. Teks saran dan petunjuk keputusan event langkah Produce. |
| `[ ]` | **Slot Tantangan Produce** | `masterTrans/ProduceChallengeSlot.json` | 54 entri | Belum Mulai. Syarat dan deskripsi pembuka slot tantangan Produce. |
| `[ ]` | **Pertumbuhan Karakter Event** | `masterTrans/ProduceEventCharacterGrowth.json` | 39 entri | Belum Mulai. Judul dan dialog pertumbuhan idol setelah event latihan. |
| `[ ]` | **Grup Skenario Produce** | `masterTrans/ProduceGroup.json` | 3 entri | Belum Mulai. Nama dan deskripsi kelompok skenario Produce. |
| `[ ]` | **Peringkat Skor Tinggi Produce** | `masterTrans/ProduceHighScore.json` | 19 entri | Belum Mulai. Label kategori pencapaian skor tertinggi Produce. |
| `[ ]` | **Navigasi & Dialog Asari-sensei** | `masterTrans/ProduceNavigation.json` | 352 entri | Belum Mulai. Instruksi dan saran navigasi Producer selama Produce. |
| `[ ]` | **Musim Kompetisi Produce** | `masterTrans/ProduceSeason.json` | 2 entri | Belum Mulai. Nama musim kompetisi panggung antarpemain. |
| `[ ]` | **Skill Pasif Produce** | `masterTrans/ProduceSkill.json` | 1536 entri | Belum Mulai. Nama dan efek skill pasif Produce idol dan support. |
| `[ ]` | **Item Kustomisasi Produce** | `masterTrans/ProduceCustomizeItem.json` | 180 entri | Belum Mulai. Nama item bahan modifikasi dan kustomisasi kartu. |
| `[ ]` | **Grup Efek Kartu** | `masterTrans/EffectGroup.json` | 67 entri | Belum Mulai. Nama klasifikasi kelompok efek skill. |
| `[ ]` | **Transisi Ujian Seminar** | `masterTrans/SeminarExamTransition.json` | 12 entri | Belum Mulai. Nama grup dan instruksi ujian seminar taktik Produce. |
| `[ ]` | **Mode Skenario Produce** | `masterTrans/Produce.json` | 8 entri | Belum Mulai. Nama mode skenario dasar Produce. |

---

### 2.2 Kartu Idol, Karakter & Kostum — 11 Berkas

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Support Card** | `masterTrans/SupportCard.json` | 208 entri | **100% Selesai**. Seluruh 208 nama Support Card (R, SR, SSR) dan 208 teks tingkat aktivasi efek telah diterjemahkan. |
| `[-]` | **Produce Idol Card (P-Idol)** | `masterTrans/IdolCard.json` | 156 entri | **Di-skip (Nama Kartu Asli)**. Nama gelar kartu Produce Idol dibiarkan sesuai nama aslinya (School Life, First Love, Fighting My Way, Fluorite, dll.) agar konsisten dengan wiki dan rilis resmi. |
| `[-]` | **Skin Kartu Produce Idol** | `masterTrans/IdolCardSkin.json` | 306 entri | **Di-skip (Nama Skin Asli)**. Nama variasi skin kartu Produce Idol dibiarkan sesuai nama rilis resminya. |
| `[ ]` | **Kostum Panggung & Pakaian** | `masterTrans/Costume.json` | 566 entri | Belum Mulai. Nama pakaian, kostum live panggung, dan pakaian kasual idol. |
| `[ ]` | **Aksesori Kepala & Gaya Rambut** | `masterTrans/CostumeHead.json` | 416 entri | Belum Mulai. Nama gaya rambut, pita, topi, dan aksesori kepala idol. |
| `[ ]` | **Data Karakter Idol & Staf** | `masterTrans/Character.json` | 24 entri | Belum Mulai. Nama lengkap kanji dan romaji alfabet idol dan guru. |
| `[ ]` | **Nama Karakter Naskah Cerita** | `masterTrans/CharacterAdv.json` | 25 entri | Belum Mulai. Nama tampilan karakter yang muncul pada script dialog ADV. |
| `[ ]` | **Profil Detail Karakter** | `masterTrans/CharacterDetail.json` | 181 entri | Belum Mulai. Biodata idol, hobi, keahlian khusus, dan profil pribadi. |
| `[ ]` | **Level Keakraban (Dearness/Bond)** | `masterTrans/CharacterDearnessLevel.json` | 471 entri | Belum Mulai. Deskripsi syarat pembuka level keakraban tiap idol. |
| `[ ]` | **Pesan Notifikasi Karakter** | `masterTrans/CharacterPushMessage.json` | 169 entri | Belum Mulai. Pesan notifikasi push dari idol ke perangkat pemain. |
| `[ ]` | **Filter Skill Support Card** | `masterTrans/SupportCardProduceSkillFilter.json` | 51 entri | Belum Mulai. Label filter pencarian efek skill support card. |

---

### 2.3 Inventaris, Toko & Gacha — 7 Berkas

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Item Tas, Mata Uang & Tiket** | `masterTrans/Item.json` | 368 entri | **100% Selesai**. Seluruh 368 item tas, Piece idol, tiket gacha, koin, buku pelajaran, deskripsi, dan rute perolehan telah diterjemahkan. |
| `[ ]` | **Tombol Banner Gacha** | `masterTrans/GashaButton.json` | 108 entri | Belum Mulai. Teks tombol tarik gacha, gacha gratis harian, dan banner promosi. |
| `[ ]` | **Tombol Gacha Koin** | `masterTrans/CoinGashaButton.json` | 38 entri | Belum Mulai. Teks tombol penarikan gacha menggunakan koin event. |
| `[ ]` | **Kategori Toko** | `masterTrans/Shop.json` | 5 entri | Belum Mulai. Nama kategori menu toko permainan. |
| `[ ]` | **Item Toko Penukaran** | `masterTrans/ShopItem.json` | 285 entri | Belum Mulai. Nama barang dan paket yang dijual di toko penukaran. |
| `[ ]` | **Produk Penjualan & Pemulihan** | `masterTrans/ShopProduct.json` | 14 entri | Belum Mulai. Nama produk pembelian jewel dan pemulihan stamina. |
| `[ ]` | **Kategori Penukaran Item** | `masterTrans/ExchangeItemCategory.json` | 6 entri | Belum Mulai. Nama kategori item penukaran di exchange shop. |

---

### 2.4 Tugas, Misi, Achievement & Ranking — 14 Berkas

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[ ]` | **Tugas Utama Producer** | `masterTrans/MainTask.json` | 310 entri | Belum Mulai. Judul, deskripsi beranda, dan petunjuk tugas utama Producer. |
| `[ ]` | **Grup Tugas Utama** | `masterTrans/MainTaskGroup.json` | 4 entri | Belum Mulai. Nama kelompok bab tugas utama Producer. |
| `[ ]` | **Misi Gameplay** | `masterTrans/Mission.json` | 3494 entri | Belum Mulai. Teks seluruh 3.494 misi harian, mingguan, event, dan debut idol. |
| `[ ]` | **Kelompok Misi** | `masterTrans/MissionGroup.json` | 282 entri | Belum Mulai. Nama kategori dan tab kelompok misi permainan. |
| `[ ]` | **Pass Misi Bulanan** | `masterTrans/MissionPass.json` | 30 entri | Belum Mulai. Nama dan deskripsi tingkatan hadiah Pass Misi bulanan. |
| `[ ]` | **Poin Pass Misi** | `masterTrans/MissionPassPoint.json` | 1 entri | Belum Mulai. Nama satuan poin kemajuan Pass Misi. |
| `[ ]` | **Poin Hadiah Misi** | `masterTrans/MissionPoint.json` | 35 entri | Belum Mulai. Nama poin milestone penyelesaian misi. |
| `[ ]` | **Lembar Misi Panel** | `masterTrans/MissionPanelSheet.json` | 57 entri | Belum Mulai. Nama lembar misi papan panel bingo debut idol. |
| `[ ]` | **Grup Lembar Misi Panel** | `masterTrans/MissionPanelSheetGroup.json` | 49 entri | Belum Mulai. Nama kelompok lembar misi panel bertingkat. |
| `[ ]` | **Misi Rilis Harian** | `masterTrans/MissionDailyReleaseGroup.json` | 31 entri | Belum Mulai. Nama kelompok misi pembuka harian kampanye. |
| `[ ]` | **Achievement & Gelar Idol** | `masterTrans/Achievement.json` | 1242 entri | Belum Mulai. Nama dan syarat 1.242 achievement, gelar, dan trofi kebanggaan. |
| `[ ]` | **Badge Penghargaan** | `masterTrans/Badge.json` | 364 entri | Belum Mulai. Nama dan deskripsi badge penghargaan pencapaian Produce. |
| `[ ]` | **Peringkat Producer** | `masterTrans/ProducerRanking.json` | 5 entri | Belum Mulai. Nama tingkatan ranking evaluasi Producer (D, C, B, A, S). |
| `[ ]` | **Konfigurasi Rating Contest** | `masterTrans/PvpRateConfig.json` | 54 entri | Belum Mulai. Keterangan tier rating kompetisi panggung antarpemain. |

---

### 2.5 Cerita Master & Cuplikan Narasi — 11 Berkas

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[ ]` | **Judul Episode Cerita Produce** | `masterTrans/ProduceStory.json` | 3454 entri | Belum Mulai. Judul 3.454 episode cerita interaksi selama masa Produce. |
| `[ ]` | **Flavor Text Support Card** | `masterTrans/SupportCardFlavor.json` | 583 entri | Belum Mulai. Teks cuplikan dialog dan narasi suasana di Support Card. |
| `[ ]` | **Daftar Cerita & Episode** | `masterTrans/Story.json` | 311 entri | Belum Mulai. Judul episode cerita umum dan cerita unit Hatsuboshi. |
| `[ ]` | **Judul Event Cerita** | `masterTrans/StoryEvent.json` | 35 entri | Belum Mulai. Nama event cerita berkala dan festival sekolah. |
| `[ ]` | **Grup Alur Cerita** | `masterTrans/StoryGroup.json` | 100 entri | Belum Mulai. Nama kelompok bab alur cerita komprehensif. |
| `[ ]` | **Bab Cerita Utama** | `masterTrans/MainStoryChapter.json` | 4 entri | Belum Mulai. Judul dan sinopsis bab cerita utama sekolah idol. |
| `[ ]` | **Bagian Cerita Utama** | `masterTrans/MainStoryPart.json` | 1 entri | Belum Mulai. Judul bagian cerita panggung utama. |
| `[ ]` | **Judul Cerita ADV Produce** | `masterTrans/ProduceAdv.json` | 32 entri | Belum Mulai. Tipe dan judul cerita visual novel sesi Produce. |
| `[ ]` | **Percabangan Cerita Produce** | `masterTrans/ProduceSplitAdv.json` | 26 entri | Belum Mulai. Judul segmen cerita percabangan Produce. |
| `[ ]` | **Cerita Khusus Karakter Produce** | `masterTrans/ProduceCharacterAdv.json` | 10 entri | Belum Mulai. Judul cerita dialog khusus karakter idol saat Produce. |
| `[ ]` | **Label Kategori Event** | `masterTrans/EventLabel.json` | 13 entri | Belum Mulai. Label penanda kategori event cerita khusus. |

---

### 2.6 Panduan, Tips, Bantuan, Audio, Media & Aset — 26 Berkas

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Tips Layar Loading** | `masterTrans/Tips.json` | 34 entri | **100% Selesai**. Seluruh tips gameplay, fitur level producer, penukaran uang/AP, dan akademi Hatsuboshi telah diterjemahkan. |
| `[ ]` | **Tutorial Master Sistem** | `masterTrans/Tutorial.json` | 217 entri | Belum Mulai. Judul dan teks navigasi tutorial fitur-fitur permainan. |
| `[ ]` | **Langkah Tutorial Produce** | `masterTrans/TutorialProduceStep.json` | 12 entri | Belum Mulai. Nama tahap panduan tutorial pertama kali Produce. |
| `[ ]` | **Artikel Panduan Bantuan** | `masterTrans/HelpContent.json` | 273 entri | Belum Mulai. Judul artikel panduan bantuan lengkap in-game. |
| `[ ]` | **Kategori Panduan Bantuan** | `masterTrans/HelpCategory.json` | 36 entri | Belum Mulai. Nama kategori navigasi menu bantuan (Help). |
| `[ ]` | **Syarat Pembuka Fitur Game** | `masterTrans/FeatureLock.json` | 13 entri | Belum Mulai. Keterangan syarat rute untuk membuka fitur terkunci. |
| `[ ]` | **Pose Pemotretan Idol** | `masterTrans/PhotoPose.json` | 1092 entri | Belum Mulai. Nama gaya dan pose foto idol di studio pemotretan. |
| `[ ]` | **Latar Belakang Studio Foto** | `masterTrans/PhotoBackground.json` | 9 entri | Belum Mulai. Nama latar pemandangan studio foto. |
| `[ ]` | **Ekspresi Wajah Pemotretan** | `masterTrans/PhotoFacialMotionGroup.json` | 4 entri | Belum Mulai. Nama kelompok gerakan ekspresi wajah idol. |
| `[ ]` | **Bingkai Kartu Nama (Meishi)** | `masterTrans/MeishiBaseAsset.json` | 301 entri | Belum Mulai. Nama template dasar kartu nama Producer. |
| `[ ]` | **Stiker Ilustrasi Meishi** | `masterTrans/MeishiIllustrationAsset.json` | 790 entri | Belum Mulai. Nama stiker dan ilustrasi hiasan kartu nama Producer. |
| `[ ]` | **Daftar Lagu & Komposer** | `masterTrans/Music.json` | 434 entri | Belum Mulai. Judul lagu, lirikis, komposer, dan arranger musik Hatsuboshi. |
| `[ ]` | **Daftar Grup Suara Idol** | `masterTrans/VoiceGroup.json` | 3609 entri | Belum Mulai. Judul kelompok rekaman suara idol di ensiklopedia. |
| `[ ]` | **Daftar Roster Suara** | `masterTrans/VoiceRoster.json` | 2001 entri | Belum Mulai. Judul rekaman suara interaksi idol per situasi. |
| `[ ]` | **Hadiah Kelulusan Memory** | `masterTrans/MemoryGift.json` | 21 entri | Belum Mulai. Nama kenang-kenangan hasil kelulusan Produce idol. |
| `[ ]` | **Tag Karakteristik Memory** | `masterTrans/MemoryTag.json` | 24 entri | Belum Mulai. Nama tag penanda kategori atribut memory. |
| `[ ]` | **Aturan & Regulasi Layanan** | `masterTrans/Rule.json` | 23 entri | Belum Mulai. Teks aturan ketentuan pengguna dan aturan event. |
| `[ ]` | **Syarat & Kebijakan** | `masterTrans/Terms.json` | 3 entri | Belum Mulai. Ketentuan hukum dan kebijakan privasi aplikasi. |
| `[ ]` | **Pengaturan Dasar Game** | `masterTrans/Setting.json` | 1 entri | Belum Mulai. Pesan peringatan sistem dan nama bawaan akun pengguna. |
| `[ ]` | **Mode Tur Wilayah** | `masterTrans/Tour.json` | 4 entri | Belum Mulai. Nama rute tur konser antarwilayah idol. |
| `[ ]` | **Mode Menara Ujian (Tower)** | `masterTrans/Tower.json` | 13 entri | Belum Mulai. Judul stage lantai menara tantangan idol. |
| `[ ]` | **Pekerjaan Idol (Work/Jobs)** | `masterTrans/Work.json` | 2 entri | Belum Mulai. Nama aktivitas pekerjaan idle luar sekolah idol. |
| `[ ]` | **Fallback Terjemahan Master** | `masterTrans/Localization.json` | 98 entri | Belum Mulai. Teks fallback deskripsi cadangan master database. |
| `[ ]` | **Daftar BGM Musik Latar** | `masterTrans/Bgm.json` | 2 entri | Belum Mulai. Nama musik latar belakang menu game. |
| `[ ]` | **Pertandingan Circle Raid** | `masterTrans/GvgRaid.json` | 1 entri | Belum Mulai. Nama event kompetisi panggung grup/Circle. |
| `[ ]` | **Galeri Video & Animasi** | `masterTrans/Media.json` | 232 entri | Belum Mulai. Nama konten video cuplikan dan animasi 4-koma. |

---

### 2.7 Berkas Konfigurasi Teknis / Non-Translatable — 2 Berkas

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[-]` | **Kondisi Logika Engine** | `masterTrans/ConditionSet.json` | 5332 entri | **Di-skip (Teknis)**. Kumpulan ID formula teknis logika engine tanpa teks antarmuka. |
| `[-]` | **Tag Teknis Kartu Skill** | `masterTrans/ProduceCardTag.json` | 3 entri | **Di-skip (Teknis)**. ID tag internal klasifikasi kartu tanpa teks antarmuka. |

---

## Fase 3 — Naskah Cerita Prolog, Tutorial & Unit (`resource/`)

Target: Menerjemahkan visual novel dialog pembuka, tutorial cerita, dan alur naratif unit utama. Total 116 berkas cerita.

| Status | Komponen | File / Folder | Volume | Status Detail |
|---|---|---|---|---|
| `[ ]` | **Prolog & Cerita Pembuka** | `resource/adv_startup_*.txt` | 33 file | Belum Mulai. Dialog awal kedatangan Producer ke Akademi Hatsuboshi. |
| `[ ]` | **Tutorial Interaktif ADV** | `resource/adv_tutorial_*.txt` | 17 file | Belum Mulai. Panduan visual cerita pertama bersama idol. |
| `[ ]` | **Cerita Unit Utama** | `resource/adv_unit_*.txt` | 66 file | Belum Mulai. Naskah cerita pembentukan dan perjalanan unit idol. |

---

## Fase 4 — Cerita Karakter & Interaksi Idol (`resource/`)

Target: Cerita mendalam tiap kandidat idol, interaksi keakraban (Commu Bond), cerita pendukung kartu, dan event produksi. Total 3.093 berkas cerita.

| Status | Komponen | File / Folder | Volume | Status Detail |
|---|---|---|---|---|
| `[ ]` | **Cerita Kandidat Idol** | `resource/adv_cidol_*.txt` | 354 file | Belum Mulai. Alur cerita individu masing-masing karakter idol. |
| `[ ]` | **Commu Bond (Keakraban)** | `resource/adv_dear_*.txt` | 494 file | Belum Mulai. Interaksi kedekatan emosional Producer bersama idol. |
| `[ ]` | **Cerita Support Card** | `resource/adv_csprt_*.txt` | 529 file | Belum Mulai. Cerita latar belakang dari kartu pendukung idol. |
| `[ ]` | **Cerita Skenario Produksi (P-Story)** | `resource/adv_pstory_*.txt` | 611 file | Belum Mulai. Skenario perjalanan audisi dan ujian produce. |
| `[ ]` | **Event Pilihan Produksi (P-Event)** | `resource/adv_pevent_*.txt` | 1.105 file | Belum Mulai. Event acak dan pilihan percabangan saat sesi Produce. |

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
| 2026-10-15 | `masterTrans/ProduceCard.json` (Nama Kartu) | Terjemahan | Menerjemahkan 1.748 nama kartu skill (457 nama dasar unik) ke Bahasa Indonesia, termasuk penyelarasan seluruh seri kartu dasar (`Dasar ...`). `ProduceCard.json` **100% SELESAI**. |
| 2026-10-15 | `generic.json` & `localization.json` | UI Fix | Memperpendek teks tombol kartu `Konfirmasi Penguatan` menjadi `Penguatan` dan `Konfirmasi Kustomisasi` menjadi `Kustomisasi` agar presisi di batas tombol antarmuka game. |
| 2026-10-15 | `masterTrans/ProduceDescriptionExamEffect.json` | Terjemahan | Menerjemahkan seluruh 89 badge efek status buff/debuff in-game (Kesan Baik, Semangat, Genki, Pengurangan Biaya Stamina, Daya Penuh, dll.). **100% SELESAI (89 entri)**. |
| 2026-10-15 | `masterTrans/ProduceDescriptionLabel.json` | Terjemahan | Menerjemahkan seluruh 228 label mekanik gameplay dan seluruh fragmen deskripsi/tooltip penjelasannya (termasuk `1x saat Lesson`, `Efek Langsung`, dan filter lesson). **100% SELESAI (228 label)**. |
| 2026-10-15 | `masterTrans/ProduceDrink.json` | Terjemahan | Menerjemahkan seluruh 29 nama P-Drink dan seluruh fragmen teks efek penggunaannya ke Bahasa Indonesia alami. **100% SELESAI (29 P-Drink)**. |
| 2026-10-15 | `masterTrans/ProduceItem.json` | Terjemahan | Menerjemahkan seluruh 7.057 fragmen efek deskripsi dan 1.088 nama P-Item Produce (534 nama dasar unik, varian +) ke Bahasa Indonesia. **100% SELESAI (1.088 P-Item)**. |
| 2026-10-15 | `masterTrans/SupportCard.json` | Terjemahan | Menerjemahkan seluruh 208 nama Support Card (R, SR, SSR) dan 208 teks tingkat aktivasi probabilitas efek (/ Tinggi, / Sedang, / Rendah). **100% SELESAI (208 Support Card)**. |
| 2026-10-15 | `masterTrans/Item.json` | Terjemahan | Menerjemahkan seluruh 368 item tas/inventaris (319 nama unik, Piece idol, tiket gacha, koin, buku pelajaran, 115 deskripsi, 44 rute perolehan). **100% SELESAI (368 Item)**. |
| 2026-10-15 | `README.md` & `docs/` | Dokumentasi | Menambahkan panduan pemakaian dan instalasi Localify untuk Android (`docs/android.md`) dan PC DMM (`docs/dmm-games.md`). |
| 2026-10-15 | `masterTrans/Tips.json` | Terjemahan | Menerjemahkan seluruh tips layar loading gameplay, level producer, penukaran uang/AP, dan akademi Hatsuboshi. **100% SELESAI (34 Tips)**. |
| 2026-10-15 | `IdolCard.json` & `IdolCardSkin.json` | Kebijakan Proyek | Menetapkan kebijakan mempertahankan nama resmi asli kartu Produce Idol dan skin (School Life, First Love, Fighting My Way, Fluorite, dll.) agar sinkron dengan wiki resmi. |
