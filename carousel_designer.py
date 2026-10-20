import argparse
import json
import os
import shutil
import struct
import subprocess
import tempfile
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "referensi_design_carousel" / "brand-assets"
TEMPLATE_PATH = BASE_DIR / "carousel_template.html"
WIDTH, HEIGHT = 1080, 1350


SLIDES = [
    {
        "layout": "cover",
        "title": "Bingung Mau Kerjain Tugas Dulu atau Review Materi?",
        "swipe": "Swipe buat tahu caranya",
    },
    {
        "layout": "problem",
        "items": [
            "Mau review materi kelas tadi pagi, tapi tugas minggu lalu belum beres.",
            "Mau ngerjain tugas, tapi materinya belum sempat dipelajari.",
        ],
        "note": "Akhirnya malah procrastinating dan sistem kebut semalam. Relate?",
        "swipe": "Swipe buat lanjut ke solusi",
    },
    {
        "layout": "matrix",
        "quadrants": [
            ("KERJAKAN", "Penting dan mendesak"),
            ("JADWALKAN", "Penting, belum mendesak"),
            ("DELEGASIKAN", "Mendesak, kurang penting"),
            ("BATASI", "Tidak mendesak dan kurang penting"),
        ],
        "note": "Pakai matriks sebagai panduan awal, lalu sesuaikan dengan kondisi dan tenggatmu.",
        "swipe": "Swipe buat coba prompt-nya",
    },
    {
        "layout": "prompt",
        "prompt": (
            "Bantu saya menyusun matriks jadwal belajar mingguan berbasis "
            "Prioritas Eisenhower berdasarkan daftar 4 mata kuliah ini: "
            "[Sebutkan 4 Matkul & Deadline Tugasnya]. Alokasikan waktu fokus "
            "90 menit per sesi dan sertakan jeda istirahat serta kegiatan "
            "organisasi kampus setiap sore/malam."
        ),
        "note": "Tambahkan jam kuliah dan waktu paling produktifmu.",
        "swipe": "Swipe untuk lihat contoh jadwal",
    },
    {
        "layout": "planner",
        "events": [
            ("SENIN", "15.30", "Tugas Analisis Data"),
            ("SENIN", "17.00", "Istirahat + rapat organisasi"),
            ("SELASA", "09.00", "Review materi kuliah"),
            ("SELASA", "MALAM", "Waktu bebas / hobi"),
        ],
        "note": "Contoh ilustratif. Sesuaikan jadwal dengan kuliah dan kegiatanmu.",
        "swipe": "Swipe buat rangkumannya",
    },
    {
        "layout": "closing",
        "cta": "Simpan postingan ini untuk dicoba di awal minggu!",
        "swipe": "Gemini Academy UB",
    },
]


def _find_chrome():
    candidates = [
        Path(os.environ.get("PROGRAMFILES", "C:/Program Files"))
        / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", "C:/Program Files (x86)"))
        / "Microsoft/Edge/Application/msedge.exe",
        Path(os.environ.get("LOCALAPPDATA", ""))
        / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("LOCALAPPDATA", ""))
        / "Microsoft/Edge/Application/msedge.exe",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    for name in ("chrome", "msedge", "google-chrome", "chromium"):
        executable = shutil.which(name)
        if executable:
            return Path(executable)
    raise RuntimeError(
        "Browser Chromium tidak ditemukan. Pasang Google Chrome atau Microsoft Edge "
        "untuk merender HTML menjadi PNG."
    )


