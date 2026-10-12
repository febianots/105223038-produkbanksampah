# Risk Register & Analisis Risiko Produk

Penilaian dilakukan menggunakan skala Likelihood (1–5) dan Impact (1–5) merujuk pada standar penilaian Tugas 1 (NIST SP 800-30 adaptation).

1. Register Risiko Lengkap

Risk ID : `R-01`
Threat ID : `T-05`
Control Saat Ini : `Port 5432 terbuka; default password PostgreSQL`
L (1-5) : `5`
Alasan Likelihood : `Terkoneksi internet, port terbuka secara default pada docker-compose.yml, dapat di-scan bot otomatis.`
I (1-5) : `5`
Alasan Impact : `Seluruh kredensial, PII nasabah, dan data transaksi dapat dicuri; pelanggaran UU PDP.`
Total Risk (L×I) : `25`
Level Risk : `Very high`
Response : `Mitigate`
Rencana Control Spesiﬁk : `Matikan eksposur port 5432 ke internet (bind 127.0.0.1 / internal docker network) dan ganti password DB.`
Peta Tugas : `Tugas 2`

Risk ID : `R-02`
Threat ID : `T-03`
Control Saat Ini : `Validasi peran hanya ada di halaman middleware UI`
L (1-5) : `4`
Alasan Likelihood : `Cukup menggunakan akun nasabah biasa dan memanggil API endpoint admin dengan Postman/Curl.`
I (1-5) : `4`
Alasan Impact : `Nasabah dapat mengubah status setoran, menaikkan saldo sendiri, dan mengambil alih fungsi admin.`
Total Risk (L×I) : `16`
Level Risk : `Very high`
Response : `Mitigate`
Rencana Control Spesiﬁk : `Terapkan pemeriksaan otorisasi berbasis peran (RBAC Check) di setiap API Handler/Controller backend.`
Peta Tugas : `Tugas 2`

Risk ID : `R-03`
Threat ID : `T-04`
Control Saat Ini : `Menggunakan ORM sederhana tanpa sanitasi penuh`
L (1-5) : `3`
Alasan Likelihood : `Membutuhkan pencarian parameter query yang rentan pada input pencarian setoran.`
I (1-5) : `5`
Alasan Impact : `Seluruh isi basis data dapat dibaca, diubah, atau dihapus total melalui perintah terinjeksi.`
Total Risk (L×I) : `15`
Level Risk : `Very high`
Response : `Mitigate`
Rencana Control Spesiﬁk : `Pakai Parameterized Query / ORM Prepared Statement secara penuh dan sanitasi input pengguna.`
Peta Tugas : `Tugas 2`

Risk ID : `R-04`
Threat ID : `T-01`
Control Saat Ini : `Belum ada mekanisme rate limiting`
L (1-5) : `4`
Alasan Likelihood : `Penyerang dapat mengunduh daftar email bocor dan menjalankan skrip brute force login secara bebas.`
I (1-5) : `3`
Alasan Impact : `Pengambilalihan akun nasabah secara acak, kerugian klaim saldo setoran pengguna.`
Total Risk (L×I) : `12`
Level Risk : `high`
Response : `Mitigate`
Rencana Control Spesiﬁk : `Pasang Rate Limiting (misal: Nginx limit_req atau express-rate-limit max 5 percobaan/menit).`
Peta Tugas : `Tugas 3 (Part A)`

Risk ID : `R-05`
Threat ID : `T-09`
Control Saat Ini : `Skrip backup menyimpan berkas teks biasa`
L (1-5) : `3`
Alasan Likelihood : `Memerlukan akses terorotisasi ke filesystem VM lokal server.`
I (1-5) : `4`
Alasan Impact : `Berkas dump memuat seluruh riwayat transaksi dan hash password nasabah secara lengkap.`
Total Risk (L×I) : `12`
Level Risk : `high`
Response : `Mitigate`
Rencana Control Spesiﬁk : `Tambahkan enkripsi simetris GPG/OpenSSL AES-256 pada skrip P2 sebelum file diletakkan di DS2.`
Peta Tugas : `Tugas 3 (Part B)`

Risk ID : `R-06`
Threat ID : `T-07`
Control Saat Ini : `Server memproses semua request langsung`
L (1-5) : `3`
Alasan Likelihood : `Diperlukan pembuatan skrip HTTP flood otomatis dari beberapa IP.`
I (1-5) : `3`
Alasan Impact : `Layanan lambat atau mengalami crash sementara (downtime).`
Total Risk (L×I) : `9`
Level Risk : `high`
Response : `Mitigate`
Rencana Control Spesiﬁk : `Konfigurasi reverse proxy / Cloudflare DDoS protection dan HTTP request timeout.`
Peta Tugas : `Tugas 3 (Part A)`

