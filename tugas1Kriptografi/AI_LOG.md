# Catatan Pemanfaatan AI (AI_LOG.md)

A. Aktivitas: Tugas 1 — Fondasi dan Komponen Dasar Kriptografi
- **Alat AI yang Digunakan:** Gemini / ChatGPT
- **Tujuan Pemanfaatan:** Membantu pembuatan struktur fungsi hashing aman, templat pengujian pytest, serta merancang skenario uji batas/negatif.

B. Ringkasan Perintah (Prompts)
1. *"Buatkan pustaka helper Python untuk hashing password PBKDF2-HMAC-SHA256 dan enkripsi Fernet."*
2. *"Buatkan 4 unit test pytest untuk fungsi crypto meliputi test positif dan test negatif untuk password kosong dan token pendek."*

C. Bagian Kode yang Dihasilkan / Diubah
- Mengadopsi fungsi `hash_password` dan `verify_password` menggunakan `secrets.compare_digest`.
- Mengimplementasikan penanganan error (*exception*) pada fungsi token jika panjang byte kurang dari 16.

D. Verifikasi & Validasi Kode
- Dipastikan tidak ada kunci privat, secret, password, atau data pribadi nyata di dalam repositori (seluruh kunci dan data uji menggunakan nilai sintetis/generated).
- Pengujian dijalankan secara lokal menggunakan perintah `pytest -v` dan seluruh 5 skenario uji lulus 100%.