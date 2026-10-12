# Asset Inventory - Produk Bank Sampah

Dokumen ini mencatat inventarisasi aset kritis sistem Bank Sampah beserta klasifikasi tingkat kerahasiaan (Confidentiality), integritas (Integrity), dan ketersediaan (Availability) berdasarkan standar penilaian risikonya.


1. Tabel Klasifikasi Aset Kritis (CIA Triad)

Asset ID : `AST-01`
Nama Aset : `Kredensial Pengguna`
Deskripsi & Lokasi Teknis : `Hash password, token JWT, dan session key nasabah & admin (DS1: PostgreSQL)`
Conf.(C) : `High`
Integ.(I) : `High`
Avail.(A) : `Moderate`
Justifikasi Dampak & Alasan Rating CIA : `Kebocoran hash/token memungkinkan pengambilalihan akun. Kerusakan kredensial menyebabkan kegagalan autentikasi total.`
Status Kriptografi : `Ya, Bcrypt/Argon2 + TLS 1.3 in-transit)`


Asset ID : `AST-02`
Nama Aset : `Data Pribadi Nasabah (PII)`
Deskripsi & Lokasi Teknis : `NIK, nama lengkap, nomor HP, alamat, dan nomor rekening (DS1: PostgreSQL)`
Conf.(C) : `High`
Integ.(I) : `High`
Avail.(A) : `Moderate`
Justifikasi Dampak & Alasan Rating CIA : `Kebocoran PII melanggar UU PDP No. 27/2022 (sanksi hukum & denda). Perubahan PII tanpa hak merugikan hak finansial nasabah.`
Status Kriptografi : `Ya, AES-256 at-rest pada kolom sensitif + TLS 1.3)`


Asset ID : `AST-03`
Nama Aset : `Rekap & Catatan Setoran`
Deskripsi & Lokasi Teknis : `Data transaksi setoran sampah, bobot kg, nominal rupiah, dan riwayat saldo (DS1: PostgreSQL)`
Conf.(C) : `Moderate`
Integ.(I) : `High`
Avail.(A) : `Moderate`
Justifikasi Dampak & Alasan Rating CIA : `Manipulasi berat/saldo berdampak langsung pada kerugian finansial Bank Sampah atau nasabah. Kebocoran data bersifat moderat.`
Status Kriptografi : `Tidak, (Dipertahankan integritasnya via DB Constraints & Audit Log)`


Asset ID : `AST-04`
Nama Aset : `Rahasia Aplikasi (Secrets & Keys)`
Deskripsi & Lokasi Teknis : `.env, JWT Secret Key, DB Passwords, API Keys Email (Host / Container Env)`
Conf.(C) : `High`
Integ.(I) : `High`
Avail.(A) : `High`
Justifikasi Dampak & Alasan Rating CIA : `Kebocoran rahasia memungkinkan attacker mengambil alih seluruh infrastruktur, basis data, dan impersonasi aplikasi.`
Status Kriptografi : `Ya (Di-hash/didekripsi saat runtime via Environment Variable)`


Asset ID : `AST-05`
Nama Aset : `Basis Data Utama (DS1)`
Deskripsi & Lokasi Teknis : `Container PostgreSQL & berkas volume data (PostgreSQL Volume)`
Conf.(C) : `High`
Integ.(I) : `High`
Avail.(A) : `High`
Justifikasi Dampak & Alasan Rating CIA : `Kegagalan/kerusakan basis data menghentikan seluruh operasional produk. Kebocoran file storage membocorkan seluruh aset AST-01 s.d AST-03.`
Status Kriptografi : `Ya, (Encrypted Storage Volume / TDE)`


Asset ID : `AST-06`
Nama Aset : `Berkas Cadangan (Backup Data)`
Deskripsi & Lokasi Teknis : `File .dump / .sql.gz hasil skrip backup otomatis (DS2: Local/Remote Backup Storage)`
Conf.(C) : `High`
Integ.(I) : `High`
Avail.(A) : `Moderate`
Justifikasi Dampak & Alasan Rating CIA : `Pencurian berkas backup membocorkan seluruh data historis sistem tanpa terdeteksi oleh logging aplikasi.`
Status Kriptografi : `Ya, (Enkripsi file AES-256 via GPG/OpenSSL sebelum disimpan)`


Asset ID : `AST-07`
Nama Aset : `Log Audit & Aplikasi`
Deskripsi & Lokasi Teknis : `Log akses, autentikasi, serta mutasi data (/var/log/app/ & Docker Logs)`
Conf.(C) : `Moderate`
Integ.(I) : `High`
Avail.(A) : `Low`
Justifikasi Dampak & Alasan Rating CIA : `Log yang diubah atau dihapus menghilangkan jejak audit forensik saat terjadi insiden keamanan (melanggar prinsip Non-repudiation).`
Status Kriptografi : `Tidak, (Protected append-only log storage)`


Asset ID : `AST-01`
Nama Aset : `Akun Administrative`
Deskripsi & Lokasi Teknis : `Hak akses root/admin aplikasi dan VM Server (PostgreSQL & App Middleware)`
Conf.(C) : `High`
Integ.(I) : `High`
Avail.(A) : `High`
Justifikasi Dampak & Alasan Rating CIA : `Kompromi akun admin memberikan kontrol penuh ke penyerang untuk merusak data, mengubah konfigurasi, dan mematikan layanan.`
Status Kriptografi : `Ya, (MFA / Encrypted Session Token)`


2. Definisi Tingkat Dampak (CIA Rating)

- High (Tinggi): Dampak sangat parah. Menyebebabkan kegagalan operasional total, kerugian finansial material, atau pelanggaran hukum/regulasi berat.
- Moderate (Sedang): Dampak terbatas. Mengganggu sebagian fungsi operasional, kerugian finansial minor, atau ketidaknyamanan pengguna.
- Low (Rendah): Dampak minimal. Tidak mengganggu operasional sistem dan tidak memiliki implikasi finansial/hukum secara langsung.
