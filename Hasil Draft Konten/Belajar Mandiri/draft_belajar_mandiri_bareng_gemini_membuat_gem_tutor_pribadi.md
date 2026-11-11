# Episode 1 — Bikin Gem Tutor Pribadi di Gemini

**Pilar:** Study Hack  
**Format:** Reel vertikal 9:16  
**Audiens:** Mahasiswa UB lintas jurusan  
**Durasi rekomendasi:** 90–105 detik, termasuk CTA kampanye wajib  
**Tujuan:** Mengenalkan apa itu Gem, manfaatnya untuk belajar, dan cara membuat Gem tutor yang bisa dipakai berulang.

## Angle dan pesan utama

**Angle:** Daripada mengulang instruksi belajar setiap kali membuka chat, atur satu Gem sebagai tutor dengan gaya belajar yang kamu mau.

**Pesan utama:** Gem adalah versi Gemini yang dikustomisasi untuk tujuan tertentu. Dengan memberi nama dan instruksi khusus, mahasiswa bisa menyiapkan pendamping belajar yang konsisten untuk membantu memahami materi—bukan menggantikan usaha atau verifikasi sendiri.

**Batas klaim:** Fokus episode ini adalah fitur Gems. Jangan menyebut Gems sebagai Guided Learning atau menyamakan keduanya. Nama menu dan ketersediaan fitur dapat berbeda; rekam antarmuka yang benar-benar tersedia di akun produksi.

## Hook

**Narasi:** “Setiap belajar kamu harus ngasih instruksi yang sama ke Gemini? Bikin Gem tutor sekali, lalu pakai lagi kapan pun kamu belajar.”

**Teks layar:** “Punya tutor belajar versi kamu sendiri”

## Alur video dan storyboard

| Waktu | Visual dan aksi | Narasi | Teks layar / catatan produksi |
|---|---|---|---|
| 0–5 dtk | Mahasiswa membuka catatan kuliah, lalu tampak lelah mengetik instruksi panjang berulang kali. | “Setiap belajar kamu harus ngasih instruksi yang sama ke Gemini?” | “Jelasin pelan-pelan… kasih analogi… jangan langsung kasih jawaban…” |
| 5–13 dtk | Ia berhenti mengetik. Tampilan beralih ke screen-record Gemini asli dan menu Gems yang tersedia pada akun. | “Kenalan sama Gems: kamu bisa mengatur Gemini jadi asisten khusus untuk kebutuhan tertentu.” | Tampilkan menu dan label yang benar-benar ada. Jangan buat UI tiruan. |
| 13–20 dtk | Screen-record membuka pembuatan Gem baru. | “Yuk bikin dari awal. Pertama, kasih nama dan deskripsi supaya fungsi Gem-mu langsung jelas.” | Tampilkan proses di antarmuka asli; nama dan deskripsi ada di bawah. |
| 20–29 dtk | Isi kolom nama “Teman Belajar” dan deskripsinya. | “Namanya Teman Belajar. Deskripsinya: pendamping belajar yang membantumu memahami materi secara bertahap.” | Pastikan kedua kolom terbaca di screen-record. |
| 29–43 dtk | Isi kolom Instructions dengan arahan tutor. | “Di instruksi, tentukan gaya jawabnya: jelaskan sederhana, pakai analogi, tanya dulu, lalu beri umpan balik.” | Tampilkan instruksi utuh atau sorot bagian penting saat proses pengisian; jangan hanya menampilkan chat prompt. |
| 43–52 dtk | Buka bagian Knowledge dan unggah file catatan kuliah yang benar-benar dipakai sebagai sumber demo. | “Nah, di Knowledge, tambahkan materi kuliah yang jadi pegangan Gem—misalnya PDF catatan yang boleh kamu bagikan.” | Tampilkan pemilihan dan status file berhasil ditambahkan. Gunakan materi nonrahasia; jangan mengarang file atau mengklaim file terunggah jika belum. |
| 52–59 dtk | Simpan Gem, buka Gem yang baru dibuat, lalu mulai chat tentang topik dalam materi. | “Simpan, lalu coba tanyakan satu konsep dari materi yang kamu unggah.” | Tampilkan alur nyata; sesuaikan nama tombol dengan UI akun. |
| 59–68 dtk | Perlihatkan potongan respons asli Gem. Visual penjelasan Remotion mengikuti analogi/konsep yang benar-benar muncul di respons; lalu tampilkan mahasiswa menjawab pertanyaan Gem dan mengecek materi sumber. | “Perhatikan penjelasan Gem ini. Visualnya membantu kita membayangkan konsep yang dijelaskan—dan jawabannya tetap kita cek ke materi.” | Gunakan cuplikan respons nyata yang sudah diverifikasi. Sinkronkan teks, narasi, dan animasi Remotion dengan cuplikan itu. |
| 68–100 dtk | Shot stabil dengan ruang untuk QR asli dan teks. Sisipkan CTA lisan lengkap; jangan mempercepat atau memotongnya. | Bacakan CTA wajib di bawah secara utuh. | QR dan tautan hanya ditambahkan saat editing dan harus diuji sebelum publikasi. |

