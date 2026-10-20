# Spesifikasi Otomasi Desain Carousel

Dokumen ini mencatat kebutuhan awal untuk mengembangkan bot Gemini Academy UB
dari generator ide dan draf menjadi alat bantu produksi desain carousel siap
unggah. Spesifikasi disusun dari dua contoh carousel pada folder
`referensi_design_carousel` dan hasil diskusi pada 20 Oktober 2026.

## Status

- **Tahap:** prototipe renderer lokal untuk trial matriks belajar.
- **Sudah diimplementasikan:** enam PNG 1080 × 1350 dengan variasi layout per
  fungsi slide; belum ada parser umum untuk mengubah semua draf Markdown menjadi
  desain otomatis.
- **Output:** satu file PNG per slide di folder konten.

## Kebutuhan yang sudah disepakati

- Ukuran setiap slide: **1080 × 1350 px** (rasio 4:5).
- Identitas visual harus konsisten di seluruh carousel dan antar konten.
- CTA pada slide terakhir fleksibel mengikuti brief dan tujuan konten.
- Aset brand tersedia di `referensi_design_carousel/brand-assets`.
- `Main Character.png` menjadi acuan karakter utama; karakter dapat dibuat
  dengan pose atau ekspresi berbeda sambil mempertahankan identitasnya.
- Aset logo dan font Inter juga telah ditambahkan.

## Hasil analisis referensi

Dua set referensi masing-masing berisi enam slide. Keduanya menunjukkan
identitas Gemini Academy yang sama dengan variasi latar dan komposisi.

### Identitas visual

- Logo Gemini dan label Gemini Academy muncul di bagian atas slide.
- Maskot kelinci wisuda menjadi karakter visual yang menonjol.
- Judul memakai tipografi sans-serif tebal, ukuran besar, dan sering disusun
  dalam beberapa kapsul/pita membulat.
- Warna aksen yang dominan: biru, hijau, merah-koral, dan kuning; teks judul
  umumnya putih.
- Elemen pendukung dapat mencakup panah/ajakan swipe, kotak informasi, contoh
  tampilan Gemini, ilustrasi, dan panel checklist.

### Acuan karakter utama

File `referensi_design_carousel/brand-assets/Main Character.png` menampilkan
kelinci putih dengan topi wisuda hitam dan tali rumbai emas, kemeja putih dengan
ikon Gemini Academy di saku, serta pose telunjuk terangkat. Gambar memiliki
latar merah tua dan bukan PNG transparan.

Gunakan file ini sebagai acuan identitas untuk menghasilkan pose atau ekspresi
yang berbeda sesuai kebutuhan slide. Pertahankan ciri yang membuat karakter
mudah dikenali: kelinci putih, bentuk wajah dan telinga, topi wisuda beserta
rumbai emas, kemeja putih, dan ikon pada saku. Pose, arah pandang, dan ekspresi
boleh berubah; jangan mengubah kostum, proporsi, spesies, atau identitas brand
tanpa persetujuan.

Karena aset sumber berlatar merah tua, proses desain perlu mempertimbangkan
pemisahan karakter dari latar atau pemakaian latar yang sesuai. Hasil variasi
generatif tetap perlu ditinjau untuk memastikan kemiripan karakter dan
keterpaduan tepi; konsistensi persis tidak boleh diasumsikan sebelum metode
generasi diuji.

### Variasi latar yang tampak

- Foto suasana belajar/kampus dengan kelinci sebagai fokus.
- Latar grid hijau dengan panel informasi.
- Latar wallpaper hijau zaitun dan panel kayu dengan pendekatan cerita.

Latar boleh menyesuaikan topik, tetapi pemilihan warna, tipografi, posisi
identitas, penggunaan maskot, dan komponen berulang harus mempertahankan satu
identitas desain yang konsisten. Hindari menyalin satu layout secara kaku untuk
semua topik.

### Pola alur konten

1. **Cover:** hook/topik yang singkat dan menarik, visual utama, serta ajakan
   untuk swipe.
