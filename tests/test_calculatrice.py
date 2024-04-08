from app.calculatrice import calculate_from_str
from app.errors import LastCaracterNotOperation, TooManyOperands, NotEnoughOperands
import pytest


@pytest.mark.parametrize(
    "calculation, answer", (
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


def test_error_last_caracter_not_an_operation():
    with pytest.raises(LastCaracterNotOperation):
        calculate_from_str("1 2 + 3")


def test_error_too_many_operand():
    with pytest.raises(TooManyOperands):
        calculate_from_str("1 2 3 +")


@pytest.mark.parametrize(
    "calculation",
    (
        "1 +",
        "+",
        "3 2 + *",
    )
)
def test_error_not_enough_operand(calculation):
    with pytest.raises(NotEnoughOperands):
        calculate_from_str(calculation)
