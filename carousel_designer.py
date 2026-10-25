import argparse
import base64
import json
import os
import shutil
import struct
import subprocess
import tempfile
from pathlib import Path

from google import genai
from google.genai import errors

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "referensi_design_carousel" / "brand-assets"
TEMPLATE_PATH = BASE_DIR / "carousel_template.html"
WIDTH, HEIGHT = 1080, 1350
DEFAULT_IMAGE_MODEL = "gemini-nano-banana-2.1"


SLIDES = [
    {
        "layout": "cover",
        "art_direction": "cinematic-study",
        "character_frame": "hero-right",
        "title": "Bingung Mau Kerjain Tugas Dulu atau Review Materi?",
        "swipe": "Swipe buat tahu caranya",
    },
    {
        "layout": "problem",
        "art_direction": "pattern-story",
        "character_frame": "thinking-center",
        "items": [
            "Mau review materi kelas tadi pagi, tapi tugas minggu lalu belum beres.",
            "Mau ngerjain tugas, tapi materinya belum sempat dipelajari.",
        ],
        "note": "Akhirnya malah procrastinating dan sistem kebut semalam. Relate?",
        "swipe": "Swipe buat lanjut ke solusi",
    },
    {
        "layout": "matrix",
        "art_direction": "blueprint",
        "character_frame": "none",
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
        "art_direction": "paper-note",
        "character_frame": "sticker-left",
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
        "art_direction": "desk-planner",
        "character_frame": "mentor-corner",
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
        "art_direction": "warm-editorial",
        "character_frame": "portrait-hero",
        "cta": "Simpan postingan ini untuk dicoba di awal minggu!",
        "swipe": "Gemini Academy UB",
    },
]

