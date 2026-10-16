# Progres — Gakumas-Translation-Data-ID

Dokumen ini memantau status pengerjaan lokalisasi Bahasa Indonesia untuk seluruh komponen game Gakuen Idolm@ster secara transparan dan terperinci.

---

## Ringkasan Progres Global

| Kategori | Cakupan File | Status Saat Ini | Detail Kemajuan |
|---|---|---|---|
| **Fase 1: UI & Sistem Inti** | 24 berkas JSON | **100% Selesai (11 Aktif, 13 Standby)** | Seluruh UI utama, kamus generik, tutorial, teks item, event blurb, kustom kartu, misi, flavor, dan trash.json (11.024 key tuntas) + 13 berkas template engine standby. |
| **Lirik Lagu Panggung & MV (`lyrics/`)** | 63 berkas JSON | **100% Selesai (1.877/1.877 baris)** | **Seluruh 4 Batch Tuntas**. Seluruh 19 lagu tema all songs, 29 lagu solo idol, dan 5 lagu unit tuntas diterjemahkan puitis & berirama alami. |
| **Fase 2: Master Database Gameplay (`masterTrans`)** | 108 berkas JSON | **100% Selesai (99 Diterjemahkan, 9 Di-skip)** | **108 Berkas Tuntas**. Seluruh database gameplay master (Fase 2.1 s/d 2.6) 100% tuntas dalam Bahasa Indonesia. |
| **Fase 3: Cerita Prolog, Tutorial & Unit (`resource/`)** | 116 berkas TXT | Belum Mulai | Naskah cerita pembuka (33 file), tutorial visual novel (17 file), dan cerita unit utama (66 file). |
| **Fase 4: Cerita Karakter, Event & Stage (`resource/`)** | 3.414 berkas TXT | **Aktif Dikerjakan (415/3.414 File)** | Cerita Support Card R tuntas 100% (26 file, 471 dialog); Support Card SR tuntas 100% (164 file, 3.196 dialog); Support Card SSR aktif (225/339 file, 4.467 dialog); cerita kandidat idol (354 file), commu bond (494 file), sisa support card SSR (114 file), p-story (611 file), pevent & event (1.256 file), live mc (106 file), p-growth (39 file), p-result (13 file), produce commu (11 file), tower commu (1 file). |
| **TOTAL DATA GAME** | **3.725 berkas** | **Aktif Dikerjakan** | **610 Berkas Tuntas (100% UI, Lirik & MasterDB + 415 Cerita Support Card Selesai)**, 3.115 Naskah Cerita Resource Siap Dikerjakan. |

---

## Keterangan Status Simbol

- `[x]` **Selesai**: Terjemahan tuntas 100%, divalidasi sintaksis JSON, dan lolos uji konsistensi glosarium.
- `[-]` **Di-skip / Teknis**: Berkas konfigurasi engine internal tanpa teks tampilan pemain.
- `[ ]` **Belum Mulai**: Berkas database belum diterjemahkan dan siap dikerjakan.

---

## Fase 1 — UI & Sistem Inti (Status: 100% Selesai)

Target: Seluruh antarmuka game, menu, tombol, item, misi, tutorial, dan string UI umum berbahasa Indonesia. **Status: 11 / 11 Berkas Teks Tuntas (11.024 Key) + 13 Berkas Template Standby (Total: 24 Berkas)**.

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
| `[-]` | `genericTrans/index/*.fmt.json` & template (13 file) | Berkas Template Engine Localify | 13 berkas | Engine System | **Standby / Engine Template**. 13 berkas wadah template format Localify (`achievement[.fmt]`, `Bond_level[.fmt]`, `Description_Split`, `News.fmt`, `Photo`, `ProduceSkill`, `chara_profiles`, `maintance`, `media`, `term[.fmt]`). Tiap file berisi 1 dummy key `{"": ""}` kosong untuk cadangan injeksi engine. |

---

## Lirik Lagu Panggung & Live MV (`local-files/genericTrans/lyrics/`)

Target: Menerjemahkan seluruh teks subtitle lirik lagu saat penampilan panggung live 3D dan Music Video (MV) idol agar pemain Indonesia dapat menghayati makna emosional lagu secara mendalam.

Status Keseluruhan Lirik: **63 Lagu Selesai (1.877 baris)** | **0 Dalam Antrean** | Total: **63 Berkas / 1.877 Baris** (Progres: **100% Selesai**)

### Rincian Pembagian Batch Lirik Lagu

| Status | Batch | Cakupan Berkas | Karakter / Kategori | Volume | Keterangan & Progres |
|---|---|---|---|---|---|
| `[x]` | **Batch 1** | `all_001` s/d `all_019` (19 berkas) | Lagu Bersama & Lagu Tema Utama (*Hajime*, *Campus mode!!*, *Kimi to Semi Blue*, *GO MY WAY!!*, dll.) | 450 baris | **100% Selesai**. Diterjemahkan puitis, berirama alami, dan mempertahankan frasa panggung ikonik. |
| `[x]` | **Batch 2** | `amao_*`, `atbm_*`, `fktn_*`, `hmsz_*`, `hrnm_*` (14 berkas) | Lagu Solo Idol (Bagian 1): Aoi, Tsubame, Kotone, Misuzu, Rinami | 436 baris | **100% Selesai**. Diterjemahkan puitis, bernuansa emosional sesuai karakter masing-masing idol. |
| `[x]` | **Batch 3** | `hski_*`, `hume_*`, `jsna_*`, `kcna_*`, `klij_*`, `kllj_*` (15 berkas) | Lagu Solo Idol (Bagian 2): Saki, Ume, Sena, China, Lilja | 510 baris | **100% Selesai**. Diterjemahkan puitis, berirama alami, nuansa kepribadian karakter idol kuat. |
| `[x]` | **Batch 4** | `shro_*`, `ssmk_*`, `ttmr_*`, `unit_*` (15 berkas) | Lagu Solo Idol (Bagian 3) & Unit: Hiro, Sumika, Temari, serta Unit (*Begrazia*, *Re;IRIS*, dll.) | 481 baris | **100% Selesai**. Diterjemahkan puitis, selaras dengan kepribadian idol dan harmoni unit. |

