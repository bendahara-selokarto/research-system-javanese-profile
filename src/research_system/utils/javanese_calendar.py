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
SELAPAN_CYCLE_DAYS = 35

_EPOCH_PAWUKON_INDEX = WUKU_NAMES.index("Kulawu") * 7 + 5

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

    return JavaneseCalendarCycles(
        gregorian_date=target_date,
        hari=hari,
        dinapitu=dinapitu,
        hari_neptu=hari_neptu,
        pasaran=pasaran,
        pasaran_neptu=pasaran_neptu,
        neptu_total=neptu_total,
        weton=f"{hari} {pasaran}",
        weton_jawa=f"{dinapitu} {pasaran}",
        wuku=wuku,
        days_since_epoch=days_since_epoch,
        pawukon_day=pawukon_index + 1,
    )


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
    summary = (
        f"{identity.gregorian_date.isoformat()} = {identity.weton_jawa}, "
        f"wuku {identity.wuku}, neptu {identity.neptu_total}."
    )

    common_uses = (
        JavaneseCulturalUse(
            category="watak_pribadi",
            description="Weton menjadi dasar menafsirkan watak dan kecenderungan seseorang.",
            example_question=f"Apa watak orang dengan weton {identity.weton_jawa}?",
        ),
        JavaneseCulturalUse(
            category="ritual_wetonan",
            description="Identitas hari digunakan untuk menghitung wetonan, selapanan, atau bancakan.",
            example_question=f"Kapan wetonan berikutnya untuk {identity.weton_jawa}?",
        ),
        JavaneseCulturalUse(
            category="kecocokan_jodoh",
            description="Weton dipasangkan untuk menghitung jenjem dan kecocokan pasangan.",
            example_question=f"Bagaimana kecocokan jodoh {identity.weton_jawa} dengan weton pasangan?",
            requires_additional_input=True,
        ),
        JavaneseCulturalUse(
            category="hari_baik_keputusan",
            description="Petung Jawa dipakai memilih hari baik nikah, rumah, usaha, atau tanam.",
            example_question=(
                f"Hari baik apa untuk nikah, pindah rumah, usaha, atau tanam jika acuannya {identity.weton_jawa}?"
            ),
            requires_additional_input=True,
        ),
        JavaneseCulturalUse(
            category="identitas_sosial",
            description="Pasaran menempel pada identitas sosial dan penamaan keluarga.",
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


def _coerce_date(value: date | datetime | str) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        return date.fromisoformat(value)
    raise TypeError("value must be a datetime.date, datetime.datetime, or ISO date string")