Risk ID : `R-07`
Threat ID : `T-08`
Control Saat Ini : `Log aplikasi standar tanpa identitas DB`
L (1-5) : `2`
Alasan Likelihood : `Memerlukan akses level admin yang sudah terkompromi.`
I (1-5) : `4`
Alasan Impact : `Tidak ada jejak pembuktian forensik jika terjadi kecurangan internal admin.`
Total Risk (L×I) : `8`
Level Risk : `high`
Response : `Mitigate`
Rencana Control Spesiﬁk : `Terapkan Structured Audit Logging (JSON Format) yang mencatat User ID, IP, dan Perubahan State.`
Peta Tugas : `Tugas 3 (Part B)`

Risk ID : `R-08`
Threat ID : `T-06`
Control Saat Ini : `Framework mode development aktif`
L (1-5) : `2`
Alasan Likelihood : `Muncul saat terjadi kesalahan tak terduga (runtime error) di aplikasi.`
I (1-5) : `2`
Alasan Impact : `Membocorkan struktur folder dan versi pustaka, namun bukan data langsung.`
Total Risk (L×I) : `4`
Level Risk : `Moderate`
Response : `Mitigate`
Rencana Control Spesiﬁk : `Atur NODE_ENV=production dan buat halaman kustom penanganan galat (Error Page).`
Peta Tugas : `Tugas 2`

Risk ID : `R-09`
Threat ID : `T-02`
Control Saat Ini : `Sertifikat TLS terpasang di reverse proxy`
L (1-5) : `1`
Alasan Likelihood : `Memerlukan penyerangan man-in-the-middle di jalur HTTPS aktif.`
I (1-5) : `4`
Alasan Impact : `Manipulasi nilai setoran saldo nasabah.`
Total Risk (L×I) : `4`
Level Risk : `Moderate`
Response : `Acc`
Rencana Control Spesiﬁk : `Pertahankan enforced HTTPS redirect (HSTS aktif).`
Peta Tugas : `Tugas 3 (Part A)`



2. Rincian 5 Risiko Prioritas Utama (Top Priority Risks)

A. R-01 (T-05): Database Port Exposed & Default Credentials
    - Level Risiko: 25 (Very High)
    - Justifikasi Condition: Port 5432 PostgreSQL terbuka langsung ke antarmuka 0.0.0.0 pada konfigurasi container dasar, memicu deteksi otomatis oleh mesin pencari seperti Shodan.
    - Rencana Kontrol: Mengisolasi port PostgreSQL ke jaringan internal Docker (bridge network) tanpa publikasi port ke host luar, serta mengubah password bawaan di .env. (Rencana Implementasi: Tugas 2).

B. R-02 (T-03): Missing Authorization Check on Admin API (BOPA / IDOR)
    - Level Risiko: 16 (Very High)
    - Justifikasi Condition: Pengecekan otorisasi pengguna hanya terjadi di sisi frontend routing, sehingga penyerang dapat melompati UI dan langsung memanggil endpoint API internal dengan hak akses JWT biasa.
    -Rencana Kontrol: Mengimplementasikan RBAC Middleware pada skema API backend yang memverifikasi atribut user.role === 'ADMIN' pada setiap permintaan HTTP inbound. (Rencana Implementasi: Tugas 2).

C. R-03 (T-04): SQL Injection pada Parameter Filter Setoran
    - Level Risiko: 15 (Very High)
    - Justifikasi Condition: Penggabungan string manual (string concatenation) masih digunakan pada pembuatan klausa WHERE di fungsi pencarian histori setoran.
    - Rencana Kontrol: Menghapus seluruh raw query terikat string concatenation dan menggantinya dengan Prepared Statements / Parameterized Queries ORM. (Rencana Implementasi: Tugas 2).

D. R-04 (T-01): Credential Stuffing & Brute-Force pada Endpoint Auth
    - Level Risiko: 12 (High)
    - Justifikasi Condition: Endpoint /api/auth/login menerima permintaan tanpa batasan kuota per alamat IP, mempermudah pengujian ribuan kombinasi kredensial per menit.
    - Rencana Kontrol: Menerapkan rate limiter berbasis Redis/Memory yang membatasi maksimum 5 kali percobaan kegagalan login per IP dalam durasi 15 menit. (Rencana Implementasi: Tugas 3 Part A).