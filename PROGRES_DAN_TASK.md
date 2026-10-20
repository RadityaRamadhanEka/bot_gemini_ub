# Progres dan Task Proyek Bot Gemini UB

Catatan progres diperbarui 20 Oktober 2026.

## Progres pengembangan sejak awal

- Bot telah dikembangkan untuk dua tahap awal: membuat ide konten mingguan dan
  membuat draf konten siap produksi. Output disimpan sebagai Markdown, dengan
  dukungan format seperti Reels, Carousel, Poster/Static, Story, Shorts, TikTok,
  dan challenge/prompt card.
- Pada 11 Oktober 2026, alur dasar diperkuat dengan validasi input, penanganan
  error API, konfigurasi model, penyimpanan hasil, dan pemeriksaan lokal.
- Pada 18 Oktober 2026, alur draf diperluas untuk input ide manual, referensi
  spreadsheet/approval REFO, pemetaan format, dan simulasi lokal tanpa
  memanggil API.
- Pada 20 Oktober 2026, arah pengembangan berikutnya dibahas: melanjutkan dari
  draf ke desain carousel siap unggah. Dua set referensi visual (masing-masing
  enam slide) telah ditinjau. Ukuran 1080 × 1350 px, identitas visual
  konsisten, aset brand tersedia untuk ditambahkan, dan CTA penutup fleksibel
  telah disepakati.
- Spesifikasi kebutuhan awal automasi desain dicatat di
  `SPESIFIKASI_AUTOMASI_DESAIN_CAROUSEL.md`. Tahap ini masih berupa analisis;
  fitur pembuatan dan ekspor gambar belum diimplementasikan.
- Folder `referensi_design_carousel\brand-assets` kini berisi `Main Character.png`,
  logo Gemini Academy/Gemini, ikon Gemini, dan font Inter. Karakter utama
  ditetapkan sebagai acuan untuk variasi pose dan ekspresi; ciri identitas
  kelinci, kostum wisuda, kemeja putih, serta ikon brand harus dipertahankan.
- `Main Character.png` memiliki latar merah tua, bukan latar transparan.
  Metode pemisahan/pemakaian latarnya dan konsistensi hasil variasi karakter
  masih perlu diuji saat implementasi.

## Kondisi proyek

- Bot dijalankan dari terminal dengan `py .\generator.py`.
- File pendukung: `system_prompt.txt` dan `knowledge_base.json`.
- Dependensi `google-genai` terpasang di Python 3.14.8; versi SDK yang terdeteksi 2.29.0.
- Model bawaan di kedua fitur: `gemini-3.8-flash` (berdasarkan saran API pada pengujian sebelumnya).
- Belum ada pengujian yang berhasil menghasilkan respons dari Gemini.
- Saat progres ini diperbarui, `GEMINI_API_KEY` tidak tersedia pada sesi PowerShell. Key tidak dibaca atau ditampilkan.

## Riwayat pengujian API

1. Panggilan awal gagal karena `GEMINI_API_KEY` belum tersedia.
2. Panggilan dengan `gemini-2.5-flash` mendapat `404 NOT_FOUND`; respons API menyarankan `gemini-3.8-flash`.
3. Panggilan berikutnya dengan model tersebut mendapat `503 UNAVAILABLE` karena layanan sedang mengalami permintaan tinggi. Keberhasilan API belum terkonfirmasi.
4. API key pernah tertulis di chat. Anggap key tersebut sudah terekspos dan cabut/revoke; jangan gunakan lagi atau simpan key di file proyek/chat.

## Perbaikan pada 11 Oktober 2026

- Path system prompt dan knowledge base sekarang ditentukan relatif terhadap lokasi `generator.py`, bukan current working directory.
- Validasi minggu menolak nilai non-angka dan angka di luar 1-7.
- Menu dan kolom wajib pada draf memberi pesan validasi yang jelas.
- API key diperiksa saat akan membuat client; pesan error tidak menampilkan nilai key.
- Error 401/403, 404, 429, dan 5xx mendapat petunjuk tindakan serta detail teknis.
- Error 429 dan 5xx dicoba ulang maksimal tiga kali dengan jeda singkat.
- Model dapat diubah tanpa mengedit kode melalui `GEMINI_MODEL`; default tetap `gemini-3.8-flash`.
- Pemeriksaan sintaks Python, validasi input minggu (1-7), pemuatan file pendukung, dan startup dari luar folder bot berhasil.
- Menu 1 menyimpan hasil sebagai `Hasil Ide Konten\hasil_minggu_N.md` (misalnya `Hasil Ide Konten\hasil_minggu_1.md`) dan tetap menampilkan hasil di terminal. Membuat ulang minggu yang sama akan memperbarui file tersebut.
- Menu 2 menyimpan hasil sebagai Markdown di `Hasil Draft Konten`, dengan nama berdasarkan judul (misalnya `draft_budgeting_bulanan_anak_kos.md`). Jika nama file sudah ada, bot menambahkan nomor agar draf sebelumnya tidak tertimpa.
- Template draft menu 2 sekarang berbeda untuk Reels, Feed/Carousel, dan Story. Semua format tetap mengikuti aturan demonstrasi Gemini, keamanan data, batas etis, CTA, hashtag, dan tag REFO; voiceover/caption panjang hanya diminta jika sesuai format.
- Tes respons nyata untuk kedua menu tetap menunggu API key baru dari pemilik; sesi saat ini tidak memiliki key.

