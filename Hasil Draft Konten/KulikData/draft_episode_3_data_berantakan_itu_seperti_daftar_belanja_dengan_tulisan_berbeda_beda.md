**Brief Asli Pengguna**  
Judul: Episode 3 - Data berantakan itu seperti daftar belanja dengan tulisan berbeda-beda  
Format: Reel (30-45 detik)  
Pilar: 📚 Study Hack  
Inti ide: Menunjukkan analogi data berantakan (tulisan tidak konsisten, nilai kosong, duplikat) sebagai daftar belanja kampus, dengan Gemini membantu memperjelas data tanpa mengubah data asli. Fokus pada edukasi praktis untuk mahasiswa UB.  

---

**Draf Produksi**  

**1. Tujuan konten dan pesan utama**  
*Tujuan*: Mengajak mahasiswa UB memahami cara mendeteksi dan mengatasi ketidakkonsistenan data melalui analogi sehari-hari.  
*Pesan utama*: "Data yang berantakan? Gemini bantu cek kekacauannya—tanpa mengubah data asli, hanya mengidentifikasi yang perlu keputusan manusia."  

**2. HOOK pembuka (0-3 detik)**  
- **Teks overlay**: *"Data yang berantakan? Ini cara mengatasinya!"*  
- **Ucapan**: "Kamu pernah lihat daftar belanja yang sama namun tulisannya berbeda-beda? Ini cara Gemini bantu kita cek data kuliah!"  

**3. Rencana pengambilan gambar per adegan**  

| Waktu   | Framing/aksi yang bisa direkam                     | Teks overlay (persis)                                                                 | Ucapan/narasi (persis)                                                                 | Aksi layar/demo (opsional)                                                                 |
|---------|---------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| 0-3s    | Screenshot daftar belanja kampus yang kacau         | *"Data yang berantakan?"*                                                          | "Kamu pernah lihat daftar belanja yang sama namun tulisannya berbeda-beda?"            | Tampilan daftar belanja dengan "Nasi Ayam", "Nasi Ayam Kuning", dan "Nasi Ayam" (tanpa konsistensi) |
| 3-10s   | Menunjukkan kolom "Harga" kosong di tabel transaksi | *"Harga kosong?"*                                                                  | "Ada yang lupa isi harga? Gemini bantu cek!"                                          | Tabel transaksi sintetis dengan kolom "Harga" kosong untuk 1 transaksi                   |
| 10-20s  | Menampilkan hasil analisis Gemini (tabel dengan tanda ✅/⚠️) | *"Ini temuan Gemini: 3 masalah!"*                                                 | "Gemini menemukan 3 hal yang perlu diperhatikan: 1) Nama menu tidak konsisten, 2) Harga kosong, 3) Duplikat transaksi." | Tabel dengan tanda: ✅ (perlu keputusan manusia), ⚠️ (usulan perbaikan)                 |
| 20-30s  | Menunjukkan contoh perbaikan (tanpa mengubah data)  | *"Solusi: Tandai yang perlu manusia!"*                                             | "Gemini hanya mengidentifikasi—bukan mengubah data. Kita yang tentukan perbaikan."      | Tabel dengan kolom "Menu" sudah diubah menjadi "Nasi Ayam" (konsisten)                 |
| 30-45s  | Screenshot akhir dengan CTA dan hashtag             | *"Coba prompt Gemini ini untuk data kamu!"*                                         | "Coba prompt ini di Gemini: 'Periksa tabel transaksi fiktif berikut untuk menemukan nilai kosong, duplikat, dan nama menu tidak konsisten. Tampilkan temuan dan usulan perbaikan.' Lihat hasilnya!" | Tampilan teks prompt Gemini dengan data sintetis (tanpa nama pribadi)                  |

**4. DEMO GEMINI**  
- **Apa yang direkam di layar**: Tabel transaksi sintetis dengan ketidakkonsistenan (lihat *Rencana pengambilan gambar*).  
- **Prompt lengkap yang siap ditempel**:  
  *"Periksa tabel transaksi fiktif berikut untuk menemukan nilai kosong, kemungkinan duplikat, dan nama menu yang penulisannya tidak konsisten. Tampilkan temuan dan usulan perbaikannya dalam tabel. Jangan mengubah data diam-diam; tandai baris yang perlu keputusan manusia. Data: [tempel data sintetis]."*  
