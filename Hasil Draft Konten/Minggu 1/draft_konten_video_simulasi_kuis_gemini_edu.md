# SPEC & STORYBOARD: Ubah Catatan Dosen Menjadi Simulasi Kuis Interaktif via Gemini (Edu Version)

Dokumen ini dirancang sebagai panduan skrip sekaligus prompt arsitektur video untuk diproses oleh **Antigravity** ke dalam kode animasi **Remotion**.

---

## 1. Metadata Proyek Remotion

- **Format**: Video Vertikal (9:16) – Instagram Reels / TikTok / YouTube Shorts
- **Resolusi**: $1080 \times 1920$ px
- **Frame Rate (FPS)**: 30 FPS
- **Target Durasi**: 60 Detik (1800 frames)
- **Tema Visual**: Modern Tech & Academic Aesthetics (Google Workspace Edu dark/light blend, gradien khas Gemini: `#4285F4`, `#9B72CB`, `#D96570`, background clean `#0F172A`)
- **Tipografi**: Inter / Plus Jakarta Sans / Fira Code (untuk box prompt)

---

## 2. Struktur Token Desain (Untuk Komponen Remotion)

```json
{
  "colors": {
    "background": "#0B0F19",
    "surface": "#1E293B",
    "surfaceBorder": "#334155",
    "primary": "#4F46E5",
    "geminiGradient": "linear-gradient(135deg, #4285F4 0%, #9B72CB 50%, #D96570 100%)",
    "textMain": "#F8FAFC",
    "textMuted": "#94A3B8",
    "accentGreen": "#10B981",
    "accentAmber": "#F59E0B"
  },
  "fonts": {
    "heading": "Plus Jakarta Sans, sans-serif",
    "body": "Inter, sans-serif",
    "code": "Fira Code, monospace"
  }
}
```

---

## 3. Breakdown Scene & Storyboard (Frame-by-Frame)

### Scene 1: The Hook (0 - 5 Detik | Frame 0 - 150)
* **Tujuan**: Menangkap atensi mahasiswa yang sedang panik menghadapi pekan ujian (UTS/UAS).
* **Visual Direction**:
  - Teks bold muncul dengan animasi spring (`spring({ frame, fps })`).
  - Animasi tumpukan PDF slide dosen berhamburan dengan label "500 Halaman", "Slide Dosen", "Minggu Depan UAS".
  - Transisi cepat glitch/zoom ke smartphone screen.
* **On-Screen Text (OST)**:
  - `"H-3 UJIAN TAPI CATATAN MASIH NUMPUK?"`
  - `"Jangan cuma dibaca, pasti lupa!"`
* **Voiceover (VO)**:
  > *"H-3 ujian tapi slide dan catatan dosen masih numpuk ratusan halaman? Kalau cuma kamu baca ulang, dijamin pas hari H bakal nge-blank!"*
* **SFX**: Whoosh cepat, book drop thud, alarm/tension tick.

---

### Scene 2: The Solution – Gemini Akun Kampus / Edu (5 - 15 Detik | Frame 150 - 450)
* **Tujuan**: Mengedukasi keuntungan menggunakan akun kampus (`.ac.id` / Google Workspace for Education).
* **Visual Direction**:
  - Mockup UI browser menampilkan halaman login Gemini.
  - Avatar user beralih ke domain `nama@kampus.ac.id`.
  - Muncul badge bercahaya: **"Gemini with Enterprise/Edu Data Protection"**.
  - Poin keunggulan muncul sequential:
    1. Konteks dokumen super panjang (muat puluhan PDF materi).
    2. Data catatan kampus aman (tidak dipakai melatih model publik).
* **On-Screen Text (OST)**:
  - `"Pakai Gemini Akun Kampus (.ac.id)"`
  - `"Kapasitas Dokumen Besar + Privasi Terjamin"`
* **Voiceover (VO)**:
  > *"Sini triknya: Manfaatin Gemini dengan akun kampus berakhiran .ac.id kamu. Fitur edukasi ini bisa membaca dokumen super panjang tanpa khawatir catatan kuliahmu bocor ke publik."*
* **SFX**: UI pop sound, badge chime.

---

### Scene 3: Step 1 & 2 – Upload & Setup Bahan Kuliah (15 - 28 Detik | Frame 450 - 840)
* **Tujuan**: Menunjukkan betapa mudahnya mengunggah berbagai format materi.
* **Visual Direction**:
  - Animasi drag-and-drop file ke dalam prompt bar Gemini.
  - File tags muncul melayang: `Slide_Pertemuan1-7.pdf`, `Rangkuman_Dosen.docx`, `Foto_Catatan.jpg`.
  - Indikator loading bar berputar halus lalu berubah menjadi checklist hijau.
* **On-Screen Text (OST)**:
  - `"Langkah 1: Upload Semua Materi Kuliah"`
  - `"Support: PDF, PPTX, Doc, bahkan foto catatan tangan!"`
* **Voiceover (VO)**:
  > *"Langkah pertama, buka Gemini dan login pakai email kampusmu. Klik ikon tambah lampiran, lalu drop semua materi kuliah: slide dosen, rangkuman, bahkan foto coretan catatan tangan sekalipun."*
* **SFX**: Mouse click, swoosh upload, subtle chime.

---

