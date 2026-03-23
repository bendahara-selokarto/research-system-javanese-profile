from __future__ import annotations

from datetime import date
from pathlib import Path

from docx import Document

from research_system.commands.javanese_profile import write_profile_docx


def test_docx_export_contains_summary() -> None:
    output_dir = Path("tests-output")
    output_dir.mkdir(exist_ok=True)
    artifact = write_profile_docx(
        target_date=date(1990, 4, 25),
        partner_date=date(2025, 1, 14),
        events=("nikah",),
        output_dir=output_dir,
    )

    try:
        doc = Document(artifact)
        text = "\n".join(p.text for p in doc.paragraphs)
        assert "Rebo Pon" in text
        assert "nikah" in text.lower()
        assert "jenjem" in text.lower()
    finally:
        if artifact.exists():
            artifact.unlink()
        if output_dir.exists():
            output_dir.rmdir()
