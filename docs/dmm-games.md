# DMM Games

Menyiapkan Localify di PC.

***

### Prasyarat

> **⚠️ Peringatan**  
> Sebelum melanjutkan, pastikan Anda sudah memiliki **Akun DMM**.

> **VPN Jepang** mungkin diperlukan untuk mengakses dan mengunduh **DMM Game Player**.

[ProtonVPN (WireSock)](/vpn/protonvpn-wiresock.md)

***

### Langkah 1: Instal DMM Game Player

1. Kunjungi **Halaman Gakumas DMM**.

[https://dmg-gakuen.idolmaster-official.jp](https://dmg-gakuen.idolmaster-official.jp)

2. Klik **Game Start**.
3. Unduh dan instal **DMM Game Player** dengan memilihnya sebagai launcher.
4. Jalankan **DMM Game Player** dan masuk ke **Akun DMM** Anda jika diminta.

***

### Langkah 2: Instal Gakumas

1. Cari **Gakumas** di **DMM Game Player**.
2. Unduh dan instal gamenya.
3. Jalankan game sekali untuk memastikan bahwa game berjalan normal.

***

### Langkah 3: Siapkan Localify

1. Unduh **DMM_GakumasLocalify_vx.x.x.zip** dari rilis **Localify** terbaru.

[https://github.com/chinosk6/gakuen-imas-localify/releases/latest](https://github.com/chinosk6/gakuen-imas-localify/releases/latest)

2. Ekstrak file zip tersebut. Anda akan mendapatkan folder bernama `gakumas-local` dan file bernama `version.dll`.
3. Letakkan kedua item tersebut ke dalam folder instalasi **Gakumas**.

> **ℹ️ Info**  
> Direktori default: `C:\Users\%username%\gakumas`

> **⚠️ Peringatan**  
> Pastikan **`version.dll`** dan **`gakumas.exe`** berada di folder yang sama.

***

### Langkah 4: Siapkan Data Terjemahan

1. Hapus semua isi di dalam folder `gakumas-local`.

> **ℹ️ Info**  
> Direktori default: `C:\Users\%username%\gakumas\gakumas-local`

> **⚠️ Peringatan**  
> Langkah ini menghapus **Data Terjemahan** yang sudah dibundel bersama **Localify**.

2. Jalankan game dan tekan **Ctrl + U** untuk membuka **Gakumas Config GUI**.
3. Nonaktifkan `Fast Initialization` di `Basic Settings`.
4. Nonaktifkan `Replace Font` di `Basic Settings`.
5. Aktifkan `Check Resource Update From API` di `Resource Settings`.
6. Masukkan `https://api.github.com/repos/SayMaven/Gakumas-Translation-Data-ID/releases/latest`
7. Klik **Check** untuk mengunduh **Data Terjemahan**.
8. Aktifkan `MasterDB Localization` di `Debug Settings`.
9. Klik `Save Config`.

***

## Pembaruan

Ketika rilis **Localify** baru dipublikasikan, unduh dan ganti `version.dll` di folder instalasi **Gakumas** Anda. **Data Terjemahan** akan diperbarui melalui tombol **Check** di `Resource Settings`.

***

## Pemecahan Masalah

> **⚠️ Peringatan**  
> ### Terjemahan sebagian masih berbahasa China
> 1. Hapus folder `local-files` dan file `version.txt` di `C:\Users\%username%\gakumas\gakumas-local`.
> 2. Mulai ulang game dan unduh ulang **Data Terjemahan**.