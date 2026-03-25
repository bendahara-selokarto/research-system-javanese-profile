from __future__ import annotations

from calendar import isleap
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
LAMBANG_BY_WINDU = {
    "Kuntara": "Kulawu",
    "Sangara": "Langkir",
    "Sengara": "Langkir",
    "Sancaya": "Kulawu",
    "Adi": "Langkir",
}
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

PRANATA_MANGSA_DEFINITIONS = (
    {
        "name": "Kasa",
        "season": "Katiga",
        "candra": "Sotya murca saka embanan",
        "natural_signs": "Daun-daun mulai berguguran dan udara cenderung kering terang.",
        "farming_guidance": "Biasanya dipakai untuk membersihkan sisa jerami dan mulai menanam palawija.",
        "duration_days": 41,
    },
    {
        "name": "Karo",
        "season": "Katiga",
        "candra": "Bantala rengka",
        "natural_signs": "Tanah mulai retak dan hawa panas terasa lebih keras.",
        "farming_guidance": "Petani menjaga palawija dan mulai mengantisipasi masa paceklik.",
        "duration_days": 23,
    },
    {
        "name": "Katelu",
        "season": "Katiga",
        "candra": "Suta manut ing bapa",
        "natural_signs": "Kemarau mencapai puncaknya dan air makin terbatas.",
        "farming_guidance": "Masa yang lazim dikaitkan dengan panen palawija dan penghematan air.",
        "duration_days": 24,
    },
    {
        "name": "Kapat",
        "season": "Labuh",
        "candra": "Waspa kumembeng jroning kalbu",
        "natural_signs": "Kemarau mulai surut dan tanda-tanda pancaroba mulai tampak.",
        "farming_guidance": "Sawah disiapkan untuk persemaian dan penataan lahan awal.",
        "duration_days": 25,
    },
    {
        "name": "Kalima",
        "season": "Labuh",
        "candra": "Pancuran emas sumawur ing jagad",
        "natural_signs": "Udara mulai basah dan aliran air mulai lebih mudah dijumpai.",
        "farming_guidance": "Umumnya dipakai untuk mengolah sawah, memperbaiki irigasi, dan menyebar padi gogo.",
        "duration_days": 27,
    },
    {
        "name": "Kanem",
        "season": "Labuh",
        "candra": "Rasa mulyo kasucian",
        "natural_signs": "Sawah kembali hijau dan air mulai mengalir lebih jernih.",
        "farming_guidance": "Petani mulai membajak sawah dan menyiapkan tanam utama.",
        "duration_days": 43,
    },
    {
        "name": "Kapitu",
        "season": "Rendheng",
        "candra": "Wisa kentaring maruta",
        "natural_signs": "Curah hujan tinggi, angin kuat, dan sungai kerap meluap.",
        "farming_guidance": "Bibit lazim mulai disemai di pawinihan saat air melimpah.",
        "duration_days": 43,
    },
    {
        "name": "Kawolu",
        "season": "Rendheng",
        "candra": "Anjrah jroning kayun",
        "natural_signs": "Tanaman sawah menghijau dan batang padi mulai meninggi.",
        "farming_guidance": "Fokus berpindah ke perawatan tanaman dan pengaturan air sawah.",
        "duration_days": 26,
        "leap_duration_days": 27,
    },
    {
        "name": "Kasanga",
        "season": "Rendheng",
        "candra": "Wedaring wacara mulyo",
        "natural_signs": "Sebagian padi mulai berbunga dan sebagian lain mulai berbuah.",
        "farming_guidance": "Masa ini biasa dipakai untuk menjaga fase pengisian bulir dan hama.",
        "duration_days": 25,
    },
    {
        "name": "Kasadasa",
        "season": "Mareng",
        "candra": "Gedhong minep jroning kalbu",
        "natural_signs": "Padi mulai menguning dan udara bergerak menuju akhir musim hujan.",
        "farming_guidance": "Saat yang lazim dianggap tepat untuk panen padi gogo awal.",
        "duration_days": 24,
    },
    {
        "name": "Dhesta",
        "season": "Mareng",
        "candra": "Sotya sinara wedi",
        "natural_signs": "Telur burung mulai menetas dan panen padi mulai berlangsung.",
        "farming_guidance": "Panen makin aktif sambil bersiap menghadapi kemarau berikutnya.",
        "duration_days": 23,
    },
    {
        "name": "Sadha",
        "season": "Mareng",
        "candra": "Tirta sah saking sasana",
        "natural_signs": "Udara pagi terasa dingin dan sawah tinggal batang padi kering.",
        "farming_guidance": "Padi dijemur dan dimasukkan ke lumbung sebelum siklus kembali ke Kasa.",
        "duration_days": 41,
    },
)


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
    lambang_name: str
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
class JavanesePranataMangsa:
    index: int
    name: str
    season: str
    candra: str
    natural_signs: str
    farming_guidance: str
    duration_days: int
    cycle_start_year: int
    start_date: date
    end_date: date

    @property
    def formatted(self) -> str:
        return f"Mangsa {self.name}"

    @property
    def period(self) -> str:
        return f"{self.start_date.isoformat()} s.d. {self.end_date.isoformat()}"


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
    pranata_mangsa: JavanesePranataMangsa
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