## Demo Gem

Isi empat bagian berikut saat membuat Gem. Label dan urutan menu dapat berbeda di akun yang digunakan.

**Nama**

```text
Teman Belajar
```

**Deskripsi**

```text
Pendamping belajar yang membantu mahasiswa memahami materi kuliah secara bertahap dengan penjelasan sederhana, analogi, dan latihan pemahaman berdasarkan materi yang ditambahkan.
```

**Instructions / Instruksi**

```text
Kamu adalah Teman Belajar, pendamping belajar untuk mahasiswa. Bantu saya memahami materi, bukan mengerjakan tugas untuk saya. Gunakan file yang ditambahkan di bagian Knowledge sebagai rujukan utama untuk pertanyaan tentang materi tersebut. Jika relevan, sebutkan nama file atau bagian yang menjadi dasar jawaban. Jangan mengarang isi file atau sumber. Jika jawabannya tidak ditemukan di Knowledge, katakan dengan jelas dan minta saya mengecek catatan atau sumber tepercaya. Mulai dengan menanyakan tingkat pemahaman dan tujuan belajar saya. Jelaskan satu gagasan dalam satu waktu dengan bahasa sederhana dan analogi yang relevan; beri tahu saya jika analoginya punya batas. Setelah menjelaskan, ajukan satu pertanyaan pemahaman dan tunggu jawaban saya. Beri umpan balik yang spesifik, luruskan kekeliruan dengan sopan, lalu lanjutkan bertahap. Jangan langsung memberi jawaban lengkap sebelum saya mencoba.
```

**Knowledge**

Tambahkan satu file materi kuliah yang memang digunakan untuk demo, misalnya PDF catatan kuliah tentang topik yang akan ditanyakan. Pilih file yang boleh dibagikan dan tidak memuat data pribadi. Jangan menganggap Knowledge sebagai teks instruksi: instruksi Gem menjelaskan bagaimana Gem bekerja, sedangkan Knowledge adalah bahan rujukan yang diunggah.

**Prompt uji setelah Gem disimpan:**

```text
Aku sedang belajar [NAMA TOPIK YANG BENAR-BENAR ADA DI FILE KNOWLEDGE]. Berdasarkan file Knowledge yang sudah aku tambahkan, jelaskan satu konsep inti dengan bahasa sederhana. Sebutkan nama file atau bagian yang kamu jadikan rujukan. Kalau konsep ini cocok dianalogikan, berikan satu analogi dan jelaskan batas analoginya. Setelah itu ajukan satu pertanyaan pemahaman yang jawabannya tidak langsung kamu berikan. Tunggu jawabanku.
```

Pilih topik yang cukup spesifik dan pastikan namanya memang muncul di dokumen sumber. Jangan isi placeholder dengan materi yang tidak ada di Knowledge. Setelah Gem bertanya, jawab pertanyaannya untuk menguji apakah Gem memberi umpan balik sesuai instruksi:

```text
[JAWAB PERTANYAAN GEM DENGAN PEMAHAMANMU SENDIRI]
```

Tampilkan respons asli, jawaban mahasiswa, umpan balik Gem, dan pemeriksaan singkat ke file sumber. Jika unggahan file atau fiturnya tidak tersedia di akun produksi, jangan merekayasa tampilan; konfirmasi alur yang tersedia sebelum syuting.

## Instruksi produksi Remotion

Gunakan instruksi ini saat membuat segmen video yang memvisualisasikan jawaban Gem:

```text
Buat segmen Remotion vertikal 9:16 yang menjelaskan SATU potongan respons nyata dari Gem Teman Belajar. Sumbernya adalah screen-record dan transkrip respons Gem yang sudah diverifikasi terhadap file Knowledge terlampir; jangan menulis respons Gemini baru atau mengubah makna kutipannya.

Pertahankan urutan ini:
1. Tampilkan cuplikan screen-record Gemini asli sebagai bukti respons, dengan teks yang tetap terbaca.
2. Ambil satu gagasan atau analogi yang memang tertulis di respons. Tampilkan kutipan pendek secara persis sebagai teks layar.
3. Buat animasi Remotion yang menerjemahkan gagasan/analogi tersebut menjadi visual sederhana. Narasi harus menjelaskan gagasan yang sama dan tidak menambahkan fakta baru.
4. Kembali ke potongan respons atau file Knowledge untuk menunjukkan dasar penjelasannya.

Gunakan placeholder [SCREEN_RECORD_GEM_ASLI], [KUTIPAN_RESPONS_PERSIS], [GAGASAN/ANALOGI_DARI_RESPONS], dan [RUJUKAN_FILE_KNOWLEDGE] hanya sebagai placeholder produksi; ganti dengan materi nyata sebelum render. Jangan membuat UI Gemini, chat, kutipan, angka, sumber, atau klaim yang tidak ada pada rekaman dan file. Jangan menyiratkan bahwa animasi adalah gambar atau video yang dihasilkan Gemini: animasi adalah visualisasi editorial yang dibuat di Remotion.

Jika respons terlalu panjang, pilih satu bagian pendek tanpa mengubah kalimatnya dan jangan menghilangkan konteks yang mengubah arti. Jika respons keliru, tidak didukung file Knowledge, atau tidak cocok divisualisasikan secara akurat, jangan poles menjadi seolah benar: ulangi demo dengan pertanyaan/instruksi yang lebih tepat, verifikasi hasil baru, lalu gunakan respons yang sudah benar. Gunakan transisi sederhana, teks ringkas, dan beri waktu baca yang cukup.
```

