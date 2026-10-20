import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "referensi_design_carousel" / "brand-assets"
WIDTH, HEIGHT = 1080, 1350
INK = "#202124"
CREAM = "#FFF8DD"
BLUE = "#1599E8"
GREEN = "#08B956"
CORAL = "#F04C5A"
YELLOW = "#F5CC22"
WHITE = "#FFFFFF"
PALE_GREEN = "#E5F5E8"
PALE_BLUE = "#E5F2FF"
PALE_CORAL = "#FFE7E7"
PALE_YELLOW = "#FFF1B7"
FONT_DIR = ASSET_DIR / "Font - Inter" / "static"


SLIDES = [
    {
        "layout": "cover",
        "eyebrow": "SAVE TIME  /  PANDUAN KULIAH",
        "title": "Matriks belajar\nanti-burnout",
        "subtitle": "Biar tahu mulai dari mana, tanpa mengorbankan waktu istirahat.",
        "accent": GREEN,
    },
    {
        "layout": "problem",
        "eyebrow": "KALAU SENIN TERASA BERAT...",
        "title": "Semua terasa harus dikerjakan sekarang.",
        "items": [
            "Review materi kelas atau selesaikan tugas dulu?",
            "Tugas menumpuk, materi baru terus berdatangan.",
            "Ada rapat sore, tapi energi sudah habis.",
        ],
        "note": "Akhirnya bingung memilih, lalu menunda semuanya.",
        "accent": CORAL,
    },
    {
        "layout": "matrix",
        "eyebrow": "CARI URUTAN, BUKAN TAMBAH JAM",
        "title": "Pisahkan yang mendesak dari yang penting.",
        "quadrants": [
            ("KERJAKAN", "Penting + mendesak", PALE_CORAL),
            ("JADWALKAN", "Penting, belum mendesak", PALE_BLUE),
            ("DELEGASIKAN", "Mendesak, kurang penting", PALE_YELLOW),
            ("BATASI", "Tidak mendesak dan kurang penting", PALE_GREEN),
        ],
        "note": "Pakai sebagai panduan awal, lalu sesuaikan dengan kondisi dan tenggatmu.",
        "accent": BLUE,
    },
    {
        "layout": "prompt",
        "eyebrow": "COBA LANGSUNG DI GEMINI",
        "title": "Mulai dari prompt ini",
        "prompt": (
            "Bantu saya menyusun jadwal belajar mingguan berdasarkan prioritas. "
            "Daftar mata kuliah dan deadline: [isi di sini]. Buat sesi fokus "
            "maksimal 90 menit, sertakan jeda, dan sisakan waktu untuk kegiatan "
            "organisasi setiap sore atau malam."
        ),
        "note": "Tambahkan jam kuliah dan waktu paling produktifmu. Jangan masukkan data pribadi.",
        "accent": CORAL,
    },
    {
        "layout": "planner",
        "eyebrow": "CONTOH ILUSTRATIF — SESUAIKAN LAGI",
        "title": "Jadwal yang realistis punya ruang bernapas.",
        "events": [
            ("SENIN", "15.30", "Tugas Analisis Data", CORAL),
            ("SENIN", "17.00", "Istirahat + rapat organisasi", GREEN),
            ("SELASA", "09.00", "Review materi kuliah", BLUE),
            ("SELASA", "MALAM", "Waktu bebas / hobi", YELLOW),
        ],
        "note": "Contoh ini simulasi, bukan hasil live dari Gemini.",
        "accent": GREEN,
    },
    {
        "layout": "closing",
        "eyebrow": "MULAI MINGGU INI",
        "title": "Belajar terarah. Istirahat tetap jalan.",
        "items": [
            "Urutkan tugas dari urgensi dan dampaknya.",
            "Buat sesi fokus, lalu sisipkan jeda.",
            "Minta Gemini bantu menyusun — kamu tetap yang memutuskan.",
        ],
        "cta": "Simpan untuk dicoba awal minggu, lalu kirim ke temanmu.",
        "accent": BLUE,
    },
]


def _font(size, weight="Regular"):
    filename = FONT_DIR / f"Inter_18pt-{weight}.ttf"
    if not filename.is_file():
        raise FileNotFoundError(f"Font Inter tidak ditemukan: {filename}")
    return ImageFont.truetype(str(filename), size)