@dataclass(frozen=True, slots=True)
class JavaneseCalculationStep:
    section: str
    title: str
    formula: str
    result: str
    note: str | None = None


@dataclass(frozen=True, slots=True)
class JavaneseManualCalculation:
    target_date: date
    weton_jawa: str
    summary: str
    steps: tuple[JavaneseCalculationStep, ...]


@dataclass(frozen=True, slots=True)
class JavaneseBibliographyEntry:
    topic: str
    source_kind: str
    citation: str
    applies_to: str
    note: str
    url: str | None = None


JAVANESE_PROFILE_BIBLIOGRAPHY = (
    JavaneseBibliographyEntry(
        topic="Kalender Jawa Sultan Agungan",
        source_kind="external",
        citation='Kraton Yogyakarta, "Kalender Jawa Sultan Agungan"',
        applies_to="Tanggal Jawa lunar, kesinambungan angka Saka, dan jangkar 1 Sura 1555 AJ.",
        note="Dipakai sebagai basis historis bahwa reformasi Sultan Agung mempertahankan angka Saka tetapi memakai logika lunar yang selaras dengan Hijriyah.",
        url="https://www.kratonjogja.id/ragam/21-kalender-jawa-sultan-agungan/",
    ),
    JavaneseBibliographyEntry(
        topic="Lambang windu",
        source_kind="external",
        citation='Karjanto dan Beauducel, "An ethnoarithmetic excursion into the Javanese calendar"',
        applies_to="Pasangan nama windu dengan lambang Kulawu atau Langkir.",
        note="Dipakai untuk mengikat label lambang ke windu setelah parity awal diverifikasi oleh sumber Kraton.",
        url="https://arxiv.org/abs/2012.10064",
    ),
    JavaneseBibliographyEntry(
        topic="Verifikasi kurup modern",
        source_kind="external",
        citation='Kraton Yogyakarta, "Hajad Kawula Dalem Mubeng Beteng 1 Sura Jimawal 1957"',
        applies_to="Verifikasi bahwa 2023-07-19 jatuh pada 1 Sura Jimawal 1957.",
        note="Dipakai untuk menguji jangkar modern sistem terhadap publikasi Kraton.",
        url="https://www.kratonjogja.id/peristiwa/1274-hajad-kawula-dalem-mubeng-beteng-1-sura-jimawal-1957-kembali-diselenggarakan-secara-langsung/",
    ),
    JavaneseBibliographyEntry(
        topic="Kurup dan taun wuntu/wastu",
        source_kind="external",
        citation='UIN Maulana Malik Ibrahim Malang, "Penyesuaian Kalender Saka dengan Kalender Hijriyah dan Aplikasinya dalam Penentuan Awal Bulan Qomariyah"',
        applies_to="Urutan kurup dan pola taun panjang pada fase Aahgi, Amiswon, Aboge, dan Asapon.",
        note="Repo memakai sumber ini untuk membedakan pola taun panjang per kurup, lalu menurunkannya ke aturan hitung modern.",
        url="https://syariah.uin-malang.ac.id/ar/penyesuaian-kalender-saka-dengan-kalender-hijriyah-dan-aplikasinya-dalam-penentuan-awal-bulan-qomariyah/",
    ),
    JavaneseBibliographyEntry(
        topic="Akulturasi Saka-Hijriyah",
        source_kind="external",
        citation='Garuda Kemdikbud, "Pengaruh Islam Terhadap Kalender Masyarakat Jawa"',
        applies_to="Konteks perubahan kalender Jawa dari basis Saka ke sistem lunar Islam-Jawa.",
        note="Dipakai sebagai sumber pendukung untuk menjelaskan reformasi kalender, bukan sebagai tabel hitung utama.",
        url="https://download.garuda.kemdikbud.go.id/article.php?article=1093555&title=Pengaruh+Islam+Terhadap+Kalender+Masyarakat+Jawa&val=6177",
    ),
    JavaneseBibliographyEntry(
        topic="Pranata mangsa",
        source_kind="external",
        citation="Ahmad Musta'id, Journal of Islamic History, 2021",
        applies_to="Urutan mangsa, candra, tanda alam, dan panduan tani.",
        note="Dipakai untuk isi deskriptif setiap mangsa dalam sistem.",
        url="https://download.garuda.kemdikbud.go.id/article.php?article=2910641&title=Perubahan+Perilaku+Masyarakat+Petani+Muslim+Undaan+Kudus+terhadap+Sistem+Penanggalan+Jawa+Pranata+Mangsa+2000-2018+Changes+in+the+Behavior+of+the+Undaan+Kudus+Muslim+Farming+Society+towards+the+Pranata+Mangsa+Javanese+Calendar+System+2000-2018&val=25538",
    ),
    JavaneseBibliographyEntry(
        topic="Pranata mangsa modern",
        source_kind="external",
        citation='Riszky Dwi Wirastuti dkk., "Nilai Luhur Pranata Mangsa dalam Sistem Pertanian Modern", Jurnal Hijau Cendekia, 2016',
        applies_to="Panjang mangsa yang tidak seragam dan konteks pranata mangsa sebagai kalender musim.",
        note="Dipakai sebagai pembanding terhadap tabel panjang mangsa yang dipakai repo.",
        url="https://download.garuda.kemdikbud.go.id/article.php?article=964870&title=NILAI+LUHUR+PRANATA+MANGSA+DALAM+SISTEM+PERTANIAN+MODERN&val=14841",
    ),
    JavaneseBibliographyEntry(
        topic="Kawolu tahun kabisat",
        source_kind="external",
        citation='Sustainability (MDPI), "Adaptation to Extreme Hydrological Events by Javanese Society through Local Knowledge", 2020',
        applies_to="Validasi bahwa siklus pranata mangsa dimulai sekitar 22 Juni dan Kawolu menjadi 27 hari pada tahun kabisat.",
        note="Dipakai untuk memverifikasi pengecualian Februari kabisat pada mangsa Kawolu.",
        url="https://www.mdpi.com/2071-1050/12/24/10373",
    ),
    JavaneseBibliographyEntry(
        topic="Naga dina sebagai keluarga petungan",
        source_kind="external",
        citation="ENGGANG: Jurnal Pendidikan, Bahasa, Sastra, Seni, dan Budaya",
        applies_to="Konteks bahwa naga dina, naga sasi, dan naga taun hidup sebagai petungan budaya.",
        note="Dipakai untuk menempatkan modul naga dina sebagai satu keluarga petungan, bukan rumus tunggal yang universal.",
        url="https://e-journal.upr.ac.id/index.php/enggang/article/view/7810",
    ),
    JavaneseBibliographyEntry(
        topic="Varian naga dina default",
        source_kind="external",
        citation='Sofiatul Annisa, "Mitos Asal-Usul Sen-Essen Jhabah dalam Tradisi Menentukan Hari Baik di Desa Ajung Kabupaten Jember", Repository Universitas Jember, 2017',
        applies_to="Pemetaan posisi naga berdasarkan dinapitu dan pasaran.",
        note="Dipakai untuk varian default sistem yang memisahkan arah hari dan arah pasaran.",
        url="https://repository.unej.ac.id/handle/123456789/80671",
    ),
    JavaneseBibliographyEntry(
        topic="Varian naga dina pembanding",
        source_kind="external",
        citation='"Tradisi Kenduri Boyongan di Desa Pojokrejo Kecamatan Kesamben Kabupaten Jombang", Repository Universitas Jember, 2022',
        applies_to="Perputaran arah sial dari jumlah neptu hari dan pasaran.",
        note="Dipakai untuk varian pembanding boyongan-neptu yang tetap ditampilkan di output.",
        url="https://repository.unej.ac.id/handle/123456789/111352",
    ),
    JavaneseBibliographyEntry(
        topic="Watak weton",
        source_kind="internal",
        citation="Aturan editorial repo pada konstanta WETON_WATAK",
        applies_to="Deskripsi singkat watak per kombinasi weton.",
        note="Belum ditautkan ke satu pustaka primer atau sekunder tertentu; gunakan sebagai ringkasan bantu, bukan otoritas final.",
    ),
    JavaneseBibliographyEntry(
        topic="Jenjem pasangan dan hari baik",
        source_kind="internal",
        citation="Aturan internal repo pada COMPATIBILITY_RULES dan EVENT_GUIDELINES",
        applies_to="Kategori kecocokan pasangan dan rentang jenjem untuk acara yang didukung CLI.",
        note="Ini adalah penyederhanaan operasional repo agar aturan bisa diaudit. Bukan klaim standar tunggal seluruh tradisi Jawa.",
    ),
)