- **Contoh hasil yang relevan (perlu diverifikasi)**:  
  ```markdown
  | Tanggal     | Menu          | Jumlah | Harga  |
  |-------------|----------------|--------|--------|
  | 2023-10-01  | Nasi Ayam      | 2      |        |
  | 2:2023-10-02| Nasi Ayam Kuning| 1      | 10000  |
  | 2023-10-03  | Nasi Ayam      | 3      | 15000  |
  | 2023-10-04  | Nasi Ayam      | 1      |        |
  
  **Temuan**:  
  1. ⚠️ *Harga kosong* pada transaksi 2023-10-01 dan 2023-10-04.  
  2. ⚠️ *Nama menu tidak konsisten*: "Nasi Ayam" vs "Nasi Ayam Kuning".  
  3. ⚠️ *Duplikat transaksi*: "Nasi Ayam" muncul 3x.  
  **Usulan**:  
  - Isi harga untuk transaksi 2023-10-01 (misal: 10000).  
  - Standardisasi nama menu menjadi "Nasi Ayam" (konsisten).  
  - Periksa apakah transaksi duplikat perlu dihapus atau dihitung ulang.  
  ```  
  *Catatan*: Hasil ini **perlu diverifikasi** di Gemini sebelum syuting—bukan hasil akhir final.  

**5. Naskah lisan lengkap**  
*(Untuk direkam dengan narasi berbahasa Indonesia)*  
*"Kamu pernah lihat daftar belanja yang sama namun tulisannya berbeda-beda? Ini cara Gemini bantu kita cek data kuliah! Gemini menemukan 3 hal yang perlu diperhatikan: 1) Harga kosong, 2) Nama menu tidak konsisten, 3) Duplikat transaksi. Tapi ingat—Gemini hanya mengidentifikasi, bukan mengubah data. Kita yang tentukan perbaikan. Coba prompt ini di Gemini: 'Periksa tabel transaksi fiktif berikut untuk menemukan nilai kosong, duplikat, dan nama menu tidak konsisten...' Lihat hasilnya!"*  

**6. Caption siap unggah, CTA, hashtag, dan tag wajib**  
```markdown
Data yang berantakan? Gemini bantu cek kekacauannya—tanpa mengubah data asli, hanya mengidentifikasi yang perlu keputusan manusia. 📊  

Coba prompt ini di Gemini:  
"Periksa tabel transaksi fiktif berikut untuk menemukan nilai kosong, kemungkinan duplikat, dan nama menu yang penulisannya tidak konsisten. Tampilkan temuan dan usulan perbaikannya dalam tabel. Jangan mengubah data diam-diam; tandai baris yang perlu keputusan manusia."  

#GeminiAcademy #GeminiAcademyUB @geminiacademybyrefo @REFO Indonesia
*(CTA)* Coba prompt ini untuk data kuliahmu! Kita bisa jadi lebih akurat bersama. 💡  
```  

**7. Checklist produksi singkat**  
- [x] Properti/asset: Tabel transaksi sintetis (tanpa data pribadi), screenshot daftar belanja kampus.  
- [x] Keterbacaan teks di layar: Teks overlay menggunakan font besar (18-24pt), kontras tinggi.  
- [x] Safe area vertikal: Teks tidak melewati 10% dari tepi layar.  
- [x] Perlindungan data pribadi: Data sintetis (tanpa NIM, no HP, atau transaksi nyata).  

---

**Saran Pengembangan (Opsional)**  
- **Tambahkan contoh perbaikan langsung** di adegan 20-30s: Tampilkan 1 contoh perbaikan menu (misal: "Nasi Ayam Kuning" → "Nasi Ayam") untuk memperjelas konsep tanpa mengubah data asli.  
- **Optimalkan CTA**: Tambahkan tautan ke panduan Gemini untuk analisis data (misal: "Coba di sini" → [link panduan sintetis]) agar lebih jelas.  
*Catatan*: Saran ini hanya untuk memperkaya konten, tidak mengubah inti ide atau pesan utama.
