**Audit dan Draf Produksi — Episode 10**

## 1. Brief konten

- **Judul:** Pivot table: ringkas banyak baris tanpa hitung manual
- **Format:** Instagram Reel, sekitar 35–40 detik
- **Pilar:** 📚 Study Hack
- **Audiens:** Mahasiswa UB yang mengolah data tugas, proyek, atau latihan
- **Pesan utama:** Pivot table merangkum angka berdasarkan kategori. Gemini dapat membantu menjelaskan langkahnya; pivot table dibuat dan diperiksa di spreadsheet seperti Google Sheets atau Excel.
- **Angle:** Mengubah data transaksi kantin fiktif menjadi ringkasan total penjualan per menu dan hari.
- **CTA:** Simpan tutorial ini dan coba dengan data latihan yang tidak memuat informasi pribadi.
- **Catatan data:** Gunakan data sintetis. Jangan masukkan data pribadi atau data sensitif ke Gemini.

## 2. Tujuan dan catatan audit

**Tujuan:** Menjelaskan fungsi pivot table lewat demo yang singkat, akurat, dan bisa diikuti penonton.

**Perbaikan dari draf sebelumnya:**
- Menghapus klaim “100 struk”, “1 jam”, dan “1 menit” karena tidak dibuktikan oleh demo dan berisiko terdengar seperti janji hasil.
- Menjelaskan bahwa Gemini memberi panduan, sedangkan pivot table dibuat di Google Sheets atau Excel.
- Memperbaiki penempatan field: **Menu** pada Rows, **Hari** pada Columns, dan **Total Penjualan** pada Values dengan ringkasan **SUM**.
- Membedakan jumlah barang dari nilai penjualan. Nilai penjualan per baris adalah **Qty × Harga Satuan**.

## 3. Skenario Reel

| Waktu | Visual/aksi | Teks overlay | Narasi |
|---|---|---|---|
| 0–3 dtk | Tampilkan spreadsheet berisi banyak baris, lalu sorot beberapa angka. | **Masih jumlahkan transaksi satu-satu?** | “Masih jumlahkan transaksi satu-satu?” |
| 3–8 dtk | Tampilkan prompt di Gemini; sorot bahwa datanya fiktif. | **Minta Gemini pandu langkahnya** | “Minta Gemini jelaskan cara merangkum data—pakai contoh fiktif ini.” |
| 8–22 dtk | Di Google Sheets/Excel, pilih data lalu buat Pivot table. Tampilkan pengaturan field. | **Rows: Menu · Columns: Hari · Values: SUM Penjualan** | “Di spreadsheet, buat Pivot table. Taruh Menu di Rows, Hari di Columns, lalu SUM Penjualan di Values.” |
| 22–31 dtk | Tampilkan tabel ringkasan dan sorot satu hasil, misalnya Nasi Ayam pada Senin. | **Nasi Ayam, Senin = Rp24.000** | “Sekarang total per menu dan hari langsung terbaca. Nasi Ayam hari Senin: dua belas ribu dikali dua, jadi dua puluh empat ribu.” |
| 31–39 dtk | Cocokkan hasil ringkasan dengan data sumber, lalu tampilkan CTA. | **Cek hasilnya · Simpan untuk dicoba** | “Cek hasilnya dengan data sumber. Simpan, lalu coba dengan data latihanmu—tanpa data pribadi.” |

**Catatan penyuntingan:** Rekam layar aplikasi yang benar-benar digunakan dan pastikan nama menu mengikuti aplikasinya. Jangan tampilkan hasil seolah Gemini membuat pivot table langsung bila prosesnya dilakukan di spreadsheet.

## 4. Demo Gemini dan data sintetis

**Prompt siap ditempel:**

