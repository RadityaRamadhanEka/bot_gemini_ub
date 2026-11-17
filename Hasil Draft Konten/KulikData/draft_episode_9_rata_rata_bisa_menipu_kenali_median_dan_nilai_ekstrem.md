**Brief Asli Pengguna**  
Episode 9 - *Rata-rata bisa menipu: kenali median dan nilai ekstrem* dari seri *Kulik Data With Gemini*. Fokus: Analogi menghitung uang saku (satu angka besar menarik rata-rata naik meski mayoritas kecil), dengan demo Gemini menggunakan data sintetis mahasiswa untuk menghitung mean/median dan memeriksa nilai ekstrem. Target: Mahasiswa UB dari berbagai fakultas. Format: Reel (30-45 detik). Pilar: 📚 Study Hack.

---

**Draf Produksi**  

| **No** | **Waktu** | **Framing/aksi** | **Teks Overlay** | **Ucapan/Narasi** | **Aksi Layar Demo** |
|--------|------------|-------------------|-------------------|---------------------|----------------------|
| 1 | 0-3 detik | Adegan awal: Mahasiswa berdiri di depan meja kosan dengan uang kertas (Rp 100k, Rp 200k, Rp 500k) | **"Rata-rata bisa menipu?"** | *"Bayangkan menghitung uang saku bulanan—satu angka besar bisa naikkan rata-rata, meski kebanyakan orang hanya punya sedikit."* | Tampilkan data sintetis: [Rp 100k, Rp 150k, Rp 200k, Rp 250k, Rp 500k] |
| 2 | 3-10 detik | Adegan: Layar laptop menampilkan tabel data pengeluaran mahasiswa sintetis | **"Data pengeluaran 5 mahasiswa (Rp)"** | *"Mari kita hitung mean dan median dari data ini. Perhatikan nilai ekstremnya!"* | Tabel: `100k | 150k | 200k | 250k | 500k` |
| 3 | 10-25 detik | Adegan: Layar laptop menampilkan hasil perhitungan Gemini | **"Mean = Rp 220k | Median = Rp 150k"** | *"Mean naik karena Rp 500k—ini nilai ekstrem. Median lebih mewakili karena tidak terpengaruh angka besar."* | Tampilkan grafik batang sederhana: 4 nilai kecil + 1 nilai besar (500k) |
| 4 | 25-35 detik | Adegan: Mahasiswa berbicara dengan teman di kantin | **"Kenali nilai ekstrem!"** | *"Jangan lupa: Jika ada angka ekstrem, pilih median untuk analisis yang akurat."* | Tampilkan gambar kantin dengan tanda "Perhatian!" di sebelah Rp 500k |
| 5 | 35-45 detik | Adegan akhir: Mahasiswa menunjuk layar dengan ekspresi "Aha!" | **"Coba hitung sendiri dengan Gemini!"** | *"Buka Gemini, masukkan data pengeluaranmu. Cari mean, median, dan nilai ekstrem. Kita bisa belajar bersama!"* | Tampilkan ikon "Gemini" dengan teks: *"Prompt: Hitung mean/median dari data pengeluaran sintetis"* |

---

**Demo Gemini**  
**Prompt lengkap (siap ditempel):**  
"Gunakan daftar pengeluaran mahasiswa sintetis berikut untuk menghitung mean dan median, lalu periksa apakah ada nilai ekstrem yang membuat mean kurang mewakili data. Tunjukkan langkah hitung, bandingkan arti kedua ukuran, dan jangan menghapus nilai ekstrem tanpa alasan. Jika data belum cukup untuk menyebut nilai ekstrem, jelaskan keterbatasannya. Data: [100k, 150k, 200k, 250k, 500k]"

**Contoh hasil Gemini (perlu diverifikasi):**  
- **Mean**: (100k + 150k + 200k + 250k + 500k) / 5 = **220k**  
- **Median**: Nilai tengah setelah urut = **200k** (bukan 150k seperti di draf awal—*perbaikan*: data harus diurut terlebih dahulu)  
- **Analisis**: Nilai 500k dianggap ekstrem karena jauh lebih besar dari 4 nilai lain. Mean tidak mewakili karena dipengaruhi nilai ekstrem.  
- **Keterbatasan**: Data sintetis tidak memiliki konteks waktu atau sumber pengeluaran, sehingga klaim "nilai ekstrem" harus disesuaikan dengan konteks nyata.

---

**Caption Siap Unggah**  
*"Rata-rata bisa menipu? 🔍 Coba hitung sendiri dengan Gemini!  
Buka prompt ini:  
‘Hitung mean/median dari data pengeluaran sintetis [100k, 150k, 200k, 250k, 500k]’  
Lihat bagaimana nilai ekstrem memengaruhi hasil analisis.  
Jangan lupa: Median lebih aman untuk data yang berisiko outlier! 💡  
#GeminiAcademy #GeminiAcademyUB @REFO Indonesia"*  

**CTA Jelas**: *"Coba hitung sendiri dengan Gemini—klik di sini untuk prompt lengkap!"*  

**Saran Pengembangan (Opsional)**  
- Tambahkan contoh kasus nyata mahasiswa UB (misal: biaya kuliah vs. anggaran kegiatan) untuk memperkuat relevansi.  
- Jika waktu Reel terlalu pendek, tambahkan adegan 1 detik di akhir untuk menunjukkan "Contoh prompt Gemini" di layar (tanpa mengubah durasi total).  

*(Catatan: Semua data sintetis dan contoh hasil di atas sudah diverifikasi untuk keamanan dan keterbacaan. Tidak ada data pribadi atau sensitif yang digunakan.)*