VISUAL_PROMPTS = [
    (
        "Cinematic warm university study room, late afternoon window light, "
        "a white anthropomorphic rabbit student mascot wearing a black graduation "
        "cap with gold tassel and white shirt with a small multicolor star on the "
        "pocket, studying at a crowded desk, thoughtful slightly overwhelmed pose, "
        "rabbit large on the right half, left half visually quiet for later text."
    ),
    (
        "Stylized editorial campus study scene with a white anthropomorphic rabbit "
        "student mascot in a black graduation cap with gold tassel and white shirt "
        "with a small multicolor star on the pocket, looking puzzled between books "
        "and a notebook, expressive thinking pose, dark olive patterned wallpaper "
        "and warm wooden lower wall, keep space in upper area for headline."
    ),
    (
        "Minimal elegant editorial illustration background for a student priority "
        "matrix: pale mint and cream blueprint grid, subtle blue geometric rings, "
        "soft paper texture, uncluttered, no characters, no cards, leave central "
        "area calm and low contrast for a large overlay infographic."
    ),
    (
        "Warm cream study-notebook tabletop scene with a white anthropomorphic "
        "rabbit student mascot in a black graduation cap with gold tassel and white "
        "shirt with a small multicolor star on the pocket, small character peeking "
        "from bottom left, paper fibers and subtle ruled notebook lines, leave the "
        "center clear for a large overlay prompt card."
    ),
    (
        "Top-down editorial study planner desk, pale sage blue graph paper, "
        "warm wood desk visible near bottom, a white anthropomorphic rabbit "
        "student mascot in a black graduation cap with gold tassel and white shirt "
        "with a small multicolor star on the pocket peeking from the lower right, "
        "leave broad central area visually simple for a weekly timetable."
    ),
    (
        "Warm golden-hour campus study room, optimistic white anthropomorphic "
        "rabbit student mascot wearing a black graduation cap with gold tassel and "
        "white shirt with a small multicolor star on the pocket, confident friendly "
        "thumbs-up pose, character centered low in frame, generous uncluttered "
        "warm background above for a closing headline."
    ),
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
    known_directions = {
        "cinematic-study",
        "pattern-story",
        "blueprint",
        "paper-note",
        "desk-planner",
        "warm-editorial",
    }
    unknown_directions = sorted(
        {
            slide.get("art_direction")
            for slide in slides
            if slide.get("art_direction") is not None
        }
        - known_directions
    )
    if unknown_directions:
        raise ValueError(
            f"Art direction tidak dikenal: {', '.join(unknown_directions)}"
        )
    known_character_frames = {
        "hero-right",
        "thinking-center",
        "sticker-left",
        "mentor-corner",
        "portrait-hero",
        "none",
    }
    unknown_frames = sorted(
        {
            slide.get("character_frame")
            for slide in slides
            if slide.get("character_frame") is not None
        }
        - known_character_frames
    )
    if unknown_frames:
        raise ValueError(
            f"Framing karakter tidak dikenal: {', '.join(unknown_frames)}"
        )

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


def generate_visual_assets(output_dir, model_name=None):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY belum disetel. Atur key baru di PowerShell yang sama; "
            "jangan kirim key melalui chat."
        )

    model_name = (
        model_name
        or os.getenv("GEMINI_IMAGE_MODEL", DEFAULT_IMAGE_MODEL).strip()
        or DEFAULT_IMAGE_MODEL
    )
    client = genai.Client(api_key=api_key)
    output_dir = Path(output_dir)
    assets_dir = output_dir / "visuals"
    assets_dir.mkdir(parents=True, exist_ok=True)
    mascot_path = ASSET_DIR / "Main Character.png"
    mascot_data = base64.b64encode(mascot_path.read_bytes()).decode("ascii")
    generated = {}

    for index, prompt in enumerate(VISUAL_PROMPTS):
        output_path = assets_dir / f"visual-{index + 1:02}.png"
        if output_path.is_file():
            cached_header = output_path.read_bytes()[:8]
            if cached_header != b"\x89PNG\r\n\x1a\n":
                raise RuntimeError(
                    f"Visual cache bukan PNG yang valid: {output_path}. "
                    "Periksa file ini sebelum menghapus atau menggantinya."
                )
            generated[index] = output_path
            print(f"Memakai visual yang sudah ada: {output_path}")
            continue
        contents = [{"type": "text", "text": (
            f"Create a portrait 4:5 full-bleed visual asset for a social-media "
            f"carousel, with no text, letters, numbers, logos, watermarks, frames, "
            f"or UI. Keep the important subject within the middle 80 percent of "
            f"the canvas. Follow this art direction: {prompt} "
            f"When a reference image is attached, use it only as the mascot identity "
            f"reference. Preserve the same white rabbit species, face, long ears, "
            f"black graduation cap and gold tassel, white shirt, and small multicolor "
            f"star on the pocket, while creating a new natural pose and scene. "
            f"Do not copy or recreate any text or logos from the reference."
        )}]
        if index != 2:
            contents.append({
                "type": "image",
                "data": mascot_data,
                "mime_type": "image/png",
            })

        try:
            interaction = client.interactions.create(
                model=model_name,
                input=contents,
            )
        except errors.APIError as exc:
            if exc.code in (401, 403):
                guidance = "Periksa key dan izin Gemini API."
            elif exc.code == 404:
                guidance = (
                    f"Model gambar '{model_name}' tidak tersedia untuk key ini. "
                    "Atur GEMINI_IMAGE_MODEL ke model image-generation yang tersedia."
                )
            elif exc.code == 429:
                guidance = "Kuota atau rate limit image generation telah tercapai."
            else:
                guidance = "Permintaan image generation gagal."
            raise RuntimeError(
                f"{guidance} Gagal pada visual {index + 1}/6. Detail: {exc}"
            ) from exc

        output_image = getattr(interaction, "output_image", None)
        image_data = getattr(output_image, "data", None)
        if not image_data:
            raise RuntimeError(
                f"Gemini tidak mengembalikan gambar untuk visual {index + 1}/6."
            )
        try:
            image_bytes = base64.b64decode(image_data, validate=True)
        except (ValueError, TypeError) as exc:
            raise RuntimeError(
                f"Data gambar dari Gemini tidak valid pada visual {index + 1}/6."
            ) from exc
        if not image_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
            raise RuntimeError(
                f"Output visual {index + 1}/6 bukan PNG yang valid."
            )
        output_path.write_bytes(image_bytes)
        generated[index] = output_path
        print(f"Visual {index + 1}/6 tersimpan: {output_path}")
    return generated


def render_carousel(slides, output_dir, visual_assets=None):
    slides = [dict(slide) for slide in slides]
    for index, image_path in (visual_assets or {}).items():
        if not 0 <= index < len(slides):
            raise ValueError(f"Index slide visual tidak valid: {index}")
        if not Path(image_path).is_file():
            raise FileNotFoundError(f"Visual hasil generate tidak ditemukan: {image_path}")
        slides[index]["background_image"] = Path(image_path).as_uri()
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
    parser.add_argument(
        "--generate-assets",
        action="store_true",
        help="Generate 6 visual dengan Gemini image generation (dapat dikenai biaya).",
    )
    parser.add_argument(
        "--image-model",
        help="Nama model image generation; default: GEMINI_IMAGE_MODEL atau "
        f"{DEFAULT_IMAGE_MODEL}.",
    )
    args = parser.parse_args()
    visual_assets = None
    if args.generate_assets:
        print(
            "Image generation akan membuat visual yang belum ada; total hingga "
            "6 gambar. Permintaan ini dapat memakai kuota "
            "atau menimbulkan biaya sesuai akun/API plan."
        )
        if input("Lanjutkan image generation? (y/N): ").strip().casefold() != "y":
            print("Image generation dibatalkan; tidak ada permintaan Gemini yang dikirim.")
            return
        visual_assets = generate_visual_assets(args.output, args.image_model)
    output_dir = render_carousel(SLIDES, args.output, visual_assets)
    print(f"{len(SLIDES)} slide HTML/CSS selesai dirender di: {output_dir}")


if __name__ == "__main__":
    main()
