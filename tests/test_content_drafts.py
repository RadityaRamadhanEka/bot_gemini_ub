import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import generator


class ContentDraftTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.project_root = Path(self.temporary_directory.name)
        self.drafts_directory = self.project_root / "Hasil Draft Konten"
        self.drafts_directory.mkdir()
        self.source_draft = self.drafts_directory / "draft_episode_satu.md"
        self.source_draft.write_text(
            "# Episode Satu\n\nNaskah cerita dengan data sintetis.",
            encoding="utf-8",
        )
        self.base_directory_patch = patch.object(
            generator, "BASE_DIR", self.project_root
        )
        self.base_directory_patch.start()

    def tearDown(self):
        self.base_directory_patch.stop()
        self.temporary_directory.cleanup()

    def test_audit_reports_missing_campaign_items_and_placeholders(self):
        warnings = generator.audit_draft_content(
            "## Caption\nCoba di sini — [masukkan tautan].",
            "Reels",
            "Festival",
        )

        self.assertTrue(
            any("geminiacademy" in warning.casefold() for warning in warnings)
        )
        self.assertTrue(
            any("refo indonesia" in warning.casefold() for warning in warnings)
        )
        self.assertTrue(
            any("geminiacademyfestival" in warning.casefold() for warning in warnings)
        )
        self.assertTrue(any("em dash" in warning for warning in warnings))
        self.assertTrue(any("placeholder" in warning for warning in warnings))
        self.assertTrue(any("9:16" in warning for warning in warnings))

    def test_audit_accepts_a_complete_short_video_brief(self):
        draft = """
        # Contoh Reel
        Format vertikal 9:16.
        | 0-5 detik | Raka di meja belajar |
        Logo Gemini Academy di penutup.
        @REFO Indonesia #GeminiAcademy #GeminiAcademyUB
        ## Caption
        Angka jadi cerita 📊 Cek lagi hasilnya ✅
        """

        self.assertEqual(generator.audit_draft_content(draft, "Reels"), [])

    def test_previous_draft_titles_extract_content_headings(self):
        nested_directory = self.drafts_directory / "KulikData"
        nested_directory.mkdir()
        nested_draft = nested_directory / "draf_baru.md"
        nested_draft.write_text(
            "# Brief Asli Pengguna\n\n## Episode Dua: Visualisasi Data",
            encoding="utf-8",
        )

        titles = generator.load_previous_draft_titles()

        self.assertEqual(
            titles,
            [
                "draft_episode_satu.md: Episode Satu",
                "KulikData/draf_baru.md: Episode Dua: Visualisasi Data",
            ],
        )

    def test_generation_receives_existing_draft_titles_and_preferences(self):
        _, knowledge_base = generator.load_supporting_files()
        with patch.object(
            generator, "load_supporting_files", return_value=("", knowledge_base)
        ):
            with patch.object(
                generator, "_generate_text", return_value="generated draft"
            ) as model:
                result = generator.generate_content_draft(
                    "Topik baru",
                    "Reels",
                    "Rutin",
                    "Jelaskan ide baru.",
                )

        self.assertEqual(result, "generated draft")
        prompt = model.call_args.args[0]
        self.assertIn("Episode Satu", prompt)
        self.assertIn("Default gender VO: male", prompt)
        self.assertIn("Hasil proyek ini adalah naskah Markdown", prompt)


if __name__ == "__main__":
    unittest.main()