def _rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def _wrap(draw, text, font, max_width):
    lines = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if current and draw.textbbox((0, 0), candidate, font=font)[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def _text_block(draw, text, xy, font, fill, max_width, line_gap=12, max_lines=None):
    x, y = xy
    lines = _wrap(draw, text, font, max_width)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines[-1] and draw.textbbox(
            (0, 0), lines[-1] + "...", font=font
        )[2] > max_width:
            lines[-1] = lines[-1][:-1]
        lines[-1] = lines[-1].rstrip() + "..."
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += draw.textbbox((0, 0), line or "Ag", font=font)[3] + line_gap
    return y


def _header(image, index, total, eyebrow, accent, dark=False):
    draw = ImageDraw.Draw(image)
    logo_path = ASSET_DIR / "Gemini Academy Logo@2x-8.png"
    with Image.open(logo_path) as logo:
        logo = logo.convert("RGBA")
        logo.thumbnail((390, 58), Image.Resampling.LANCZOS)
        image.alpha_composite(logo, (72, 48))
    draw.text((905, 60), f"{index:02}/{total:02}", font=_font(27, "Bold"), fill=INK)
    _rounded(draw, (72, 137, 72 + min(500, max(240, len(eyebrow) * 15)), 184), 22, accent)
    draw.text((94, 147), eyebrow, font=_font(19, "Bold"), fill=INK if accent == YELLOW else WHITE)
    draw.line((72, 210, 1008, 210), fill="#E6DEBE", width=2)


def _mascot_panel(image, box, radius=34):
    path = ASSET_DIR / "Main Character.png"
    with Image.open(path) as source:
        mascot = source.convert("RGBA")
    x1, y1, x2, y2 = box
    target_w, target_h = x2 - x1, y2 - y1
    scale = min(target_w / mascot.width, target_h / mascot.height)
    mascot = mascot.resize(
        (round(mascot.width * scale), round(mascot.height * scale)),
        Image.Resampling.LANCZOS,
    )
    panel = Image.new("RGBA", (target_w, target_h), "#681C29")
    panel_draw = ImageDraw.Draw(panel)
    panel_draw.rounded_rectangle((0, 0, target_w - 1, target_h - 1), radius=radius, fill="#681C29")
    offset = ((target_w - mascot.width) // 2, (target_h - mascot.height) // 2)
    panel.alpha_composite(mascot, offset)
    mask = Image.new("L", (target_w, target_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, target_w - 1, target_h - 1), radius=radius, fill=255)
    image.paste(panel, (x1, y1), mask)
    ImageDraw.Draw(image).rounded_rectangle(box, radius=radius, outline=YELLOW, width=8)


def _cover(image, slide):
    draw = ImageDraw.Draw(image)
    draw.ellipse((765, 220, 1190, 650), fill=PALE_GREEN)
    draw.ellipse((-160, 1070, 260, 1490), fill=PALE_BLUE)
    _text_block(draw, slide["title"], (78, 270), _font(78, "ExtraBold"), INK, 610, 5)
    _rounded(draw, (78, 584, 492, 649), 24, slide["accent"])
    draw.text((104, 599), "ATUR PRIORITAS", font=_font(25, "Bold"), fill=WHITE)
    _text_block(draw, slide["subtitle"], (82, 695), _font(31, "Regular"), INK, 485, 14)
    _mascot_panel(image, (570, 637, 972, 1164), 38)
    draw.text((82, 1190), "Geser untuk mulai menyusun minggu.", font=_font(24, "SemiBold"), fill=INK)
    draw.line((82, 1244, 440, 1244), fill=slide["accent"], width=10)


def _problem(image, slide):
    draw = ImageDraw.Draw(image)
    draw.ellipse((780, 240, 1130, 590), fill=PALE_CORAL)
    _text_block(draw, slide["title"], (82, 260), _font(61, "ExtraBold"), INK, 850, 8)
    colors = [PALE_BLUE, PALE_YELLOW, PALE_GREEN]
    for index, item in enumerate(slide["items"], 1):
        y = 535 + (index - 1) * 176
        x = 92 + (index % 2) * 34
        _rounded(draw, (x, y, 970, y + 132), 30, colors[index - 1])
        draw.ellipse((x + 20, y + 22, x + 92, y + 94), fill=slide["accent"])
        draw.text((x + 45, y + 34), str(index), font=_font(31, "Bold"), fill=WHITE)
        _text_block(draw, item, (x + 116, y + 28), _font(28, "SemiBold"), INK, 690, 9, 2)
    _rounded(draw, (120, 1095, 960, 1214), 28, INK)
    _text_block(draw, slide["note"], (158, 1124), _font(27, "SemiBold"), WHITE, 760, 8, 2)


def _matrix(image, slide):
    draw = ImageDraw.Draw(image)
    _text_block(draw, slide["title"], (78, 252), _font(56, "ExtraBold"), INK, 900, 8)
    left, top, gap, cell_w, cell_h = 80, 505, 20, 440, 225
    draw.text((185, 464), "MENDESAK", font=_font(19, "Bold"), fill=INK)
    draw.text((642, 464), "TIDAK MENDESAK", font=_font(19, "Bold"), fill=INK)
    for index, (label, desc, color) in enumerate(slide["quadrants"]):
        col, row = index % 2, index // 2
        x = left + col * (cell_w + gap)
        y = top + row * (cell_h + gap)
        _rounded(draw, (x, y, x + cell_w, y + cell_h), 28, color)
        draw.text((x + 26, y + 26), f"0{index + 1}", font=_font(22, "Bold"), fill=slide["accent"])
        _text_block(draw, label, (x + 26, y + 75), _font(34, "ExtraBold"), INK, cell_w - 50, 4, 2)
        _text_block(draw, desc, (x + 26, y + 157), _font(20, "Regular"), INK, cell_w - 50, 6, 2)
    _rounded(draw, (80, 1080, 1000, 1210), 28, slide["accent"])
    _text_block(draw, slide["note"], (116, 1110), _font(25, "SemiBold"), WHITE, 840, 8, 2)


def _prompt(image, slide):
    draw = ImageDraw.Draw(image)
    _text_block(draw, slide["title"], (84, 266), _font(64, "ExtraBold"), INK, 830, 8)
    draw.text((52, 435), "“", font=_font(180, "ExtraBold"), fill=slide["accent"])
    _rounded(draw, (116, 470, 964, 1000), 34, WHITE, outline="#E5DDBE", width=3)
    _text_block(draw, slide["prompt"], (158, 520), _font(34, "Regular"), INK, 760, 15, 8)
    _rounded(draw, (117, 1035, 963, 1178), 26, PALE_BLUE)
    _text_block(draw, slide["note"], (153, 1065), _font(24, "SemiBold"), INK, 770, 8, 3)
    draw.text((796, 1213), "PROMPT / 01", font=_font(20, "Bold"), fill=slide["accent"])


def _planner(image, slide):
    draw = ImageDraw.Draw(image)
    _text_block(draw, slide["title"], (80, 258), _font(57, "ExtraBold"), INK, 870, 8)
    _rounded(draw, (88, 455, 990, 1066), 32, WHITE, outline="#E6DEBE", width=3)
    draw.text((126, 490), "MINGGU INI", font=_font(22, "Bold"), fill="#6B6B62")
    for index, (day, time, event, color) in enumerate(slide["events"]):
        y = 560 + index * 112
        draw.line((126, y + 76, 950, y + 76), fill="#EEE9D9", width=2)
        draw.text((130, y + 4), day, font=_font(18, "Bold"), fill="#6B6B62")
        draw.text((267, y + 4), time, font=_font(22, "Bold"), fill=INK)
        _rounded(draw, (388, y - 8, 923, y + 60), 20, color)
        _text_block(draw, event, (410, y + 6), _font(22, "SemiBold"), INK, 480, 5, 2)
    _rounded(draw, (90, 1110, 990, 1212), 24, PALE_YELLOW)
    _text_block(draw, slide["note"], (122, 1138), _font(23, "SemiBold"), INK, 820, 6, 2)


def _closing(image, slide):
    draw = ImageDraw.Draw(image)
    draw.ellipse((760, 227, 1155, 620), fill=PALE_BLUE)
    _text_block(draw, slide["title"], (78, 275), _font(64, "ExtraBold"), INK, 830, 7)
    for index, item in enumerate(slide["items"], 1):
        y = 570 + (index - 1) * 144
        _rounded(draw, (94, y, 974, y + 112), 28, WHITE, outline="#E8DFBE", width=3)
        draw.ellipse((118, y + 20, 190, y + 92), fill=YELLOW)
        draw.text((142, y + 31), str(index), font=_font(29, "Bold"), fill=INK)
        _text_block(draw, item, (220, y + 22), _font(26, "SemiBold"), INK, 715, 7, 2)
    _rounded(draw, (92, 1043, 988, 1193), 30, slide["accent"])
    _text_block(draw, slide["cta"], (132, 1078), _font(29, "Bold"), WHITE, 820, 8, 3)
    draw.text((786, 1223), "GEMINI ACADEMY UB", font=_font(19, "Bold"), fill=INK)


LAYOUTS = {
    "cover": _cover,
    "problem": _problem,
    "matrix": _matrix,
    "prompt": _prompt,
    "planner": _planner,
    "closing": _closing,
}


def render_carousel(slides, output_dir):
    if not slides:
        raise ValueError("Carousel harus berisi minimal satu slide.")
    for slide in slides:
        if slide.get("layout") not in LAYOUTS:
            raise ValueError(f"Layout tidak dikenal: {slide.get('layout')}")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for index, slide in enumerate(slides, 1):
        image = Image.new("RGBA", (WIDTH, HEIGHT), CREAM)
        draw = ImageDraw.Draw(image)
        _header(image, index, len(slides), slide["eyebrow"], slide["accent"])
        LAYOUTS[slide["layout"]](image, slide)
        output_path = output_dir / f"slide-{index:02}-{slide['layout']}.png"
        image.convert("RGB").save(output_path, optimize=True)
    return output_dir


def main():
    parser = argparse.ArgumentParser(description="Render trial carousel matriks belajar.")
    parser.add_argument(
        "--output",
        type=Path,
        default=BASE_DIR / "Hasil Desain Carousel" / "trial_matriks_belajar_flexible",
        help="Folder output slide PNG.",
    )
    args = parser.parse_args()
    output_dir = render_carousel(SLIDES, args.output)
    print(f"{len(SLIDES)} slide selesai dibuat di: {output_dir}")


if __name__ == "__main__":
    main()
