from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta

JAVANESE_CALENDAR_EPOCH = date(1633, 7, 8)
GREGORIAN_WEEKDAYS = (
    "Senin",
    "Selasa",
    "Rabu",
    "Kamis",
    "Jumat",
    "Sabtu",
    "Minggu",
)
JAVANESE_DINAPITU = (
    "Senen",
    "Selasa",
    "Rebo",
    "Kemis",
    "Jemuwah",
    "Setu",
    "Ngahad",
)
HARI_NEPTU = (4, 3, 7, 8, 6, 9, 5)
PASARAN_NAMES = (
    "Legi",
    "Pahing",
    "Pon",
    "Wage",
    "Kliwon",
)
PASARAN_NEPTU = (5, 9, 7, 4, 8)
WUKU_NAMES = (
    "Sinta",
    "Landep",
    "Wukir",
    "Kurantil",
    "Tolu",
    "Gumbreg",
    "Warigalit",
    "Warigagung",
    "Julungwangi",
    "Sungsang",
    "Galungan",
    "Kuningan",
    "Langkir",
    "Mandasiya",
    "Julungpujut",
    "Pahang",
    "Kuruwelut",
    "Marakeh",
    "Tambir",
    "Medangkungan",
    "Maktal",
    "Wuye",
    "Manahil",
    "Prangbakat",
    "Bala",
    "Wugu",
    "Wayang",
    "Kulawu",
    "Dukut",
    "Watugunung",
)
JAVANESE_YEAR_NAMES = (
    "Alip",
    "Ehe",
    "Jimawal",
    "Je",
    "Dal",
    "Be",
    "Wawu",
    "Jimakir",
)
WINDU_NAMES = (
    "Kuntara",
    "Sangara",
    "Sancaya",
    "Adi",
)
JAVANESE_MONTH_NAMES = (
    "Sura",
    "Sapar",
    "Mulud",
    "Bakda Mulud",
    "Jumadilawal",
    "Jumadilakir",
    "Rejeb",
    "Ruwah",
    "Pasa",
    "Sawal",
    "Dulkangidah",
    "Besar",
)
HIJRI_MONTH_NAMES = (
    "Muharram",
    "Safar",
    "Rabiulawal",
    "Rabiulakhir",
    "Jumadilawal",
    "Jumadilakhir",
    "Rajab",
    "Syakban",
    "Ramadan",
    "Syawal",
    "Zulkaidah",
    "Zulhijah",
)
SELAPAN_CYCLE_DAYS = 35

_EPOCH_PAWUKON_INDEX = WUKU_NAMES.index("Kulawu") * 7 + 5
_EPOCH_JAVANESE_YEAR = 1555
_EPOCH_HIJRI_YEAR = 1043
_JAVANESE_TO_HIJRI_YEAR_OFFSET = _EPOCH_JAVANESE_YEAR - _EPOCH_HIJRI_YEAR
_ASAPON_ANCHOR_DATE = date(1936, 3, 25)
_ASAPON_ANCHOR_JAVANESE_YEAR = 1867
_ASAPON_ANCHOR_HIJRI_YEAR = 1355
_HIJRI_LEAP_YEAR_POSITIONS = frozenset({2, 5, 7, 10, 13, 16, 18, 21, 24, 26, 29})

KURUPS = (
    {
        "code": "Aahgi",
        "name": "Alip Jumat Legi",
        "start_year": 1555,
        "end_year_exclusive": 1627,
        "leap_years": frozenset({"Ehe", "Dal", "Jimakir"}),
    },
    {
        "code": "Amiswon",
        "name": "Alip Kamis Kliwon",
        "start_year": 1627,
        "end_year_exclusive": 1747,
        "leap_years": frozenset({"Ehe", "Dal", "Jimakir"}),
    },
    {
        "code": "Aboge",
        "name": "Alip Rebo Wage",
        "start_year": 1747,
        "end_year_exclusive": 1867,
        "leap_years": frozenset({"Ehe", "Je", "Jimakir"}),
    },
    {
        "code": "Asapon",
        "name": "Alip Selasa Pon",
        "start_year": 1867,
        "end_year_exclusive": 1987,
        "leap_years": frozenset({"Ehe", "Je", "Jimakir"}),
    },
    {
        "code": "Anenhing",
        "name": "Alip Senin Pahing",
        "start_year": 1987,
        "end_year_exclusive": 2107,
        "leap_years": None,
    },
)