**Bahan yang disiapkan editor:** screen-record asli saat prompt uji ditempel dan Gem menjawab; transkrip respons persis; nama file Knowledge dan bagian yang mendukungnya; kutipan pendek yang dipilih; serta storyboard visual Remotion yang memetakan setiap kalimat narasi ke bagian respons dan materi sumber. Jangan mulai animasi penjelasan sebelum respons final dipilih dan diverifikasi.

## Naskah lisan

“Setiap belajar kamu harus ngasih instruksi yang sama ke Gemini? Kenalan sama Gems: kamu bisa mengatur Gemini jadi asisten khusus untuk kebutuhan tertentu. Yuk bikin Gem Teman Belajar. Isi namanya, tulis deskripsi singkat, lalu atur instruksinya supaya dia menjelaskan dengan sederhana dan menguji pemahamanmu. Di bagian Knowledge, tambahkan catatan kuliah yang jadi bahan rujukan. Simpan dan coba tanyakan konsep dari materi itu. Perhatikan penjelasan Gem ini, lalu lihat visualisasinya. Gem membantu kamu belajar bertahap, tapi tetap cek jawabannya ke sumber asli.”

**CTA lisan wajib — bacakan persis dan utuh:**

```text
Jangan lupa follow Instagram @geminiacademybyrefo untuk info dan hacks AI seru lainnya!
Untuk mencoba lebih lanjut hacks-hacks ini, kalian bisa buka link ini: https://bit.ly/belajarmandirigemini, dan bisa taruh QR-nya: https://drive.google.com/file/d/1tWnHjuzW36vvRbQH0i-tyKi_Gq9yE_9k/view?usp=sharing.
Dan pastikan kalian mengisi daftar hadir Festival di: bit.ly/belajarmandirigemini
```

## Caption

```text
Jangan lupa follow Instagram @geminiacademybyrefo untuk info dan hacks AI seru lainnya!
Untuk mencoba lebih lanjut hacks-hacks ini, buka https://bit.ly/belajarmandirigemini dan gunakan QR: https://drive.google.com/file/d/1tWnHjuzW36vvRbQH0i-tyKi_Gq9yE_9k/view?usp=sharing.
Isi daftar hadir Festival di: bit.ly/belajarmandirigemini

Pernah mengulang instruksi yang sama setiap kali belajar bareng Gemini? Dengan Gems, kamu bisa mengatur asisten khusus sesuai kebutuhan—misalnya Gem Teman Belajar yang menjelaskan bertahap dan menguji pemahamanmu. Atur instruksinya, coba di topik kuliahmu, lalu sesuaikan dengan gaya belajarmu. Tetap cek fakta penting ke catatan atau sumber tepercaya.

@REFO Indonesia
#GeminiAcademy #GeminiAcademyUB
```

## Checklist sebelum publikasi

- [ ] Rekam alur Gems dan label menu dari akun yang benar-benar digunakan; sesuaikan jika antarmukanya berbeda.
- [ ] Tampilkan pengisian nama, deskripsi, instruksi, serta unggah file Knowledge dalam screen-record nyata.
- [ ] Pastikan file Knowledge boleh dibagikan, berhasil ditambahkan, dan benar-benar menjadi sumber pertanyaan demo.
- [ ] Ganti placeholder pada prompt uji dengan topik yang memang tercantum di file Knowledge; rekam prompt dan respons nyata.
- [ ] Visual Remotion dan narasi penjelasan mengikuti respons Gem yang nyata dan sudah dicek ke file Knowledge; jangan membuat jawaban, UI, atau klaim baru.
- [ ] Gunakan respons Gemini yang benar-benar dihasilkan dan cek akurasinya.
- [ ] Jangan menjanjikan Gem selalu benar atau menggantikan dosen, sumber, maupun proses belajar.
- [ ] Uji tautan dan QR; pastikan daftar hadir Festival sudah benar.
- [ ] Sisakan waktu yang cukup untuk membacakan CTA wajib dengan jelas.
