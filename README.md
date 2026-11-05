# Bot Gemini Academy UB

Bot berbasis Python yang menggunakan Ollama secara lokal untuk membantu Raditya
Ramadhan menyiapkan ide dan draf konten Gemini Academy untuk mahasiswa
Universitas Brawijaya (UB). Bot tidak memerlukan API key.

## Tujuan

- Membuat perencanaan konten mingguan yang sesuai target Tier C.
- Membantu menyiapkan draf produksi konten dalam file Markdown.
- Menggunakan pilar dan opsi format spreadsheet REFO sebagai referensi di
  `knowledge_base.json`.
- Spreadsheet REFO tetap menjadi tracker approval manual untuk aset media final;
  bot tidak mengirim ide atau draf ke spreadsheet.
- Menggunakan Gemini sebagai alat bantu belajar dan produktivitas secara
  edukatif, bertanggung jawab, dan relevan bagi mahasiswa dari berbagai fakultas.

## Fitur

### 1. Ide konten mingguan

- Membuat editorial plan untuk minggu ke-1 sampai ke-7.
- Menghasilkan tujuh ide konten dalam tabel Markdown.
- Memakai fokus editorial berbeda untuk tiap minggu dari `knowledge_base.json`.
- Menerima konteks khusus mingguan, misalnya periode UTS, kegiatan kampus, atau
  tema kampanye; jika dikosongkan, bot memakai fokus otomatis.
- Membandingkan rencana minggu-minggu sebelumnya agar ide tidak berulang.
- Mengikuti arahan proporsi topik dan format pada `system_prompt.txt`.
- Menampilkan hasil di terminal dan menyimpan file ke
  `Hasil Ide Konten\hasil_minggu_N.md`, misalnya `hasil_minggu_1.md`.
- Jika minggu yang sama dibuat kembali, file sebelumnya akan diperbarui.

### 2. Draf konten

Jalur draf menerima input manual: judul dan penjelasan ide/isi konten wajib,
format, dan jenis konten (`Rutin` atau `Festival`). Pilar, pesan utama, prompt
demo Gemini, CTA, serta konteks tambahan bersifat opsional. Jika tidak diisi,
Gemini dapat melengkapinya sebagai asumsi/rekomendasi. Inti dan angle ide harus
tetap dipertahankan; saran perubahan ide ditampilkan terpisah dari draf.

Draf tetap ditampilkan dan disimpan sebagai Markdown; draf ini adalah bahan
untuk membuat aset final, bukan pengajuan approval otomatis. Format yang
tersedia:

- **Reels, TikTok, YouTube Short:** hook, rencana pengambilan gambar per adegan,
  teks layar, naskah lisan, demo Gemini, caption, CTA, dan checklist produksi.
- **Feed/Carousel:** rancangan 4-8 slide sesuai kompleksitas topik, dengan teks
  siap desain, arahan visual, demo Gemini, caption, CTA, dan checklist desain.
- **Poster/Static:** teks final dan arahan layout untuk satu desain statis,
  disertai demo Gemini, caption, CTA, dan checklist desain.
- **Story:** rancangan empat frame, teks layar, demo Gemini, interaksi, caption
  singkat, CTA, dan checklist produksi.
- **Challenge card / prompt card:** teks kartu dan prompt Gemini yang siap dicoba,
  arahan visual, caption, CTA, dan checklist desain.

Semua draf meminta prompt demo dan contoh hasil yang ditandai sebagai ilustrasi
bila belum dibuat langsung di Gemini. Buat ulang dan verifikasi hasil sebelum
syuting atau publikasi. Draf disimpan di `Hasil Draft Konten` dengan nama dari
judul, misalnya
`draft_budgeting_bulanan_anak_kos.md`. Jika nama tersebut sudah digunakan,
bot menambahkan nomor agar draf lama tidak tertimpa.

Untuk mengajukan konten ke REFO, buat baris spreadsheet secara manual setelah
aset final (video/desain) tersedia di Drive. Gunakan status awal `Please Check`;
draf Markdown, ide, atau rencana konten yang belum diproduksi tidak otomatis
menjadi item approval.

## Persiapan

1. Pastikan Python dan Ollama untuk Windows sudah terpasang. Instal Ollama
   melalui `winget` jika belum ada:

   ```powershell
   winget install --id Ollama.Ollama --exact
   ```

2. Setelah instalasi, tutup dan buka ulang PowerShell atau terminal VS Code
   agar perintah `ollama` tersedia di PATH.
3. Buka atau jalankan aplikasi Ollama, lalu unduh model yang direkomendasikan:

   ```powershell
   ollama pull qwen3:4b
   ```

## Menjalankan bot

Dari PowerShell, pindah ke folder proyek:

```powershell
Set-Location "D:\ADIT KULIAH\LIMAAA\PROJECT\REFO - GSA\bot_gemini_ub"
py .\generator.py
```

Bot menampilkan menu berikut:

```text
1. Generate 7 Ide Konten Mingguan (Editorial Plan)
2. Generate Draf dari Ide Manual
3. Generate Draft dari Seri Kulik Data With Gemini
```

### Membuat ide mingguan

1. Masukkan `1`, lalu tekan Enter.
2. Masukkan nomor minggu dari `1` sampai `7`.
3. Isi konteks/fokus khusus minggu tersebut jika ada, misalnya
   `minggu UTS, bantu mahasiswa belajar aktif tanpa burnout`. Tekan Enter jika
   ingin menggunakan fokus otomatis dari `knowledge_base.json`.
4. Hasil tampil di terminal dan tersimpan, misalnya, di
   `Hasil Ide Konten\hasil_minggu_1.md`.

Sebelum menghasilkan rencana, bot membaca hasil minggu-minggu sebelumnya yang
tersedia dan meminta model menghindari pengulangan topik maupun angle. Fokus
otomatis untuk tujuh minggu membentuk alur dari belajar mandiri, keseharian
kampus, literasi digital, kolaborasi, eksplorasi kreatif, persiapan karier,
hingga refleksi. Atur peta tersebut pada `weekly_focuses` di
`knowledge_base.json`; konteks yang dimasukkan saat menjalankan bot hanya
berlaku untuk rencana itu.

### Membuat draf konten

1. Masukkan `2`, lalu tekan Enter.
2. Masukkan judul/topik konten.
3. Jelaskan ide/isi konten yang ingin dibuat. Kolom ini wajib; tulis angle dan
   hal yang ingin disampaikan dengan kata-katamu sendiri.
4. Pilih format: `Reels`, `Feed`/`Carousel`, `Story`, `TikTok`,
   `YouTube Short`, `Static/Carousel/Poster`, atau
   `Challenge card / prompt card`.
5. Masukkan jenis konten: `Rutin` atau `Festival`.
6. Isi nama pilar jika sudah ditentukan. Emoji tidak wajib; misalnya, cukup
   masukkan `University Life`. Pesan utama, prompt/demo, CTA, dan konteks
   tambahan juga opsional; tekan Enter untuk melewatinya.
7. Hasil tampil di terminal dan tersimpan di folder `Hasil Draft Konten`.

Format `Static/Carousel/Poster` menghasilkan draf carousel 4-8 slide sesuai
kompleksitas topik. Masukkan `Poster` atau `Static` secara langsung jika ingin
draf satu desain statis.

### Membuat draf dari Seri Kulik Data With Gemini

1. Masukkan `3`, lalu pilih salah satu dari tujuh episode yang ditampilkan.
2. Tentukan format dan jenis konten (`Rutin` atau `Festival`).
3. Isi pilar, pesan utama, CTA, atau konteks tambahan jika diinginkan. Topik,
   analogi sehari-hari, dan prompt demo Gemini diambil otomatis dari episode.
4. Hasil tampil di terminal dan tersimpan di folder `Hasil Draft Konten`.

Gunakan data sintetis/fiktif untuk demonstrasi analisis; jangan masukkan data
pribadi atau transaksi asli. Rincian episode tersedia di
`Kulik Data With Gemini\Seri Kulik Data With Gemini.md`.

Jalankan kembali `py .\generator.py` untuk setiap konten atau minggu yang ingin
dibuat. Folder output dibuat otomatis ketika hasil pertama kali disimpan.

## Mengganti model lokal

Model bawaan adalah `qwen3:4b`. Jika ingin model lain, unduh model tersebut
dengan `ollama pull`, lalu atur `OLLAMA_MODEL` pada PowerShell yang sama:

```powershell
$env:OLLAMA_MODEL="qwen3:8b"
py .\generator.py
```

Ollama berjalan di komputer sendiri; kecepatan bergantung pada spesifikasi
perangkat. Model yang lebih kecil biasanya lebih ringan, tetapi hasilnya dapat
kurang terperinci.

## Membaca file hasil

File hasil menggunakan Markdown. Untuk melihat tabel atau formatnya dengan rapi
di Visual Studio Code, buka file `.md`, lalu tekan `Ctrl+Shift+V` untuk membuka
Markdown Preview.

## Pemecahan masalah

- **Tidak dapat terhubung ke Ollama:** buka aplikasi Ollama dan pastikan layanan
  berjalan, lalu jalankan ulang bot.
- **Model belum tersedia:** jalankan `ollama pull qwen3:4b` atau unduh model
  yang dipilih melalui `OLLAMA_MODEL`.
- **Model lambat atau kehabisan memori:** coba model yang lebih kecil, misalnya
  `qwen3:4b`, dan tutup aplikasi lain yang berat.