NAGA_DINA_DAY_DIRECTIONS = {
    "Senen": ("Barat Daya",),
    "Selasa": ("Barat",),
    "Rebo": ("Barat Laut",),
    "Kemis": ("Utara", "Timur Laut"),
    "Jemuwah": ("Timur",),
    "Setu": ("Tenggara",),
    "Ngahad": ("Selatan",),
}
NAGA_DINA_PASARAN_DIRECTIONS = {
    "Legi": "Timur",
    "Pahing": "Selatan",
    "Pon": "Barat",
    "Wage": "Utara",
    "Kliwon": "Tengah",
}
NAGA_DINA_NEPTU_ROTATION = ("Timur", "Selatan", "Barat", "Utara")

WETON_WATAK = {
    "Senen Legi": "Pendamai, suka menjaga keharmonisan keluarga.",
    "Senen Pahing": "Kritis, cermat terhadap detail urusan rumah tangga.",
    "Senen Pon": "Pembawa pesan tenang yang senang menolong orang lain.",
    "Senen Wage": "Berenergi tapi sabar, cocok jadi mediator.",
    "Senen Kliwon": "Pemikir mendalam yang menjaga tradisi.",
    "Selasa Legi": "Cerdas cepat tanggap dan penuh rasa keadilan.",
    "Selasa Pahing": "Berani mengambil risiko, cocok sebagai pemimpin proyek.",
    "Selasa Pon": "Berjiwa kompetitif tapi menjaga kepercayaan.",
    "Selasa Wage": "Penuh semangat, mudah berada di depan publik.",
    "Selasa Kliwon": "Menyimpan intuisi kuat dan menjaga privasi.",
    "Rebo Legi": "Penyabar, mudah menemukan solusi tanpa emosi.",
    "Rebo Pahing": "Cepat belajar dan suka menyusun rencana teknis.",
    "Rebo Pon": "Kritis sekaligus kreatif, menyeimbangkan logika dan rasa.",
    "Rebo Wage": "Sosial dengan jiwa gotong royong yang tinggi.",
    "Rebo Kliwon": "Selalu menyiapkan cadangan, berhati-hati namun setia.",
    "Kemis Legi": "Berkomunikasi lembut, mampu menjembatani dua pihak.",
    "Kemis Pahing": "Berwibawa, dipercaya menjaga amanah besar.",
    "Kemis Pon": "Suka belajar, menyenangi pengembangan diri.",
    "Kemis Wage": "Suka seni, menjadikan ide menjadi kenyataan.",
    "Kemis Kliwon": "Berhati-hati, menilai risiko secara sistematis.",
    "Jumat Legi": "Selalu optimis, membawa keberanian dan keteguhan.",
    "Jumat Pahing": "Kuat prinsip, suka menegakkan aturan.",
    "Jumat Pon": "Pembawa perubahan yang tetap menjaga nilai-nilai.",
    "Jumat Wage": "Hangat namun disiplin, memimpin tanpa keras.",
    "Jumat Kliwon": "Misterius, mengandalkan intuisi ketika membuat keputusan.",
    "Sabtu Legi": "Pengamat tajam, cenderung senang kerja analitik.",
    "Sabtu Pahing": "Pragmatis, mengambil segmen pekerjaan paling berat.",
    "Sabtu Pon": "Pelaksana yang disiplin dan mampu bekerja di bawah tekanan.",
    "Sabtu Wage": "Puitis dan menjadi penghibur dalam keluarga.",
    "Sabtu Kliwon": "Berjiwa mandiri, menjaga jarak tapi setia.",
    "Minggu Legi": "Optimis, gemar merayakan pencapaian kecil.",
    "Minggu Pahing": "Mengayomi, sering jadi tempat curhat teman.",
    "Minggu Pon": "Efisien, menyelesaikan banyak tugas tanpa ribet.",
    "Minggu Wage": "Kaya empati, mudah menciptakan suasana damai.",
    "Minggu Kliwon": "Bijak, menggabungkan logika dan nurani.",
}