#### Rincian Lagu Batch 1 (Selesai 100%):
- `all_001_Hajime.json` — **初 (Hajime)** (22 baris)
- `all_002_Campusmode.json` — **Campus mode!!** (39 baris)
- `all_003_Kimitosemiblue.json` — **キミとセミブルー (Kimi to Semi Blue)** (29 baris)
- `all_004_Kamurogiku.json` — **冠菊 (Kamurogiku)** (19 baris)
- `all_005_CapriccioOfMasquerades.json` — **仮装狂騒曲 (Capriccio of Masquerades)** (34 baris)
- `all_006_WhiteNightWhiteWish.json` — **White Night! White Wish!** (15 baris)
- `all_007_HappyMillefeuille.json` — **ハッピーミルフィーユ (Happy Millefeuille)** (23 baris)
- `all_008_ItsAWalkInThePark.json` — **It's a walk in the park** (19 baris)
- `all_009_InThawedSnow.json` — **雪解けに (In Thawed Snow)** (14 baris)
- `all_010_SakuraPhotograph.json` — **Sakura Photograph** (12 baris)
- `all_011_HowlingOverTheWorld.json` — **Howling over the World** (23 baris)
- `all_012_MirakuluNaNow.json` — **ミラクル・ナ・ナウ！ (Miracle na Now!)** (35 baris)
- `all_013_GamusharaNiIkou.json` — **がむしゃらに行こう！ (Gamushara ni Ikou!)** (24 baris)
- `all_014_ENDLESSDANCE.json` — **ENDLESS DANCE** (17 baris)
- `all_015_Shirube.json` — **標 (Shirube - Mars Hatsuboshi)** (13 baris)
- `all_016_GarakutaRoad.json` — **ガラクタロード (Garakuta Road)** (43 baris)
- `all_017_GoMyWay.json` — **GO MY WAY!!** (28 baris)
- `all_018_NeeIcchauYo.json` — **ねえ、言っちゃうよ (Nee, Icchau yo)** (21 baris)
- `all_019_Agitato.json` — **Agitato** (20 baris)

#### Rincian Lagu Batch 2 (Selesai 100%):
- `amao_001_Fluorite.json` — **Fluorite** / Aoi (23 baris)
- `amao_002_FeelJewelDream.json` — **Feel Jewel Dream** / Aoi (28 baris)
- `amao_004_Mite.json` — **Feel Jewel Dream (Short/Alternative)** / Aoi (29 baris)
- `atbm_001_RironBusouShite.json` — **理論武装して (Riron Busou Shite)** / Tsubame (16 baris)
- `atbm_004_Kuraiai.json` — **喰らい愛 (Kuraiai)** / Tsubame (24 baris)
- `fktn_001_SekaiichiKawaiiWatashi.json` — **世界一可愛い私 (Sekaiichi Kawaii Watashi)** / Kotone (39 baris)
- `fktn_002_YellowBigBang.json` — **Yellow Big Bang!** / Kotone (52 baris)
- `fktn_004_ShukiShuki.json` — **スキスキ (Shuki Shuki)** / Kotone (57 baris)
- `hmsz_001_MoonTurtle.json` — **Moon Turtle** / Misuzu (22 baris)
- `hmsz_002_Superlative.json` — **Superlative** / Misuzu (25 baris)
- `hmsz_004_VEIL.json` — **VEIL** / Misuzu (11 baris)
- `hrnm_001_ClumsyTrick.json` — **Clumsy Trick** / Rinami (40 baris)
- `hrnm_002_LUV.json` — **L.U.V** / Rinami (38 baris)
- `hrnm_004_36CUBU.json` — **36℃UBU** / Rinami (32 baris)

#### Rincian Lagu Batch 3 (Selesai 100%):
- `hski_001_FightingMyWay.json` — **Fighting My Way** / Saki (55 baris)
- `hski_002_BoomBoomPow.json` — **Boom Boom Pow** / Saki (43 baris)
- `hski_004_WildestFlower.json` — **Wildest Flower** / Saki (40 baris)
- `hume_001_TheRollingRiceball.json` — **The Rolling Riceball** / Ume (45 baris)
- `hume_002_Gu-Su-Pi.json` — **ぐーすーぴー (Gu-Su-Pi)** / Ume (60 baris)
- `hume_004_MashiroPage.json` — **ましろページ (Mashiro Page)** / Ume (23 baris)
- `jsna_001_TinyAmbition.json` — **小さな野望 (Tiny Ambition)** / Sena (23 baris)
- `jsna_002_OurChant.json` — **Our Chant** / Sena (36 baris)
- `jsna_004_Sekirara.json` — **赤裸々 (Sekirara)** / Sena (25 baris)
- `kcna_001_WonderScale.json` — **Wonder Scale** / China (27 baris)
- `kcna_002_EveryStepisforDiscovery.json` — **Every Step is for Discovery** / China (28 baris)
- `kcna_004_BravePromise.json` — **Brave Promise** / China (15 baris)
- `klij_004_Atmosphere.json` — **Atmosphere** / Lilja (23 baris)
- `kllj_001_Hakusen.json` — **白線 (Hakusen)** / Lilja (39 baris)
- `kllj_002_Aurora.json` — **極光 (Aurora)** / Lilja (28 baris)

#### Rincian Lagu Batch 4 (Selesai 100%):
- `shro_001_Koukei.json` — **光景 (Koukei)** / Hiro (28 baris)
- `shro_002_Contrast.json` — **コントラスト (Contrast)** / Hiro (43 baris)
- `shro_004_Sunfaded.json` — **Sunfaded** / Hiro (21 baris)
- `shro_006_Me.json` — **仮面 (Me)** / Hiro (11 baris)
- `ssmk_001_TameLieOneStep.json` — **Tame-Lie-One-Step** / Sumika (41 baris)
- `ssmk_002_MyHiddenSelf.json` — **裏腹な自分 (My Hidden Self)** / Sumika (33 baris)
- `ssmk_004_LoveJoy.json` — **Love & Joy** / Sumika (46 baris)
- `ttmr_001_LunaSayMaybe.json` — **Luna say maybe** / Temari (43 baris)
- `ttmr_002_IVY.json` — **アイヴィ (IVY)** / Temari (35 baris)
- `ttmr_004_IttaiItsukara.json` — **いったいいつから (Ittai Itsu kara)** / Temari (30 baris)
- `unit_001_AmeagariNoIris.json` — **雨上がりのアイリス (Ameagari no Iris)** / Begrazia (26 baris)
- `unit_002_StarMine.json` — **Star Mine** / Re;IRIS (45 baris)
- `unit_003_MichinaruHirogaru.json` — **未知なるひろがる (Michinaru Hirogaru)** / Unit (33 baris)
- `unit_004_TokimekiEmotion.json` — **ときめきエモーション (Tokimeki Emotion)** / Unit (29 baris)
- `unit_005_SugarFlavor.json` — **Sugar Flavor** / Unit (17 baris)

---

## Fase 2 — Master Database Gameplay (`local-files/masterTrans/`)