```text
Saya menggunakan Google Sheets. Berdasarkan data sintetis berikut, pandu saya membuat Pivot table untuk melihat total penjualan menurut menu dan hari. Sebutkan field yang diletakkan pada Rows, Columns, dan Values, serta cara memeriksa hasilnya terhadap data sumber. Jelaskan bahwa Values perlu diringkas dengan SUM untuk kolom Total Penjualan. Jangan mengklaim telah mengubah spreadsheet saya.

Hari | Menu | Qty | Harga Satuan (Rp) | Total Penjualan (Rp)
Senin | Nasi Ayam | 2 | 12000 | 24000
Senin | Es Teh | 3 | 5000 | 15000
Selasa | Nasi Ayam | 1 | 12000 | 12000
Selasa | Es Teh | 2 | 5000 | 10000
```

**Pengaturan Pivot table yang ditunjukkan di layar:**
- **Rows:** Menu
- **Columns:** Hari
- **Values:** SUM dari Total Penjualan (Rp)

**Hasil yang diharapkan:**

| Menu | Senin | Selasa | Total keseluruhan |
|---|---:|---:|---:|
| Nasi Ayam | Rp24.000 | Rp12.000 | Rp36.000 |
| Es Teh | Rp15.000 | Rp10.000 | Rp25.000 |
| **Total keseluruhan** | **Rp39.000** | **Rp22.000** | **Rp61.000** |

Periksa satu hasil dengan sumber: Nasi Ayam hari Senin = 2 × Rp12.000 = Rp24.000. Jumlah seluruh transaksi = Rp61.000. Jika spreadsheet menampilkan mata uang atau pemisah angka dengan format berbeda, nilainya tetap harus sama.

## 5. Naskah lisan lengkap

> “Masih jumlahkan transaksi satu-satu? Minta Gemini jelaskan cara merangkum data—pakai contoh fiktif ini. Di spreadsheet, buat Pivot table. Taruh Menu di Rows, Hari di Columns, lalu SUM Penjualan di Values. Sekarang total per menu dan hari langsung terbaca. Nasi Ayam hari Senin: dua belas ribu dikali dua, jadi dua puluh empat ribu. Cek hasilnya dengan data sumber. Simpan, lalu coba dengan data latihanmu—tanpa data pribadi.”

## 6. Caption Instagram siap unggah

```text
Masih menjumlahkan baris satu per satu? Ada cara yang lebih ringkas. 👀

Pivot table membantu mengelompokkan dan menjumlahkan data berdasarkan kategori. Di demo ini, kita merangkum penjualan kantin fiktif:

• Rows: Menu
• Columns: Hari
• Values: SUM Total Penjualan

Contoh: 2 Nasi Ayam × Rp12.000 = Rp24.000 untuk hari Senin. Hasil ringkasannya tetap perlu dicek dengan data sumber.

Gemini bisa memandu langkahnya; Pivot table dibuat di Google Sheets atau Excel. Simpan Reel ini dan coba dengan data latihanmu. Jangan masukkan data pribadi atau sensitif ke Gemini.

Kamu mau diringkaskan pakai pivot table: data survei, inventaris, atau anggaran proyek?

#StudyHack #PivotTable #GoogleSheets #Excel #LiterasiData #MahasiswaUB
```

**Catatan publikasi:** Pastikan tag akun seperti `@REFO Indonesia` hanya ditambahkan setelah akun resminya diverifikasi. Hindari tag yang belum dicek.

## 7. Checklist produksi

- [ ] Gunakan data sintetis yang sama dengan contoh di atas pada Gemini dan spreadsheet.
- [ ] Pastikan **Total Penjualan = Qty × Harga Satuan** sebelum membuat Pivot table.
- [ ] Tampilkan pengaturan Rows, Columns, dan Values dengan jelas dan benar.
- [ ] Verifikasi hasil pivot: Rp39.000 untuk Senin, Rp22.000 untuk Selasa, dan Rp61.000 total.
- [ ] Hindari klaim waktu atau hasil yang tidak diukur dalam demo.
- [ ] Jangan tampilkan data pribadi/sensitif; gunakan data sintetis dari awal hingga akhir.
- [ ] Periksa keterbacaan teks dan safe area Reel di layar ponsel.
