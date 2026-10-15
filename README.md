# Gakumas-Translation-Data-ID

Repositori data lokalisasi Bahasa Indonesia untuk game Gakuen Idolm@ster (学園アイドルマスター).

Proyek ini merupakan adaptasi dari repositori terjemahan Bahasa Inggris [Gakumas-Translation-Data-EN](https://github.com/NatsumeLS/Gakumas-Translation-Data-EN) dan ditujukan untuk digunakan bersama plugin [gakuen-imas-localify](https://github.com/chinosk6/gakuen-imas-localify).

---

## Gambaran Proyek

Proyek ini bertujuan menghadirkan teks permainan Gakuen Idolm@ster dalam Bahasa Indonesia yang mengalir, alami, dan mempertahankan kepribadian masing-masing karakter serta istilah mekanik game resmi.

Seluruh panduan penulisan, filosofi terjemahan, dan glosarium istilah tercantum di [PROPOSAL_TERJEMAHAN.md](./PROPOSAL_TERJEMAHAN.md).  
Profil detail kepribadian dan hubungan antar karakter tersedia di [Gakuen_Idolmaster_Karakter.md](./Gakuen_Idolmaster_Karakter.md).  
Status dan pelacakan progres pengerjaan dapat dilihat di [PROGRESS.md](./PROGRESS.md).

---

## Lingkup Konten

1. UI dan Menu Sistem (`local-files/localization.json`)
2. Teks Tutorial dan Notifikasi Umum (`local-files/genericTrans/index/`)
3. Naskah Cerita dan Dialog ADV (`local-files/resource/`)
4. Deskripsi Kartu, Misi, dan Database Permainan (`local-files/masterTrans/`)

Lirik lagu (`genericTrans/lyrics/`) dan data teknis engine tidak diterjemahkan.

---

## Cara Pemasangan

### Prasyarat
- Gakuen Idolm@ster (versi DMM Games / PC atau Android yang mendukung injeksi).
- Plugin `gakuen-imas-localify` terpasang dan berfungsi normal.

### Langkah Instalasi
1. Unduh atau clone repositori ini:
   ```bash
   git clone https://github.com/SayMaven/Gakumas-Translation-Data-ID.git
   ```
2. Salin isi folder `local-files/` dari repositori ini ke folder data terjemahan plugin `gakuen-imas-localify` di direktori game Anda.
3. Pastikan konfigurasi plugin mengarah ke file terjemahan yang baru disalin.
4. Jalankan game seperti biasa.

---

## Struktur Repositori

```
Gakumas-Translation-Data-ID/
├── local-files/
│   ├── localization.json      # Terjemahan teks antarmuka (UI)
│   ├── generic.json           # Teks umum hasil kompilasi
│   ├── genericTrans/          # Berkas sumber teks umum per kategori
│   ├── masterTrans/           # Berkas database game (kartu, misi, achievement)
│   └── resource/              # Skrip dialog dan cerita ADV (.txt)
├── scripts/                   # Skrip validasi dan pembantu format
├── PROPOSAL_TERJEMAHAN.md     # Panduan gaya bahasa, aturan terjemahan, dan glosarium
├── Gakuen_Idolmaster_Karakter.md # Referensi detail karakter dan relasi
├── PROGRESS.md                # Pelacak progres pengerjaan
└── README.md                  # Dokumentasi utama proyek
```

---

## Pedoman Kontribusi

1. Sebelum menerjemahkan, baca dan pahami [PROPOSAL_TERJEMAHAN.md](./PROPOSAL_TERJEMAHAN.md) agar gaya bahasa dan istilah tetap konsisten.
2. Periksa [PROGRESS.md](./PROGRESS.md) untuk memastikan file yang akan Anda kerjakan belum diambil oleh orang lain.
3. Pertahankan tag format Unity seperti `<color=#...>`, newline `\n`, dan placeholder `{0}`, `{1}`.
4. Gunakan format pesan commit standar:
   - `translate: <nama file/bagian yang diterjemahkan>`
   - `fix: <koreksi typo atau makna>`
   - `review: <penyesuaian gaya bahasa>`

---

## Kredit dan Lisensi

- Hak cipta intelektual Gakuen Idolm@ster (学園アイドルマスター) sepenuhnya dimiliki oleh BANDAI NAMCO Entertainment Inc.
- Repositori basis terjemahan Bahasa Inggris oleh [NatsumeLS/Gakumas-Translation-Data-EN](https://github.com/NatsumeLS/Gakumas-Translation-Data-EN).
- Plugin loader oleh [chinosk6/gakuen-imas-localify](https://github.com/chinosk6/gakuen-imas-localify).
- Data terjemahan Bahasa Indonesia dalam repositori ini disediakan untuk tujuan non-komersial bagi komunitas pemain di Indonesia.