Target: Menyelesaikan seluruh data gameplay di folder `local-files/masterTrans/` (total 108 berkas) agar fitur **MasterDB Localization** pada Localify bekerja 100% dalam Bahasa Indonesia tanpa ada teks sistem yang bocor.

Status Keseluruhan Fase 2: **99 Selesai** | **0 Belum Mulai** | **9 Di-skip (Nama Karakter/Musik/Regulasi)** (Total: 108 Berkas) — **100% TUNTAS**

### 2.1 Inti Produce, Kartu Skill & Pertandingan (Lesson & Audition) — 37 Berkas (Status: 100% Selesai)

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Kartu Skill Produce** | `masterTrans/ProduceCard.json` | 1748 entri | **100% Selesai**. Seluruh 447 fragmen efek (11.340 entri) dan 1.748 nama kartu (457 nama unik) telah diterjemahkan. |
| `[x]` | **P-Item (Item Produce)** | `masterTrans/ProduceItem.json` | 1088 entri | **100% Selesai**. Seluruh 7.057 fragmen deskripsi efek dan 1.088 nama item Produce (534 nama unik) telah diterjemahkan. |
| `[x]` | **P-Drink (Minuman Produce)** | `masterTrans/ProduceDrink.json` | 29 entri | **100% Selesai**. Seluruh 29 nama minuman P-Drink dan seluruh efek deskripsinya telah diterjemahkan. |
| `[x]` | **Badge Status Efek Game** | `masterTrans/ProduceDescriptionExamEffect.json` | 89 entri | **100% Selesai**. Seluruh 89 badge efek status buff/debuff (Kesan Baik, Semangat, Genki, Pengurangan Biaya Stamina, dll.). |
| `[x]` | **Label & Tooltip Mekanik** | `masterTrans/ProduceDescriptionLabel.json` | 228 entri | **100% Selesai**. Seluruh 228 label mekanik gameplay dan seluruh fragmen deskripsi/tooltip penjelasannya. |
| `[x]` | **Deskripsi Efek Produce** | `masterTrans/ProduceDescriptionProduceEffect.json` | 92 entri | **100% Selesai**. Seluruh 92 efek perolehan parameter, pemulihan stamina, diskon konsultasi, dan bonus produce. |
| `[x]` | **Efek Pertumbuhan Kartu** | `masterTrans/ProduceDescriptionProduceCardGrowEffect.json` | 53 entri | **100% Selesai**. Seluruh 53 deskripsi efek pertumbuhan dan penyesuaian biaya/parameter kartu skill. |
| `[x]` | **Teks Pergantian Kartu** | `masterTrans/ProduceDescriptionSwap.json` | 78 entri | **100% Selesai**. Seluruh 78 teks instruksi swap istilah giliran, ujian, lesson, dan posisi deck. |
| `[x]` | **Label Rencana Produce** | `masterTrans/ProduceDescriptionProducePlan.json` | 4 entri | **100% Selesai**. Kategori rencana Umum, Khusus Sense, Khusus Logic, dan Khusus Anomaly. |
| `[x]` | **Label Tipe Produce** | `masterTrans/ProduceDescriptionProduceType.json` | 5 entri | **100% Selesai**. Jalur Khusus Hajime, Khusus N.I.A, Khusus H.I.F, Kualifikasi, dan Final. |
| `[x]` | **Label Tahapan Produce** | `masterTrans/ProduceDescriptionProduceStep.json` | 2 entri | **100% Selesai**. Teks tahapan Jalan-jalan dan Hadiah Produce. |
| `[x]` | **Kustomisasi Kartu Skill** | `masterTrans/ProduceCardCustomize.json` | 347 entri | **100% Selesai**. Seluruh 347 entri deskripsi kustomisasi kartu skill Produce. |
| `[x]` | **Pencarian Kartu Skill** | `masterTrans/ProduceCardSearch.json` | 283 entri | **100% Selesai**. Seluruh 283 entri filter, target deck/hand/exclusion, dan nama kartu skill pencarian Produce. |
| `[x]` | **Enchant Status Kartu** | `masterTrans/ProduceCardStatusEnchant.json` | 79 entri | **100% Selesai**. Seluruh 79 entri deskripsi status enchant tambahan (pertumbuhan, giliran, penggunaan). |
| `[x]` | **Database Efek Ujian/Audisi** | `masterTrans/ProduceExamEffect.json` | 2112 entri | **100% Selesai**. Seluruh 2.112 entri kumpulan formula dan efek aksi saat lesson/audition Produce. |
| `[x]` | **Status Enchant Ujian** | `masterTrans/ProduceExamStatusEnchant.json` | 2054 entri | **100% Selesai**. Seluruh 2.054 entri efek status enchant khusus saat evaluasi audisi. |
| `[x]` | **Grup Efek Gimmick Ujian** | `masterTrans/ProduceExamGimmickEffectGroup.json` | 3762 entri | **100% Selesai**. Seluruh 3.762 entri gimmick khusus rintangan dan mekanik panggung ujian. |
| `[x]` | **Pemicu Aksi Ujian** | `masterTrans/ProduceExamTrigger.json` | 691 entri | **100% Selesai**. Seluruh 691 entri syarat aktivasi pemicu efek skill saat ujian berlangsung. |
| `[x]` | **Nama NPC Rival Audisi** | `masterTrans/ProduceExamBattleNpcMob.json` | 62 entri | **100% Selesai**. Batas Skor diterjemahkan, nama idol/NPC tetap sesuai aslinya. |
| `[x]` | **Panel Pertumbuhan Idol** | `masterTrans/ProduceGrowthPanel.json` | 50 entri | **100% Selesai**. Seluruh 50 entri peningkatan status idol (Vocal, Dance, Visual, SP Lesson, P-Point) pada panel perkembangan. |
| `[x]` | **Kategori Panduan Kartu** | `masterTrans/ProduceGuideProduceCardCategory.json` | 67 entri | **100% Selesai**. Seluruh 67 label kategori rekomendasi kartu skill (Peningkat Semangat, Genki, dll.). |
| `[x]` | **Grup Panduan Kartu** | `masterTrans/ProduceGuideProduceCardCategoryGroup.json` | 16 entri | **100% Selesai**. Deskripsi panduan sinergi kartu (Semangat, Kesan Baik, Fokus, Kondisi Baik, dll.). |
| `[x]` | **Sampel Deck Panduan** | `masterTrans/ProduceGuideProduceCardSampleDeckCategory.json` | 65 entri | **100% Selesai**. Seluruh 65 label susunan contoh deck rekomendasi pemula. |
| `[x]` | **Sesi Lesson Produce** | `masterTrans/ProduceStepLesson.json` | 955 entri | **100% Selesai**. Seluruh 955 sesi latihan Produce (Lesson SP, Lesson Normal, Lesson Intensif, dll.). |
| `[x]` | **Detail Event Langkah Produce** | `masterTrans/ProduceStepEventDetail.json` | 6921 entri | **100% Selesai**. Seluruh 6.921 detail event langkah Produce, nama event idol/support, dan hadiah pilihan. |
| `[x]` | **Saran Pilihan Event** | `masterTrans/ProduceStepEventSuggestion.json` | 3066 entri | **100% Selesai**. Seluruh 3.066 petunjuk saran keputusan, peluang sukses/gagal, dan efek perolehan kartu/P-Drink. |
| `[x]` | **Slot Tantangan Produce** | `masterTrans/ProduceChallengeSlot.json` | 54 entri | **100% Selesai**. Seluruh syarat pembuka slot tantangan Master Produce. |
| `[x]` | **Pertumbuhan Karakter Event** | `masterTrans/ProduceEventCharacterGrowth.json` | 39 entri | **100% Selesai**. Seluruh 39 judul dan syarat batas parameter event pertumbuhan karakter idol. |
| `[x]` | **Grup Skenario Produce** | `masterTrans/ProduceGroup.json` | 3 entri | **100% Selesai**. Nama dan sinopsis skenario Hajime, NEXT IDOL AUDITION, dan Hatsuboshi IDOL FESTIVAL. |
| `[x]` | **Peringkat Skor Tinggi Produce** | `masterTrans/ProduceHighScore.json` | 19 entri | **100% Selesai**. Seluruh nama event skor tinggi Bulan Peningkatan Idol Kunio Juo. |
| `[x]` | **Navigasi & Dialog Asari-sensei** | `masterTrans/ProduceNavigation.json` | 352 entri | **100% Selesai**. Seluruh 352 instruksi navigasi bimbingan Produce dan tips taktik ujian. |
| `[x]` | **Musim Kompetisi Produce** | `masterTrans/ProduceSeason.json` | 2 entri | **100% Selesai**. Penamaan Musim 0 dan Musim 1 kompetisi Produce. |
| `[x]` | **Skill Pasif Produce** | `masterTrans/ProduceSkill.json` | 1536 entri | **100% Selesai**. Seluruh 1.536 nama dan efek skill pasif Produce idol dan support. |
| `[x]` | **Item Kustomisasi Produce** | `masterTrans/ProduceCustomizeItem.json` | 180 entri | **100% Selesai**. Seluruh 180 nama item pesona kustomisasi (Beruang, Boneka, Kelinci, Burung Parkit, Robot) dan efek Produce. |
| `[x]` | **Grup Efek Kartu** | `masterTrans/EffectGroup.json` | 67 entri | **100% Selesai**. Seluruh 67 nama klasifikasi grup efek skill Produce (Genki, Semangat, Fokus, dll.). |
| `[x]` | **Transisi Ujian Seminar** | `masterTrans/SeminarExamTransition.json` | 12 entri | **100% Selesai**. Seluruh 12 nama grup dan instruksi modul ujian seminar taktik Produce. |
| `[x]` | **Mode Skenario Produce** | `masterTrans/Produce.json` | 8 entri | **100% Selesai**. Mode tingkat kesulitan Reguler, Pro, Master, Legend, Babak Kualifikasi, dan Babak Final. |

