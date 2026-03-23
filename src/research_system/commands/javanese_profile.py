from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Iterable

from docx import Document

from research_system.utils import (
    EVENT_GUIDELINES,
    SELAPAN_CYCLE_DAYS,
    compatibility_result,
    get_watak_profile,
    hari_baik_advice,
    javanese_day_profile,
)


DEFAULT_EVENTS = list(EVENT_GUIDELINES.keys())


def _parse_date(raw: str) -> date:
    return date.fromisoformat(raw)


def write_profile_docx(
    target_date: date | str,
    partner_date: date | str | None = None,
    events: Iterable[str] | None = None,
    output_dir: Path | None = None,
) -> Path:
    target = _parse_date(target_date) if isinstance(target_date, str) else target_date
    partner = _parse_date(partner_date) if isinstance(partner_date, str) else partner_date
    profile = javanese_day_profile(target)
    output_base = (output_dir or Path("output")).expanduser()
    output_base.mkdir(parents=True, exist_ok=True)
    artifact = output_base / f"{target:%Y-%m-%d}.docx"

    document = Document()
    document.add_heading(f"Profil Hari Jawa - {target:%Y-%m-%d}", level=1)
    document.add_paragraph(profile.summary)

    document.add_heading("Identitas dasar", level=2)
    table = document.add_table(rows=0, cols=2)
    for label, value in (
        ("Hari", profile.identity.hari),
        ("Dinapitu", profile.identity.dinapitu),
        ("Pasaran", profile.identity.pasaran),
        ("Weton Jawa", profile.identity.weton_jawa),
        ("Wuku", profile.identity.wuku),
        ("Neptu total / jenjem", str(profile.identity.neptu_total)),
        ("Watak singkat", get_watak_profile(target)),
    ):
        row = table.add_row().cells
        row[0].text = label
        row[1].text = value

    document.add_heading("Selapan dan wetonan berikutnya", level=2)
    document.add_paragraph(
        f"Selapan ke-{profile.selapan_day} dari {SELAPAN_CYCLE_DAYS}-hari; "
        f"weton berikutnya: {profile.next_weton_date.isoformat()}."
    )
    for idx, next_date in enumerate(profile.next_three_weton_dates, start=1):
        document.add_paragraph(f"#{idx}: {next_date.isoformat()}")

    document.add_heading("Kegunaan budaya", level=2)
    for cultural_use in profile.common_uses:
        paragraph = document.add_paragraph()
        paragraph.add_run(cultural_use.category.replace("_", " ").capitalize() + ": ").bold = True
        paragraph.add_run(f"{cultural_use.description} ({cultural_use.example_question})")
        if cultural_use.requires_additional_input:
            paragraph.add_run(" [Butuh input tambahan]").italic = True

    document.add_heading("Kecocokan jodoh", level=2)
    if partner:
        compatibility = compatibility_result(target, partner)
        document.add_paragraph(
            f"{compatibility.first_weton} + {compatibility.second_weton} = "
            f"{compatibility.jenjem_sum} ({compatibility.category}). {compatibility.recommendation}"
        )
    else:
        document.add_paragraph("Tambahkan --partner-date untuk melihat jenjem pasangan.")

    document.add_heading("Hari baik", level=2)
    events_to_check = events or DEFAULT_EVENTS
    for event in events_to_check:
        advice = hari_baik_advice(target, event)
        document.add_paragraph(
            f"{event.title()}: {'Baik' if advice.is_good else 'Tidak baik'} - {advice.reason} ({advice.note})"
        )

    document.save(artifact)
    return artifact


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a Word document that profiles a Javanese hari or weton."
    )
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        type=_parse_date,
        help="Tanggal Masehi dalam format YYYY-MM-DD.",
    )
    parser.add_argument(
        "--partner-date",
        type=_parse_date,
        help="Tanggal Masehi pasangan untuk menghitung jenjem dua orang.",
    )
    parser.add_argument(
        "--events",
        nargs="*",
        choices=DEFAULT_EVENTS,
        help="Jenis acara yang ingin diperiksa hari baiknya.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output"),
        help="Direktori tempat menyimpan file .docx.",
    )

    args = parser.parse_args()
    artifact = write_profile_docx(
        args.date,
        partner_date=args.partner_date,
        events=args.events,
        output_dir=args.output_dir,
    )
    print(f"{artifact} telah dibuat.")


if __name__ == "__main__":
    main()