def _render_html(slides, output_dir):
    if not TEMPLATE_PATH.is_file():
        raise FileNotFoundError(f"Template HTML tidak ditemukan: {TEMPLATE_PATH}")
    if not slides:
        raise ValueError("Carousel harus berisi minimal satu slide.")
    unknown_layouts = sorted(
        {slide.get("layout") for slide in slides}
        - {"cover", "problem", "matrix", "prompt", "planner", "closing"}
    )
    if unknown_layouts:
        raise ValueError(f"Layout carousel tidak dikenal: {', '.join(unknown_layouts)}")

    font_dir = ASSET_DIR / "Font - Inter" / "static"
    assets = {
        "__FONT_REGULAR__": (font_dir / "Inter_18pt-Regular.ttf").as_uri(),
        "__FONT_BOLD__": (font_dir / "Inter_18pt-ExtraBold.ttf").as_uri(),
        "__GEMINI_ICON__": (ASSET_DIR / "Gemini Icon@2x-8.png").as_uri(),
        "__ACADEMY_LOGO__": (ASSET_DIR / "Gemini Academy Logo@2x-8.png").as_uri(),
        "__MASCOT__": (ASSET_DIR / "Main Character.png").as_uri(),
    }
    for asset_path in (
        font_dir / "Inter_18pt-Regular.ttf",
        font_dir / "Inter_18pt-ExtraBold.ttf",
        ASSET_DIR / "Gemini Icon@2x-8.png",
        ASSET_DIR / "Gemini Academy Logo@2x-8.png",
        ASSET_DIR / "Main Character.png",
    ):
        if not asset_path.is_file():
            raise FileNotFoundError(f"Aset desain tidak ditemukan: {asset_path}")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    serialized_slides = json.dumps(slides, ensure_ascii=False).replace("<", "\\u003c")
    html = template.replace("__SLIDE_DATA__", serialized_slides)
    for placeholder, uri in assets.items():
        html = html.replace(placeholder, uri)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    html_path = output_dir / "index.html"
    html_path.write_text(html, encoding="utf-8")
    browser = _find_chrome()
    names = {
        "cover": "cover",
        "problem": "dilema",
        "matrix": "matriks",
        "prompt": "prompt",
        "planner": "jadwal",
        "closing": "cta",
    }
    with tempfile.TemporaryDirectory(prefix="carousel-chrome-") as profile_dir:
        for index, slide in enumerate(slides):
            output_path = output_dir / f"slide-{index + 1:02}-{names[slide['layout']]}.png"
            command = [
                str(browser),
                "--headless",
                "--disable-gpu",
                "--disable-extensions",
                "--disable-background-networking",
                "--no-first-run",
                "--no-default-browser-check",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                f"--window-size={WIDTH},{HEIGHT}",
                f"--user-data-dir={profile_dir}",
                f"--screenshot={output_path}",
                f"{html_path.as_uri()}?slide={index}",
            ]
            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=60,
                )
            except subprocess.TimeoutExpired as exc:
                raise RuntimeError(
                    f"Render slide {index + 1} melewati batas waktu 60 detik."
                ) from exc
            if result.returncode != 0 or not output_path.is_file():
                details = result.stderr.strip() or result.stdout.strip()
                raise RuntimeError(
                    f"Browser gagal merender slide {index + 1}: {details}"
                )
            with output_path.open("rb") as image:
                header = image.read(24)
            if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
                raise RuntimeError(f"Output bukan PNG yang valid: {output_path}")
            dimensions = struct.unpack(">II", header[16:24])
            if dimensions != (WIDTH, HEIGHT):
                raise RuntimeError(
                    f"Ukuran slide {index + 1} salah: {dimensions}; "
                    f"seharusnya {(WIDTH, HEIGHT)}."
                )
    return output_dir


def render_carousel(slides, output_dir):
    return _render_html(slides, output_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Render trial carousel matriks belajar dengan HTML/CSS."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=BASE_DIR
        / "Hasil Desain Carousel"
        / "trial_matriks_belajar_html",
        help="Folder output slide PNG dan pratinjau HTML.",
    )
    args = parser.parse_args()
    output_dir = render_carousel(SLIDES, args.output)
    print(f"{len(SLIDES)} slide HTML/CSS selesai dirender di: {output_dir}")


if __name__ == "__main__":
    main()
