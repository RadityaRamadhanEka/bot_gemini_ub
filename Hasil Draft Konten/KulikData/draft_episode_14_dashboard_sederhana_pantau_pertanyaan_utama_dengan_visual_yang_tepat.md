**Brief Asli Pengguna**  
Episode 14 - Dashboard sederhana: pantau pertanyaan utama dengan visual yang tepat. Analogi kantin: papan ringkasan yang menampilkan angka penting agar pengelola cepat melihat kondisi, bukan semua catatan transaksi. Fokus pada dashboard sederhana dengan maksimal 3 metrik, visual yang mudah dipahami, dan batas interpretasi. Gunakan data sintetis untuk demo.

---

**Draf Produksi**

### 1. Tujuan Konten & Pesan Utama
Membantu mahasiswa UB menyusun dashboard sederhana yang menjawab satu pertanyaan: menu apa yang paling banyak terjual? Tampilkan maksimal tiga metrik yang dapat dihitung dari data, pilih visual yang sesuai, dan jangan menarik kesimpulan di luar cakupan data.

### 2. Hook Pembuka (0-3 detik)
- **Teks overlay**: *"Menu apa yang paling laris? Lihat datanya."*
- **Visual**: Raka mengangkat papan ringkasan dengan grafik batang kecil dan tiga kartu angka.
- **VO**: *"Bukan semua catatan yang perlu dilihat."*

### 3. Ringkasan Alur Cerita
- **Tokoh utama**: Raka, mahasiswa UB.
- **Lokasi/latar utama**: Kantin kampus UB.
- **Situasi cerita**: Raka memakai Gemini untuk merangkum data transaksi sintetis menjadi dashboard yang menjawab pertanyaan tentang menu terlaris. Ia menunjukkan metrik, visual, dan batas kesimpulannya.

### 4. Storyboard Terperinci

| Waktu | Lokasi/latar | Aksi dan ekspresi tokoh | Framing/kamera | Transisi | Teks overlay | Ucapan/VO | Aksi visual/demo |
|-------|---------------|-------------------------|-----------------|-----------|----------------|-------------|-------------------|
| 0-3s | Kantin UB | Raka menunjuk papan ringkasan | Close-up papan, lalu Raka | Fade in | *"Menu apa yang paling laris?"* | *"Bukan semua catatan yang perlu dilihat."* | Tiga kartu metrik muncul |
| 3-10s | Kantin UB | Raka memasukkan data sintetis dan prompt ke Gemini | Medium shot, cut ke laptop | Cut | *"Tujuan: cari menu terlaris"* | *"Saya minta Gemini menjawab satu pertanyaan dari data."* | Tampilkan prompt dan cuplikan data |
| 10-25s | Kantin UB | Raka menunjukkan hasil dashboard | Medium shot, lalu layar dashboard | Cut ke dashboard | *"10 transaksi"*<br>*"Nasi Ayam: 7 porsi"*<br>*"Rata-rata nilai transaksi: Rp 17.900"* | *"Dari sepuluh transaksi, Nasi Ayam paling banyak terjual: tujuh porsi. Rata-rata nilai per transaksi tujuh belas ribu sembilan ratus rupiah."* | Tiga kartu metrik dan grafik batang jumlah porsi per menu |
| 25-35s | Kantin UB | Raka menunjuk grafik lalu memberi catatan batas data | Close-up grafik | Cut | *"Jumlah terjual ≠ penyebab penjualan"* | *"Grafik menunjukkan jumlah porsi dalam data ini saja. Data ini tidak menjelaskan penyebab penjualan atau mewakili semua hari."* | Sorot label sumbu dan tampilkan catatan batas interpretasi |
| 35-40s | Kantin UB | Raka menutup dengan senyum | Wide shot | Fade out | *"Pilih pertanyaan, metrik, dan visual yang tepat."* | *"Coba buat dashboard dari data sintetismu di Gemini."* | Tampilkan CTA dan papan ringkasan |

