# Research System Javanese Profile

[![Tests](https://github.com/bendahara-selokarto/research-system-javanese-profile/actions/workflows/tests.yml/badge.svg)](https://github.com/bendahara-selokarto/research-system-javanese-profile/actions/workflows/tests.yml)
[![Release](https://img.shields.io/github/v/release/bendahara-selokarto/research-system-javanese-profile)](https://github.com/bendahara-selokarto/research-system-javanese-profile/releases/tag/v0.1.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/bendahara-selokarto/research-system-javanese-profile/blob/main/LICENSE)

Repo ini adalah repo mandiri untuk fitur `research_system.commands.javanese_profile` tanpa membawa seluruh pipeline `ai-research-system`.

Isi repo:

- kalkulasi kalender Jawa: hari, pasaran, weton, neptu, wuku
- kalkulasi siklus tahun Jawa: taun, windu, kurup, dan kelanjutan angka tahun Saka
- kalkulasi tanggal Jawa lengkap: tanggal, bulan, tahun Jawa, dan padanan Hijriyah
- petungan naga dina dengan varian pepali arah dan boyongan-neptu
- ringkasan profil hari Jawa
- hitung kecocokan jodoh berbasis jenjem
- saran hari baik untuk beberapa jenis acara
- ekspor profil ke file Word `.docx`
- CLI `javanese-profile`

## Struktur

```text
.
|-- .github/
|   `-- workflows/
|       `-- tests.yml
|-- docs/
|-- src/
|   `-- research_system/
|       |-- commands/
|       |   `-- javanese_profile.py
|       `-- utils/
|           `-- javanese_calendar.py
|-- tests/
|-- LICENSE
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

Jika file sudah ada, nama file akan diberi suffix otomatis seperti `-2`, `-3`, dan seterusnya.
Untuk mode pasangan, nama file akan menjadi `output/YYYY-MM-DD-partner-YYYY-MM-DD.docx`.
Dokumen output kini juga memuat tanggal Jawa lengkap, padanan Hijriyah, taun Jawa, windu, kurup, petungan naga dina, dan catatan bahwa angka tahun Jawa Sultan Agungan meneruskan penomoran Saka.

## API Python

```python
from research_system.commands.javanese_profile import write_profile_docx
from research_system.utils import compatibility_result, javanese_day_profile, javanese_naga_dina

profile = javanese_day_profile("1990-04-25")
print(profile.identity.year_cycle)
print(javanese_naga_dina("1990-04-25").summary)
compat = compatibility_result("2025-01-14", "2025-01-05")
artifact = write_profile_docx("1990-04-25")
```

Catatan:

- Repo ini sengaja mempertahankan path import `research_system.commands.javanese_profile`.
- Dependensi dibuat minimal agar repo ini bisa berdiri sendiri.
- Hitungan exact taun, windu, dan kurup diimplementasikan dengan dua jangkar sumber: epoch Sultan Agungan 8 Juli 1633 dan jangkar Asapon 25 Maret 1936, lalu diturunkan ke siklus tahun Jawa modern yang dipakai sistem.
- Modul naga dina disimpan terpisah dari hitungan weton utama. Default sistem memakai varian pepali arah hari-pasaran, sedangkan varian boyongan-neptu tetap ditampilkan sebagai pembanding karena sumber lokal menunjukkan praktik yang tidak tunggal.
- Ringkasan sumber analisa tersimpan di folder `docs/` sebagai markdown bertimestamp.

## Test

```bash
python -m pytest
```

Workflow CI akan menjalankan test otomatis pada Python 3.11 dan 3.12 setiap push ke `main` dan setiap pull request.