### Scene 4: Step 3 – The Magic Prompt (28 - 43 Detik | Frame 840 - 1290)
* **Tujuan**: Memberikan template prompt yang terbukti efektif (bukan sekadar minta kuis, tapi simulasi interaktif step-by-step).
* **Visual Direction**:
  - Animasi typing effect ke dalam UI Gemini chatbox.
  - Syntax highlighting di bagian peran dosen, model soal, dan metode satu per satu.
  - Tombol "Copy Prompt" bercahaya di sudut layar.
* **On-Screen Text (OST)**:
  - `"Langkah 2: Gunakan Prompt Simulasi Dosen Penguji"`
  - Highlight kata kunci: `Roleplay Dosen`, `Soal 1 per 1`, `Evaluasi & Feedback`.
* **Voiceover (VO)**:
  > *"Langkah kedua, masukkan prompt magis ini. Jangan cuma minta 'buatkan soal', tapi suruh Gemini berperan sebagai dosen penguji killer yang ngasih soal satu per satu, nunggu jawabanmu, baru ngasih feedback dan skor!"*
* **SFX**: Mechanical keyboard typing, soft digital confirmation bell.

---

### Scene 5: Step 4 – Live Simulation in Action (43 - 53 Detik | Frame 1290 - 1590)
* **Tujuan**: Menunjukkan interaksi tanya jawab aktif dan feedback edukatif.
* **Visual Direction**:
  - Chat bubble Gemini: Mengeluarkan Soal Kasus (Pertanyaan 1).
  - Chat bubble User: Mengetik jawaban singkat.
  - Chat bubble Gemini: Evaluasi instan:
    - `"Skor: 8/10"`
    - `"Kelebihan: Konsep A tepat"`
    - `"Koreksi: Masih melewatkan regulasi B..."`
    - `"Lanjut ke Soal 2?"`
* **On-Screen Text (OST)**:
  - `"Simulasi Real-time: Langsung Tahu Di Mana Lemahmu"`
* **Voiceover (VO)**:
  > *"Liat hasilnya: Begitu kamu jawab, Gemini langsung bedah bagian mana konsep yang kamu kuasai, dan bagian mana yang masih bolong sebelum lanjut ke soal berikutnya."*
* **SFX**: Message pop, bubble send, subtle celebratory ping.

---

### Scene 6: Outro & Call to Action (53 - 60 Detik | Frame 1590 - 1800)
* **Tujuan**: Mendorong engagement dan penyimpanan konten.
* **Visual Direction**:
  - Tampilan kartu ringkas dengan template prompt siap copy.
  - Ikon Bookmark / Save beranimasi membesar (bounce effect).
  - Teks ajakan bertindak & handle akun kreator.
* **On-Screen Text (OST)**:
  - `"Save video ini & Coba malam ini!"`
  - `"Prompt lengkap ada di caption / komentar 👇"`
* **Voiceover (VO)**:
  > *"Simpan video ini sekarang juga buat bahan belajar nanti malam, dan share ke temen sekelompokmu biar lulus ujian bareng!"*
* **SFX**: Deep sub-bass whoosh, pop bell notification.

---

## 4. Master Prompt Template (Asset untuk Teks Layar & Caption)

Berikut teks prompt presisi yang ditampilkan dalam video dan dapat disematkan pada komponen Remotion:

```text
Bertindaklah sebagai Dosen Penguji senior untuk mata kuliah berdasarkan dokumen yang saya lampirkan. 

Tugasmu:
1. Buat simulasi ujian interaktif sebanyak 5 soal esai analitis tingkat lanjut (HOTS).
2. BERIKAN SOAL SATU PER SATU. Jangan keluarkan soal berikutnya sebelum saya memberikan jawaban.
3. Setelah saya menjawab tiap soal:
   - Berikan penilaian (skor 1-100).
   - Tunjukkan konsep yang sudah tepat dan bagian yang masih salah/kurang lengkap berdasarkan materi.
   - Jelaskan jawaban ideal secara ringkas.
4. Setelah itu, baru ajukan soal berikutnya.

Jika kamu paham, sapa saya sebagai mahasiswa bimbinganmu dan mulai dengan Pertanyaan 1!
```

---

## 5. Instruksi Teknis untuk Eksekusi Antigravity (Remotion Code Generator)

Gunakan arahan berikut saat mengonversi storyboard ini menjadi file `Root.tsx` dan `Composition.tsx`:

1. **Komposisi Modular**:
   - Buat folder `src/scenes/` berisi komponen terpisah: `HookScene.tsx`, `EduFeatureScene.tsx`, `UploadScene.tsx`, `PromptScene.tsx`, `QuizDemoScene.tsx`, dan `OutroScene.tsx`.
   - Satukan semua scene di `MainComposition.tsx` menggunakan tag `<Sequence>` dengan offset frame yang telah ditentukan di atas.

2. **Animasi & Transisi**:
   - Manfaatkan fungsi `interpolate` dan `spring` dari `@remotion/core` untuk setiap elemen teks dan kartu mockup.
   - Hindari transisi hard-cut tanpa motion: gunakan `fade` atau `slide-up` dengan damping $12$ dan stiffness $90$.

3. **Komponen UI Mockup**:
   - Bangun komponen `GeminiChatBubble.tsx` yang mendukung props `sender: 'gemini' | 'user'`, `message: string`, dan `scoreBadge?: string`.
   - Bangun komponen `TypingPromptBox.tsx` yang menggunakan `frame` untuk menghitung substring teks yang dirender seolah-olah sedang diketik secara live.