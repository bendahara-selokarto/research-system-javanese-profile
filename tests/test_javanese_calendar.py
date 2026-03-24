from __future__ import annotations

from datetime import date, datetime

import pytest

from research_system.utils import (
    EVENT_GUIDELINES,
    compatibility_result,
    get_watak_profile,
    hari_baik_advice,
    javanese_calendar_cycles,
    javanese_day_profile,
    javanese_naga_dina,
    javanese_year_cycle,
    marriage_jenjem,
)



def test_epoch_matches_sultan_agungan_anchor() -> None:
    result = javanese_calendar_cycles("1633-07-08")

    assert result.hari == "Jumat"
    assert result.dinapitu == "Jemuwah"
    assert result.weton == "Jumat Legi"
    assert result.wuku == "Kulawu"
    assert result.neptu_total == 11
    assert result.year_cycle is not None
    assert result.year_cycle.year_number == 1555
    assert result.year_cycle.year_name == "Alip"
    assert result.year_cycle.windu_name == "Kuntara"
    assert result.year_cycle.kurup_code == "Aahgi"
    assert result.javanese_date is not None
    assert result.javanese_date.formatted == "1 Sura 1555 AJ"
    assert result.hijri_date is not None
    assert result.hijri_date.formatted == "1 Muharram 1043 H"



def test_kurup_asapon_anchor_matches_falak_reference() -> None:
    result = javanese_year_cycle("1936-03-25")

    assert result is not None
    assert result.year_number == 1867
    assert result.year_name == "Alip"
    assert result.kurup_code == "Asapon"
    assert result.year_start_date == date(1936, 3, 25)



def test_kraton_reference_for_1_sura_jimawal_1957() -> None:
    result = javanese_year_cycle("2023-07-19")

    assert result is not None
    assert result.year_number == 1957
    assert result.year_name == "Jimawal"
    assert result.kurup_code == "Asapon"
    assert result.year_start_date == date(2023, 7, 19)



def test_lunar_dates_follow_javanese_and_hijri_year_start() -> None:
    result = javanese_calendar_cycles("2023-07-19")

    assert result.javanese_date is not None
    assert result.javanese_date.formatted == "1 Sura 1957 AJ"
    assert result.hijri_date is not None
    assert result.hijri_date.formatted == "1 Muharram 1445 H"



def test_watak_profile_returns_known_description() -> None:
    description = get_watak_profile("1990-04-25")
    assert "kritis" in description.lower()


@pytest.mark.parametrize(
    ("target_date", "hari", "dinapitu", "neptu", "wuku"),
    [
        (date(1968, 12, 3), "Selasa", "Selasa", 11, "Julungwangi"),
        (date(2020, 10, 1), "Kamis", "Kemis", 16, "Langkir"),
        (date(2021, 8, 10), "Selasa", "Selasa", 10, "Kulawu"),
    ],
)
def test_known_reference_dates_match_published_examples(
    target_date: date,
    hari: str,
    dinapitu: str,
    neptu: int,
    wuku: str,
) -> None:
    result = javanese_calendar_cycles(target_date)
    assert result.hari == hari
    assert result.dinapitu == dinapitu
    assert result.neptu_total == neptu
    assert result.wuku == wuku



def test_naga_dina_supports_default_and_comparison_variants() -> None:
    naga = javanese_naga_dina("1990-04-25")

    assert naga.default_variant_code == "pepali_arah"
    assert naga.default_variant_label == "Pepali arah hari-pasaran"
    assert naga.day_directions == ("Barat Laut",)
    assert naga.pasaran_direction == "Barat"
    assert naga.neptu_cycle_total == 14
    assert naga.neptu_cycle_direction == "Selatan"
    assert {variant.code for variant in naga.variants} == {"pepali_arah", "boyongan_neptu"}



def test_naga_dina_keeps_dual_direction_for_kemis() -> None:
    naga = javanese_naga_dina("2020-10-01")

    assert naga.day_directions == ("Utara", "Timur Laut")
    assert naga.pasaran_direction == "Tengah"



def test_day_profile_bundle_and_selapan() -> None:
    profile = javanese_day_profile("1990-04-25")
    uses = {use.category: use for use in profile.common_uses}

    assert profile.summary.startswith("1990-04-25 = Rebo Pon, wuku Julungpujut, neptu 14")
    assert "Hijriyah 29 Ramadan 1410 H" in profile.summary
    assert "tanggal Jawa 29 Pasa 1922 AJ" in profile.summary
    assert "kurup Asapon" in profile.summary
    assert profile.selapan_cycle_days == 35
    assert profile.selapan_day == 13
    assert profile.next_weton_date == date(1990, 5, 30)
    assert profile.next_three_weton_dates == (date(1990, 5, 30), date(1990, 7, 4), date(1990, 8, 8))
    assert profile.identity.weton_jawa == "Rebo Pon"
    assert profile.identity.year_cycle is not None
    assert profile.identity.javanese_date is not None
    assert profile.identity.javanese_date.month_name == "Pasa"
    assert profile.identity.hijri_date is not None
    assert profile.identity.hijri_date.month_name == "Ramadan"
    assert profile.identity.naga_dina.default_variant_code == "pepali_arah"
    assert profile.identity.naga_dina.neptu_cycle_direction == "Selatan"
    assert "Rebo Pon" in uses["watak_pribadi"].description
    assert "1990-05-30" in uses["ritual_wetonan"].description
    assert str(profile.identity.year_cycle.year_number) in uses["siklus_tahun_jawa"].description
    assert "neptu 14" in uses["kecocokan_jodoh"].description
    assert "nikah" in uses["hari_baik_keputusan"].description
    assert "Barat Laut" in uses["naga_dina"].description
    assert "Selatan" in uses["naga_dina"].description
    assert "Pon" in uses["identitas_sosial"].description



def test_future_dates_keep_year_cycle_information() -> None:
    result = javanese_year_cycle("2053-01-01")
    assert result is not None
    assert result.kurup_code in {"Asapon", "Anenhing"}



def test_marriage_jenjem_and_compatibility() -> None:
    assert marriage_jenjem("2025-01-14", "2025-01-05") == 22
    compatibility = compatibility_result("2025-01-14", "2025-01-05")
    assert compatibility.category == "Netral"
    assert "diskusi" in compatibility.recommendation.lower()



def test_hari_baik_advice_starts_when_supported_event() -> None:
    advice = hari_baik_advice("2021-08-10", "nikah")
    assert advice.event == "nikah"
    assert advice.reason == EVENT_GUIDELINES["nikah"]["reason"]
    assert advice.is_good is False



def test_hari_baik_advice_raises_unknown_event() -> None:
    with pytest.raises(ValueError):
        hari_baik_advice("2021-08-10", "tidak-ada")



def test_accepts_iso_and_datetime_inputs() -> None:
    iso_profile = javanese_day_profile("2021-08-10")
    datetime_profile = javanese_day_profile(datetime(2021, 8, 10, 22, 45, 0))
    assert iso_profile.identity.weton == datetime_profile.identity.weton
    assert iso_profile.identity.javanese_date == datetime_profile.identity.javanese_date
    assert iso_profile.identity.hijri_date == datetime_profile.identity.hijri_date
