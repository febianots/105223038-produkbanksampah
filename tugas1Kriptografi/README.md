# Aplikasi Bank Sampah Digital — Komponen Dasar Kriptografi

Sistem manajemen Bank Sampah Digital yang menyediakan layanan pencatatan setoran sampah, pengelolaan saldo nasabah, autentikasi pengguna, dan penerbitan token transaksi aman.

1. Tabel Kebutuhan Kriptografi

No : `1`
Data yang Dilindungi : `Kredensial Pengguna (Password)`
Tujuan Keamanan : `Confidentiality & Integrity`
Prioritas : `High`
Mekanisme Kriptografi : `Hashing aman menggunakan Argon2id / PBKDF2 (SHA-256) dengan salt acak per pengguna.`

No : `2`
Data yang Dilindungi : `Token Sesi & Reset Password`
Tujuan Keamanan : ``
Prioritas : ``
Mekanisme Kriptografi : ``

No : `3`
Data yang Dilindungi : `Data Pribadi Nasabah (NIK/No. HP)`
Tujuan Keamanan : `Authenticity & Unpredictability`
Prioritas : `High`
Mekanisme Kriptografi : `Kriptografis acak berkekuatan tinggi (secrets.token_urlsafe(32)).`

2. Rancangan Komponen Kriptografi

A. Hashing Password & Garam (Salt)
Masukan: Kata sandi teks biasa (_plain text_) dan _salt_ acak 16-byte.
Proses: Menghasilkan hash derivasi kunci menggunakan PBKDF2-HMAC-SHA256 dengan 100.000 iterasi.
Keluaran: Kombinasi `$pbkdf2-sha256$iterations$salt_hex$hash_hex` berformat standar.
Representasi Data: String terformat Hexadecimal/Base64.
Sumber Keacakan: `secrets.token_bytes(16)` (OS CSPRNG).

B. Generator Token Transaksi & Sesi
Masukan:** Panjang byte acak (default: 32 byte).
Proses:** Membaca byte aman kriptografis dari sistem operasi.
Keluaran:** String URL-safe Base64 tanpa karakter ambigu.
Sumber Keacakan:** `secrets.token_urlsafe(32)`.

C. Enkripsi Simetris Data Sensitif Nasabah
Masukan: Teks biasa (misal: NIK/Nomor Telepon) dan Kunci Simetris 256-bit.
Proses: AES-CBC/GCM (via Fernet / `cryptography.fernet`).
Keluaran: Teks tersandi (_ciphertext_) terautentikasi HMAC.
Representasi Data: String terenkripsi Base64.

3. Cara Menjalankan Aplikasi dan Pengujian

Prasyarat
Python 3.9+
Pustaka `pytest`

Langkah-langkah

1. Pasang dependensi yang dibutuhkan:
   ```bash
   pip install pytest cryptography

   ```
2. Jalankan seluruh pengujian otomatis dengan pytest untuk memastikan seluruh komponen kriptografi berjalan dengan benar :
   `pytest -v`