COMPATIBILITY_RULES = [
    ("Bagus", 14, 18, "Jenjem-nya masuk zona harmonis; bisa dijadikan rujukan acara nikah."),
    ("Netral", 19, 24, "Perlu diskusi tapi tidak ada sinyal bahaya; pertimbangkan hal lain juga."),
    ("Perlu hati-hati", 25, 34, "Jenjem tinggi memberi tantangan, cocok jika ada komunikasi terbuka."),
]

EVENT_GUIDELINES = {
    "nikah": {
        "range": (14, 16),
        "reason": "Jenjem 14-16 kerap disebut awet dan seimbang dalam primbon umum.",
    },
    "rumah": {
        "range": (12, 16),
        "reason": "Angka genap di rentang ini dianggap mendatangkan jalan rezeki.",
    },
    "usaha": {
        "range": (14, 18),
        "reason": "Jenjem 14-18 memberi keberanian yang dibutuhkan saat mulai usaha.",
    },
    "tanam": {
        "range": (11, 15),
        "reason": "Rentang ini menyeimbangkan kerja keras dan hasil panen.",
    },
    "selamatan": {
        "range": (11, 17),
        "reason": "Nilai sedang dianggap stabil untuk ritual perlindungan.",
    },
}


@dataclass(frozen=True, slots=True)
class JavaneseYearCycle:
    year_number: int
    saka_continuity_year: int
    year_name: str
    year_type: str
    year_length_days: int
    year_start_date: date
    next_year_start_date: date
    windu_name: str
    windu_year_number: int
    kurup_code: str
    kurup_name: str
    kurup_start_year: int
    kurup_end_year: int


@dataclass(frozen=True, slots=True)
class JavaneseLunarDate:
    day: int
    month_number: int
    month_name: str
    year_number: int
    year_name: str

    @property
    def formatted(self) -> str:
        return f"{self.day} {self.month_name} {self.year_number} AJ"


@dataclass(frozen=True, slots=True)
class HijriDate:
    day: int
    month_number: int
    month_name: str
    year_number: int

    @property
    def formatted(self) -> str:
        return f"{self.day} {self.month_name} {self.year_number} H"


@dataclass(frozen=True, slots=True)
class JavaneseNagaDinaVariant:
    code: str
    label: str
    source_label: str
    basis: str
    directions: tuple[str, ...]
    note: str


@dataclass(frozen=True, slots=True)
class JavaneseNagaDina:
    weton_jawa: str
    default_variant_code: str
    default_variant_label: str
    day_directions: tuple[str, ...]
    pasaran_direction: str
    neptu_cycle_total: int
    neptu_cycle_direction: str
    summary: str
    variants: tuple[JavaneseNagaDinaVariant, ...]


@dataclass(frozen=True, slots=True)
class JavaneseCalendarCycles:
    gregorian_date: date
    hari: str
    dinapitu: str
    hari_neptu: int
    pasaran: str
    pasaran_neptu: int
    neptu_total: int
    weton: str
    weton_jawa: str
    wuku: str
    days_since_epoch: int
    pawukon_day: int
    year_cycle: JavaneseYearCycle | None
    javanese_date: JavaneseLunarDate | None
    hijri_date: HijriDate | None
    naga_dina: JavaneseNagaDina

    @property
    def jenjem(self) -> int:
        return self.neptu_total


