# Research System Javanese Profile

Repo ini khusus untuk fitur `research_system.commands.javanese_profile` tanpa membawa seluruh pipeline `ai-research-system`.

Isi repo:

- kalkulasi kalender Jawa: hari, pasaran, weton, neptu, wuku
- ringkasan profil hari Jawa
- hitung kecocokan jodoh berbasis jenjem
- saran hari baik untuk beberapa jenis acara
- ekspor profil ke file Word `.docx`
- CLI `javanese-profile`

## Struktur

```text
.
|-- src/
|   `-- research_system/
|       |-- commands/
|       |   `-- javanese_profile.py
|       `-- utils/
|           `-- javanese_calendar.py
|-- tests/
|-- pyproject.toml
`-- README.md
```

## Instalasi

```bash
python -m pip install -e .
```

Untuk dependensi dev:

```bash
python -m pip install -e .[dev]
```

## Pemakaian CLI

Generate profil dasar:

```bash
javanese-profile --date 1990-04-25
```

Tambahkan tanggal pasangan dan jenis acara:

```bash
javanese-profile --date 1990-04-25 --partner-date 2025-01-14 --events nikah rumah
```

Simpan ke folder tertentu:

```bash
javanese-profile --date 1990-04-25 --output-dir output
```

Output default akan dibuat di:

```text
output/YYYY-MM-DD.docx
```

## API Python

```python
from research_system.commands.javanese_profile import write_profile_docx
from research_system.utils import javanese_day_profile, compatibility_result

profile = javanese_day_profile("1990-04-25")
compat = compatibility_result("2025-01-14", "2025-01-05")
artifact = write_profile_docx("1990-04-25")
```

Catatan:

- Repo ini sengaja mempertahankan path import `research_system.commands.javanese_profile`.
- Dependensi dibuat minimal agar repo ini bisa berdiri sendiri.

## Test

```bash
python -m pytest
```
