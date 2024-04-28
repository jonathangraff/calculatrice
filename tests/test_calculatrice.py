from app.calculatrice import calculate_from_str
from app.errors import InvalidString, InvalidCharacter, DivisionByZero
import pytest


@pytest.mark.parametrize(
    "calculation, answer", (
        ("1", 1),
        ("1 2 +", 3),
        ("5.8 2.3 -", 3.5),
        ("3 2 5 * + 8 7 + +", 28),
        ("27 9 /", 3),
        ("15 5 3 - -", 13),
        ("12 -3 +", 9),
    )
)
def test_calculate_works(calculation, answer):
    assert calculate_from_str(calculation) == answer


@pytest.mark.parametrize(
    "calculation",
    (
        "1 +",
        "+",
        "3 2 + *",
        "1 2 3 +",
    )
)
def test_error_invalid_string(calculation):
    with pytest.raises(InvalidString):
        calculate_from_str(calculation)


@pytest.mark.parametrize(
    "calculation",
    (
        "1 !",
        "z",
        "ab -1 + ",
        "1 2 x +",
    )
)
def test_error_invalid_character(calculation):
    with pytest.raises(InvalidCharacter):
        calculate_from_str(calculation)


@pytest.mark.parametrize(
    "calculation",
    (
        "1 0 /",
        "2 3 3 - /",
        "1 2 -2 + / 3 +",
    )
)
def test_error_with_division_by_0(calculation):
    with pytest.raises(DivisionByZero):
        calculate_from_str(calculation)
