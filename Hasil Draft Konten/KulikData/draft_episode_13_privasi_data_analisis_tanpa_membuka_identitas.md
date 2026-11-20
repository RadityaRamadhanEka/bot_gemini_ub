
# Episode 13 — Analisis Tanpa Membuka Identitas

**Seri:** Kulik Data With Gemini  
**Format:** Video vertikal pendek untuk Reels/Shorts  
**Durasi target:** 35 detik  
**Tokoh:** Raka, mahasiswa laki-laki yang sedang memeriksa contoh data di kantin  
**VO:** Suara laki-laki muda/dewasa, natural dan ramah; gunakan satu karakter suara yang konsisten sepanjang video.  
**Pesan utama:** Menghapus nama dan NIM mengurangi risiko, tetapi privasi belum tentu terjaga jika kombinasi kolom lain masih dapat mempersempit identitas. Gunakan data sintetis, minimalkan atribut, hindari kelompok kecil, dan cek hasil Gemini.

## Audit dan perbaikan inti

- Menghapus Nama dan NIM tidak otomatis membuat data aman. Gabungan Kuliah, angkatan, lokasi, atau kebutuhan dapat menjadi pengenal tidak langsung.
- Contoh 120 mahasiswa diganti dengan hasil yang benar-benar dapat dihitung dari dataset sintetis.
- Klaim “privasi yang aman” diubah menjadi “lebih hati-hati” karena hasil agregat tetap dapat berisiko.
- Angka agregat harus menyertakan jumlah kelompok yang cukup besar atau menyembunyikan kombinasi yang terlalu spesifik.
- Gemini diposisikan sebagai alat bantu, bukan penentu otomatis bahwa data sudah aman.

## Dataset sintetis untuk visual

Setiap baris adalah satu orang fiktif. Dataset ini hanya contoh untuk video, bukan data mahasiswa sungguhan.

| Baris | Kuliah | Kebutuhan |
|---|---|---|
| 1 | Teknik Informatika | Makanan ringan |
| 2 | Teknik Informatika | Minuman dingin |
| 3 | Teknik Informatika | Makanan berat |
| 4 | Teknik Informatika | Makanan ringan |
| 5 | Teknik Informatika | Minuman dingin |
| 6 | Ekonomi | Makanan berat |
| 7 | Ekonomi | Makanan ringan |
| 8 | Ekonomi | Minuman dingin |
| 9 | Hukum | Makanan berat |
| 10 | Hukum | Minuman dingin |

**Ringkasan agregat sintetis:**

- Teknik Informatika: 5 orang
- Ekonomi: 3 orang
- Hukum: 2 orang
- Makanan ringan: 3 orang
- Makanan berat: 3 orang
- Minuman dingin: 4 orang

Angka-angka ini hanya untuk sepuluh baris latihan. Jangan gunakan sebagai gambaran jumlah mahasiswa UB yang sesungguhnya.

## Storyboard siap produksi

| Waktu | Adegan dan aksi tokoh | Narasi/dialog Raka | Teks overlay | Arahan visual/Remotion |
|---|---|---|---|---|
| 0–3 dtk | Raka melihat tabel contoh di tablet dan menunjuk kolom Nama serta NIM. | “Nama dan NIM itu pengenal langsung. Tapi apakah menghapusnya sudah cukup?” | **Menghapus identitas — sudah aman?** | Close-up tablet. Beri label “DATA SINTETIS”. Nama dan NIM hanya muncul sebentar sebagai kolom awal, bukan data nyata. |
| 3–10 dtk | Raka menggeser kedua kolom sampai hilang dari tabel. | “Nama dan NIM bisa dihapus agar identitas langsung tidak terlihat.” | **Hapus Nama + NIM** | Animasi sederhana menghapus dua kolom. Sisakan Kuliah dan Kebutuhan. Jangan menampilkan nama atau NIM nyata. |
| 10–18 dtk | Raka menunjuk kombinasi Kuliah dan Kebutuhan; satu baris disorot dengan tanda hati-hati. | “Kuliah dan kebutuhan tetap dapat menjadi gabungan yang unik. Artinya, risiko identifikasi bisa tetap ada.” | **Gabungan kolom bisa mengidentifikasi** | Tunjukkan Hukum + Makanan Berat sebagai contoh konsep, lalu beri catatan “potensi risiko”, bukan klaim bahwa identitas tertentu pasti terbongkar. |
| 18–26 dtk | Raka membatalkan daftar baris dan menggantinya dengan kartu ringkasan jumlah. | “Kalau pertanyaannya hanya jumlah per jurusan, cukup tampilkan ringkasan: Teknik Informatika lima, Ekonomi tiga, Hukum dua.” | **Lihat angka, bukan individu** | Tiga kartu jumlah. Gunakan angka dari dataset 10 baris. Beri tanda bahwa kelompok yang terlalu kecil perlu disembunyikan atau dikelompokkan lagi. |
| 26–35 dtk | Raka mengetik prompt singkat di antarmuka generik, lalu kartu CTA Belajar Mandiri bareng Gemini ditampilkan. | “Gemini dapat membantu meninjau risiko dan menyusun ringkasan. Namun keputusan privasi tetap perlu kamu periksa. Pakai modul ini sebagai acuan belajar mandiri dan pindai QR di layar untuk lanjut belajar.” | **Pakai modul ini sebagai acuan · Scan QR-nya** | Tampilkan prompt singkat, tabel agregat, lalu kartu CTA besar dengan QR resmi Belajar Mandiri bareng Gemini, handle `@geminiacademybyrefo`, dan tautan `https://bit.ly/belajarmandirigemini`. QR ditempatkan paling menonjol dan sisakan durasi cukup untuk di-scan. |

