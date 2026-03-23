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
    marriage_jenjem,
)


def test_epoch_matches_sultan_agungan_anchor() -> None:
    result = javanese_calendar_cycles("1633-07-08")

    assert result.hari == "Jumat"
    assert result.dinapitu == "Jemuwah"
    assert result.weton == "Jumat Legi"
    assert result.wuku == "Kulawu"
    assert result.neptu_total == 11


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


def test_day_profile_bundle_and_selapan() -> None:
    profile = javanese_day_profile("1990-04-25")

    assert profile.summary == "1990-04-25 = Rebo Pon, wuku Julungpujut, neptu 14."
    assert profile.selapan_cycle_days == 35
    assert profile.selapan_day == 13
    assert profile.next_weton_date == date(1990, 5, 30)
    assert profile.next_three_weton_dates == (date(1990, 5, 30), date(1990, 7, 4), date(1990, 8, 8))
    assert profile.identity.weton_jawa == "Rebo Pon"
    assert any("watak" in use.description for use in profile.common_uses)


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
