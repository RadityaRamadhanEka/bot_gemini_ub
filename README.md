# Bot Gemini Academy UB

Bot berbasis Python yang menggunakan Gemini untuk membantu Raditya Ramadhan
menyiapkan ide dan draf konten Gemini Academy untuk mahasiswa Universitas
Brawijaya (UB).

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

### 3. Trial desain carousel

Menu `3` merender enam PNG 1080 × 1350 untuk trial matriks belajar dengan
HTML/CSS dan Chrome atau Microsoft Edge, tanpa memanggil Gemini API. Komposisi
slide mengikuti referensi Figma dengan art direction berbeda per fungsi:
cinematic study, pattern story, blueprint, paper note, desk planner, dan warm
editorial. Variasi diterapkan pada latar, tekstur, framing maskot, komposisi, dan
perlakuan tipografi; isi setiap slide tetap dapat disunting. Hasil PNG dan
pratinjau HTML disimpan terpisah di
`Hasil Desain Carousel\trial_matriks_belajar_html`.

Untuk menjalankan, pilih menu `3` atau gunakan `py .\carousel_designer.py`.
Konten, art direction, dan framing karakter per slide dapat diubah di `SLIDES`
pada `carousel_designer.py`; pilihan tampilan dan template diatur di
`carousel_template.html`.

Untuk membuat visual AI mengikuti brief trial, atur `GEMINI_API_KEY` secara
lokal di PowerShell yang sama, lalu pilih menu `4` atau jalankan:

```powershell
py .\carousel_designer.py --generate-assets
```

Image generation meminta konfirmasi sebelum mengirim permintaan. Pembuatan dapat
menggunakan kuota atau menimbulkan biaya sesuai model dan akun. Model bawaan
adalah `gemini-nano-banana-2.1`; bila tidak tersedia, atur model gambar yang
tersedia:

```powershell
$env:GEMINI_IMAGE_MODEL="MODEL_IMAGE_YANG_TERSEDIA"
```

Visual disimpan di subfolder `visuals` dan dipakai ulang saat render berikutnya
agar tidak mengirim permintaan gambar berulang. Hasil pose dan kesesuaian
maskot perlu ditinjau sebelum digunakan.

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

1. Pastikan Python dan paket `google-genai` tersedia. Jika paket belum terpasang:

   ```powershell
   py -m pip install google-genai
   ```

2. Buat API key Gemini melalui Google AI Studio. Simpan key dengan aman; jangan
   menaruhnya di source code, README, atau file proyek.
3. Buka PowerShell baru. Atur key di sesi tersebut setiap kali akan menjalankan
   bot:

   ```powershell
   $env:GEMINI_API_KEY="API_KEY_MILIKMU"
   ```

   Pengaturan ini berlaku hanya untuk sesi PowerShell saat ini. Jika membuka
   sesi baru, atur kembali API key.

## Menjalankan bot

Dari PowerShell, pindah ke folder proyek:

```powershell
Set-Location "D:\ADIT KULIAH\LIMAAA\PROJECT\REFO - GSA\bot_gemini_ub"
$env:GEMINI_API_KEY="API_KEY_MILIKMU"
py .\generator.py
```

Bot menampilkan menu berikut:

```text
1. Generate 7 Ide Konten Mingguan (Editorial Plan)
2. Generate Draf Detail Konten Spesifik
```

### Membuat ide mingguan

1. Masukkan `1`, lalu tekan Enter.
2. Masukkan nomor minggu dari `1` sampai `7`.
3. Hasil tampil di terminal dan tersimpan, misalnya, di
   `Hasil Ide Konten\hasil_minggu_1.md`.

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

Jalankan kembali `py .\generator.py` untuk setiap konten atau minggu yang ingin
dibuat. Folder output dibuat otomatis ketika hasil pertama kali disimpan.

## Konfigurasi model

Model bawaan adalah `gemini-3.8-flash`. Jika model tersebut tidak tersedia untuk
API key yang digunakan, atur `GEMINI_MODEL` ke nama model yang tersedia sebelum
menjalankan bot:

```powershell
$env:GEMINI_MODEL="NAMA_MODEL_YANG_TERSEDIA"
py .\generator.py
```

## Membaca file hasil

File hasil menggunakan Markdown. Untuk melihat tabel atau formatnya dengan rapi
di Visual Studio Code, buka file `.md`, lalu tekan `Ctrl+Shift+V` untuk membuka
Markdown Preview.

## Pemecahan masalah

- **`GEMINI_API_KEY belum disetel`:** atur `$env:GEMINI_API_KEY` di PowerShell
  yang sama sebelum menjalankan bot.
- **HTTP 401/403:** periksa key dan akses Gemini API.
- **HTTP 404:** periksa nama model atau atur `GEMINI_MODEL`.
- **HTTP 429:** periksa kuota, rate limit, atau billing API.
- **HTTP 5xx:** layanan sedang sibuk/bermasalah; bot mencoba ulang secara
  terbatas. Tunggu sebentar sebelum mencoba lagi.

Jangan membagikan API key saat meminta bantuan atau melaporkan error.
