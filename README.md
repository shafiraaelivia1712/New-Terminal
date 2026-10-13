# HackNet v2.0 🖥️⚡

> `SYSTEM BREACHED - ROOT OK`

Selamat datang di **HackNet v2.0**, sebuah aplikasi berbasis CLI (Command Line Interface) bergaya terminal hacker interaktif. Program ini mensimulasikan lingkungan sistem terminal dengan perintah internal bawaan serta integrasi perintah sistem operasi.

---

## 🚀 Fitur Utama

- **Tampilan Retro Hacker:** Antarmuka terminal dengan *prompt* kustom bergaya akses `root`.
- **Daftar Perintah Lengkap:** Menyediakan perintah internal untuk simulasi dan utilitas navigasi dasar.
- **Dukungan Perintah Jaringan (`ping`):** Mendukung perintah `ping` lengkap beserta parameter opsionalnya.

---

## 📋 Perintah yang Tersedia

Ketik `help` pada terminal untuk menampilkan daftar perintah berikut:

### Perintah Internal
* `help` — Menampilkan daftar perintah yang tersedia.
* `clear` — Membersihkan tampilan terminal.
* `matrix` — Efek visual antarmuka Matrix.
* `scan` — Melakukan pemindaian target/jaringan.

### Perintah Sistem
* `cd` — Mengubah direktori kerja.
* `ping` — Memeriksa konektivitas ke host target.
* `dir` / `ls` — Menampilkan isi direktori saat ini.

---

## 🛠️ Opsi Perintah `ping`

Penggunaan perintah `ping` mendukung berbagai opsi bawaan sistem:

```text
Usage: ping [-t] [-a] [-n count] [-l size] [-f] [-i TTL] [-v TOS]
            [-r count] [-s count] [-j host-list] [-k host-list]
            [-w timeout] [-R] [-S srcaddr] [-c compartment] [-p]
            [-4] [-6] target_name
```

| Opsi | Keterangan |
| :--- | :--- |
| `-t` | Melakukan ping terus-menerus sampai dihentikan (Ctrl+C). |
| `-n count` | Menentukan jumlah paket echo yang dikirim. |
| `-l size` | Menentukan ukuran buffer yang dikirim. |
| `-w timeout` | Menentukan batas waktu tunggu (*timeout*) dalam milidetik. |
| `-4` / `-6` | Memaksa penggunaan IPv4 atau IPv6. |

---

## 💻 Cara Menjalankan

1. Pastikan Anda telah menginstal **Python 3.x**.
2. Clone repositori ini atau unduh kode sumbernya:
   ```bash
   git clone https://github.com/username-anda/nama-repo.git
   cd nama-repo
   ```
3. Jalankan script utama:
   ```bash
   python main.py
   ```

---

## 📷 Tangkapan Layar

```text
root@hacknet:F:\WEB\WEB ; INSPIRATIONS\New Terminal # help
Perintah internal: help, clear, matrix, scan
Perintah sistem   : cd, ping, dir/ls, dll (tergantung OS)
```

---

*Dikembangkan untuk eksperimen terminal CLI.*