@dataclass(frozen=True, slots=True)
class JavaneseCulturalUse:
    category: str
    description: str
    example_question: str
    requires_additional_input: bool = False


@dataclass(frozen=True, slots=True)
class JavaneseDayProfile:
    identity: JavaneseCalendarCycles
    summary: str
    selapan_cycle_days: int
    selapan_day: int
    previous_weton_date: date
    next_weton_date: date
    next_three_weton_dates: tuple[date, ...]
    common_uses: tuple[JavaneseCulturalUse, ...]


@dataclass(frozen=True, slots=True)
class JavaneseCompatibilityResult:
    first_weton: str
    second_weton: str
    jenjem_sum: int
    category: str
    recommendation: str


@dataclass(frozen=True, slots=True)
class JavaneseHariBaikAdvice:
    event: str
    is_good: bool
    reason: str
    note: str


def javanese_calendar_cycles(value: date | datetime | str) -> JavaneseCalendarCycles:
    target_date = _coerce_date(value)
    days_since_epoch = (target_date - JAVANESE_CALENDAR_EPOCH).days
    weekday_index = target_date.weekday()
    pasaran_index = days_since_epoch % len(PASARAN_NAMES)

    hari = GREGORIAN_WEEKDAYS[weekday_index]
    dinapitu = JAVANESE_DINAPITU[weekday_index]
    hari_neptu = HARI_NEPTU[weekday_index]
    pasaran = PASARAN_NAMES[pasaran_index]
    pasaran_neptu = PASARAN_NEPTU[pasaran_index]
    neptu_total = hari_neptu + pasaran_neptu
    pawukon_index = (days_since_epoch + _EPOCH_PAWUKON_INDEX) % 210
    wuku = WUKU_NAMES[pawukon_index // 7]
    weton_jawa = f"{dinapitu} {pasaran}"
    year_cycle = javanese_year_cycle(target_date)
    if year_cycle is not None:
        javanese_date, hijri_date = _build_lunar_dates(target_date, year_cycle)
    else:
        javanese_date = None
        hijri_date = None
    naga_dina = _build_naga_dina(weton_jawa, dinapitu, pasaran, neptu_total)

    return JavaneseCalendarCycles(
        gregorian_date=target_date,
        hari=hari,
        dinapitu=dinapitu,
        hari_neptu=hari_neptu,
        pasaran=pasaran,
        pasaran_neptu=pasaran_neptu,
        neptu_total=neptu_total,
        weton=f"{hari} {pasaran}",
        weton_jawa=weton_jawa,
        wuku=wuku,
        days_since_epoch=days_since_epoch,
        pawukon_day=pawukon_index + 1,
        year_cycle=year_cycle,
        javanese_date=javanese_date,
        hijri_date=hijri_date,
        naga_dina=naga_dina,
    )


def javanese_year_cycle(value: date | datetime | str) -> JavaneseYearCycle | None:
    target_date = _coerce_date(value)
    if target_date < JAVANESE_CALENDAR_EPOCH:
        return None

    if target_date >= _ASAPON_ANCHOR_DATE:
        return _year_cycle_from_asapon_anchor(target_date)

    year_number = _EPOCH_JAVANESE_YEAR
    year_start_date = JAVANESE_CALENDAR_EPOCH
    while True:
        year_length_days = _javanese_year_length_pre_asapon(year_number)
        next_year_start_date = year_start_date + timedelta(days=year_length_days)
        if target_date < next_year_start_date:
            return _build_year_cycle(year_number, year_start_date, next_year_start_date, year_length_days)

        year_number += 1
        year_start_date = next_year_start_date


def javanese_naga_dina(value: date | datetime | str) -> JavaneseNagaDina:
    return javanese_calendar_cycles(value).naga_dina


def get_watak_profile(value: date | datetime | str) -> str:
    identity = javanese_calendar_cycles(value)
    return WETON_WATAK.get(identity.weton_jawa, "Kombinasi watak yang fleksibel dan adaptif.")


def javanese_day_profile(value: date | datetime | str) -> JavaneseDayProfile:
    identity = javanese_calendar_cycles(value)
    previous_weton_date = identity.gregorian_date - timedelta(days=SELAPAN_CYCLE_DAYS)
    next_weton_date = identity.gregorian_date + timedelta(days=SELAPAN_CYCLE_DAYS)
    next_three_weton_dates = tuple(
        identity.gregorian_date + timedelta(days=SELAPAN_CYCLE_DAYS * step)
        for step in range(1, 4)
    )
    selapan_day = identity.days_since_epoch % SELAPAN_CYCLE_DAYS + 1
    watak_profile = get_watak_profile(identity.gregorian_date)
    naga_dina = identity.naga_dina
    supported_events = ("nikah", "rumah", "usaha", "tanam", "selamatan")
    event_snapshot = ", ".join(
        f"{event} {'baik' if hari_baik_advice(identity.gregorian_date, event).is_good else 'tidak'}"
        for event in supported_events
    )
    summary = (
        f"{identity.gregorian_date.isoformat()} = {identity.weton_jawa}, "
        f"wuku {identity.wuku}, neptu {identity.neptu_total}"
    )
    if identity.javanese_date is not None and identity.hijri_date is not None:
        summary += (
            f", tanggal Jawa {identity.javanese_date.formatted}, "
            f"Hijriyah {identity.hijri_date.formatted}"
        )
    if identity.year_cycle is not None:
        summary += (
            f", taun {identity.year_cycle.year_name} {identity.year_cycle.year_number}, "
            f"windu {identity.year_cycle.windu_name}, kurup {identity.year_cycle.kurup_code}."
        )
        year_cycle_description = (
            f"Tanggal {identity.gregorian_date.isoformat()} masuk taun {identity.year_cycle.year_name} "
            f"{identity.year_cycle.year_number}, windu {identity.year_cycle.windu_name}, "
            f"kurup {identity.year_cycle.kurup_code}."
        )
    else:
        summary += "."
        year_cycle_description = (
            f"Tanggal {identity.gregorian_date.isoformat()} belum terpetakan ke taun, windu, dan kurup exact di sistem ini."
        )

    naga_dina_description = (
        f"Untuk {identity.weton_jawa}, varian default sistem menempatkan {identity.dinapitu} di "
        f"{_format_directions(naga_dina.day_directions)}; {identity.pasaran} di {naga_dina.pasaran_direction}; "
        f"varian boyongan-neptu dengan jumlah {naga_dina.neptu_cycle_total} mengarah ke {naga_dina.neptu_cycle_direction}."
    )

    common_uses = (
        JavaneseCulturalUse(
            category="watak_pribadi",
            description=f"Untuk {identity.weton_jawa}, watak yang sering dikaitkan adalah: {watak_profile}",
            example_question=f"Apa watak orang dengan weton {identity.weton_jawa}?",
        ),
        JavaneseCulturalUse(
            category="ritual_wetonan",
            description=(
                f"Wetonan berikutnya untuk {identity.weton_jawa} jatuh pada {next_weton_date.isoformat()}, "
                f"dan hari ini berada di selapan ke-{selapan_day}."
            ),
            example_question=f"Kapan wetonan berikutnya untuk {identity.weton_jawa}?",
        ),
        JavaneseCulturalUse(
            category="siklus_tahun_jawa",
            description=year_cycle_description,
            example_question=f"Tahun Jawa untuk {identity.gregorian_date.isoformat()} masuk taun apa dan windu apa?",
        ),
        JavaneseCulturalUse(
            category="kecocokan_jodoh",
            description=(
                f"Weton dasar {identity.weton_jawa} membawa neptu {identity.neptu_total}; "
                "sistem akan menambahkan neptu pasangan untuk membaca jenjem dan kecocokan."
            ),
            example_question=f"Bagaimana kecocokan jodoh {identity.weton_jawa} dengan weton pasangan?",
            requires_additional_input=True,
        ),
        JavaneseCulturalUse(
            category="hari_baik_keputusan",
            description=(
                f"Dengan neptu {identity.neptu_total}, ringkasan hari ini adalah: {event_snapshot}."
            ),
            example_question=(
                f"Hari baik apa untuk nikah, pindah rumah, usaha, tanam, atau selamatan jika acuannya {identity.weton_jawa}?"
            ),
            requires_additional_input=True,
        ),
        JavaneseCulturalUse(
            category="naga_dina",
            description=naga_dina_description,
            example_question=f"Ke arah mana naga dina untuk {identity.weton_jawa}?",
        ),
        JavaneseCulturalUse(
            category="identitas_sosial",
            description=(
                f"Pada hari {identity.weton_jawa}, pasaran {identity.pasaran} menjadi penanda yang dalam sebagian tradisi "
                "dipakai untuk mengingat hari lahir, wetonan keluarga, atau bancakan."
            ),
            example_question=(
                f"Apakah pasaran {identity.pasaran} pada {identity.weton_jawa} berkaitan dengan nama keluarga?"
            ),
        ),
    )

    return JavaneseDayProfile(
        identity=identity,
        summary=summary,
        selapan_cycle_days=SELAPAN_CYCLE_DAYS,
        selapan_day=selapan_day,
        previous_weton_date=previous_weton_date,
        next_weton_date=next_weton_date,
        next_three_weton_dates=next_three_weton_dates,
        common_uses=common_uses,
    )


def compatibility_result(
    first: date | datetime | str,
    second: date | datetime | str,
) -> JavaneseCompatibilityResult:
    first_identity = javanese_calendar_cycles(first)
    second_identity = javanese_calendar_cycles(second)
    jenjem_sum = first_identity.neptu_total + second_identity.neptu_total

    for category, low, high, description in COMPATIBILITY_RULES:
        if low <= jenjem_sum <= high:
            return JavaneseCompatibilityResult(
                first_weton=first_identity.weton_jawa,
                second_weton=second_identity.weton_jawa,
                jenjem_sum=jenjem_sum,
                category=category,
                recommendation=description,
            )

    return JavaneseCompatibilityResult(
        first_weton=first_identity.weton_jawa,
        second_weton=second_identity.weton_jawa,
        jenjem_sum=jenjem_sum,
        category="Tidak biasa",
        recommendation="Jenjem di luar rentang umum; komunikasikan harapan masing-masing.",
    )


def hari_baik_advice(
    value: date | datetime | str,
    event_type: str,
) -> JavaneseHariBaikAdvice:
    identity = javanese_calendar_cycles(value)
    event = event_type.lower()
    guideline = EVENT_GUIDELINES.get(event)
    if guideline is None:
        raise ValueError(f"Event '{event_type}' belum didukung untuk saran hari baik.")

    low, high = guideline["range"]
    is_good = low <= identity.neptu_total <= high
    note = "Jenjem masuk zona favorit." if is_good else "Pertimbangkan selapan lain atau ritual tambahan."

    return JavaneseHariBaikAdvice(
        event=event_type,
        is_good=is_good,
        reason=guideline["reason"],
        note=note,
    )


def marriage_jenjem(
    first: date | datetime | str,
    second: date | datetime | str,
) -> int:
    return (
        javanese_calendar_cycles(first).neptu_total
        + javanese_calendar_cycles(second).neptu_total
    )


def _build_naga_dina(
    weton_jawa: str,
    dinapitu: str,
    pasaran: str,
    neptu_total: int,
) -> JavaneseNagaDina:
    day_directions = NAGA_DINA_DAY_DIRECTIONS[dinapitu]
    pasaran_direction = NAGA_DINA_PASARAN_DIRECTIONS[pasaran]
    neptu_cycle_direction = _naga_dina_neptu_direction(neptu_total)
    day_text = _format_directions(day_directions)
    summary = (
        f"Varian default sistem memakai pepali arah: {dinapitu} berada di {day_text} "
        f"dan {pasaran} di {pasaran_direction}. Varian boyongan-neptu memutar jumlah "
        f"{neptu_total} ke {neptu_cycle_direction}."
    )

    return JavaneseNagaDina(
        weton_jawa=weton_jawa,
        default_variant_code="pepali_arah",
        default_variant_label="Pepali arah hari-pasaran",
        day_directions=day_directions,
        pasaran_direction=pasaran_direction,
        neptu_cycle_total=neptu_total,
        neptu_cycle_direction=neptu_cycle_direction,
        summary=summary,
        variants=(
            JavaneseNagaDinaVariant(
                code="pepali_arah",
                label="Pepali arah hari-pasaran",
                source_label="Unej 2017 (Desa Ajung, Jember)",
                basis=(
                    f"Hari {dinapitu} ditempatkan di {day_text} dan pasaran {pasaran} "
                    f"ditempatkan di {pasaran_direction}."
                ),
                directions=day_directions + (pasaran_direction,),
                note="Sistem memilih varian ini sebagai default karena hari dan pasaran dipetakan secara eksplisit.",
            ),
            JavaneseNagaDinaVariant(
                code="boyongan_neptu",
                label="Boyongan neptu berputar",
                source_label="Unej 2022 (Kenduri boyongan Pojokrejo)",
                basis=(
                    f"Jumlah angka hari-pasaran {neptu_total} diputar pada urutan "
                    "Timur-Selatan-Barat-Utara."
                ),
                directions=(neptu_cycle_direction,),
                note=f"Dengan neptu {neptu_total}, arah sial jatuh ke {neptu_cycle_direction}.",
            ),
        ),
    )


def _build_lunar_dates(
    target_date: date,
    year_cycle: JavaneseYearCycle,
) -> tuple[JavaneseLunarDate, HijriDate]:
    day_of_year = (target_date - year_cycle.year_start_date).days
    month_number, day = _lunar_month_day(day_of_year, year_cycle.year_length_days)
    hijri_year_number = year_cycle.year_number - _JAVANESE_TO_HIJRI_YEAR_OFFSET

    return (
        JavaneseLunarDate(
            day=day,
            month_number=month_number,
            month_name=JAVANESE_MONTH_NAMES[month_number - 1],
            year_number=year_cycle.year_number,
            year_name=year_cycle.year_name,
        ),
        HijriDate(
            day=day,
            month_number=month_number,
            month_name=HIJRI_MONTH_NAMES[month_number - 1],
            year_number=hijri_year_number,
        ),
    )



def _lunar_month_day(day_of_year: int, year_length_days: int) -> tuple[int, int]:
    remaining_days = day_of_year
    for month_number, month_length in enumerate(_lunar_month_lengths(year_length_days), start=1):
        if remaining_days < month_length:
            return month_number, remaining_days + 1
        remaining_days -= month_length

    raise ValueError(
        f"Offset hari lunar {day_of_year} berada di luar panjang tahun {year_length_days}."
    )



def _lunar_month_lengths(year_length_days: int) -> tuple[int, ...]:
    if year_length_days not in {354, 355}:
        raise ValueError(f"Panjang tahun lunar {year_length_days} tidak didukung.")

    return (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, year_length_days - 325)



def _naga_dina_neptu_direction(total: int) -> str:
    return NAGA_DINA_NEPTU_ROTATION[(total - 1) % len(NAGA_DINA_NEPTU_ROTATION)]


def _format_directions(directions: tuple[str, ...]) -> str:
    if len(directions) == 1:
        return directions[0]
    if len(directions) == 2:
        return f"{directions[0]} dan {directions[1]}"
    return ", ".join(directions[:-1]) + f", dan {directions[-1]}"


def _coerce_date(value: date | datetime | str) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        return date.fromisoformat(value)
    raise TypeError("value must be a datetime.date, datetime.datetime, or ISO date string")


def _year_name(year_number: int) -> str:
    return JAVANESE_YEAR_NAMES[(year_number - _EPOCH_JAVANESE_YEAR) % len(JAVANESE_YEAR_NAMES)]


def _kurup_for_year(year_number: int) -> dict[str, object] | None:
    for kurup in KURUPS:
        if kurup["start_year"] <= year_number < kurup["end_year_exclusive"]:
            return kurup
    return None


def _build_year_cycle(
    year_number: int,
    year_start_date: date,
    next_year_start_date: date,
    year_length_days: int,
) -> JavaneseYearCycle:
    kurup = _kurup_for_year(year_number)
    if kurup is None:
        kurup = {
            "code": "Tidak diketahui",
            "name": "Di luar rentang kurup baku sistem",
            "start_year": year_number,
            "end_year_exclusive": year_number + 1,
        }

    windu_year_number = (year_number - _EPOCH_JAVANESE_YEAR) % len(JAVANESE_YEAR_NAMES) + 1
    windu_name = WINDU_NAMES[((year_number - _EPOCH_JAVANESE_YEAR) // len(JAVANESE_YEAR_NAMES)) % len(WINDU_NAMES)]
    return JavaneseYearCycle(
        year_number=year_number,
        saka_continuity_year=year_number,
        year_name=_year_name(year_number),
        year_type="Taun Wuntu" if year_length_days == 355 else "Taun Wastu",
        year_length_days=year_length_days,
        year_start_date=year_start_date,
        next_year_start_date=next_year_start_date,
        windu_name=windu_name,
        windu_year_number=windu_year_number,
        kurup_code=kurup["code"],
        kurup_name=kurup["name"],
        kurup_start_year=kurup["start_year"],
        kurup_end_year=kurup["end_year_exclusive"] - 1,
    )


def _year_cycle_from_asapon_anchor(target_date: date) -> JavaneseYearCycle:
    year_number = _ASAPON_ANCHOR_JAVANESE_YEAR
    hijri_year = _ASAPON_ANCHOR_HIJRI_YEAR
    year_start_date = _ASAPON_ANCHOR_DATE

    while True:
        year_length_days = _asapon_anchor_year_length(hijri_year, year_number)
        next_year_start_date = year_start_date + timedelta(days=year_length_days)
        if target_date < next_year_start_date:
            return _build_year_cycle(year_number, year_start_date, next_year_start_date, year_length_days)

        year_number += 1
        hijri_year += 1
        year_start_date = next_year_start_date


def _is_hijri_leap_year(hijri_year: int) -> bool:
    cycle_position = (hijri_year - 1) % 30 + 1
    return cycle_position in _HIJRI_LEAP_YEAR_POSITIONS


def _asapon_anchor_year_length(hijri_year: int, year_number: int) -> int:
    if hijri_year == _ASAPON_ANCHOR_HIJRI_YEAR or year_number == _ASAPON_ANCHOR_JAVANESE_YEAR:
        return 354
    return 355 if _is_hijri_leap_year(hijri_year) else 354


def _javanese_year_length_pre_asapon(year_number: int) -> int:
    kurup = _kurup_for_year(year_number)
    if kurup is None:
        raise ValueError(f"Tahun Jawa {year_number} berada di luar rentang kurup yang dikenal sistem ini.")

    leap_years = kurup["leap_years"]
    if leap_years is None:
        raise ValueError(f"Tahun Jawa {year_number} membutuhkan jangkar modern, bukan tabel pra-Asapon.")

    if year_number in (1746, 1866):
        return 354

    year_name = _year_name(year_number)
    return 355 if year_name in leap_years else 354