---

### 2.2 Kartu Idol, Karakter & Kostum — 11 Berkas (Status: 100% Selesai)

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Support Card** | `masterTrans/SupportCard.json` | 208 entri | **100% Selesai**. Seluruh 208 nama Support Card (R, SR, SSR) dan 208 teks tingkat aktivasi efek telah diterjemahkan. |
| `[-]` | **Produce Idol Card (P-Idol)** | `masterTrans/IdolCard.json` | 156 entri | **Di-skip (Nama Kartu Asli)**. Nama gelar kartu Produce Idol dibiarkan sesuai nama aslinya (School Life, First Love, Fighting My Way, Fluorite, dll.) agar konsisten dengan wiki dan rilis resmi. |
| `[-]` | **Skin Kartu Produce Idol** | `masterTrans/IdolCardSkin.json` | 306 entri | **Di-skip (Nama Skin Asli)**. Nama variasi skin kartu Produce Idol dibiarkan sesuai nama rilis resminya. |
| `[x]` | **Kostum Panggung & Pakaian** | `masterTrans/Costume.json` | 566 entri | **100% Selesai**. Nama busana kasual, seragam, pakaian event, dan seluruh deskripsi syarat perolehan (Idol Road, Rank Bakat, Pass Misi) diterjemahkan. |
| `[x]` | **Aksesori Kepala & Gaya Rambut** | `masterTrans/CostumeHead.json` | 416 entri | **100% Selesai**. Nama gaya rambut kasual, kacamata, pita, telinga hewan, tiara, dan seluruh deskripsi syarat perolehan diterjemahkan. |
| `[-]` | **Data Karakter Idol & Staf** | `masterTrans/Character.json` | 24 entri | **Di-skip (Nama Karakter Asli)**. Nama karakter idol, guru, dan pelatih tetap menggunakan nama resmi aslinya sesuai instruksi proyek. |
| `[-]` | **Nama Karakter Naskah Cerita** | `masterTrans/CharacterAdv.json` | 25 entri | **Di-skip (Nama Karakter Asli)**. Nama tampilan karakter pada naskah dialog ADV tetap menggunakan nama resmi aslinya. |
| `[x]` | **Profil Detail Karakter** | `masterTrans/CharacterDetail.json` | 181 entri | **100% Selesai**. Biodata pengantar profil idol, hobi, keahlian khusus, kelas, zodiak, tangan dominan, dan tanggal lahir diterjemahkan ke Bahasa Indonesia natural. |
| `[x]` | **Level Keakraban (Dearness/Bond)** | `masterTrans/CharacterDearnessLevel.json` | 471 entri | **100% Selesai**. Seluruh 471 syarat pembuka level keakraban tiap idol (minggu Produce, audisi, True End, pencapaian) diterjemahkan. |
| `[x]` | **Pesan Notifikasi Karakter** | `masterTrans/CharacterPushMessage.json` | 169 entri | **100% Selesai**. Seluruh 169 pesan notifikasi push 13 idol ke Producer diterjemahkan sesuai karakter masing-masing (nama idol pada judul dipertahankan). |
| `[x]` | **Filter Skill Support Card** | `masterTrans/SupportCardProduceSkillFilter.json` | 51 entri | **100% Selesai**. Seluruh 51 label filter pencarian efek skill support card pada menu deck Produce. |

