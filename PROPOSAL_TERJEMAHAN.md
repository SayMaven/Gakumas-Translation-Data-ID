# 📋 Proposal Terjemahan — Gakumas-Translation-Data-ID
> Lokalisasi **Gakuen Idolm@ster** ke Bahasa Indonesia  
> Repo ID: [SayMaven/Gakumas-Translation-Data-ID](https://github.com/SayMaven/Gakumas-Translation-Data-ID)  
> Menggunakan data acuan dari [NatsumeLS/Gakumas-Translation-Data-EN](https://github.com/NatsumeLS/Gakumas-Translation-Data-EN)  
> Plugin: [gakuen-imas-localify](https://github.com/chinosk6/gakuen-imas-localify)

---

## 📌 Daftar Isi
1. [Gambaran Umum](#1-gambaran-umum)
2. [Filosofi Terjemahan](#2-filosofi-terjemahan)
3. [Panduan Gaya Bahasa](#3-panduan-gaya-bahasa)
4. [Panduan Per Jenis Konten](#4-panduan-per-jenis-konten)
5. [Glosarium & Istilah Tetap](#5-glosarium--istilah-tetap)
6. [Struktur File & Prioritas](#6-struktur-file--prioritas)
7. [Alur Kerja (Workflow)](#7-alur-kerja-workflow)
8. [Standar Kualitas & Review](#8-standar-kualitas--review)
9. [Konvensi Format File](#9-konvensi-format-file)
10. [Referensi Karakter](#10-referensi-karakter)

---

## 1. Gambaran Umum

### Tujuan
Menghadirkan pengalaman bermain **Gakuen Idolm@ster** dalam Bahasa Indonesia yang natural, mengalir, dan terasa seperti konten yang memang dibuat dalam bahasa Indonesia — bukan sekadar terjemahan mesin.

### Sumber & Target
| | Sumber (EN) | Target (ID) |
|---|---|---|
| **Bahasa asal** | Jepang → Inggris | Inggris → Indonesia |
| **Repo** | `Gakumas-Translation-Data-EN` | `Gakumas-Translation-Data-ID` |
| **Pendekatan** | Literal-ish, game-accurate | Natural, mengalir, sesuai karakter |

### Ruang Lingkup Konten
| Jenis | Volume | Status |
|---|---|---|
| UI & Menu Inti (`localization.json`) | 6.958 key | ✅ Selesai (100%) |
| Kamus Generik Root (`generic.json`) | 525 key | ✅ Selesai (100%) |
| UI Umum & Fallback (`genericTrans/index/trash.json`) | 2.510 key | ✅ Selesai (100%) |
| General Strings & Misi (`genericTrans/index/*.json`) | 9 file JSON (1.031 key) | ✅ Selesai (100%) |
| Kartu Skill Produce (`masterTrans/ProduceCard.json`) | 1.748 kartu (~438K baris) | ✅ Selesai (100%) |
| Lirik Lagu Panggung / MV (`genericTrans/lyrics/`) | 63 file JSON (1.877 baris) | ✅ Selesai (100%) |
| Database Master Game (`masterTrans/`) | 108 file JSON | 🔄 79 File Selesai (73,1%) |
| Script ADV/Dialog (`resource/`) | 3.530 file TXT | 🔲 Belum mulai |

---

## 2. Filosofi Terjemahan

> **Prinsip Utama: Kelancaran & Nuansa di atas Kesetiaan Literal**

Terjemahan ini **bukan** kamus. Tujuannya adalah membuat pemain Indonesia bisa menikmati game seolah-olah memang dibuat dalam bahasa mereka sendiri.

### ❌ Yang HARUS Dihindari
- Terjemahan kata-per-kata yang kaku
- Struktur kalimat yang terasa "Jepang banget" (Subject-Object-Verb dipertahankan)
- Bahasa formal/baku kecuali konteks memang formal
- Hasil terjemahan mesin mentah tanpa review
- Hilangnya nuansa emosi karakter aslinya
- Inkonsistensi penamaan karakter / istilah antar file

### ✅ Yang HARUS Dilakukan
- Prioritaskan kelancaran membaca
- Pertahankan kepribadian dan nada emosional karakter
- Gunakan bahasa yang dipakai anak muda Indonesia sehari-hari
- Buat dialog terasa hidup seperti percakapan sungguhan
- Pertahankan istilah game penting dalam bahasa Inggris (lihat Glosarium)
- Sesuaikan panjang teks dengan batasan UI (untuk strings pendek)

---

## 3. Panduan Gaya Bahasa

### 3.1 Register Bahasa
Gunakan **bahasa Indonesia semi-formal ke informal** — seperti gaya bahasa:
- Novel light novel / webtoon lokal Indonesia
- Cara ngobrol teman sebaya yang akrab
- Subtitle anime fansub berkualitas Indonesia

**Bukan** seperti:
- Buku pelajaran / ensiklopedia
- Bahasa berita TV
- Terjemahan Google Translate mentah

---

### 3.2 Partikel & Filler Bahasa Gaul (Gunakan secara wajar)

| Partikel | Kapan dipakai |
|---|---|
| **sih** | Keheranan, klarifikasi santai ("Emang gitu sih...") |
| **dong** | Permintaan, sedikit memaksa ("Ayolah dong!") |
| **deh** | Pasrah, setuju enggan-enggan ("Ya udah deh...") |
| **ya** | Minta persetujuan, afirmasi ("Bener kan ya?") |
| **kok** | Keheranan, sedikit protes ("Kok bisa gitu?") |
| **gitu** | Pengganti "seperti itu" yang informal |
| **sih** | Penekanan ringan ("Kamu sih...") |
| **lah** | Melunak perintah/pernyataan ("Udah lah...") |
| **kali** | Kemungkinan ("Mungkin kali ya...") |

> ⚠️ **Jangan terlalu banyak** — partikel harus terasa natural, bukan dipaksakan.

---

### 3.3 Penyesuaian Kepribadian Karakter

Setiap karakter punya gaya bicara yang berbeda. Terjemahan harus mencerminkan kepribadian ini:

| Tipe Karakter | Gaya Bahasa Indonesia |
|---|---|
| **Ceria / Genki** | Kalimat pendek, banyak tanda seru, kata-kata bersemangat ("Ayo!", "Seru banget!", "Pasti bisa!") |
| **Tsundere** | Tersendat, sering menyangkal, nada defensif ("B-bukan gitu maksudnya!", "Siapa yang peduli!") |
| **Kalem / Pendiam** | Kalimat tenang, memilih kata dengan hati-hati, jarang pakai filler |
| **Cool / Elegan** | Sedikit lebih formal dari yang lain, tapi tetap tidak kaku |
| **Polos / Naif** | Kalimat sederhana, kadang salah ngerti, tapi tulus |
| **Dewasa / Onee-san** | Hangat, sedikit menggoda, bahasa lembut tapi percaya diri |
| **Galak / Keras** | Tegas, kalimat pendek, tidak banyak basa-basi |

---

### 3.4 Teknik Penulisan Dialog

```
❌ BURUK (terlalu literal):
"Aku... aku tidak tahu apa yang harus aku lakukan. Ini sungguh memalukan."

✅ BAGUS (natural & sesuai karakter malu-malu):
"A-aku... nggak tau harus ngapain. Malu banget sih..."

---

❌ BURUK (struktur Jepang dipertahankan):
"Produce ini, karena kamu bersamaku, bisa selesai."

✅ BAGUS (disusun ulang natural):
"Produce ini bisa selesai karena ada kamu di sini."

---

❌ BURUK (terlalu formal untuk konteks santai):
"Apakah engkau bersedia untuk berjuang bersama?"

✅ BAGUS (sesuai konteks):
"Mau berjuang bareng nggak?"
```

---

### 3.5 Penanganan Karakter Khusus & Emosi

| Situasi | Cara Menulis |
|---|---|
| Karakter tergagap/kaget | "A-aku..." / "I-itu..." |
| Karakter menghela napas | *(menghela napas)* atau "...Hah." |
| Ellipsis (jeda panjang) | `...` — pertahankan |
| Tanda seru ganda | `!!` — boleh, tapi jangan lebay |
| Pikiran dalam hati | Tanda kurung `(...)` atau miring *...* |
| Suara/onomatopoeia Jepang | Adaptasi atau hilangkan kalau tidak ada padanannya |

---

## 4. Panduan Per Jenis Konten

### 4.1 UI Strings (`localization.json`)
- Teks harus **pendek dan jelas** — ini tombol, label, judul
- Gunakan kata kerja aktif yang ringkas (contoh: *"Latihan"*, bukan *"Melakukan Pelatihan"*)
- Pertahankan format placeholder: `{0}`, `{1}`, `\n`, `<color=...>`
- Hindari pemanjangan teks berlebihan yang bisa merusak container UI

#### 4.1.1 Penanganan Text Overflow & Pedoman Singkatan
Jika ruang UI sempit atau teks berpotensi terpotong (overflow), terapkan aturan berikut:
1. **Gunakan Padanan Ringkas**:
   - *"Kondisi Prima"* → di kotak kecil kartu/buff cukup tulis **"Prima"** (contoh: *"Prima +3"*)
   - *"Kondisi Puncak"* → cukup tulis **"Puncak"**
   - *"Kesan Baik"* → cukup tulis **"Kesan"**
   - *"Latihan Mandiri"* → cukup tulis **"Mandiri"**
   - *"Penggunaan Kartu +1"* → cukup tulis **"Play +1"**
2. **Singkatan Standar yang Diizinkan**:
   - Maksimal → **Maks.**
   - Level / P-Level → **Lv. / P-Lv.**
   - Persentase / Nilai Parameter → **Prm.** / **Poin**
   - Rekomendasi → **Rekom.**
3. **Prinsip Tombol Aksi**:
   - Pakai kata dasar/perintah langsung: *"Mulai"*, *"Pilih"*, *"Batal"*, *"Klaim"*, *"Upgrade"*.

```json
// Contoh
"work.result.title": "Pekerjaan Selesai",
"achievement.detail.title": "Detail Achievement",
"tutorial.idol.select": "Pilih Idol"
```

---

### 4.2 Dialog ADV/Script (`.txt` di `resource/`)
Setiap berkas naskah visual novel (ADV) memiliki 3 jenis elemen teks yang **WAJIB diterjemahkan ke Bahasa Indonesia**:
1. **Dialog Karakter**: `[message text=... name=...]`
2. **Teks Narasi & Monolog**: `[narration text=...]` (misal: pidato pengantar, narasi suasana adegan panggung, atau penjelasan latar belakang).
3. **Pilihan Respons Dialog Pemain**: `[choice text=...]` atau `[choicegroup choices=[choice text=...] ...]` (opsi pilihan interaktif Producer).

#### Aturan Format ADV:
- **Hanya ubah isi nilai `text=`** pada tag `[message]`, `[narration]`, maupun `[choice]`.
- **Dilarang keras mengubah** parameter lain (`name=`, `clip={...}`, `choices=[choice text=...]`, `se=`, `actorId=`, dll.).
- Hati-hati dengan backslash escape `\{`, `\}`, dan `\"` — biarkan apa adanya tanpa diubah.
- Pertahankan newline literal `\n` jika ada di dalam parameter `text=`.
- Format baris baru file wajib menggunakan **LF (`\n`) murni** dan encoding **UTF-8 No BOM**.

```
// Contoh BENAR:
[message text=Eh, kamu juga ada di sini? name=Ume clip={...}]
[narration text=Sebuah festival yang digelar di Akademi Hatsuboshi\nuntuk menentukan idol nomor satu. clip={...}]
[choicegroup choices=[choice text=Jawabanku adalah tidak] clip={...}]

// Contoh SALAH (nama tag atau parameter ikut diubah / narration terlewat):
[pesan teks=Eh, kamu juga ada di sini? nama=Ume ...]
[narration text=A festival held at Hatsuboshi Academy... clip={...}] // <- SALAH: Narasi tidak boleh dibiarkan berbahasa Inggris!
```

---

### 4.3 JSON Key-Value (`genericTrans/`, `masterTrans/`)
- **Jangan ubah key** — hanya value yang ditranslate
- Pertahankan escape character: `\"`, `\\n`, `\n`
- Untuk teks multiline, gunakan `\n` bukan newline literal
- Pertahankan tag HTML/Unity: `<color=#...>`, `<b>`, `</color>`

```json
// Contoh BENAR:
"「Indomitable like a flower」": "「Pantang menyerah seperti bunga」",

// Contoh SALAH (key ikut diubah):
"「Pantang menyerah seperti bunga」": "「Pantang menyerah seperti bunga」"
```

---

### 4.4 Narasi (bukan dialog)
- Bisa sedikit lebih puitis / sastrawi jika konteksnya memang dramatis
- Tapi tetap hindari bahasa yang terasa artifisial
- Cocok untuk opening, penutup cerita, monolog batin

---

## 5. Glosarium & Istilah Tetap

> Istilah-istilah ini **TIDAK diterjemahkan** atau memiliki padanan baku yang harus konsisten dipakai di seluruh project.

### 5.1 Istilah Game — Tetap dalam Bahasa Inggris
| Istilah Asli | Perlakuan | Catatan |
|---|---|---|
| **Produce** | Tetap "Produce" | Istilah gameplay inti |
| **Audition** | Tetap "Audition" | |
| **Producer** | Tetap "Producer" | Peran pemain |
| **P-Item** | Tetap "P-Item" | |
| **P-Drink** | Tetap "P-Drink" | |
| **Skill Card** | Tetap "Skill Card" | |
| **Support Card** | Tetap "Support Card" | |
| **Gacha** | Tetap "Gacha" | Sudah umum di komunitas |
| **SSR / SR / R** | Tetap | Rarity label |
| **True End** | Tetap "True End" | |
| **H.I.F** | Tetap | Nama event dalam game |
| **N.I.A** | Tetap | Nama event dalam game |
| **Prima Stella** | Tetap | |
| **Hatsuboshi Academy** | Tetap "Hatsuboshi Academy" | Tidak diterjemahkan |

### 5.2 Nama Karakter — Tidak Diterjemahkan
Semua nama karakter dipertahankan persis seperti di EN project (ejaan dan urutannya):
`Hoshimi Yuika`, `Fujita Kotone`, `Hanami Ume`, `Katsuragi Lilja`, dst.

> Gunakan order **Nama Belakang + Nama Depan** (format Jepang) — mengikuti konvensi EN project.

### 5.3 Tabel Istilah — Keputusan Final
| Inggris | Indonesia | Aturan |
|---|---|---|
| **Bond** | **Bond** | Tetap, tidak diterjemahkan |
| **Bond Effect** | **Efek Bond** | Pengaruh level keakraban idol |
| **Bond Commu** | **Commu Bond** | Cerita interaksi hubungan idol |
| **Turn** | **Turn** | Tetap, tidak diterjemahkan |
| **Fan** | **Fan** / **Penggemar** | Kontekstual — lihat aturan di bawah |
| **Talent Bloom** | **Rank Bakat** | Peningkatan bintang Produce Idol (bukan Mekar Bakat) |
| **Awakening** | **Buka Batas** / **Batas Terbuka** | Peningkatan batas level kartu |
| **Stage** | **Stage** | Tetap "Stage" (bukan Panggung) |
| **Refresh** | **Refresh** | Tetap "Refresh" (bukan Segarkan) |
| **Trade Pts / 交換Pt** | **Poin Tukar** | Penukaran gacha / shop (bukan Poin Penukaran) |
| Achievement | Achievement | Tetap, sudah umum |
| Mission | Misi | Diterjemahkan |
| Item | Item | Tetap |
| Work | Pekerjaan / Kerja | Diterjemahkan |
| Stamina | Stamina | Tetap |
| Idol | Idol | Tetap |
| Memory | Memory | Tetap — fitur game |
| Costume | Kostum | Diterjemahkan |
| Jewel | Jewel | Tetap — mata uang game |
| Paid Jewel / 有償ジュエル | Jewel Paid / Paid | Mata uang premium berbayar (Gacha, Toko, Saldo) |
| Free Jewel / 無償ジュエル | Jewel Gratis / Gratis | Mata uang reward gratis |

#### Aturan Khusus: "Fan" vs "Penggemar"

> **UI / Statistik / Angka** → Gunakan **"Fan"**
> - Ringkas, cocok untuk kotak statistik kecil
> - Contoh: `"Target Fan: 10.000"`, `"Fan +1.500"`, `"Jumlah Fan"`

> **Dialog / Narasi / Cerita** → Fleksibel: **"Fan"** atau **"Penggemar"**
> - `"Penggemar"` → terasa lebih dramatis, emosional, menyentuh
> - `"Fan"` → terasa lebih santai dan kasual
> - Contoh: *"Aku ingin memberikan penampilan terbaik untuk para penggemar yang sudah datang"* (dramatis) vs *"untuk para fans"* (santai)

### 5.4 Aturan Sapaan kepada Pemain (Producer)

**Default di seluruh game: gunakan "Kamu"**

Alasan: Hubungan Producer–idol bersifat personal dan sebaya (remaja), sehingga "kamu" jauh lebih natural daripada "Anda" yang terlalu formal.

| Konteks | Sapaan | Penjelasan |
|---|---|---|
| **UI / Menu / Tutorial** | **Kamu** | Default — bersahabat dan interaktif |
| **Dialog idol santai / percaya diri** | **Kamu** | Saki, Temari, Lilja, dll |
| **Dialog idol yang memanggil Senpai di audio** | **Senpai** | ⭐ Lihat penjelasan di bawah |
| **Dialog idol sangat formal / bisnis** | **Anda** | Kotone (mode bisnis), Sumika, dll |

> **Catatan penting**: Fleksibilitas sapaan berlaku **hanya di teks cerita (Commu/ADV)**. Di luar cerita (UI, notifikasi, loading), selalu gunakan **"Kamu"**.

#### ⭐ Mengapa "Senpai" Dipertahankan (Bukan "Kak/Kakak")

Untuk idol yang memanggil Producer dengan sebutan senior sekolah, **tetap gunakan "Senpai"** — bukan ditranslate jadi "Kak" atau "Kakak".

**Alasan:**
- **Nuansa budaya yang tidak tergantikan** — "Senpai" membawa makna spesifik hubungan senior-junior di sekolah Jepang (Hatsuboshi Gakuen) yang tidak bisa direplikasi sepenuhnya oleh "Kak". Di Indonesia, "Kak" terasa terlalu kasual dan kehilangan nuansa kultus sekolah Jepangnya.
- **Selaras dengan audio** — Pemain mendengar kata "Senpai" langsung dari suara karakter. Jika teks tertulis "Kak", akan ada ketidaksesuaian antara audio dan teks yang justru terasa aneh.
- **Target audiens** — Pemain Gakuen Idolmaster mayoritas adalah penggemar subkultur anime yang sudah sangat familier dengan kata "Senpai". Menggantinya akan terasa tidak selaras dengan ekspektasi mereka.

```
// ❌ Terasa aneh bagi pemain anime:
"Kak, hari ini juga semangat ya!"

// ✅ Natural dan selaras dengan audio:
"Senpai, hari ini juga semangat ya!"
```

#### Pengecualian: Panggilan Keluarga (Onee-chan, Onii-chan, dll)

Panggilan keluarga **berbeda** dari panggilan senior sekolah — ini adalah konteks yang terpisah.

| Panggilan Asli | Terjemahan | Contoh |
|---|---|---|
| **Onee-chan** | **Kak [nama]** | Ume memanggil Saki → "Kak Saki" |
| **Onii-chan** | **Kak [nama]** / **Mas [nama]** | Sesuaikan konteks karakter |
| **Onee-san** | **Kak [nama]** (lebih sopan) | |
| **Senpai** (sekolah) | **Senpai** | Tetap, jangan diubah |

> **Catatan**: Perbedaan antara "Kak Saki" (panggilan kakak kandung) dan "Senpai" (panggilan senior sekolah) justru menjadi pembeda yang penting dalam cerita — dan ini adalah keputusan yang disengaja.

### 5.5 Glosarium Mekanik Gameplay (Kartu & Pertarungan)

#### A. Atribut & Tipe Plan
| Istilah Asli (JP / EN) | Terjemahan Resmi | Catatan & Pedoman UI |
|---|---|---|
| **Vocal / Dance / Visual** | **Vo / Da / Vi** (tetap) | Wajib disingkat di ikon kartu, tooltip, formula. Tulis lengkap hanya di tutorial. |
| **Sense (センス)** | **Sense** | Tetap — nama archetype kartu resmi. |
| **Logic (ロジック)** | **Logic** | Tetap — nama archetype kartu resmi. |
| **Anomaly (アノマリー)** | **Anomaly** | Tetap — archetype kartu baru. |
| **Active Card (アクティブ)** | **Kartu Aktif** (Active) | Kartu yang langsung menghasilkan skor/parameter. |
| **Mental Card (メンタル)** | **Kartu Mental** (Mental) | Kartu pendukung buff status atau penataan stamina. |
| **Trouble Card (トラブル)** | **Kartu Trouble** | Kartu beban/debuff penahan aksi. |

#### B. Status & Buff Inti Kartu
| Istilah Asli (JP / EN) | Terjemahan Resmi | Aturan & Singkatan UI |
|---|---|---|
| **好調 (Good Condition)** | **Kondisi Prima** | Multiplier skor (1.5x). Boleh disingkat **"Prima"** di UI sempit (*"Prima +3"*). |
| **絶好調 (Peak Condition)** | **Kondisi Puncak** | Tier di atas Kondisi Prima. Boleh disingkat **"Puncak"**. |
| **不調 (Poor Condition)** | **Kondisi Buruk** | Debuff penurun efektivitas skor. |
| **集中 (Concentration)** | **Fokus** | Flat bonus skor pada setiap kartu aktif. Ringkas dan pas di kartu. |
| **やる気 (Motivation)** | **Motivasi** | Arketipe Logic, meningkatkan perolehan Genki/shield. |
| **好印象 (Good Impression)** | **Kesan Baik** | Memberikan skor pasif di akhir setiap turn. Singkatan UI: **"Kesan"**. |
| **元気 (Genki)** | **Genki** | ⭐ **TETAP "Genki"**. Berfungsi sebagai shield penahan stamina. Selaras dengan audio & identitas game. |
| **消費体力減少** | **Konsumsi Stamina Turun** | Efek efisiensi penggunaan stamina. |
| **消費体力増加** | **Konsumsi Stamina Naik** | Efek penalti/kartu beresiko. |
| **体力回復** | **Pemulihan Stamina** | Pemulihan HP stamina idol. |

#### C. Mekanik Kartu & Giliran
| Istilah Asli (JP / EN) | Terjemahan Resmi | Catatan Penggunaan |
|---|---|---|
| **Turn (ターン)** | **Turn** | Tetap. Standar game modern (*"Sisa 3 Turn"*). |
| **Extra Turn (追加ターン)** | **Turn Tambahan** | Contoh: *"Mendapatkan 1 Turn Tambahan"*. |
| **Hand (手札)** | **Hand** *(UI)* / **Kartu di tangan** *(Dialog)* | Di teks efek kartu: *"Kartu di Hand"*. |
| **Deck (山札)** | **Deck** | Tetap. Standar card game. |
| **Discard Pile (捨て札)** | **Discard** | Tempat pembuangan kartu. Alternatif: *"Buangan"*. |
| **Exile / Remove (除外)** | **Exile** | Kartu disingkirkan sampai ujian berakhir (tidak masuk Discard). |
| **Hold / Retain (保持)** | **Hold** | Kartu tetap bertahan di tangan untuk turn berikutnya. Alternatif: *"Simpan"*. |
| **Card Plays (スキルカード使用数追加)** | **Penggunaan Kartu** | Contoh: *"Penggunaan Kartu +1"* (UI sempit: *"Play +1"*). |
| **Draw (ドロー)** | **Draw** | Contoh: *"Draw 1"* atau *"Tarik 1 kartu"*. |
| **Parameter Gain (パラメータ上昇)** | **Kenaikan Parameter** / **Skor** | Nilai poin ujian yang diperoleh. |

---

### 5.6 Glosarium Aktivitas Sesi Produce (Jadwal Mingguan)

| Istilah Asli (JP / EN) | Terjemahan Resmi | Catatan & Konteks |
|---|---|---|
| **Lesson (レッスン)** | **Lesson** | Tetap. Istilah baku dalam kultur idol (*"Lesson Vokal"*, *"Lesson Dance"*). |
| **Intensive Lesson (追い込みレッスン)** | **Intensive Lesson** | Tetap. Sesi latihan penentu di akhir paruh semester. |
| **Class / Lecture (授業)** | **Kelas** | Pelajaran teori idol di kelas sekolah. |
| **Consultation (相談)** | **Konsultasi** | Tempat belanja P-Drink & kartu (shop). |
| **Rest (休憩)** | **Istirahat** | Memulihkan stamina idol. |
| **Go Out (おでかけ)** | **Jalan-jalan** | Rekreasi untuk stamina/menghilangkan debuff (alternatif singkat: *"Keluar"*). |
| **Self Practice (自主練)** | **Latihan Mandiri** | Latihan malam hari (singkat: *"Mandiri"*). |
| **Midterm Exam (中間試験)** | **Ujian Tengah** | Ringkas dan jelas di UI (alternatif: *"Midterm"*). |
| **Final Exam (最終試験)** | **Ujian Akhir** | Ujian penentu kelulusan dan rank akhir. |

---

## 6. Struktur File & Prioritas

### Fase 1 — UI Inti & Sistem Game 🔴 (Kerjakan Pertama)
*Dampak: semua layar game, menu, tombol, item, tutorial, dan teks umum langsung berubah ke Indonesia*

| File | Isi | Volume | Status / Prioritas |
|---|---|---|---|
| `local-files/localization.json` | String UI utama, menu, live, profil, setting | 6.958 key | ✅ Selesai (100%) |
| `local-files/generic.json` | Kamus generik root sistem UI & fallback | 525 key | ✅ Selesai (100%) |
| `local-files/genericTrans/index/tutorial.json` | Teks panduan tutorial & mekanik | 299 key | ✅ Selesai (100%) |
| `local-files/genericTrans/index/News.json` | Pengumuman update, gacha, event | 283 key | ✅ Selesai (100%) |
| `local-files/genericTrans/index/ProduceCardCustomize.json` | Kustomisasi kartu & biaya | 43 key | ✅ Selesai (100%) |
| `local-files/genericTrans/index/Item.json` | Nama & deskripsi item login/paket | 27 key | ✅ Selesai (100%) |
| `local-files/genericTrans/index/flavor.json` | Flavor text & peringatan hukum | 12 key | ✅ Selesai (100%) |
| `local-files/genericTrans/index/mission.json` | Teks target misi Produce | 11 key | ✅ Selesai (100%) |
| `local-files/genericTrans/index/mission.fmt.json` | Format string misi dinamis | 22 key | ✅ Selesai (100%) |
| `local-files/genericTrans/index/EventBlurb.json` | Teks blurb dialog banner event | 334 key | ✅ Selesai (100%) |
| `local-files/genericTrans/index/trash.json` | Kamus string UI umum & fallback | 2.510 key | ✅ Selesai (100%) |
| `local-files/genericTrans/lyrics/*.json` | Lirik lagu panggung / live MV (63 file) | 1.877 baris | 🔄 **Batch 1 Selesai (450 baris)** |

### Fase 2 — Kartu Skill (ProduceCard) & Cerita Utama 🟠
*Dampak: kartu skill battle/lesson Produce langsung berbahasa Indonesia, lalu diikuti alur cerita utama*

| File | Isi | Jumlah | Prioritas |
|---|---|---|---|
| `masterTrans/ProduceCard.json` | Deskripsi & nama kartu skill | 1.748 kartu (~438K baris) | ✅ **Selesai (100%)** |
| `resource/adv_startup_*.txt` | Opening / cutscene awal | 33 file | Prioritas 2 |
| `resource/adv_tutorial_*.txt` | Tutorial interaktif | 17 file | Prioritas 3 |
| `resource/adv_unit_*.txt` | Cerita unit (main story) | 66 file | Prioritas 4 |
| `masterTrans/ProduceStory.json` | Judul story produksi | ~18K baris | Prioritas 5 |

### Fase 3 — Konten Idol 🟡
*Dampak: cerita per karakter bisa dinikmati*

| File | Isi | Jumlah |
|---|---|---|
| `resource/adv_cidol_*.txt` | Cerita idol kandidat | 354 file |
| `resource/adv_dear_*.txt` | Bond/keakraban ADV | 494 file |
| `masterTrans/Achievement.json` | Deskripsi achievement | ~6K baris |
| `masterTrans/HelpContent.json` | Konten bantuan | ~2K baris |
| `masterTrans/SupportCardFlavor.json` | Flavor text support card | ~3K baris |

### Fase 4 — Konten Gameplay Dalam 🟢
*Dampak: pengalaman gameplay lebih lengkap*

| File | Isi | Jumlah |
|---|---|---|
| `resource/adv_pstory_*.txt` | Story produksi | 611 file |
| `resource/adv_csprt_*.txt` | Support card ADV | 529 file |
| `resource/adv_pevent_*.txt` | Event produksi | 1.105 file |

### Skip / Opsional ⚪
| File | Alasan Skip |
|---|---|
| `masterTrans/ProduceExam*.json` | Data teknis engine, bukan teks narasi |
| `masterTrans/ConditionSet.json` | Data kondisi teknis |
| `masterTrans/VoiceGroup.json` | Mapping voice ID |
| File berukuran 16 bytes | Placeholder kosong `{}` |

---

## 7. Alur Kerja (Workflow)

### 7.1 Alur per File

```
[Ambil file dari EN] 
    → [Buat draft terjemahan]
    → [Review natural & konsistensi]
    → [Cek format & placeholder]
    → [Validasi dengan script]
    → [Commit ke repo ID]
```

### 7.2 Langkah Detail

**Step 1 — Setup**
- [x] Sinkronisasi data acuan EN ke repo ID sebagai baseline
- [x] Setup struktur folder ID mengikuti hierarki game
- [x] Siapkan script validasi Python `resource_validator.py`
- [x] Siapkan script updater JSON Python `scripts/update_translation.py`

**Step 2 — Translate**
- [ ] Buka file target (mulai dari Fase 1)
- [ ] Buat draft terjemahan menggunakan panduan bahasa di dokumen ini
- [ ] Tandai istilah yang tidak yakin dengan `# TODO:` atau `[PERLU REVIEW]`
- [ ] Cek konsistensi dengan Glosarium

**Step 3 — Review**
- [ ] Baca ulang terjemahan — apakah terasa natural?
- [ ] Cek semua placeholder `{0}`, `{1}`, `\n` masih ada
- [ ] Cek tag HTML/Unity tidak rusak
- [ ] Cek tidak ada inkonsistensi nama/istilah

**Step 4 — Validasi Teknis & Pembaruan File**
- [ ] Untuk file resource `.txt`: jalankan `resource_validator.py`
- [ ] Untuk file JSON (`localization.json`, `genericTrans/*.json`): gunakan `python scripts/update_translation.py <batch_terjemahan.json> -t <target.json>` untuk menerapkan pembaruan tanpa mengacak urutan key, menjaga integritas placeholder/tag, dan memvalidasi sintaks otomatis.
- [ ] Test di game jika memungkinkan

**Step 5 — Commit**
- [ ] Commit dengan message yang deskriptif:
  ```
  translate: localization.json - UI strings (achievement, tutorial sections)
  translate: adv_unit_01-01 - Unit 1 Chapter 1 dialog
  fix: typo di localization.json key work.result.title
  ```

---

### 7.3 Penggunaan AI untuk Draft Awal

AI (GPT/Claude) **boleh digunakan** untuk membuat draft, tapi dengan aturan:

1. **Selalu berikan konteks karakter** ke AI saat menerjemahkan dialog
2. **Jangan langsung pakai** hasil AI tanpa review manual
3. **Prompt yang direkomendasikan:**

```
Kamu adalah penerjemah profesional untuk game Gakuen Idolm@ster ke bahasa Indonesia.
Terjemahkan teks berikut dengan gaya bahasa natural anak muda Indonesia,
pertahankan kepribadian karakter, dan jangan terjemahkan istilah game
(Produce, Audition, Skill Card, dll).

Karakter: [nama & deskripsi singkat kepribadian]
Konteks: [situasi scene]

Teks:
[teks yang akan diterjemahkan]
```

4. Setelah dapat draft dari AI, **review berdasarkan checklist** di bagian 8.

---

## 8. Standar Kualitas & Review

### 8.1 Checklist Review per Terjemahan

Sebelum commit, pastikan:

- [ ] **Natural** — teks enak dibaca, tidak terasa hasil mesin
- [ ] **Kepribadian** — gaya bicara sesuai karakter (jika dialog)
- [ ] **Konsisten** — nama/istilah sesuai Glosarium
- [ ] **Format aman** — placeholder `{0}`, `\n`, tag HTML tidak hilang/rusak
- [ ] **Panjang wajar** — teks tidak terlalu panjang untuk UI (untuk strings pendek)
- [ ] **Tidak ada typo** — cek ejaan Indonesia yang benar

### 8.2 Contoh Kasus

```
// Sumber EN:
"I have an important matter to discuss regarding our future direction."

// ❌ Draft Buruk:
"Aku memiliki sebuah hal penting yang harus didiskusikan mengenai arah masa depan kita."

// ✅ Draft Bagus:
"Ada hal penting yang perlu kita bicarain soal ke mana arah kita ke depannya."

---

// Sumber EN (karakter tsundere):
"I-It's not like I was worried about you or anything!"

// ❌ Draft Buruk:
"B-Bukan berarti aku khawatir tentangmu atau apapun!"

// ✅ Draft Bagus:
"B-Bukan berarti aku khawatir sama kamu atau gimana ya!"
```

### 8.3 Penandaan Teks Bermasalah

Gunakan komentar atau tag berikut jika menemui teks yang sulit:

| Tag | Arti |
|---|---|
| `[PERLU REVIEW]` | Terjemahan tidak yakin, butuh pendapat kedua |
| `[KONTEKS KURANG]` | Tidak cukup konteks untuk menerjemahkan dengan akurat |
| `[ISTILAH BARU]` | Ada istilah baru yang belum ada di Glosarium |
| `[CEKPANJANG]` | Teks mungkin terlalu panjang untuk UI |

---

## 9. Konvensi Format File

### 9.1 JSON Files
```json
{
  "key.name": "Terjemahan Indonesia di sini",
  "key.with.placeholder": "Teks dengan nilai {0} di sini",
  "key.with.newline": "Baris pertama\nBaris kedua",
  "key.with.color": "<color=#FF3381>Teks berwarna</color>"
}
```

### 9.2 Resource TXT Files
```
// HANYA ubah nilai setelah text=
// JANGAN ubah apapun di luar text=...

// Sebelum (EN):
[message text=It's finally time. name={user} se=sud_se_adv_message-01 clip=\{...\}]

// Sesudah (ID):
[message text=Akhirnya saatnya tiba. name={user} se=sud_se_adv_message-01 clip=\{...\}]
```

### 9.3 Struktur Commit Message
```
<tipe>: <deskripsi singkat>

Tipe yang valid:
- translate  : menambah terjemahan baru
- fix        : memperbaiki terjemahan yang salah/typo
- review     : perbaikan gaya bahasa tanpa mengubah makna
- glossary   : update glosarium
- docs       : update dokumentasi (termasuk file ini)
```

---

## 📝 Log Keputusan

> Semua keputusan sudah disepakati per Oktober 2026

| # | Topik | Status | Keputusan |
|---|---|---|---|
| 1 | Istilah "Bond" | ✅ Selesai | **Tetap "Bond"** — tidak diterjemahkan |
| 2 | Istilah "Turn" | ✅ Selesai | **Tetap "Turn"** — tidak diterjemahkan |
| 3 | Istilah "Fan" | ✅ Selesai | **Kontekstual** — UI=Fan, Dialog=Fan/Penggemar (lihat §5.3) |
| 4 | Lirik lagu | ✅ Selesai | **Diterjemahkan** — diterjemahkan puitis & berirama alami sesuai mood lagu / subtitle live stage (Batch 1 Selesai) |
| 5 | Format nama karakter | ✅ Selesai | **Ikut EN project** — JP order, ejaan asli |
| 6 | "Hatsuboshi Academy" | ✅ Selesai | **Tetap "Hatsuboshi Academy"** — tidak diterjemahkan |
| 7 | Sapaan ke pemain | ✅ Selesai | **Default "Kamu"** — idol yg panggil senpai tetap tulis **"Senpai"** (bukan Kak), pengecualian "Anda" untuk idol formal (lihat §5.4) |
| 8 | Atribut & Plan Gameplay | ✅ Selesai | **Vo / Da / Vi**, **Sense**, **Logic**, **Anomaly**, **Kartu Aktif**, **Kartu Mental**, **Kartu Trouble** (lihat §5.5.A) |
| 9 | Status & Buff Inti | ✅ Selesai | **Kondisi Prima**, **Kondisi Puncak**, **Kondisi Buruk**, **Fokus**, **Semangat**, **Kesan Baik** (lihat §5.5.B) |
| 10 | Status "Genki" | ✅ Selesai | ⭐ **Tetap "Genki"** — shield stamina, selaras audio & mekanik khas game |
| 11 | Mekanik Kartu & Giliran | ✅ Selesai | **Turn Tambahan**, **Hand** (UI) / **kartu di tangan** (dialog), **Deck**, **Discard**, **Exile**, **Hold**, **Penggunaan Kartu**, **Draw**, **Kenaikan Parameter** (lihat §5.5.C) |
| 12 | Aktivitas Sesi Produce | ✅ Selesai | **Lesson**, **Intensive Lesson**, **Kelas**, **Konsultasi**, **Istirahat**, **Jalan-jalan**, **Latihan Mandiri**, **Ujian Tengah**, **Ujian Akhir** (lihat §5.6) |
| 13 | Panggilan Staf & Sapaan Mao | ✅ Selesai | **Asari-sensei / Sensei** (guru), **Kepala Sekolah** (Gakuenchou), **Trainer** (pelatih), Mao memanggil Producer **"Kamu"** (lihat §10.3 & §10.4) |

---

## 📝 Catatan Terbuka

> Catat di sini jika muncul kasus baru yang belum ada aturannya

| # | Topik | Status | Catatan |
|---|---|---|---|
| — | *(belum ada)* | — | — |

---

## 10. Referensi Karakter

> Gunakan bagian ini sebagai **cheat sheet** saat menerjemahkan dialog. Pastikan gaya bicara dan sapaan antar karakter konsisten di seluruh file.
>
> 📄 Dokumen karakter lengkap (latar belakang, kelas, hubungan detail): [`Gakumas_Karakter.md`](./Gakumas_Karakter.md)

---

### 10.1 Unit & Kelompok Utama

| Unit | Anggota | Keterangan |
|---|---|---|
| **Re;IRIS** | Saki, Temari, Kotone | Unit inti *Hatsuboshi Komyu*. Trio "sinyal lalu lintas" (merah-biru-kuning). |
| **Begrazia** | Ume, Misuzu, Sena | Unit rival utama di awal story. |
| **SyngUp!** | Temari, Misuzu, Rinha *(bubar)* | Unit lama SMP, bubar karena konflik. |
| Pasangan 2 orang | Lilja+Sumika, China+Hiro, Mao+Rinami | Sering muncul di story produce. |

---

### 10.2 Profil Gaya Bicara per Karakter

#### 🔴 花海 咲季 — Hanami Saki
- **Kepribadian**: Kompetitif, temperamental, sombong di permukaan, sangat peduli di dalam
- **Gaya bicara**: Blak-blakan, penuh semangat, sering menantang, kadang agresif
- **Partikel favorit**: `ぞ / だ / じゃないか` → Indonesia: kalimat tegas pendek, "nggak mungkin aku kalah!", "liat aja nanti!"
- **Sapaan ke Producer**: **Kamu** (santai, blak-blakan)
- **Sapaan ke Ume**: nama langsung ("Ume!") — adik kandung, sangat akrab
- **Hindari**: Bahasa terlalu sopan/lembut — tidak sesuai karakter

```
// Contoh tone Saki:
"Hah? Kamu pikir aku bakal kalah? Nggak mungkin!"
"Gue nggak butuh dikasihani. Gue bisa sendiri!"
```

---

#### 🔵 月村 手毬 — Tsukimura Temari
- **Kepribadian**: Luar: cool, stoic, sinis. Dalam: manja, pemalas, suka makan
- **Gaya bicara**: Kalimat pendek, kering, sinis — tapi kadang "bocor" jadi childish kalau momen tertentu
- **Sapaan ke Producer**: **Kamu** (dingin, tidak hangat)
- **Sapaan ke Misuzu**: nama langsung, hangat tersembunyi
- **Hindari**: Terlalu banyak emosi di permukaan — Temari menyembunyikan perasaan

```
// Contoh tone Temari:
"...Terserah."
"Bukan berarti aku mau bantuin kamu atau gimana."
"Hm. Lumayan lah."
```

---

#### 🟡 藤田 ことね — Fujita Kotone
- **Kepribadian**: Ceria, realistis, gila uang, pandai bergaul, tapi kurang percaya diri di dalam
- **Gaya bicara**: Riang, sering nyebut soal uang/popularitas, pandai basa-basi, kadang jadi penengah
- **Sapaan ke Producer**: **Kamu** (ramah, santai)
- **Hindari**: Terlalu dalam/serius — Kotone selalu ada sisi praktis/kalkulatif-nya

```
// Contoh tone Kotone:
"Eh, beneran? Wah, itu menguntungkan banget dong~"
"Aku nggak insecure kok! ...mungkin."
```

---

#### 有村 麻央 — Arimura Mao
- **Kepribadian**: Tomboy, bertanggung jawab, caring seperti kakak asrama
- **Gaya bicara**: Tegas tapi hangat, seperti kakak yang perhatian
- **Sapaan ke Producer**: **Kamu** (santai, setara)
- **Sapaan ke junior**: Nama langsung atau dengan sentuhan "kakak yang perhatian"
- **Catatan**: Sebenarnya ingin terlihat feminin/lucu — kalau ada momen ini, tunjukkan kecanggungannya

---

#### 葛城 リーリヤ — Katsuragi Lilja
- **Kepribadian**: Pemalu, kurang percaya diri, polos, rajin
- **Gaya bicara**: Ragu-ragu, kalimat sering tidak selesai, banyak "e..." dan "a...", tapi tulus
- **Sapaan ke Producer**: **Senpai** (junior yang menghormati senior)
- **Hindari**: Terlalu percaya diri — Lilja masih dalam proses tumbuh

```
// Contoh tone Lilja:
"E-eh... aku boleh ikut, Senpai?"
"Aku... aku pasti bisa. Mungkin."
```

---

#### 倉本 千奈 — Kuramoto China
- **Kepribadian**: Awalnya manja/spoiled, tapi baik hati dan punya potensi tersembunyi
- **Gaya bicara**: Sedikit centil, kadang terkesan manja, tapi hangat
- **Sapaan ke Producer**: **Senpai**

---

#### 紫雲 清夏 — Shiun Sumika
- **Kepribadian**: Gyaru ceria, santai, mudah akrab — tapi ada trauma tersembunyi soal dance
- **Gaya bicara**: Santai, gaul, banyak senyum — tapi kalau menyinggung dance, ada keretakan
- **Sapaan ke Producer**: **Senpai** atau **Kamu** (tergantung kedekatan di scene)
- **Catatan**: Saat membahas trauma ballet, nada harus berubah drastis — lebih tenang, tertutup

---

#### 篠澤 広 — Shinosawa Hiro
- **Kepribadian**: Genius akademik ekstrem, kemampuan fisik/idol hampir nol, eccentric
- **Gaya bicara**: Analitis, sering pakai istilah teknis/ilmiah, tapi polos soal hal sehari-hari
- **Sapaan ke Producer**: **Senpai**

```
// Contoh tone Hiro:
"Secara statistik, probabilitas keberhasilan metode ini adalah..."
"Oh. Jadi *ini* yang disebut 'lelah'. Menarik."
```

---

#### 姫崎 莉波 — Himesaki Rinami
- **Kepribadian**: Dewasa, gentle, tipe kakak — tapi punya sisi yang belum sembuh dari trauma peran "adik"
- **Gaya bicara**: Lembut, hangat, dewasa — *childhood friend Producer*, jadi bisa lebih santai
- **Sapaan ke Producer**: **Kamu** (akrab, childhood friend — boleh lebih personal)
- **Catatan**: Satu-satunya karakter yang punya latar sebagai childhood friend pemain

---

#### 花海 佑芽 — Hanami Ume
- **Kepribadian**: Sangat energik, loud, impulsive, childlike — fisik kuat tapi ingatan buruk
- **Gaya bicara**: Antusias, banyak tanda seru, langsung to the point, kadang salah ngerti
- **Sapaan ke Producer**: **Senpai**
- **Sapaan ke Saki**: "Onee-chan" → terjemahkan **"Kak Saki"**

```
// Contoh tone Ume:
"WAAAAH SENPAI KEREN BANGET!!!"
"Kak Saki, aku pasti bisa ngalahin kamu suatu hari!"
```

---

#### 秦谷 美鈴 — Hataya Misuzu
- **Kepribadian**: Sangat santai, soft-spoken, caring seperti ibu — tapi ada sisi possessive tersembunyi
- **Gaya bicara**: Lambat, lembut, banyak jeda, tapi kata-katanya mengena
- **Sapaan ke Producer**: **Senpai**
- **Sapaan ke Temari**: "Mari-chan" — sangat motherly
- **Catatan**: Di permukaan selalu tenang — tapi kalau momen cemburu/takut ditinggal, tunjukkan lewat pilihan kata yang sedikit lebih intens

```
// Contoh tone Misuzu:
"Mari-chan... jangan terlalu memaksakan diri, ya."
"Hm~ Senpai boleh ke mana saja, kok... selama balik ke sini."
```

---

#### 十王 星南 — Juo Sena
- **Kepribadian**: Prima Stella, sempurna di segala hal, elegan — tapi di baliknya sedang mencari arti baru
- **Gaya bicara**: Formal, elegan, terkontrol — tapi bukan kaku
- **Sapaan ke Producer**: **Anda** *(karena posisi dan kepribadiannya yang formal)*
- **Catatan**: Sena adalah pengecualian utama yang pakai "Anda" ke Producer

```
// Contoh tone Sena:
"Apakah Anda sudah mempersiapkan diri dengan baik?"
"Saya mengakui bakat Anda. Tapi apakah itu sudah cukup?"
```

---

#### 雨夜 燕 — Amaya Tsubame
- **Kepribadian**: Sangat proud, sombong, keras — tapi sebenarnya caring dan mengidolakan Sena
- **Gaya bicara**: Tegas, sedikit angkuh, tidak suka basa-basi — tapi bisa hangat saat guard-nya turun
- **Sapaan ke Producer**: **Kamu** (tidak mau terlalu formal, tapi juga tidak terlalu akrab)

```
// Contoh tone Tsubame:
"Hmph. Jangan bangga dulu."
"...Bagus juga. Tapi masih jauh dari Sena."
```

---

### 10.3 Ringkasan Relasi Kunci (untuk Konsistensi Sapaan)

| Dari → Ke | Sapaan | Catatan |
|---|---|---|
| **Ume → Saki** | "Kak Saki" | Adik ke kakak kandung (Onee-chan → Kak [nama]) |
| **Ume → Producer** | "Senpai" | Junior ke senior sekolah |
| **Lilja → Producer** | "Senpai" | Junior, sangat menghormati |
| **China → Producer** | "Senpai" | Junior |
| **Sumika → Producer** | "Senpai" | Junior |
| **Hiro → Producer** | "Senpai" | Junior |
| **Misuzu → Producer** | "Senpai" | Junior |
| **Mao → Producer** | "Kamu" | Siswi tahun ke-3, akrab & setara (sesekali "Producer" saat formal) |
| **Rinami → Producer** | "Kamu" | Childhood friend, hubungan akrab setara |
| **Saki → Producer** | "Kamu" | Santai, blak-blakan |
| **Temari → Producer** | "Kamu" | Dingin, tidak banyak basa-basi |
| **Kotone → Producer** | "Kamu" | Ramah, santai |
| **Sena → Producer** | "Anda" | Formal, Prima Stella |
| **Tsubame → Producer** | "Kamu" | Tidak terlalu formal |
| **Misuzu → Temari** | "Mari-chan" | Panggilan sayang, motherly |
| **Temari → Misuzu** | Nama langsung | Akrab tapi tidak lebay |
| **Producer → Asari-sensei** | "Asari-sensei" / "Sensei" | Menghormati guru & wali kelas |
| **Asari-sensei → Producer** | "Producer" | Default profesional & hangat (boleh "Kamu" di momen santai) |
| **Semua → Juo Kunio** | "Kepala Sekolah" | Resmi dan wajar di sekolah |
| **Semua → Trainer** | "Trainer" | Instruktur Vo/Da/Vi |

---

### 10.4 Karakter Staf, Pelatih & NPC

#### 根緒 亜紗里 — Neo Asari
- **Peran**: Guru Producer Department & wali kelas Producer (pemain)
- **Kepribadian**: Ramah, keibuan, lembut, penuh dukungan
- **Gaya bicara**: Sopan, mendidik, hangat — memandu pemain memahami sistem & memberi nasihat
- **Sapaan dari Producer**: **Asari-sensei** atau **Sensei**
- **Sapaan ke Producer**: **Producer** (default resmi/hangat) atau **Kamu** (saat santai)

#### 十王 邦夫 — Juo Kunio
- **Peran**: Kepala Sekolah Hatsuboshi Gakuen (kakek Sena Juo)
- **Kepribadian**: Berwibawa, berpengaruh, namun ramah dan eksentrik
- **Gaya bicara**: Berkarisma, santai tapi berbobot, penuh visi untuk murid-muridnya
- **Sapaan**: **Kepala Sekolah**

#### Trainer (Vocal, Dance, Visual)
- **Peran**: Instruktur pelatihan teknis di Hatsuboshi Gakuen
- **Gaya bicara**: Profesional, to-the-point, instruktif, memberi feedback performa latihan
- **Sapaan**: **Trainer** (tetap, tidak diubah jadi "Pelatih")

#### 真城 優 — Mashiro Yu
- **Peran**: Siswi Ordinary Department (Tahun 2) & MC *Hatsuboshi Broadcasting Club*
- **Kepribadian**: Normal, ramah, pengamat setia para idol
- **Gaya bicara**: Hidup, ceria layaknya penyiar radio/MC sekolah

---

*Dokumen ini bersifat aktif — akan terus diperbarui seiring project berkembang.*  
*Terakhir diperbarui: Oktober 2026*
