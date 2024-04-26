from app.errors import InvalidString, InvalidCharacter
from app.calc_data import store_result_in_bdd


operations = {
    "+": float.__add__,
    "-": float.__sub__,
    "*": float.__mul__,
    "/": float.__truediv__,
}


def calculate_from_str(calculation: str) -> float:
    """
    This function takes a string representing the calculation to compute and returns the answer
    :param calculation: the string, each value being separated by a space
    :return: a float, the computation made
    """
    calculation_list = calculation.split()
    calculation_list_with_floats = []
    for car in calculation_list:
        try:
            calculation_list_with_floats.append(float(car))
        except ValueError:
            if car not in operations:
                raise InvalidCharacter(car)
            calculation_list_with_floats.append(car)

    try:
        result = _calculate_from_list(calculation_list_with_floats)
    except InvalidString:
        raise InvalidString(calculation)
    store_result_in_bdd(calculation, result)
    return result


def _calculate_from_list(calculation: list) -> float:

    pile = calculation[:2]
    for i in range(2, len(calculation)):
        if calculation[i] in operations:
            try:
                x, y = pile.pop(), pile.pop()
                pile.append(operations[calculation[i]](y, x))
            except IndexError:
                raise InvalidString()
        else:
            pile.append(calculation[i])
    if len(pile) != 1 or pile[0] in operations:
        raise InvalidString()
    return pile[0]
