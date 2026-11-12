**Brief Asli Pengguna**  
Episode 7 - Mini proyek: dari data mentah ke satu insight yang bisa dicek (Kulik Data With Gemini). Fokus: Analisis tabel transaksi kantin sintetis langkah demi langkah (cek kualitas data → hitung transaksi per menu → rangkum insight berbasis angka). Analogi: Merapikan buku kas, menghitung penjualan, lalu menyampaikan temuan dengan bukti hitungan. Tidak menyimpulkan sebab-akibat, menggunakan data sintetis fiktif, dan posisi Gemini sebagai alat bantu belajar.

---

### **Draf Produksi**  

#### **1. Tujuan konten dan satu pesan utama**  
*Tujuan*: Menunjukkan cara menganalisis data mentah (transaksi kantin) secara praktis dengan Gemini untuk mendapatkan insight yang bisa dicek.  
*Pesan utama*: **"Dari data mentah ke satu insight yang bisa dicek—tanpa klaim berlebihan, hanya langkah-langkah yang bisa diuji."**

---

#### **2. HOOK pembuka (0-3 detik)**  
- **Teks overlay**: *"Data mentah? Bisa dihitung!"* (font: Bold, ukuran 28pt, warna biru UB)  
- **Ucapan narasi**: *"Ayo lihat bagaimana kita mengubah data kantin menjadi insight yang bisa dibuktikan—tanpa jargon teknis."* (suara nyaman, cepat)  
- **Sound effect**: *Ding-ding* ringan (1 detik) untuk menarik perhatian.

---

#### **3. Rencana pengambilan gambar per adegan**  

| Waktu   | Framing/aksi yang bisa direkam                                                                 | Teks overlay (persis)                                                                 | Ucapan/narasi (persis)                                                                                                                               | Aksi layar/demo (jika ada)                                                                 |
|---------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **0-3s** | Layar hitam dengan teks overlay "Data mentah? Bisa dihitung!" + suara *ding-ding*              | *"Data mentah? Bisa dihitung!"*                                                   | *"Ayo lihat bagaimana kita mengubah data kantin menjadi insight yang bisa dibuktikan—tanpa jargon teknis."*                                              | Tidak ada (hanya teks)                                                                 |
| **3-10s** | Layar menampilkan tabel transaksi kantin sintetis (10 baris) dengan kolom: *tanggal, menu, jumlah, harga* | *"Terdapat 1 baris dengan nilai kosong di kolom 'jumlah' pada tanggal 2023-10-06"* | *"Pertama, kita cek kualitas data. Ada 1 baris yang belum lengkap—ini yang perlu diperbaiki."*                                                         | Tabel dengan baris ke-7 kosong di kolom *jumlah* (contoh data sintetis)                 |
| **10-20s** | Layar menampilkan bar chart sederhana (Nasi Ayam vs Es Teh) dengan angka transaksi             | *"Total transaksi Nasi Ayam: 65 kali | Es Teh: 58 kali"*                            | *"Kedua, kita hitung total transaksi per menu. Nasi Ayam lebih laku dibanding Es Teh."*                                                              | Bar chart dengan angka 65 dan 58 (tanpa interpretasi)                                  |
| **20-30s** | Layar menampilkan teks hasil analisis Gemini (sederhana)                                      | *"Insight: Nasi Ayam terjual 65 kali vs Es Teh 58 kali—bisa dicek dengan data ini."* | *"Ketiga, kita rangkum satu insight yang didukung angka. Ini bisa dicek sendiri!"*                                                                 | Teks hasil analisis Gemini (tanpa klaim sebab-akibat)                                  |
| **30-45s** | Layar berisi CTA + logo Gemini + teks hashtag dan tag                                         | *"Coba analisis data kamu sendiri di Gemini! #GeminiAcademy #GeminiAcademyUB @REFO Indonesia"* | *"Gimana? Coba analisis data kamu sendiri di Gemini—lalu bagikan hasilnya di komentar!"*                                                           | Tidak ada (hanya teks dan logo)                                                       |

---

