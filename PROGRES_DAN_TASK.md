# Progres dan Task Proyek Bot Gemini UB

Catatan progres diperbarui 1 November 2026.

## Fitur yang dipakai

- Menu 1 membuat tujuh ide konten untuk minggu ke-1 sampai ke-7 dan menyimpan
  hasil Markdown ke `Hasil Ide Konten\hasil_minggu_N.md`.
- Menu 2 membuat draf produksi dari ide yang dimasukkan pengguna dan
  menyimpannya ke `Hasil Draft Konten`. Jika nama file sudah ada, nomor
  ditambahkan agar draf sebelumnya tidak tertimpa.
- Model bahasa berjalan lokal melalui Ollama; bot tidak lagi menggunakan
  Gemini API atau membutuhkan API key.
- Format Carousel tetap tersedia sebagai format draf konten. Bot tidak lagi
  membuat desain atau gambar carousel.

## Menyiapkan Ollama

1. Instal Ollama untuk Windows jika belum terpasang:

   ```powershell
   winget install --id Ollama.Ollama --exact
   ```

2. Jalankan aplikasi Ollama dan unduh model bawaan:

   ```powershell
   ollama pull qwen3:8b
   ```

3. Jalankan bot dari folder proyek:

   ```powershell
   py .\generator.py
   ```

Untuk memakai model lain, unduh dengan `ollama pull NAMA_MODEL`, lalu atur
`$env:OLLAMA_MODEL="NAMA_MODEL"` pada sesi PowerShell yang sama.

## File pendukung dan output

- File prompt dan knowledge base: `system_prompt.txt` dan `knowledge_base.json`.
- Hasil ide mingguan: `Hasil Ide Konten`.
- Draf produksi: `Hasil Draft Konten`.
- Baris approval spreadsheet REFO tetap dibuat manual setelah aset final siap;
  ide dan draf Markdown tidak diajukan otomatis.

## Perubahan 1 November 2026

- Integrasi generator teks diganti dari Google Gemini API menjadi endpoint chat
  lokal Ollama.
- Model bawaan `qwen3:8b`; dapat diganti melalui `OLLAMA_MODEL`. Host Ollama
  dapat dikonfigurasi melalui `OLLAMA_HOST`.
- Dependensi Python `google-genai` tidak lagi diperlukan oleh generator.
- Menu generator kini hanya memuat pembuatan ide mingguan dan draf dari ide.
- Fitur desain carousel dihapus. File renderer, template, spesifikasi, hasil,
  dan aset referensinya tidak lagi menjadi bagian proyek.
