# Ringkasan Aktivitas

Sesi: Penyusunan Threat Model, DFD, Asset Inventory, dan Risk Register (Pekan 3).

Model AI yang Digunakan: Gemini 3 Flash / Claude 3.5 Sonnet.

Tujuan Penggunaan: Generasi draf diagram Mermaid DFD, validasi kelengkapan kategori STRIDE-per-element, dan penataan format tabel Markdown.

Log Pertanyaan & Evaluasi Mandiri

1. Generasi Kategori STRIDE

Prompt AI: "Berikan usulan threat STRIDE untuk aplikasi Bank Sampah dengan komponen Next.js, PostgreSQL, dan skrip Backup Cron Job."

Hasil AI: AI memberikan 12 usulan threat. Sebagian ancaman bersifat generik seperti "Server diretas" dan "Layanan terbakar".

Tindakan/Koreksi Manusia:

Dihapus: Threat generik yang tidak memiliki rujukan elemen DFD dan dampaknya abstrak.

Disesuaikan: Menulis ulang threat agar presisi sesuai format standard [Threat source] + [Tindakan] + [Elemen DFD] + [Cara/Kelemahan] + [Dampak]. Contoh: Mengubah "Database dimasuki orang" menjadi "Attacker dapat membaca seluruh data nasabah di DS1 melalui port 5432..." (T-05).

2. Penilaian Likelihood dan Impact

Prompt AI: "Berapa CVSS score untuk SQL Injection dan buatkan nilai Likelihood/Impact-nya."

Hasil AI: AI memberikan nilai Likelihood 5 dan Impact 5 untuk semua threat.

Tindakan/Koreksi Manusia:

AI cenderung menyamakan CVSS dengan Risk Level tanpa melihat exposure produk di lingkungan lab.

Nilai disesuaikan ulang menggunakan Skala Tugas 1 (1–5) berdasarkan kondisi konkret arsitektur produk yang berjalan di docker environment (misalnya: R-08 dinilai Likelihood 2 karena NODE_ENV hanya muncul saat galat sistem terjadi).

3. Pemetaan Rencana Kontrol Ke Tugas Selanjutnya

Tindakan Manusia: Memetakan secara mandiri 5 risiko prioritas utama ke Tugas 2 (Software & Application Level Security) dan Tugas 3 (Infrastructure & Operating System Security).

Pernyataan Integritas

Seluruh analisis ancaman, penilaian risiko, dan penetapan kontrol telah diperiksa, disesuaikan dengan kondisi riil produk, dan ditinjau ulang secara mandiri tanpa memuat klaim atau nilai generik dari hasil otomatisasi AI.
