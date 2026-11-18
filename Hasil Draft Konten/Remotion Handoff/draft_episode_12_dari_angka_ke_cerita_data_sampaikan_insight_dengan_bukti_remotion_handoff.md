# Instruksi Implementasi Video Remotion

Gunakan file ini sebagai brief lengkap untuk implementasi. Bagian **Draf sumber**
adalah acuan utama untuk judul, alur, dialog, data, dan pesan. Jangan menyalin
ulang, mengganti, atau menambah isi yang mengubah maksud draf.

## Arahan produksi

- Periksa workspace untuk menemukan proyek Remotion, pola komponen, perintah
  render, aset, dan identitas visual yang sudah ada. Ikuti pola yang tersedia;
  jangan mengubah bagian proyek yang tidak terkait.
- Ikuti storyboard dan durasi di draf. Jika durasi tidak dicantumkan, gunakan
  30-45 detik. Video vertikal 9:16, 1080x1920, 30 fps.
- Pertahankan tokoh, lokasi, alur cerita, angka, dan dialog sesuai draf. Buat
  latar dan aksi terasa konsisten; jika detail visual belum ditentukan, isi
  seperlunya tanpa mengubah cerita.
- Gunakan visual dan gerak sebagai pencerita utama. Hindari layar yang padat
  teks; sinkronkan subtitle dengan VO dan jaga semua elemen dalam safe area.
- Gunakan arahan gender VO yang tercantum di draf. Jika draf tidak menentukan,
  gunakan tokoh utama dan VO laki-laki yang konsisten.
- Cari aset resmi logo Gemini Academy dan ikuti penempatan konten sebelumnya.
  Jangan menggambar ulang logo. Jika aset tidak ditemukan, gunakan placeholder
  yang jelas dan laporkan.
- Gunakan VO/audio yang tersedia di workspace. Jika belum tersedia, jangan
  mengarang audio atau memakai pengganti yang bertentangan dengan arahan draf;
  siapkan placeholder yang jelas dan laporkan.
- Jika workspace belum memiliki proyek Remotion, jangan memasang dependency atau
  membuat aplikasi baru tanpa arahan pengguna. Berhenti dan jelaskan yang
  dibutuhkan.
- Setelah implementasi, jalankan pemeriksaan atau render preview yang tersedia.
  Laporkan file yang diubah, cara render/preview, hasil validasi, dan aset yang
  masih diperlukan.

## Draf sumber

<!-- BEGIN SOURCE DRAFT: KulikData/draft_episode_12_dari_angka_ke_cerita_data_sampaikan_insight_dengan_bukti.md -->

# Episode 12 — Dari Angka ke Cerita Data

**Seri:** Kulik Data With Gemini  
**Format:** Video vertikal pendek untuk Reels/Shorts  
**Durasi target:** 45 detik  
**Tokoh:** Raka, mahasiswa laki-laki yang sedang menyiapkan presentasi tugas  
**VO:** Suara laki-laki muda/dewasa, natural dan ramah; gunakan satu karakter suara yang konsisten sepanjang video.  
**Pesan utama:** Cerita data yang baik berangkat dari pertanyaan, didukung angka yang bisa dicek, dan jujur tentang hal yang belum diketahui. Gemini membantu menyusun draf; hasilnya tetap perlu diverifikasi.

## Audit dan perbaikan inti

- Contoh lama menyebut Nasi Ayam terjual 4 kali, tetapi tabel transaksi dan grafiknya tidak mendukung angka tersebut. Naskah ini memakai satu dataset sintetis yang konsisten: Nasi Ayam tercatat 3 dari 5 transaksi.
- Harga dan rata-rata yang sebelumnya muncul tidak punya dasar data yang jelas. Harga dihilangkan agar fokus tetap pada cara membaca pola.
- Klaim bahwa menu paling laku bisa dijelaskan oleh harga atau promo tidak bisa dibuktikan dari data ini. Naskah membedakan temuan dari dugaan dan tidak menyimpulkan sebab-akibat.
- Gemini tidak digambarkan sebagai sumber kebenaran atau pembuat kesimpulan otomatis. Tokoh menunjukkan cara memberi konteks, meminta bantuan menyusun draf, lalu mengecek kembali hitungannya.
- Pesan panjang dipindahkan ke narasi/caption. Teks overlay dibuat singkat agar video tidak terasa seperti slide presentasi.