---

### 2.3 Inventaris, Toko & Gacha — 7 Berkas (Status: 100% Selesai)

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Item Tas, Mata Uang & Tiket** | `masterTrans/Item.json` | 368 entri | **100% Selesai**. Seluruh 368 item tas, Piece idol, tiket gacha, koin, buku pelajaran, deskripsi, dan rute perolehan telah diterjemahkan. |
| `[x]` | **Tombol Banner Gacha** | `masterTrans/GashaButton.json` | 108 entri | **100% Selesai**. Seluruh teks tombol tarik gacha (Gacha 10x Jewel Beli, Gacha Tiket, Gacha Item, Step-up, Pasti SSR, dll.) dan teks banner promosi. |
| `[x]` | **Tombol Gacha Koin** | `masterTrans/CoinGashaButton.json` | 38 entri | **100% Selesai**. Seluruh teks tombol penarikan box gacha koin event ("Tarik", "Tarik 1x"). |
| `[x]` | **Kategori Toko** | `masterTrans/Shop.json` | 5 entri | **100% Selesai**. Seluruh 5 kategori menu toko (Kostum, Jewel, Paket, Pass, Pembayaran). |
| `[x]` | **Item Toko Penukaran** | `masterTrans/ShopItem.json` | 285 entri | **100% Selesai**. Seluruh 285 item dan paket penawaran khusus toko (Paket Anniversary, Paket Piece Idol, Paket Celemek Anak, Busana Kasual, Jewel, dll.). |
| `[x]` | **Produk Penjualan & Pemulihan** | `masterTrans/ShopProduct.json` | 14 entri | **100% Selesai**. Seluruh produk pembelian Jewel dan aktivasi Premium Mission Pass. |
| `[x]` | **Kategori Penukaran Item** | `masterTrans/ExchangeItemCategory.json` | 6 entri | **100% Selesai**. Seluruh 6 kategori tab penukaran item di exchange shop (Semua, Piece, Support Card, Lainnya). |

---

### 2.4 Tugas, Misi, Achievement & Ranking — 14 Berkas (Status: 100% Selesai)

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Tugas Utama Producer** | `masterTrans/MainTask.json` | 310 entri | **100% Selesai**. Seluruh judul, deskripsi beranda, dan petunjuk tugas utama Producer. |
| `[x]` | **Grup Tugas Utama** | `masterTrans/MainTaskGroup.json` | 4 entri | **100% Selesai**. Seluruh nama kelompok bab tugas utama Producer. |
| `[x]` | **Misi Gameplay** | `masterTrans/Mission.json` | 3494 entri | **100% Selesai**. Seluruh 3.494 teks misi harian, mingguan, event, dan debut idol ke Bahasa Indonesia natural. |
| `[x]` | **Kelompok Misi** | `masterTrans/MissionGroup.json` | 282 entri | **100% Selesai**. Seluruh nama kategori dan tab kelompok misi permainan. |
| `[x]` | **Pass Misi Bulanan** | `masterTrans/MissionPass.json` | 30 entri | **100% Selesai**. Seluruh nama dan deskripsi tingkatan hadiah Pass Misi bulanan. |
| `[x]` | **Poin Pass Misi** | `masterTrans/MissionPassPoint.json` | 1 entri | **100% Selesai**. Nama satuan poin kemajuan Pass Misi ("Poin Pass"). |
| `[x]` | **Poin Hadiah Misi** | `masterTrans/MissionPoint.json` | 35 entri | **100% Selesai**. Seluruh nama poin milestone penyelesaian misi. |
| `[x]` | **Lembar Misi Panel** | `masterTrans/MissionPanelSheet.json` | 57 entri | **100% Selesai**. Seluruh nama lembar misi papan panel bingo debut idol. |
| `[x]` | **Grup Lembar Misi Panel** | `masterTrans/MissionPanelSheetGroup.json` | 49 entri | **100% Selesai**. Seluruh nama kelompok lembar misi panel bertingkat. |
| `[x]` | **Misi Rilis Harian** | `masterTrans/MissionDailyReleaseGroup.json` | 31 entri | **100% Selesai**. Seluruh nama kelompok misi pembuka harian kampanye. |
| `[x]` | **Achievement & Gelar Idol** | `masterTrans/Achievement.json` | 1242 entri | **100% Selesai**. Seluruh 1.242 achievement, gelar, dan trofi kebanggaan (nama idol/kartu tetap original). |
| `[x]` | **Badge Penghargaan** | `masterTrans/Badge.json` | 364 entri | **100% Selesai**. Seluruh 364 nama dan deskripsi badge penghargaan pencapaian ranking Produce. |
| `[x]` | **Peringkat Producer** | `masterTrans/ProducerRanking.json` | 5 entri | **100% Selesai**. Musim ranking evaluasi Producer (Musim 0 s/d 4). |
| `[x]` | **Konfigurasi Rating Contest** | `masterTrans/PvpRateConfig.json` | 54 entri | **100% Selesai**. Seluruh keterangan tier rating kompetisi panggung antarpemain ("Contest Pertama" & S2-S54). |

---

### 2.5 Cerita Master & Cuplikan Narasi — 11 Berkas (Status: 100% Selesai)

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Judul Episode Cerita Produce** | `masterTrans/ProduceStory.json` | 3454 entri | **100% Selesai**. Seluruh 1.349 judul episode cerita dan 75 syarat kondisi interaksi selama masa Produce. |
| `[x]` | **Flavor Text Support Card** | `masterTrans/SupportCardFlavor.json` | 583 entri | **100% Selesai**. Seluruh 583 teks cuplikan dialog dan narasi suasana di Support Card telah diterjemahkan secara alami sesuai kepribadian masing-masing idol. |
| `[x]` | **Daftar Cerita & Episode** | `masterTrans/Story.json` | 311 entri | **100% Selesai**. Seluruh 311 judul episode cerita umum, ulang tahun idol/Producer, dan cerita unit Hatsuboshi. |
| `[x]` | **Judul Event Cerita** | `masterTrans/StoryEvent.json` | 35 entri | **100% Selesai**. Seluruh 35 nama event cerita berkala, tur live, dan festival sekolah. |
| `[x]` | **Grup Alur Cerita** | `masterTrans/StoryGroup.json` | 100 entri | **100% Selesai**. Seluruh 100 nama kelompok bab alur cerita komprehensif. |
| `[x]` | **Bab Cerita Utama** | `masterTrans/MainStoryChapter.json` | 4 entri | **100% Selesai**. Seluruh 4 judul dan sinopsis bab cerita utama sekolah idol (Bab 1 s/d Bab 4). |
| `[x]` | **Bagian Cerita Utama** | `masterTrans/MainStoryPart.json` | 1 entri | **100% Selesai**. Judul bagian cerita panggung utama ("Bagian 1"). |
| `[x]` | **Judul Cerita ADV Produce** | `masterTrans/ProduceAdv.json` | 32 entri | **100% Selesai**. Seluruh 32 judul segmen cerita Produce (Sehari sebelum audisi, Awal lesson, Hasil akhir, dll.). |
| `[x]` | **Percabangan Cerita Produce** | `masterTrans/ProduceSplitAdv.json` | 26 entri | **100% Selesai**. Seluruh 26 judul segmen percabangan Kualifikasi & Final H.I.F. |
| `[x]` | **Cerita Khusus Karakter Produce** | `masterTrans/ProduceCharacterAdv.json` | 10 entri | **100% Selesai**. Judul cerita interaksi khusus idol (Ep.10.5). |
| `[x]` | **Label Kategori Event** | `masterTrans/EventLabel.json` | 13 entri | **100% Selesai**. Seluruh 13 label penanda kategori event cerita khusus. |