### 5. Demo Gemini
- **Yang direkam di layar**: Prompt, data sintetis, lalu hasil berupa tiga kartu metrik dan grafik batang jumlah porsi per menu.
- **Prompt lengkap**:

  ```text
  Buat rancangan dashboard sederhana untuk menjawab pertanyaan: menu mana yang paling banyak terjual?

  Setiap baris adalah satu transaksi. Kolom jumlah menunjukkan banyaknya porsi dalam transaksi itu; harga adalah harga per porsi dalam rupiah.

  Hitung maksimal tiga metrik dari data berikut:
  1. Jumlah transaksi (jumlah baris).
  2. Menu terlaris berdasarkan total porsi, bukan jumlah baris; tampilkan jumlah porsinya.
  3. Rata-rata nilai transaksi, yaitu total (jumlah x harga) dibagi jumlah transaksi.

  Sarankan visual yang mudah dibaca. Jangan menambah angka atau membuat perbandingan/tren yang tidak didukung data. Jelaskan satu batas interpretasi.

  | Tanggal | Menu | Jumlah (porsi) | Harga per porsi (Rp) |
  |---|---|---:|---:|
  | 2026-10-01 | Nasi Ayam | 2 | 15000 |
  | 2026-10-01 | Soto | 1 | 12000 |
  | 2026-10-01 | Nasi Ayam | 1 | 15000 |
  | 2026-10-01 | Mie Ayam | 1 | 13000 |
  | 2026-10-01 | Nasi Ayam | 2 | 15000 |
  | 2026-10-02 | Nasi Ayam | 1 | 15000 |
  | 2026-10-02 | Soto | 2 | 12000 |
  | 2026-10-02 | Mie Ayam | 1 | 13000 |
  | 2026-10-02 | Nasi Ayam | 1 | 15000 |
  | 2026-10-02 | Soto | 1 | 12000 |
  ```

- **Hasil acuan untuk verifikasi saat demo**:
  - Jumlah transaksi: **10**.
  - Total porsi: Nasi Ayam **7**, Soto **4**, Mie Ayam **2**; menu terlaris: **Nasi Ayam (7 porsi)**.
  - Total nilai transaksi: **Rp 179.000**; rata-rata nilai transaksi: **Rp 17.900**.
  - Visual: grafik batang jumlah porsi per menu; hindari grafik tren karena data hanya mencakup dua tanggal dan tujuan utamanya membandingkan menu.
  - Batas interpretasi: data sintetis dua hari ini tidak menjelaskan penyebab penjualan dan tidak mewakili pola penjualan kantin secara umum.

### 6. Naskah Lisan & Arah Karakter VO
- **Naskah**: *"Bukan semua catatan yang perlu dilihat. Saya minta Gemini menjawab satu pertanyaan dari data. Dari sepuluh transaksi, Nasi Ayam paling banyak terjual: tujuh porsi. Rata-rata nilai per transaksi tujuh belas ribu sembilan ratus rupiah. Grafik ini hanya merangkum data contoh, bukan menjelaskan penyebab penjualan atau mewakili semua hari. Coba buat dashboard dari data sintetismu di Gemini."*
- **Arah karakter VO**:
  - Suara laki-laki, mewakili Raka.
  - Semi-formal, jelas, edukatif, tanpa jargon teknis.
  - Kecepatan sekitar 120-140 kata/menit; sisakan jeda untuk membaca angka dan grafik.

### 7. Catatan Produksi
- **Rasio**: 9:16.
- **Resolusi**: 1080x1920.
- **Frame rate**: 30 fps.
- **Durasi total**: 40 detik.
- **Safe area**: Tempatkan teks penting dalam area aman; cek keterbacaan pada pratinjau layar ponsel.
- **Aset**: Data sintetis di atas, mockup dashboard/grafik batang, papan ringkasan, dan logo Gemini Academy sesuai panduan merek yang berlaku.

### 8. Caption Siap Unggah
```text
📊 Dashboard yang baik dimulai dari satu pertanyaan.

Contoh ini mencari menu dengan jumlah porsi terjual terbanyak dari data sintetis. Dari 10 transaksi contoh, Nasi Ayam paling laris (7 porsi) dengan rata-rata nilai transaksi Rp 17.900—dan grafik hanya merangkum data yang tersedia, bukan penyebab penjualan atau gambaran semua hari.

👉 Coba buat dashboard dari data sintetismu di Gemini.

Mau belajar mandiri lebih lanjut? Pakai modul ini sebagai acuan dan scan QR Belajar Mandiri bareng Gemini di akhir video untuk membuka modul & panduan lainnya! Follow @geminiacademybyrefo atau buka https://bit.ly/belajarmandirigemini.

@geminiacademybyrefo @REFO Indonesia

#KulikData #LiterasiData #DashboardSederhana #GeminiAcademy #GeminiAcademyUB #MahasiswaUB
```

### 9. Checklist Produksi
- [ ] Angka pada dashboard sudah dicocokkan dengan data dan hasil acuan.
- [ ] Menu terlaris dihitung dari total porsi, bukan jumlah baris transaksi.
- [ ] Maksimal tiga metrik dan grafik batang memiliki label yang jelas.
- [ ] Batas interpretasi terlihat dan terdengar.
- [ ] Logo dan safe area mengikuti panduan merek/platform.
- [ ] Demo hanya menggunakan data sintetis, tanpa data pribadi.