## Storyboard siap produksi

| Waktu | Adegan dan aksi tokoh | Narasi/dialog Dita | Teks overlay | Arahan visual/Remotion |
|---|---|---|---|---|
| 0–5 dtk | Raka menatap lembar angka di laptop, lalu menghadap kamera. | “Punya banyak angka, tapi bingung mau cerita apa? Aku mulai dari satu pertanyaan.” | **Angka banyak. Mulai dari mana?** | Medium shot Raka. Angka-angka kecil memenuhi layar, lalu merapikan diri menjadi satu tanda tanya. |
| 5–12 dtk | Raka mengetuk satu baris data; lima kartu transaksi muncul satu per satu. | “Ini lima transaksi kantin fiktif. Pertanyaanku: menu apa yang paling sering tercatat?” | **Pertanyaan dulu** | Tampilkan ringkasan dataset, bukan tabel padat: Nasi Ayam muncul 3 kali, Mie Ayam 1 kali, Es Teh 1 kali. Beri label “data sintetis”. |
| 12–21 dtk | Raka menggeser kartu ke grafik batang sederhana. | “Nasi Ayam tercatat tiga dari lima transaksi. Itu temuan dari sampel kecil ini—bukan bukti semua orang paling suka Nasi Ayam.” | **3 dari 5 transaksi** | Batang Nasi Ayam = 3; Mie Ayam = 1; Es Teh = 1. Angka muncul bersamaan dengan label kategori. Sorot frasa “dalam data ini”. |
| 21–30 dtk | Muncul gelembung saran “Karena lebih murah?”; Raka menggeleng dan mencoretnya. | “Kita belum tahu alasannya. Tidak ada data harga, promo, atau jumlah pengunjung. Jadi jangan menebak penyebab.” | **Pola ≠ penyebab** | Tampilkan gelembung dugaan sebentar, lalu beri tanda tanya/coret. Jangan tampilkan dugaan sebagai fakta. |
| 30–39 dtk | Raka mengetik prompt singkat; kartu “temuan” dan “batas” tersusun rapi. | “Aku minta Gemini membantu merapikan temuan dan batasnya. Setelah itu, aku cek lagi apakah angkanya sesuai data.” | **Bantu susun. Tetap cek.** | Tampilkan antarmuka generik, bukan klaim hasil pasti. Sorot prompt: “Ringkas pola dari data ini. Pisahkan fakta dan dugaan; jangan menambah angka.” |
| 39–45 dtk | Raka menutup laptop dan menghadap kamera dengan gestur mengajak. | “Coba mulai dari satu pertanyaan. Biar angka punya cerita—dengan bukti.” | **Tanya → cek → ceritakan** | Grafik berubah menjadi tiga kartu berurutan. Akhiri dengan lockup “Kulik Data With Gemini” dan logo Gemini Academy. |

### Catatan tempo dan penyajian

- Bawakan dialog seperti Dita sedang menjelaskan temuannya kepada teman, bukan membaca materi presentasi.
- Gunakan satu tokoh laki-laki (Raka) dan satu situasi dari awal sampai akhir; jaga kostum, posisi, palet warna, dan gaya ilustrasi tetap konsisten.
- Tampilkan logo Gemini Academy dengan aset resmi yang sama seperti konten sebelumnya, pada posisi dan ukuran standar kampanye. Pertahankan secara konsisten di area aman dan sertakan pada lockup penutup; jangan menggambar ulang logonya.
- Sisakan jeda pendek setelah angka “3 dari 5” dan setelah “kita belum tahu alasannya”, agar dua gagasan utama sempat dipahami.
- Batasi overlay ke satu gagasan pendek per adegan. Subtitle mengikuti dialog, tetapi jangan menumpuk subtitle, prompt, dan tabel sekaligus.
- Gunakan transisi kartu/angka yang sederhana dan konsisten. Hindari animasi yang mengalihkan perhatian dari bukti.
- Untuk komposisi vertikal 9:16, letakkan tokoh, grafik, dan teks penting di area aman; jangan menaruh informasi utama dekat tepi atau area kontrol aplikasi.