---

### 2.6 Panduan, Tips, Bantuan, Audio, Media & Aset — 26 Berkas

| Status | Komponen | Berkas di `local-files/` | Volume Data | Status Detail & Keterangan |
|---|---|---|---|---|
| `[x]` | **Tips Layar Loading** | `masterTrans/Tips.json` | 34 entri | **100% Selesai**. Seluruh tips gameplay, fitur level producer, penukaran uang/AP, dan akademi Hatsuboshi telah diterjemahkan. |
| `[x]` | **Tutorial Master Sistem** | `masterTrans/Tutorial.json` | 217 entri | **100% Selesai**. Seluruh 217 judul dan teks panduan tutorial sistem permainan ke Bahasa Indonesia. |
| `[x]` | **Langkah Tutorial Produce** | `masterTrans/TutorialProduceStep.json` | 12 entri | **100% Selesai**. Seluruh 12 nama tahapan panduan latihan dan ujian Produce. |
| `[x]` | **Artikel Panduan Bantuan** | `masterTrans/HelpContent.json` | 273 entri | **100% Selesai**. Seluruh 273 judul artikel panduan bantuan lengkap in-game. |
| `[x]` | **Kategori Panduan Bantuan** | `masterTrans/HelpCategory.json` | 36 entri | **100% Selesai**. Seluruh 36 nama kategori dan teks pengantar panduan bantuan. |
| `[x]` | **Syarat Pembuka Fitur Game** | `masterTrans/FeatureLock.json` | 13 entri | **100% Selesai**. Seluruh 13 syarat dan petunjuk rute pembuka fitur terkunci. |
| `[x]` | **Pose Pemotretan Idol** | `masterTrans/PhotoPose.json` | 1092 entri | **100% Selesai**. Seluruh 1.092 penamaan 71 ragam gaya dan pose foto idol di studio pemotretan. |
| `[x]` | **Latar Belakang Studio Foto** | `masterTrans/PhotoBackground.json` | 9 entri | **100% Selesai**. Seluruh 9 nama latar pemandangan studio foto. |
| `[x]` | **Ekspresi Wajah Pemotretan** | `masterTrans/PhotoFacialMotionGroup.json` | 4 entri | **100% Selesai**. Seluruh 4 nama gerakan ekspresi wajah idol (Senyum, Marah, Bingung, Malu). |
| `[x]` | **Bingkai Kartu Nama (Meishi)** | `masterTrans/MeishiBaseAsset.json` | 301 entri | **100% Selesai**. Seluruh 301 nama template dasar kartu nama Producer dan ranking event. |
| `[x]` | **Stiker Ilustrasi Meishi** | `masterTrans/MeishiIllustrationAsset.json` | 790 entri | **100% Selesai**. Seluruh 790 nama stiker hiasan kartu nama Producer, badge P-Ranking, dan bulan pelatihan. |
| `[-]` | **Daftar Lagu & Komposer** | `masterTrans/Music.json` | 434 entri | **Di-skip (Nama Asli)**. Nama musik, nama karakter, nama komposer, dan pembuat lagu tetap dalam bahasa asli sesuai instruksi. |
| `[x]` | **Daftar Grup Suara Idol** | `masterTrans/VoiceGroup.json` | 3609 entri | **100% Selesai**. Seluruh judul suara kostum/sistem ke Bahasa Indonesia; judul lagu/musik idol tetap asli. |
| `[x]` | **Daftar Roster Suara** | `masterTrans/VoiceRoster.json` | 2001 entri | **100% Selesai**. Seluruh 2.001 judul rekaman suara interaksi idol per situasi ke Bahasa Indonesia. |
| `[x]` | **Hadiah Kelulusan Memory** | `masterTrans/MemoryGift.json` | 21 entri | **100% Selesai**. Seluruh 21 kenang-kenangan hasil kelulusan Produce idol ke Bahasa Indonesia. |
| `[x]` | **Tag Karakteristik Memory** | `masterTrans/MemoryTag.json` | 24 entri | **100% Selesai**. Seluruh 24 tag penanda kategori atribut memory (Vocal, Dance, Visual, Semangat, Genki, dll.). |
| `[-]` | **Aturan & Regulasi Layanan** | `masterTrans/Rule.json` | 23 entri | **Di-skip (Hukum Legal)**. Dokumen regulasi undang-undang penyelesaian dana resmi Bandai Namco Jepang. |
| `[x]` | **Syarat & Kebijakan** | `masterTrans/Terms.json` | 3 entri | **100% Selesai**. Seluruh nama dokumen ketentuan hukum dan kebijakan privasi. |
| `[x]` | **Pengaturan Dasar Game** | `masterTrans/Setting.json` | 1 entri | **100% Selesai**. Pesan peringatan keamanan sistem dan nama akun bawaan. |
| `[x]` | **Mode Tur Wilayah** | `masterTrans/Tour.json` | 4 entri | **100% Selesai**. Seluruh 4 nama rute tur konser live idol. |
| `[x]` | **Mode Menara Ujian (Tower)** | `masterTrans/Tower.json` | 13 entri | **100% Selesai**. Seluruh 13 judul Idol Road tiap karakter idol. |
| `[x]` | **Pekerjaan Idol (Work/Jobs)** | `masterTrans/Work.json` | 2 entri | **100% Selesai**. Seluruh 2 aktivitas pekerjaan idle idol (Mini Live & Siaran Langsung). |
| `[x]` | **Fallback Terjemahan Master** | `masterTrans/Localization.json` | 98 entri | **100% Selesai**. Seluruh 98 teks fallback deskripsi cadangan master database. |
| `[-]` | **Daftar BGM Musik Latar** | `masterTrans/Bgm.json` | 2 entri | **Di-skip (Nama Audio Asli)**. Nama track musik latar belakang bawaan. |
| `[x]` | **Pertandingan Circle Raid** | `masterTrans/GvgRaid.json` | 1 entri | **100% Selesai**. Nama event kompetisi panggung grup/Circle. |
| `[x]` | **Galeri Video & Animasi** | `masterTrans/Media.json` | 232 entri | **100% Selesai**. Seluruh 232 nama konten video cuplikan dan animasi komik 4-koma ke Bahasa Indonesia. |

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

