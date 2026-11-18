import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import generator


class RemotionHandoffTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.project_root = Path(self.temporary_directory.name)
        self.drafts_directory = self.project_root / "Hasil Draft Konten"
        self.drafts_directory.mkdir()
        self.source_draft = (
            self.drafts_directory / "draft_episode_satu.md"
        )
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

    def test_lists_markdown_drafts_but_not_handoff_outputs(self):
        nested_draft = self.drafts_directory / "KulikData" / "episode_dua.md"
        nested_draft.parent.mkdir()
        nested_draft.write_text("# Episode Dua", encoding="utf-8")
        handoff_directory = self.drafts_directory / "Remotion Handoff"
        handoff_directory.mkdir()
        (handoff_directory / "episode_lama_remotion_handoff.md").write_text(
            "# Existing handoff", encoding="utf-8"
        )

        drafts = generator.list_remotion_source_drafts()

        self.assertEqual(
            drafts,
            [
                self.source_draft,
                nested_draft,
            ],
        )

    def test_creates_self_contained_handoff_without_overwriting(self):
        first_output = generator.create_remotion_handoff(self.source_draft)
        second_output = generator.create_remotion_handoff(self.source_draft)

        self.assertTrue(first_output.is_file())
        self.assertTrue(second_output.is_file())
        self.assertNotEqual(first_output, second_output)
        content = first_output.read_text(encoding="utf-8")
        self.assertIn("9:16, 1080x1920, 30 fps", content)
        self.assertIn("<!-- BEGIN SOURCE DRAFT:", content)
        self.assertIn("Naskah cerita dengan data sintetis.", content)

    def test_rejects_files_outside_draft_directory(self):
        outside_draft = self.project_root / "outside.md"
        outside_draft.write_text("# Not a content draft", encoding="utf-8")

        with self.assertRaises(ValueError):
            generator.create_remotion_handoff(outside_draft)

    def test_rejects_handoff_as_a_source_draft(self):
        handoff_directory = self.drafts_directory / "Remotion Handoff"
        handoff_directory.mkdir()
        handoff_draft = handoff_directory / "previous_remotion_handoff.md"
        handoff_draft.write_text("# Previous handoff", encoding="utf-8")

        with self.assertRaises(ValueError):
            generator.create_remotion_handoff(handoff_draft)

    def test_audit_reports_missing_campaign_items_and_unresolved_placeholders(self):
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

    def test_previous_draft_titles_skip_handoff_and_extract_content_heading(self):
        handoff_directory = self.drafts_directory / "Remotion Handoff"
        handoff_directory.mkdir()
        (handoff_directory / "old_remotion_handoff.md").write_text(
            "# Instruksi Implementasi Video Remotion\n# Episode Lama",
            encoding="utf-8",
        )
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


if __name__ == "__main__":
    unittest.main()
