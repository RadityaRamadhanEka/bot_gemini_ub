# Kulik Data With Gemini

## Konsep Seri

Seri ini mengajak mahasiswa dan audiens umum mengenal dunia data tanpa harus punya latar belakang teknis. Setiap episode mengambil satu konsep seputar data analyst atau data engineer, menjelaskannya dengan analogi sehari-hari, lalu mendemokannya lewat prompt di Gemini Edu.

**Benang merah analogi:** bayangkan data seperti catatan pesanan kantin. *Data analyst* membaca catatan itu untuk menjawab pertanyaan seperti menu terlaris; *data engineer* menyiapkan jalur agar catatan dari kasir bisa dikumpulkan, dirapikan, dan tersedia untuk dianalisis. Analogi ini penyederhanaan untuk pemula, bukan gambaran lengkap seluruh tugas kedua profesi.

## Rencana Episode

| Episode | Bahasan / Hook | Analogi sehari-hari | Inti Prompt Gemini Edu yang Didemokan |
| :---: | :--- | :--- | :--- |
| **1** | **Data analyst vs data engineer: siapa membaca data, siapa menyiapkan jalurnya?** | Di kantin, analyst mencari tahu menu terlaris; engineer memastikan catatan pesanan dari kasir terkumpul dan rapi. | *"Jelaskan perbedaan data analyst dan data engineer untuk pemula dengan analogi kantin kampus. Berikan contoh pekerjaan harian masing-masing, hasil kerja yang biasanya dibuat, dan satu hal yang sering disalahpahami. Gunakan bahasa sehari-hari dan jelaskan bahwa analoginya hanya penyederhanaan."* |
| **2** | **Dari catatan transaksi ke pertanyaan yang berguna** | Sebelum menghitung, pemilik kantin menentukan dulu pertanyaan yang ingin dijawab—misalnya menu apa yang paling laku. | *"Saya punya data transaksi kantin fiktif dengan kolom tanggal, menu, jumlah, dan harga. Sarankan 5 pertanyaan bisnis sederhana yang bisa dijawab dari kolom tersebut. Untuk tiap pertanyaan, sebutkan kolom yang diperlukan dan jangan menyimpulkan hal yang tidak tersedia di data. Jangan mengarang hasil."* |
| **3** | **Data berantakan itu seperti daftar belanja dengan tulisan berbeda-beda** | Nama menu yang sama bisa tercatat dengan ejaan berbeda; ada juga catatan kosong atau transaksi ganda. | *"Periksa tabel transaksi fiktif berikut untuk menemukan nilai kosong, kemungkinan duplikat, dan nama menu yang penulisannya tidak konsisten. Tampilkan temuan dan usulan perbaikannya dalam tabel. Jangan mengubah data diam-diam; tandai baris yang perlu keputusan manusia. Data: [tempel data sintetis]."* |
| **4** | **SQL itu seperti meminta petugas mencari pesanan tertentu di buku kas** | Kita menyebutkan kriteria pencarian—misalnya transaksi untuk satu menu—lalu petugas menyaring catatannya. | *"Ajari saya query SQL dasar untuk menampilkan transaksi menu 'Nasi Ayam' dari tabel transaksi. Jelaskan setiap baris query dengan bahasa sehari-hari, gunakan hanya SELECT, FROM, dan WHERE, lalu berikan satu latihan serupa tanpa langsung memberi jawabannya."* |
| **5** | **Grafik bukan hiasan: pilih visual yang menjawab pertanyaan** | Seperti memilih papan menu yang memudahkan pemilik kantin melihat perubahan penjualan, bukan sekadar membuatnya ramai. | *"Dari tujuan analisis [tujuan] dan kolom yang tersedia [daftar kolom], sarankan jenis grafik yang paling mudah dipahami dan alasannya. Sebutkan sumbu yang digunakan serta satu cara agar grafik tidak menyesatkan. Jangan membuat angka atau tren yang tidak ada di data."* |
| **6** | **Data engineer dan “jalur antar” dari kasir ke laporan** | Pesanan melewati jalur: dicatat kasir, dikumpulkan, diperiksa, lalu disimpan agar bisa dipakai membuat laporan. | *"Buat diagram alur sederhana untuk data transaksi kantin fiktif dari sumber kasir sampai siap dipakai membuat laporan. Tunjukkan tahap pengumpulan, pemeriksaan/rapi-rapi, penyimpanan, dan penggunaan. Jelaskan fungsi tiap tahap dengan bahasa nonteknis; jangan masuk ke konfigurasi cloud atau kode."* |
| **7** | **Mini proyek: dari data mentah ke satu insight yang bisa dicek** | Seperti merapikan buku kas, menghitung penjualan, lalu menyampaikan satu temuan beserta bukti hitungannya. | *"Bimbing saya menganalisis tabel transaksi kantin sintetis ini langkah demi langkah: cek kualitas data, hitung total transaksi per menu, lalu rangkum satu temuan yang didukung angka. Tampilkan cara perhitungannya agar bisa saya cek, tanyakan jika format data tidak jelas, dan jangan menyimpulkan sebab-akibat. Data: [tempel data sintetis]."* |

## Catatan Produksi

- Gunakan data buatan untuk demo (misalnya transaksi kantin dengan nama menu dan angka fiktif), bukan data mahasiswa atau transaksi asli.
- Tampilkan proses memeriksa output Gemini, bukan hanya jawaban akhirnya.
- Perlakukan Gemini sebagai teman belajar, bukan pengganti pengecekan hasil atau sumber kebenaran.
- Jika fitur atau tampilan Gemini Edu berbeda di akun/perangkat, sesuaikan demo dengan prompt teks yang tetap bisa dicoba.
