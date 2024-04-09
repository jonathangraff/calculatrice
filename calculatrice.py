from app.errors import LastCaracterNotOperation, TooManyOperands, NotEnoughOperands

import csv
import sqlite3


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
    result = _calculate_from_list(calculation.split())
    _store_result_in_bdd(calculation, result)
    return result


def _calculate_from_list(calculation: list) -> float:

    last_character = calculation[-1]
    if last_character not in operations:
        if len(calculation) == 1:
            return float(last_character)
        raise LastCaracterNotOperation(last_character)

    index_second_operand = _get_index_operand(calculation[:-1], last_character)
    second_operand = calculation[index_second_operand:-1]
    first_operand = calculation[:index_second_operand]
    if not first_operand:
        raise NotEnoughOperands(' '.join(calculation))
    if _get_index_operand(first_operand, last_character) != 0:
        raise TooManyOperands(' '.join(calculation))
    return _basic_calculation(_calculate_from_list(first_operand), _calculate_from_list(second_operand), last_character)


def _get_index_operand(calculation: list, last_operation) -> int:

    if not calculation:
        raise NotEnoughOperands(' '.join(calculation+[last_operation]))
    nb_characters = 1
    index = len(calculation) - 1
    while nb_characters != 0:
        if calculation[index] in operations:
            nb_characters += 1
        else:
            nb_characters -= 1
        index -= 1
    return index + 1


def _basic_calculation(x: float, y: float, operation: str) -> float:

    return operations[operation](x, y)


def _store_result_in_bdd(calculation, result):

    conn = sqlite3.connect('data/calculation_results.db')
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS calculations(
                 id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                 calculation TEXT,
                 result FLOAT
            )
            """
        )
        cursor.execute(
            """INSERT INTO calculations(calculation, result) VALUES(?, ?)""",
            (calculation, result)
        )
        conn.commit()
    finally:
        conn.close()


def _get_data_rows_from_bdd():
    conn = sqlite3.connect('data/calculation_results.db')
    try:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT * FROM calculations"""
        )
        rows = cursor.fetchall()
    finally:
        conn.close()
    return rows


def create_csv_with_data():
    """
    This function creates a cvs file named 'data.csv'
    :return: None
    """
    rows = _get_data_rows_from_bdd()
    with open("data/data.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