## Dataset sintetis untuk visual

Setiap baris adalah satu transaksi; data ini hanya contoh untuk video, bukan data kantin sungguhan.

| Transaksi | Menu |
|---|---|
| 1 | Nasi Ayam |
| 2 | Mie Ayam |
| 3 | Nasi Ayam |
| 4 | Es Teh |
| 5 | Nasi Ayam |

**Ringkasan yang benar:** Nasi Ayam 3 transaksi; Mie Ayam 1 transaksi; Es Teh 1 transaksi. Jumlah ini menunjukkan frekuensi dalam lima baris contoh, bukan jumlah porsi, total penjualan kantin, atau preferensi semua pembeli.

## Prompt demo Gemini

Tempelkan data sintetis di atas setelah prompt ini:

> Dari data transaksi sintetis berikut, jawab pertanyaan: “Menu apa yang paling sering tercatat?” Hitung frekuensi setiap menu hanya dari baris yang diberikan. Sajikan: (1) temuan dan angka pendukung, (2) batas interpretasi, dan (3) satu pertanyaan lanjutan yang dapat diuji. Pisahkan fakta dari dugaan. Jangan menambah data, menyimpulkan sebab-akibat, atau menggeneralisasi di luar data ini. Jika ada informasi yang tidak tersedia, nyatakan bahwa informasinya tidak tersedia.

**Contoh hasil yang diharapkan (tetap periksa terhadap data):**

- **Temuan:** Nasi Ayam paling sering tercatat, sebanyak 3 dari 5 transaksi.
- **Batas:** Data hanya berisi lima transaksi sintetis; tidak menjelaskan alasan pilihan menu dan tidak mewakili seluruh pembeli.
- **Pertanyaan lanjutan:** Apakah pola yang sama terlihat pada periode pengamatan yang lebih panjang?

## Caption siap unggah

Angka belum otomatis jadi cerita 📊 Mulai dari pertanyaan yang jelas, tunjukkan angka pendukung, lalu sebutkan apa yang belum bisa disimpulkan 🔎

Di contoh lima transaksi fiktif ini, Nasi Ayam tercatat 3 kali 🍗 Tapi kita belum tahu alasannya. Data ini tidak memuat harga, promo, atau informasi pembeli.

Gemini bisa membantu merapikan draf analisis ✨ Tetap cek hitungan dan pastikan kesimpulannya sesuai data ✅

**Coba:** gunakan prompt di video dengan data sintetis, lalu periksa kembali hasilnya 🧠  
**CTA:** Lihat panduan cepat Gemini di sini 👇 [masukkan tautan panduan yang sudah diverifikasi]

#GeminiAcademy #GeminiAcademyUB #GeminiAcademyFestival  
Tag: @REFO Indonesia

## Checklist produksi

- [ ] Data yang tampil dan yang disebut tokoh konsisten: 5 transaksi; Nasi Ayam 3, Mie Ayam 1, Es Teh 1.
- [ ] Beri label “data sintetis” saat dataset pertama kali muncul.
- [ ] Grafik batang memiliki label kategori dan skala yang mudah dibaca.
- [ ] Tidak menampilkan dugaan sebagai fakta atau menyiratkan hubungan sebab-akibat.
- [ ] Teks overlay singkat, kontras, dan terbaca pada layar ponsel; subtitle tidak menutupi grafik atau wajah.
- [ ] Elemen penting berada di area aman video vertikal dan tetap terbaca tanpa audio.
- [ ] Tautan CTA dan tag akun diperiksa sebelum publikasi.
- [ ] Gunakan aset resmi logo Gemini Academy dan samakan posisi/ukurannya dengan konten sebelumnya; jangan menggambar ulang logo.
- [ ] Pastikan penggunaan nama/logo Gemini dan identitas kampanye mengikuti panduan merek yang berlaku.

<!-- END SOURCE DRAFT -->