## Fase 4 — Cerita Karakter, Event & Interaksi Panggung (`resource/`)

Target: Cerita mendalam tiap kandidat idol, interaksi keakraban (Commu Bond), cerita pendukung kartu, event produksi, dan dialog panggung live. Total **3.414 berkas cerita**.

| Status | Komponen | File / Folder | Volume | Status Detail |
|---|---|---|---|---|
| `[ ]` | **Cerita Kandidat Idol** | `resource/adv_cidol_*.txt` | 354 file | Belum Mulai. Alur cerita individu masing-masing karakter idol. |
| `[ ]` | **Commu Bond (Keakraban)** | `resource/adv_dear_*.txt` | 494 file | Belum Mulai. Interaksi kedekatan emosional Producer bersama idol. |
| `[>]` | **Cerita Support Card** | `resource/adv_csprt_*.txt` | 529 file | **Aktif Dikerjakan (415/529 Selesai)**. Support Card R tuntas 100% (26 file, 471 dialog); Support Card SR tuntas 100% (164 file, 3.196 dialog); Support Card SSR aktif (225/339 file, 4.467 dialog tuntas). |
| `[ ]` | **Cerita Skenario Produksi (P-Story)** | `resource/adv_pstory_*.txt` / `adv_pidol_*.txt` | 611 file | Belum Mulai. Skenario perjalanan audisi dan ujian produce. |
| `[ ]` | **Event Pilihan Produksi & Story Event** | `resource/adv_pevent_*.txt` / `adv_event_*.txt` | 1.256 file | Belum Mulai. Event acak pilihan Produce dan narasi event festival. |
| `[ ]` | **Dialog Interaksi Panggung Live (MC)** | `resource/adv_live_*.txt` | 106 file | Belum Mulai. Percakapan panggung, seruan konser, dan interaksi live show idol. |
| `[ ]` | **Dialog Pertumbuhan Idol (Growth)** | `resource/adv_pgrowth_*.txt` | 39 file | Belum Mulai. Percakapan perkembangan kemampuan dan evaluasi latihan idol. |
| `[ ]` | **Dialog Evaluasi Hasil Akhir Produce** | `resource/adv_presult_*.txt` | 13 file | Belum Mulai. Reaksi kelulusan dan penutup hasil Produce. |
| `[ ]` | **Interaksi Khusus Mingguan Produce** | `resource/adv_produce_*.txt` | 11 file | Belum Mulai. Dialog percakapan transisi jadwal produce idol. |
| `[ ]` | **Percakapan Mode Menara (Tower)** | `resource/adv_tower_*.txt` | 1 file | Belum Mulai. Cerita naratif tantangan lantai menara Idol Road. |

### Rincian Progres Cerita Support Card (`adv_csprt*.txt`)

Total: **529 berkas** (10.414 baris dialog).