def javanese_profile_bibliography(
    include_internal: bool = True,
) -> tuple[JavaneseBibliographyEntry, ...]:
    if include_internal:
        return JAVANESE_PROFILE_BIBLIOGRAPHY
    return tuple(
        entry
        for entry in JAVANESE_PROFILE_BIBLIOGRAPHY
        if entry.source_kind != "internal"
    )


def manual_calculation_detail(
    value: date | datetime | str,
    partner: date | datetime | str | None = None,
    events: tuple[str, ...] | list[str] | None = None,
) -> JavaneseManualCalculation:
    target_date = _coerce_date(value)
    partner_date = _coerce_date(partner) if partner is not None else None
    events_to_check = tuple(events) if events is not None else tuple(EVENT_GUIDELINES)
    identity = javanese_calendar_cycles(target_date)
    steps: list[JavaneseCalculationStep] = []
    weekday_index = target_date.weekday()
    pasaran_index = identity.days_since_epoch % len(PASARAN_NAMES)
    pawukon_index = identity.pawukon_day - 1
    selapan_day = identity.days_since_epoch % SELAPAN_CYCLE_DAYS + 1

    steps.extend(
        (
            JavaneseCalculationStep(
                section="Weton inti",
                title="Offset hari dari epoch",
                formula=f"({target_date.isoformat()} - {JAVANESE_CALENDAR_EPOCH.isoformat()}).days",
                result=f"{identity.days_since_epoch} hari",
                note="Offset yang sama dipakai untuk pasaran, pawukon, dan selapan.",
            ),
            JavaneseCalculationStep(
                section="Weton inti",
                title="Hari tujuhan",
                formula=f"weekday index {weekday_index} -> {GREGORIAN_WEEKDAYS[weekday_index]} / {JAVANESE_DINAPITU[weekday_index]}",
                result=f"{identity.hari} / {identity.dinapitu}",
            ),
            JavaneseCalculationStep(
                section="Weton inti",
                title="Pasaran",
                formula=f"{identity.days_since_epoch} mod {len(PASARAN_NAMES)} = {pasaran_index}",
                result=identity.pasaran,
            ),
            JavaneseCalculationStep(
                section="Weton inti",
                title="Neptu weton",
                formula=f"{identity.dinapitu}({identity.hari_neptu}) + {identity.pasaran}({identity.pasaran_neptu})",
                result=f"{identity.neptu_total}",
            ),
            JavaneseCalculationStep(
                section="Weton inti",
                title="Wuku",
                formula=f"({identity.days_since_epoch} + {_EPOCH_PAWUKON_INDEX}) mod 210 = {pawukon_index}",
                result=identity.wuku,
            ),
            JavaneseCalculationStep(
                section="Weton inti",
                title="Posisi selapan",
                formula=f"({identity.days_since_epoch} mod {SELAPAN_CYCLE_DAYS}) + 1 = {selapan_day}",
                result=f"Selapan ke-{selapan_day}",
            ),
        )
    )

    if identity.year_cycle is not None and identity.javanese_date is not None and identity.hijri_date is not None:
        year_cycle = identity.year_cycle
        day_of_year = (target_date - year_cycle.year_start_date).days
        month_lengths = _lunar_month_lengths(year_cycle.year_length_days)
        anchor_mode = (
            "jangkar Asapon modern"
            if target_date >= _ASAPON_ANCHOR_DATE
            else "epoch Sultan Agungan"
        )
        steps.extend(
            (
                JavaneseCalculationStep(
                    section="Siklus taun Jawa",
                    title="Jalur jangkar hitung",
                    formula=f"Bandingkan {target_date.isoformat()} dengan {_ASAPON_ANCHOR_DATE.isoformat()}",
                    result=anchor_mode,
                    note="Tanggal modern memakai jalur Asapon 1936; tanggal lebih awal dilacak dari epoch 1633.",
                ),
                JavaneseCalculationStep(
                    section="Siklus taun Jawa",
                    title="Rentang taun aktif",
                    formula=f"{year_cycle.year_start_date.isoformat()} <= tanggal < {year_cycle.next_year_start_date.isoformat()}",
                    result=(
                        f"{year_cycle.year_name} {year_cycle.year_number} / "
                        f"{year_cycle.year_type} / lambang {year_cycle.lambang_name} / "
                        f"kurup {year_cycle.kurup_code}"
                    ),
                ),
                JavaneseCalculationStep(
                    section="Siklus taun Jawa",
                    title="Posisi dalam windu dan lambang",
                    formula=(
                        f"({year_cycle.year_number} - {_EPOCH_JAVANESE_YEAR}) mod {len(JAVANESE_YEAR_NAMES)} + 1 = "
                        f"{year_cycle.windu_year_number}"
                    ),
                    result=(
                        f"Windu {year_cycle.windu_name}, lambang {year_cycle.lambang_name}, "
                        f"taun ke-{year_cycle.windu_year_number}"
                    ),
                ),
                JavaneseCalculationStep(
                    section="Siklus taun Jawa",
                    title="Tanggal Jawa dan Hijriyah",
                    formula=f"Offset {day_of_year} hari ditelusuri pada panjang bulan {month_lengths}",
                    result=f"{identity.javanese_date.formatted} / {identity.hijri_date.formatted}",
                ),
            )
        )
    else:
        steps.append(
            JavaneseCalculationStep(
                section="Siklus taun Jawa",
                title="Ketersediaan data taun",
                formula="Tanggal berada di luar rentang kurup baku yang diimplementasikan sistem",
                result="Nama taun, windu, lambang, dan kurup exact tidak ditampilkan",
            )
        )

    pranata = identity.pranata_mangsa
    cycle_start = date(pranata.cycle_start_year, 6, 22)
    steps.extend(
        (
            JavaneseCalculationStep(
                section="Pranata mangsa",
                title="Mulai siklus mangsa",
                formula=(
                    f"Jika tanggal >= {pranata.cycle_start_year}-06-22 maka siklus memakai tahun {pranata.cycle_start_year}; "
                    "jika tidak, tahun sebelumnya"
                ),
                result=cycle_start.isoformat(),
            ),
            JavaneseCalculationStep(
                section="Pranata mangsa",
                title="Mangsa aktif",
                formula=f"{pranata.start_date.isoformat()} <= tanggal <= {pranata.end_date.isoformat()}",
                result=f"{pranata.formatted} / {pranata.season} / {pranata.duration_days} hari",
                note=pranata.candra,
            ),
        )
    )

    naga = identity.naga_dina
    steps.extend(
        (
            JavaneseCalculationStep(
                section="Naga dina",
                title="Arah hari",
                formula=f"{identity.dinapitu} -> tabel pepali arah",
                result=_format_directions(naga.day_directions),
            ),
            JavaneseCalculationStep(
                section="Naga dina",
                title="Arah pasaran",
                formula=f"{identity.pasaran} -> tabel pasaran",
                result=naga.pasaran_direction,
            ),
            JavaneseCalculationStep(
                section="Naga dina",
                title="Arah varian boyongan-neptu",
                formula=(
                    f"({identity.neptu_total} - 1) mod {len(NAGA_DINA_NEPTU_ROTATION)} -> "
                    f"urutan {'-'.join(NAGA_DINA_NEPTU_ROTATION)}"
                ),
                result=naga.neptu_cycle_direction,
            ),
        )
    )

    if partner_date is not None:
        partner_identity = javanese_calendar_cycles(partner_date)
        compatibility = compatibility_result(target_date, partner_date)
        steps.extend(
            (
                JavaneseCalculationStep(
                    section="Kecocokan pasangan",
                    title="Neptu pasangan",
                    formula=(
                        f"{target_date.isoformat()} = {identity.weton_jawa}({identity.neptu_total}); "
                        f"{partner_date.isoformat()} = {partner_identity.weton_jawa}({partner_identity.neptu_total})"
                    ),
                    result=f"{compatibility.first_weton} + {compatibility.second_weton}",
                ),
                JavaneseCalculationStep(
                    section="Kecocokan pasangan",
                    title="Jenjem gabungan",
                    formula=f"{identity.neptu_total} + {partner_identity.neptu_total}",
                    result=f"{compatibility.jenjem_sum} -> {compatibility.category}",
                    note=compatibility.recommendation,
                ),
            )
        )

    for event in events_to_check:
        guideline = EVENT_GUIDELINES[event]
        low, high = guideline["range"]
        advice = hari_baik_advice(target_date, event)
        steps.append(
            JavaneseCalculationStep(
                section="Hari baik",
                title=f"Acara {event}",
                formula=f"{low} <= neptu {identity.neptu_total} <= {high}",
                result="Baik" if advice.is_good else "Tidak baik",
                note=f"{advice.reason} {advice.note}",
            )
        )

    summary = (
        f"{target_date.isoformat()} dihitung sebagai {identity.weton_jawa} dengan neptu {identity.neptu_total}, "
        f"wuku {identity.wuku}, dan pranata mangsa {pranata.name}."
    )
    return JavaneseManualCalculation(
        target_date=target_date,
        weton_jawa=identity.weton_jawa,
        summary=summary,
        steps=tuple(steps),
    )


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
    pranata_mangsa = _build_pranata_mangsa(target_date)
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
        pranata_mangsa=pranata_mangsa,
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


