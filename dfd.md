# Data Flow Diagram (DFD) - Produk Bank Sampah

1. Diagram Arsitektur Mermaid

graph TB
    %% External Entities
    subgraph EE["Entitas Eksternal"]
        E1["Nasabah (Browser / Mobile)"]
        E2["Admin / Operator (Browser)"]
        E3["Layanan Email SMTP Pihak Ke-3"]
    end

    %% Trust Boundary 1: Internet vs VM Server (Docker Host)
    subgraph TB1["Trust Boundary 1: Internet / Public Boundary"]
        direction TB

        %% Process P1
        subgraph AppHost["VM Server (Docker Host)"]
            P1["P1: Aplikasi Web (Next.js Node.js Container)"]
            
            %% Trust Boundary 2: Internal Container Network
            subgraph TB2["Trust Boundary 2: Internal Container Network"]
                DS1[("DS1: PostgreSQL Database Container\n Data At-Rest Encrypted")]
                P2["P2: Skrip Backup Otomatis (Cron Job)"]
            end

            %% Trust Boundary 3: Secure Backup Storage
            subgraph TB3["Trust Boundary 3: Storage Isolated Boundary"]
                DS2[("DS2: Encrypted Backup Storage\n File Backup Encrypted")]
            end
        end
    end

    %% Data Flows dengan ID dan Label Data
    E1 -- "F1: Kredensial, Data Setoran, Profile Request [TLS 1.3]" --> P1
    E2 -- "F2: Kredensial Admin, Verifikasi Setoran, Config [TLS 1.3]" --> P1
    P1 -- "F3: Query SQL (Read/Write Data, User, Transaksi)" --> DS1
    P1 -- "F4: Kirim Notifikasi Email / Token Reset" --> E3
    P2 -- "F5: Dump Query / Export DB" --> DS1
    P2 -- "F6: Berkas Enkripsi Backup (.sql.gz.enc)" --> DS2

    %% Styling
    classDef boundary fill:none,stroke:#e74c3c,stroke-width:2px,stroke-dasharray: 5 5;
    classDef process fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#fff;
    classDef datastore fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff;
    classDef entity fill:#f39c12,stroke:#d35400,stroke-width:2px,color:#fff;

    class P1,P2 process;
    class DS1,DS2 datastore;
    class E1,E2,E3 entity;
    class TB1,TB2,TB3 boundary;

2. Penjelasan Elemen dan Trust Boundaries (TB)

- P1 (Aplikasi Next.js): Menerima input dari pengguna luar, memproses autentikasi, dan menjalankan bisnis logika.

- DS1 (PostgreSQL Container): Menyimpan kredensial (AST-01), PII (AST-02), dan transaksi (AST-03). Aset data sensitif dilindungi enkripsi.

- P2 (Skrip Backup): Eksekutor cron job internal untuk membuat cadangan basis data secara berkala.

- DS2 (Backup Storage): Penyimpanan terisolasi khusus untuk berkas cadangan terenkripsi.

- TB1 (Public Boundary): Memisahkan entitas eksternal yang tidak terpercaya di internet dari server aplikasi internal. Memerlukan proteksi TLS/HTTPS dan Web Application Firewall.

- TB2 (Internal Container Network): Memisahkan proses aplikasi publik dengan basis data internal. Hanya container aplikasi yang boleh berkomunikasi ke port 5432 basis data.

- TB3 (Storage Isolation Boundary): Memisahkan lingkungan eksekusi aplikasi dengan penyimpanan cadangan jangka panjang untuk mencegah penghapusan cadangan jika aplikasi diretas.