#### **4. DEMO GEMINI**  
**Prompt lengkap yang siap ditempel**:  
```markdown
Bimbing saya menganalisis tabel transaksi kantin sintetis ini langkah demi langkah: cek kualitas data, hitung total transaksi per menu, lalu rangkum satu temuan yang didukung angka. Tampilkan cara perhitungannya agar bisa saya cek, tanyakan jika format data tidak jelas, dan jangan menyimpulkan sebab-akibat. Data: [tempel data sintetis].

Data sintetis:
| tanggal     | menu      | jumlah | harga |
|-------------|-----------|--------|-------|
| 2023-10-01  | Nasi Ayam | 15     | 5000  |
| 2023-10-01  | Es Teh    | 20     | 2000  |
| 2023-10-02  | Nasi Ayam | 10     | 5000  |
| 2023-10-02  | Es Teh    | 15     | 2000  |
| 2023-10-03  | Nasi Ayam | 8      | 5000  |
| 2023-10-03  | Es Teh    | 5      | 2000  |
| 2023-10-04  | Nasi Ayam | 20     | 5000  |
| 2023-10-04  | Es Teh    | 10     | 2000  |
| 2023-10-05  | Nasi Ayam | 12     | 5000  |
| 2023-10-05  | Es Teh    | 8      | 2000  |
| 2023-10-06  | Nasi Ayam |        | 5000  |
```

**Contoh hasil Gemini (ilustrasi yang perlu diverifikasi)**:  
> *"Terdapat 1 baris dengan nilai kosong di kolom 'jumlah' pada tanggal 2023-10-06. Total transaksi Nasi Ayam: 15+10+8+20+12 = 65. Es Teh: 20+15+5+10+8 = 58. Insight: Nasi Ayam terjual 65 kali vs Es Teh 58 kali—bisa dicek dengan data ini."*  
*(Catatan: Hasil ini hanya ilustrasi. Pengguna harus memverifikasi kembali data dan formatnya sebelum menggunakan di produksi.)*

---

#### **5. Naskah lisan lengkap**  
*(Siap direkam dalam bahasa Indonesia)*  
1. **(0-3s)**: *"Data mentah? Bisa dihitung!"*  
2. **(3-10s)**: *"Pertama, kita cek kualitas data. Ada 1 baris yang belum lengkap—ini yang perlu diperbaiki."*  
3. **(10-20s)**: *"Kedua, kita hitung total transaksi per menu. Nasi Ayam lebih laku dibanding Es Teh."*  
4. **(20-30s)**: *"Ketiga, kita rangkum satu insight yang bisa dicek sendiri."*  
5. **(30-45s)**: *"Gimana? Coba analisis data kamu sendiri di Gemini—lalu bagikan hasilnya di komentar!"*

---

#### **6. Caption siap unggah, CTA, hashtag, dan tag wajib**  
**Caption**:  
*"Dari data mentah ke satu insight yang bisa dicek—tanpa klaim berlebihan, hanya langkah-langkah yang bisa diuji. Coba analisis data kamu sendiri di Gemini dan bagikan hasilnya di komentar! 📊✨  
#GeminiAcademy #GeminiAcademyUB @geminiacademybyrefo @REFO Indonesia"*

**CTA**: *"Coba analisis data kamu sendiri di Gemini—lalu bagikan hasilnya di komentar!"*  

**Hashtag wajib**: `#GeminiAcademy #GeminiAcademyUB` (tidak ada #GeminiAcademyFestival karena konten rutin).  
**Tag wajib**: `@geminiacademybyrefo` dan `@REFO Indonesia`.

---

#### **7. Checklist produksi singkat**  
- ✅ Properti/asset: Data sintetis kantin (10 baris), bar chart sederhana, teks overlay dengan font yang sesuai.  
- ✅ Keterbacaan teks di layar: Teks overlay menggunakan font sans-serif (misal: Arial) dengan ukuran 28pt untuk 9:16.  
- ✅ Safe area vertikal: Teks dan elemen visual berada di area aman (20% dari tepi layar).  
- ✅ Perlindungan data pribadi: Data transaksi kantin menggunakan data sintetis fiktif (tidak ada NIM, nomor HP, atau informasi nyata).  

---

### **Saran Pengembangan (Opsional)**  
1. **Penambahan konteks visual**: Tambahkan gambar kantin UB (misal: kantin fakultas) di adegan 3-10s untuk memperkuat analogi "buku kas" dengan kehidupan nyata mahasiswa.  
2. **Variasi CTA**: Jika konten ini akan dipasang di platform lain (misal: TikTok), tambahkan opsi CTA berupa "Tag 1 teman untuk latihan data bersama!" untuk meningkatkan interaksi.  
3. **Validasi data sintetis**: Pastikan data sintetis yang digunakan dalam prompt Gemini sesuai dengan format yang ditentukan (tanpa kolom tambahan atau data yang tidak konsisten).  

*(Catatan: Saran ini bersifat opsional dan tidak mengubah pesan utama konten.)*