## Langkah untuk menguji koneksi dan kedua fitur

1. Cabut key lama dan buat key baru melalui Google AI Studio. Jangan kirim key ke chat atau simpan di file proyek.
2. Di PowerShell, jalankan:

   ```powershell
   cd "D:\ADIT KULIAH\LIMAAA\PROJECT\REFO - GSA\bot_gemini_ub"
   $env:GEMINI_API_KEY="API_KEY_BARU"
   py .\generator.py
   ```

3. Pilih menu `1`, masukkan minggu `1`, lalu pastikan Editorial Plan memuat tujuh konten.
4. Jalankan lagi, pilih menu `2`, dan pastikan draf berisi enam bagian yang diminta.
5. Jika model tidak ditemukan, periksa model yang tersedia untuk key tersebut dan jalankan ulang dengan model yang sesuai:

   ```powershell
   $env:GEMINI_MODEL="NAMA_MODEL_YANG_TERSEDIA"
   ```

6. Jika muncul 429, periksa kuota/rate limit; jika 5xx terus berulang, tunggu lalu coba lagi dan periksa status layanan.
7. Jangan mencatat atau membagikan API key saat melaporkan error.

## Konteks spreadsheet approval dan penyempurnaan pada 18 Oktober 2026

- Spreadsheet `Raditya` adalah tracker approval REFO untuk aset media final yang sudah tersedia di Drive, bukan untuk ide mingguan atau draf Markdown yang masih akan diproduksi.
- Output bot tetap berupa Markdown. Tidak ada integrasi atau pengiriman otomatis ke spreadsheet; baris dibuat manual setelah video/desain final siap direview, dengan status awal `Please Check`.
- Pemetaan format: `Story` ke `IG Story`, `Feed/Carousel` ke `Static/Carousel/Poster`, dan format lainnya mengikuti pilihan Type pada spreadsheet. Dropdown hanya tercatat berlaku pada baris 2-7; ini bukan batas jumlah konten per minggu.
- Menu draf mendukung Reel, IG Story, Static/Carousel/Poster, YouTube Short, TikTok, dan Challenge card / prompt card. Nilai Static/Carousel/Poster menggunakan carousel 4-8 slide sesuai kompleksitas topik; `Poster` atau `Static` dapat dimasukkan untuk satu desain statis.
- Draf produksi diperkuat dengan shot plan, teks dan naskah yang siap direkam/desain, prompt demo Gemini, caption/CTA/tag, serta checklist produksi. Contoh hasil demo harus diberi label ilustrasi dan dibuat ulang serta diverifikasi di Gemini sebelum syuting/publikasi.
- `knowledge_base.json` sekarang mencakup pilar kampanye, kolom sheet, opsi dropdown, pemetaan format, fungsi dashboard, dan alur bahwa hanya aset final yang diajukan manual. Prompt editorial plan dan draf memakai referensi ini tanpa mengarang metadata approval.
- Verifikasi lokal pada 18 Oktober: sintaks Python dan tujuh kasus normalisasi/pemetaan format lolos menggunakan generator Gemini tiruan; tidak ada panggilan API nyata. Keberhasilan respons API tetap belum terkonfirmasi.
- Menu draf sekarang menerima judul dan uraian ide manual yang wajib, serta pilar, pesan utama, prompt/demo, CTA, dan konteks tambahan yang opsional. Prompt meminta Gemini mempertahankan angle pengguna dan memisahkan saran pengembangan dari draf produksi.
- Validasi alur manual: sintaks/JSON valid; input wajib dan validasi pilar diuji; seluruh input opsional masuk ke prompt; simulasi menu draf berhasil menggunakan generator tiruan tanpa memanggil Gemini API.