## Naskah lisan siap direkam

> “Nama dan NIM itu pengenal langsung. Tapi apakah menghapusnya sudah cukup? Nama dan NIM bisa dihapus agar identitas langsung tidak terlihat. Namun, kuliah dan kebutuhan bisa menjadi gabungan yang unik. Jadi risiko identifikasi masih bisa ada. Kalau pertanyaannya hanya jumlah per jurusan, gunakan ringkasan: Teknik Informatika lima, Ekonomi tiga, dan Hukum dua. Gemini dapat membantu meninjau risiko dan menyusun ringkasan, tetapi keputusan privasi tetap perlu kamu periksa. Pakai modul ini sebagai acuan belajar mandiri. Untuk modul dan panduan Gemini lainnya, ikuti Instagram Gemini Academy, buka tautan di layar, atau pindai QR Belajar Mandiri di ujung video ini.”

**Arahan VO:**

- **Gender:** Laki-laki, Raka.
- **Tone:** Edukatif, tenang, hati-hati; jangan terdengar menggurui.
- **Tempo:** Jeda singkat setelah “menghapusnya sudah cukup?” dan setelah “risiko identifikasi masih bisa ada”.
- Tekankan frasa **“gabungan kolom”**, **“kelompok kecil”**, dan **“tetap perlu diperiksa”**.

## Prompt demo Gemini

Tempelkan data sintetis di atas setelah prompt ini:

```text
Tinjau tabel data sintetis berikut untuk menjawab pertanyaan:
"Berapa jumlah mahasiswa pada setiap kategori Kuliah?"

Data sintetis berisi kolom Kuliah dan Kebutuhan. Nama, NIM, dan
kolom pengenal langsung tidak tersedia.

1. Identifikasi pengenal langsung atau pengenal tidak langsung yang masih berpotensi muncul.
2. Jelaskan risiko gabungan kolom Kuliah dan Kebutuhan.
3. Jelaskan bahwa hasil agregat dapat tetap berisiko jika jumlah kelompok terlalu kecil.
4. Sarankan cara mengurangi risiko, termasuk minimasi kolom, pengelompokan kategori, dan penyembunyian atau penggabungan kelompok kecil.
5. Hitung ringkasan setiap kategori Kuliah hanya dari baris yang diberikan.
6. Pisahkan fakta dari saran dan jelaskan batasan analisis.
7. Jangan mengarang angka atau menyatakan bahwa data sudah aman hanya karena nama dan NIM dihapus.

Gunakan hanya data sintetis. Jangan minta, menebak, atau mengolah data mahasiswa nyata.
```

**Contoh hasil yang diharapkan (tetap periksa terhadap data):**

| Kolom | Hasil atau status | Penjelasan |
|---|---|---|
| Nama | Tidak tersedia | Pengenal langsung tidak disertakan |
| NIM | Tidak tersedia | Pengenal langsung tidak disertakan |
| Kuliah | Pertahankan jika relevan | Diperlukan untuk pertanyaan jumlah per jurusan |
| Kebutuhan | Minimalkan atau hapus | Tidak diperlukan untuk pertanyaan tersebut dan dapat mempersempit identitas |
| Teknik Informatika | 5 baris | Data sintetis |
| Ekonomi | 3 baris | Data sintetis |
| Hukum | 2 baris | Kelompok kecil; perlu dipertimbangkan kembali sebelum dipublikasikan |