| Status | Tingkat Kelangkaan | Prefiks Berkas | Jumlah File | Jumlah Baris Dialog | Status Detail |
|---|---|---|---|---|---|
| `[x]` | **Support Card R** | `adv_csprt-1-*.txt` | **26 file** | **471 baris** | **100% Selesai**. Terdiri dari Batch 1A (file 1-13, 242 dialog) & Batch 1B (file 14-26, 229 dialog). Lolos validasi sintaksis. |
| `[x]` | **Support Card SR** | `adv_csprt-2-*.txt` | **164 file** | **3.196 baris** | **100% Selesai**. Terdiri dari 6 batch (Batch 2A: 25 file / 439 dialog, Batch 2B: 25 file / 484 dialog, Batch 2C: 25 file / 498 dialog, Batch 2D: 25 file / 497 dialog, Batch 2E: 30 file / 598 dialog, Batch 2F: 34 file / 680 dialog). Lolos validasi sintaksis ADV. |
| `[>]` | **Support Card SSR** | `adv_csprt-3-*.txt` | 339 file | ~6.700 baris | **Aktif Dikerjakan (225/339 Berkas / 4.467 Baris Selesai)**. Terdiri dari Batch 3A (25 berkas / 496 dialog), Batch 3B (25 berkas / 481 dialog), Batch 3C (25 berkas / 499 dialog), Batch 3D (25 berkas / 499 dialog), Batch 3E (25 berkas / 494 dialog), Batch 3F (25 berkas / 499 dialog), Batch 3G (25 berkas / 499 dialog), Batch 3H (25 berkas / 500 dialog), dan Batch 3I (25 berkas / 500 dialog tuntas). Lolos validasi sintaksis ADV. |

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
| 2026-10-15 | `masterTrans/Produce*.json` (Batch 1 & 2) | Terjemahan | Menerjemahkan 23 berkas Produce (2.289 baris data): Produce, ProduceGroup, ProduceSeason, ProducerRanking, ProduceDescriptionProducePlan/Step/Type/Effect/GrowEffect/Swap, ProduceChallengeSlot, ProduceHighScore, ProduceGuideProduceCardCategory/Group/SampleDeck, ProduceAdv, ProduceSplitAdv, ProduceCharacterAdv, ProduceEventCharacterGrowth, ProduceExamBattleNpcMob, ProduceStepLesson, ProduceNavigation, ProduceCardCustomize. Total 29 dari 41 berkas Produce 100% selesai. |
| 2026-10-15 | `masterTrans/Produce*.json` (Batch 3) | Terjemahan | Menerjemahkan 4 berkas Produce (2.513 baris data): ProduceGrowthPanel, ProduceCardStatusEnchant, ProduceCardSearch, ProduceCustomizeItem. Total 33 dari 41 berkas Produce 100% selesai. |
| 2026-10-15 | `ProduceStepEvent*.json` | Terjemahan | Menerjemahkan ProduceStepEventDetail (6.921 baris) dan ProduceStepEventSuggestion (3.066 baris) mencakup seluruh saran keputusan dan detail event pilihan Produce. Total 35 dari 41 berkas Produce 100% selesai. |
| 2026-10-16 | `genericTrans/lyrics/` (Batch 1) | Terjemahan | Menerjemahkan seluruh 19 lagu tema utama & all songs (`all_001` - `all_019`, total 450 baris lirik) ke Bahasa Indonesia dengan gaya puitis, berirama alami, dan mempertahankan frasa ikonik. **Batch 1 SELESAI (450 baris)**. |
| 2026-10-16 | `genericTrans/lyrics/` (Batch 2-4) | Terjemahan | Menerjemahkan seluruh sisa 44 lagu solo idol dan unit (1.427 baris lirik). Seluruh 63 lagu panggung & live MV (1.877 baris lirik) tuntas 100% ke Bahasa Indonesia. **LIRIK 100% SELESAI (63 Lagu, 1.877 Baris)**. |
| 2026-10-16 | `masterTrans/` (Fase 2.5 Cerita Master) | Terjemahan | Menerjemahkan 11 berkas cerita master (MainStoryChapter, MainStoryPart, Story, StoryEvent, StoryGroup, EventLabel, SupportCardFlavor [583 entri], ProduceAdv, ProduceSplitAdv, ProduceCharacterAdv). Total Fase 2.5 **100% SELESAI**. |
| 2026-10-16 | `masterTrans/` (Fase 2.6 Batch 1 Sistem & Bantuan) | Terjemahan | Menerjemahkan 14 berkas batch 1 (HelpContent, HelpCategory, FeatureLock, Tour, Tower, Work, GvgRaid, MemoryTag, Terms, Setting, Localization, PhotoBackground, PhotoFacialMotionGroup, TutorialProduceStep). Total 493 entri tuntas. |
| 2026-10-16 | `masterTrans/` (Fase 2.6 Batch 2 & Final) | Terjemahan | Menerjemahkan MemoryGift (21), PhotoPose (1.092), Tutorial (217), Media (232 komik/movie), MeishiBaseAsset (301), MeishiIllustrationAsset (790), VoiceGroup (3.609), VoiceRoster (2.001). Mempertahankan nama asli lagu, komposer, lirikis, dan karakter idol. |
| 2026-10-16 | **Fase 2: Master Database Gameplay** | Milestone | **108 Berkas MasterDB TUNTAS 100%** (99 berkas diterjemahkan, 9 berkas di-skip nama asli/regulasi). Fitur MasterDB Localization siap penuh dalam Bahasa Indonesia. |
| 2026-10-16 | Audit & Pendataan Repositori Global | Audit File | Melakukan pemindaian menyeluruh terhadap seluruh 3.725 berkas game: mendata 13 berkas template engine di `genericTrans/index` dan 321 berkas cerita tambahan di `resource/` (live MC 106, p-growth 39, p-result 13, produce 11, tower 1, event 1.256). Struktur PROGRESS.md 100% sinkron dengan disk fisik. |
| 2026-10-16 | `resource/adv_csprt-1-*.txt` (Support Card R) | Terjemahan | Menerjemahkan seluruh 26 berkas cerita Support Card R (471 baris dialog) ke Bahasa Indonesia natural ala fansub anime. Validasi sintaksis ADV 100% lolos tanpa error, line endings LF murni. **Support Card R 100% SELESAI (26 Berkas / 471 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-2*.txt` (Support Card SR Batch 2A) | Terjemahan | Menerjemahkan 25 berkas pertama cerita Support Card SR (439 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 2A SELESAI (25 Berkas / 439 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-2*.txt` (Support Card SR Batch 2B) | Terjemahan | Menerjemahkan 25 berkas kedua cerita Support Card SR (484 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 2B SELESAI (25 Berkas / 484 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-2*.txt` (Support Card SR Batch 2C) | Terjemahan | Menerjemahkan 25 berkas ketiga cerita Support Card SR (498 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 2C SELESAI (25 Berkas / 498 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-2*.txt` (Support Card SR Batch 2D) | Terjemahan | Menerjemahkan 25 berkas keempat cerita Support Card SR (497 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 2D SELESAI (25 Berkas / 497 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-2*.txt` (Support Card SR Batch 2E) | Terjemahan | Menerjemahkan 30 berkas kelima cerita Support Card SR (598 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 2E SELESAI (30 Berkas / 598 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-2*.txt` (Support Card SR Batch 2F & Final SR) | Terjemahan | Menerjemahkan 34 berkas keenam cerita Support Card SR (680 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Support Card SR 100% SELESAI (164 Berkas / 3.196 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-3*.txt` (Support Card SSR Batch 3A) | Terjemahan | Menerjemahkan 25 berkas pertama cerita Support Card SSR (496 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 3A SELESAI (25 Berkas / 496 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-3*.txt` (Support Card SSR Batch 3B) | Terjemahan | Menerjemahkan 25 berkas kedua cerita Support Card SSR (481 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 3B SELESAI (25 Berkas / 481 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-3*.txt` (Support Card SSR Batch 3C) | Terjemahan | Menerjemahkan 25 berkas ketiga cerita Support Card SSR (499 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 3C SELESAI (25 Berkas / 499 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-3*.txt` (Support Card SSR Batch 3D) | Terjemahan | Menerjemahkan 25 berkas keempat cerita Support Card SSR (499 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 3D SELESAI (25 Berkas / 499 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-3*.txt` (Support Card SSR Batch 3E) | Terjemahan | Menerjemahkan 25 berkas kelima cerita Support Card SSR (494 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 3E SELESAI (25 Berkas / 494 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-3*.txt` (Support Card SSR Batch 3F) | Terjemahan | Menerjemahkan 25 berkas keenam cerita Support Card SSR (499 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 3F SELESAI (25 Berkas / 499 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-3*.txt` (Support Card SSR Batch 3G) | Terjemahan | Menerjemahkan 25 berkas ketujuh cerita Support Card SSR (499 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 3G SELESAI (25 Berkas / 499 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-3*.txt` (Support Card SSR Batch 3H) | Terjemahan | Menerjemahkan 25 berkas kedelapan cerita Support Card SSR (500 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 3H SELESAI (25 Berkas / 500 Baris)**. |
| 2026-10-16 | `resource/adv_csprt-3*.txt` (Support Card SSR Batch 3I) | Terjemahan | Menerjemahkan 25 berkas kesembilan cerita Support Card SSR (500 baris dialog) ke Bahasa Indonesia natural. Lolos validasi sintaksis tanpa error, line endings LF murni. **Batch 3I SELESAI (25 Berkas / 500 Baris)**. |