def javanese_pranata_mangsa(value: date | datetime | str) -> JavanesePranataMangsa:
    return javanese_calendar_cycles(value).pranata_mangsa


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
    pranata_mangsa = identity.pranata_mangsa
    supported_events = ("nikah", "rumah", "usaha", "tanam", "selamatan")
    event_snapshot = ", ".join(
        f"{event} {'baik' if hari_baik_advice(identity.gregorian_date, event).is_good else 'tidak'}"
        for event in supported_events
    )
    summary = (
        f"{identity.gregorian_date.isoformat()} = {identity.weton_jawa}, "
        f"wuku {identity.wuku}, neptu {identity.neptu_total}, "
        f"pranata mangsa {pranata_mangsa.name} ({pranata_mangsa.season})"
    )
    if identity.javanese_date is not None and identity.hijri_date is not None:
        summary += (
            f", tanggal Jawa {identity.javanese_date.formatted}, "
            f"Hijriyah {identity.hijri_date.formatted}"
        )
    if identity.year_cycle is not None:
        summary += (
            f", taun {identity.year_cycle.year_name} {identity.year_cycle.year_number}, "
            f"windu {identity.year_cycle.windu_name}, lambang {identity.year_cycle.lambang_name}, "
            f"kurup {identity.year_cycle.kurup_code}."
        )
        year_cycle_description = (
            f"Tanggal {identity.gregorian_date.isoformat()} masuk taun {identity.year_cycle.year_name} "
            f"{identity.year_cycle.year_number}, windu {identity.year_cycle.windu_name}, "
            f"lambang {identity.year_cycle.lambang_name}, kurup {identity.year_cycle.kurup_code}."
        )
    else:
        summary += "."
        year_cycle_description = (
            f"Tanggal {identity.gregorian_date.isoformat()} belum terpetakan ke taun, windu, lambang, dan kurup exact di sistem ini."
        )

    naga_dina_description = (
        f"Untuk {identity.weton_jawa}, varian default sistem menempatkan {identity.dinapitu} di "
        f"{_format_directions(naga_dina.day_directions)}; {identity.pasaran} di {naga_dina.pasaran_direction}; "
        f"varian boyongan-neptu dengan jumlah {naga_dina.neptu_cycle_total} mengarah ke {naga_dina.neptu_cycle_direction}."
    )
    pranata_mangsa_description = (
        f"Tanggal {identity.gregorian_date.isoformat()} masuk {pranata_mangsa.formatted} "
        f"({pranata_mangsa.season}) pada rentang {pranata_mangsa.period}. "
        f"Candra-nya adalah '{pranata_mangsa.candra}'. Tanda alam yang biasa dikaitkan: "
        f"{pranata_mangsa.natural_signs} Dalam praktik tani, fase ini kerap dipakai untuk "
        f"{pranata_mangsa.farming_guidance.lower()}"
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
            example_question=(
                f"Tahun Jawa untuk {identity.gregorian_date.isoformat()} masuk taun apa, windu apa, dan lambang apa?"
            ),
        ),
        JavaneseCulturalUse(
            category="pranata_mangsa",
            description=pranata_mangsa_description,
            example_question=f"Tanggal {identity.gregorian_date.isoformat()} masuk mangsa apa dalam pranata mangsa?",
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


def _build_pranata_mangsa(target_date: date) -> JavanesePranataMangsa:
    cycle_start_year = target_date.year if (target_date.month, target_date.day) >= (6, 22) else target_date.year - 1
    current_start = date(cycle_start_year, 6, 22)
    has_leap_february = isleap(cycle_start_year + 1)

    for index, definition in enumerate(PRANATA_MANGSA_DEFINITIONS, start=1):
        duration_days = definition["duration_days"]
        if has_leap_february and "leap_duration_days" in definition:
            duration_days = definition["leap_duration_days"]

        current_end = current_start + timedelta(days=duration_days - 1)
        if current_start <= target_date <= current_end:
            return JavanesePranataMangsa(
                index=index,
                name=definition["name"],
                season=definition["season"],
                candra=definition["candra"],
                natural_signs=definition["natural_signs"],
                farming_guidance=definition["farming_guidance"],
                duration_days=duration_days,
                cycle_start_year=cycle_start_year,
                start_date=current_start,
                end_date=current_end,
            )
        current_start = current_end + timedelta(days=1)

    raise ValueError(
        f"Tanggal {target_date.isoformat()} tidak masuk ke siklus pranata mangsa yang diimplementasikan."
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


def _lambang_name_for_windu(windu_name: str) -> str:
    try:
        return LAMBANG_BY_WINDU[windu_name]
    except KeyError as exc:
        raise ValueError(f"Windu '{windu_name}' belum punya mapping lambang di sistem ini.") from exc


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
    lambang_name = _lambang_name_for_windu(windu_name)
    return JavaneseYearCycle(
        year_number=year_number,
        saka_continuity_year=year_number,
        year_name=_year_name(year_number),
        year_type="Taun Wuntu" if year_length_days == 355 else "Taun Wastu",
        year_length_days=year_length_days,
        year_start_date=year_start_date,
        next_year_start_date=next_year_start_date,
        windu_name=windu_name,
        lambang_name=lambang_name,
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