2. **Masalah atau konteks:** situasi yang relevan dengan audiens mahasiswa.
3. **Isi utama:** langkah, tips, atau solusi; gunakan contoh visual bila
   membantu pemahaman.
4. **Rangkuman atau aturan penting:** poin inti, checklist, atau hal yang perlu
   diverifikasi.
5. **Penutup:** CTA yang dipilih sesuai brief, misalnya ajakan menyimpan,
   berkomentar, atau membagikan konten.

Urutan dan jumlah slide dapat menyesuaikan materi. Draf konten yang sudah ada
mendukung carousel 4-8 slide; automasi desain sebaiknya mengikuti jumlah slide
yang disetujui pada brief/draf, bukan menambahkan isi sendiri.

## Alur automasi yang dituju

1. Pengguna memilih draf konten carousel yang sudah dibuat atau memberikan
   brief carousel.
2. Bot membaca teks per slide dan arahan visual, lalu meminta konfirmasi atau
   koreksi sebelum produksi.
3. Bot memakai aset brand dan referensi desain yang tersedia di
   `referensi_design_carousel`.
4. Bot menyusun komposisi dan menghasilkan PNG 1080 × 1350 px untuk setiap
   slide.
5. Bot menyimpan hasil dalam folder khusus untuk konten tersebut dan
   menampilkan lokasi file serta pratinjau/daftar hasil.
6. Sebelum hasil dianggap siap, bot memeriksa ukuran, jumlah dan urutan slide,
   keterbacaan teks, margin aman, konsistensi brand, serta kesesuaian isi
   terhadap draf yang disetujui.

Teks harus dirender sebagai elemen grafis terpisah dari foto/ilustrasi agar
ejaan, tanda baca, dan keterbacaannya terjaga. Jangan mengandalkan generator
gambar untuk menggambar teks, logo, atau elemen identitas secara akurat.

## Aturan produksi dan pemeriksaan

- Pertahankan isi, angle, dan klaim dari draf yang disetujui; jangan
  mengarang data atau mengubah makna.
- Pastikan teks nyaman dibaca pada ukuran ponsel dan tidak terlalu padat.
- Jaga margin aman; jangan biarkan logo, teks, atau CTA terpotong atau saling
  menutupi.
- Pastikan elemen pengarah swipe tidak menutupi isi penting dan penggunaannya
  sesuai posisi slide.
- Jangan membuat CTA penutup yang tidak sesuai dengan tujuan/brief.
- Periksa urutan file agar urutan unggah sama dengan urutan baca carousel.
- Contoh hasil Gemini yang bersifat ilustrasi tetap perlu diverifikasi di
  Gemini sebelum publikasi, mengikuti aturan draf konten yang ada.

## Aset brand dan hal yang masih perlu disiapkan

Folder `referensi_design_carousel/brand-assets` sekarang memuat:

- `Main Character.png` sebagai acuan karakter utama.
- `Gemini Academy Logo@2x-8.png`.
- `Gemini Full Logo - Black@2x.png`.
- `Gemini Icon@2x-8.png`.
- Font Inter variabel dan file font Inter statis pada folder `Font - Inter`,
  termasuk `OFL.txt`.

Sebelum implementasi, tinjau transparansi/ukuran logo dan pilih berkas yang
tepat untuk tiap penggunaan. Panduan warna/brand terpisah belum tercatat;
sementara gunakan warna dari referensi visual. Jika suatu aset resmi tidak
tersedia, bot harus menginformasikan keterbatasannya dan tidak membuat ulang
logo seolah-olah aset resmi.

## Keputusan teknis yang belum ditetapkan

Prototipe menggunakan Pillow untuk menggambar elemen grafis dan teks secara
lokal; tidak memerlukan API key atau layanan generatif. Layout trial telah
dipisah menjadi variasi cover, pain point, matriks, prompt, planner, dan CTA.
Langkah lanjutan yang masih diperlukan adalah parser/konfirmasi isi per slide
dari draf umum, lebih banyak variasi ilustrasi, serta pemeriksaan keterbacaan
dan margin otomatis sebelum ekspor final.
