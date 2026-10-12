# STRIDE Threat Model - Produk Bank Sampah

Analisis menggunakan pendekatan `STRIDE-per-element` berdasarkan DFD produk.

# Tabel Daftar Ancaman (Minimal 10 Threat)

Threat ID : `T-01`
ID Elemen DFD : `F1`
Kategori STRIDE : `Spoofing`
Threat Statement (Spesifik & Teruji) : `Attacker eksternal dapat melakukan credential stuffing atau brute-force pada endpoint login P1 melalui lalu lintas HTTP/HTTPS tanpa pembatasan rate limit, sehingga dapat impersonate nasabah valid.`
Aset Terdampak : `AST-01, AST-02`


Threat ID : `T-02`
ID Elemen DFD : `F1`
Kategori STRIDE : `Tampering`
Threat Statement (Spesifik & Teruji) : `Attacker di jaringan lokal terdekat (MITM) dapat mengubah bobot setoran pada payload HTTP permintaan transaksi F1 jika komunikasi tidak dipaksa menggunakan HTTPS (TLS 1.3), sehingga memanipulasi nilai saldo.`
Aset Terdampak : `AST-03`


Threat ID : `T-03`
ID Elemen DFD : `P1`
Kategori STRIDE : `Elevation of Privilege`
Threat Statement (Spesifik & Teruji) : `Nasabah terautentikasi dapat memanggil secara langsung endpoint REST API khusus Admin (misal: /api/admin/setoran/approve) pada P1 tanpa pengecekan otorisasi berbasis peran (RBAC) di tingkat API handler, sehingga dapat menyetujui setorannya sendiri.`
Aset Terdampak : `AST-03, AST-08`


Threat ID : `T-04`
ID Elemen DFD : `F3`
Kategori STRIDE : `Tampering`
Threat Statement (Spesifik & Teruji) : `Attacker dapat menyisipkan perintah SQL berbahaya (SQL Injection) pada parameter pencarian transaksi di P1 menuju DS1, sehingga mengubah atau menghapus catatan setoran pada basis data.`
Aset Terdampak : `AST-03, AST-05`


Threat ID : `T-05`
ID Elemen DFD : `DS1`
Kategori STRIDE : `Information Disclosure`
Threat Statement (Spesifik & Teruji) : `Attacker atau pengguna yang tidak berhak dapat membaca file volume basis data DS1 yang tidak di-at-rest-encrypt atau membaca port 5432 PostgreSQL yang terbuka langsung ke public host tanpa password kuat, sehingga PII nasabah bocor.`
Aset Terdampak : `AST-01, AST-02, AST-05`


Threat ID : `T-06`
ID Elemen DFD : `P1`
Kategori STRIDE : `Information Disclosure`
Threat Statement (Spesifik & Teruji) : `Aplikasi P1 menampilkan stack trace dan detail query SQL pada respons galat HTTP 500 saat terjadi error, sehingga membeberkan struktur skema basis data dan direktori internal kepada attacker.`
Aset Terdampak : `AST-04, AST-05`


Threat ID : `T-07`
ID Elemen DFD : `P1`
Kategori STRIDE : `Denial of Service`
Threat Statement (Spesifik & Teruji) : `Attacker dapat mengirimkan ribuan permintaan login dan pembuatan laporan PDF secara simultan ke P1 tanpa adanya throttling/rate limiter, sehingga menguras konsumsi CPU/Memory VM server dan mematikan aplikasi.`
Aset Terdampak : `AST-05`


Threat ID : `T-08`
ID Elemen DFD : `DS1`
Kategori STRIDE : `Repudiation`
Threat Statement (Spesifik & Teruji) : `Admin yang nakal menghapus data setoran sampah nasabah pada DS1 langsung dari DBMS terminal tanpa adanya audit log terpusat yang mencatat identity dan command execution, sehingga tindakan manipulasi tidak dapat dibuktikan.`
Aset Terdampak : `AST-03, AST-07`


Threat ID : `T-09`
ID Elemen DFD : `F6`
Kategori STRIDE : `Information Disclosure`
Threat Statement (Spesifik & Teruji) : `Attacker yang berhasil mendapatkan akses shell lokal pada VM dapat membaca berkas .dump hasil skrip P2 sebelum dikirim ke DS2 karena file cadangan disimpan tanpa enkripsi (plain SQL text).`
Aset Terdampak : `AST-01, AST-02, AST-06`


Threat ID : `T-10`
ID Elemen DFD : `P2`
Kategori STRIDE : `Tampering / DoS`
Threat Statement (Spesifik & Teruji) : `Attacker memodifikasi skrip cron job P2 di container untuk menghentikan pembackupan otomatis atau mengarahkan tujuan cadangan F6 ke direktori tak valid, sehingga cadangan data rusak dan pemulihan bencana gagal.`
Aset Terdampak : `AST-05, AST-06`


Threat ID : `T-11`
ID Elemen DFD : `P1`
Kategori STRIDE : `Spoofing`
Threat Statement (Spesifik & Teruji) : `Attacker menggunakan JWT Token palsu yang di-sign menggunakan weak secret key yang berhasil ditebak dari repositori .env, sehingga dapat melewati validasi autentikasi P1.`
Aset Terdampak : `AST-01, AST-04`