## Catatan produksi

- Rasio: 9:16, resolusi 1080×1920, frame rate 30 fps, durasi 35 detik.
- Gunakan font yang konsisten dengan kampanye, misalnya Montserrat, dengan ukuran teks yang terbaca di layar ponsel.
- Letakkan teks dan elemen penting di area aman; hindari area kontrol aplikasi dan tepi layar.
- Tampilkan logo Gemini Academy melalui aset resmi yang sama seperti konten sebelumnya. Jangan menggambar ulang logonya.
- Semua nama, NIM, dan identitas dalam draft adalah ilustrasi atau tidak boleh ditampilkan sama sekali. Pastikan visual hanya memakai data sintetis.
- Gabungkan atau sembunyikan kelompok kecil pada hasil publik. Untuk contoh Hukum yang berjumlah dua baris, jelaskan bahwa angka tersebut terlalu kecil untuk ditampilkan dalam konteks identifikasi.

## Caption siap unggah

```text
Menghapus nama dan NIM belum tentu membuat data benar-benar aman.

Misalnya, kombinasi jurusan dan kebutuhan tertentu bisa mempersempit identitas seseorang. Karena itu, analisis perlu dilakukan dengan hati-hati:

• Hapus identitas langsung
• Minimalkan kolom yang tidak diperlukan
• Hindari kombinasi atribut yang terlalu spesifik
• Jangan menampilkan kelompok yang terlalu kecil
• Gunakan data sintetis untuk belajar

Dalam contoh ini, hanya ada sepuluh baris data fiktif:
• Teknik Informatika: 5 orang
• Ekonomi: 3 orang
• Hukum: 2 orang

Gemini bisa membantu meninjau risiko dan menyusun ringkasan. Namun, hasil dan keputusan privasi tetap perlu kamu cek.

Coba prompt di video. Dari hasilnya, atribut atau kombinasi apa yang masih berpotensi mengidentifikasi seseorang?

Mau belajar mandiri lebih lanjut? Pakai modul ini sebagai acuan dan scan QR Belajar Mandiri bareng Gemini di akhir video untuk membuka modul & panduan lainnya. Bisa juga follow @geminiacademybyrefo atau buka https://bit.ly/belajarmandirigemini.

@geminiacademybyrefo @REFO Indonesia

#KulikData #PrivasiData #LiterasiData #GeminiAcademy #GeminiAcademyUB #MahasiswaUB
```

**CTA:**

> “Coba analisis data latihan sintetismu di Gemini, lalu periksa pengenal langsung, pengenal tidak langsung, dan risiko kelompok kecil. Untuk memperdalam materi, pakai modul Belajar Mandiri bareng Gemini lewat QR di akhir video, @geminiacademybyrefo, atau https://bit.ly/belajarmandirigemini.”

## Checklist produksi

- [ ] Dataset yang tampil hanya berisi 10 baris sintetis; angka per kategori konsisten.
- [ ] Tabel awal diberi label “DATA SINTETIS” dan tidak menampilkan Nama/NIM nyata.
- [ ] Kolom Nama dan NIM dihapus sebelum tahap analisis agregat.
- [ ] Visual tidak menyebut bahwa kelompok kecil pasti mengungkap identitas; gunakan bahasa “berpotensi”.
- [ ] Hukum ditampilkan sebagai kelompok 2 hanya sebagai ilustrasi, lalu diberi catatan perlu disembunyikan/dikelompokkan untuk konteks publik.
- [ ] Tidak ada klaim bahwa nama dan NIM yang dihapus otomatis menjamin privasi.
- [ ] Overlay singkat, kontras, dan tidak menumpuk dengan tabel atau wajah.
- [ ] Elemen penting berada di area aman vertikal.
- [ ] Logo Gemini Academy memakai aset resmi; posisi dan ukurannya konsisten dengan konten sebelumnya.
- [ ] QR resmi Belajar Mandiri ditampilkan besar, kontras tinggi, dan cukup lama di bagian akhir video.
- [ ] Tautan CTA, handle `@geminiacademybyrefo`, dan tag akun diperiksa sebelum publikasi.
- [ ] Caption sudah menggunakan tag dan hashtag wajib yang berlaku.
