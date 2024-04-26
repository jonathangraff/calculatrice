from app.errors import StringInvalid

import csv
import sqlite3
import os


operations = {
    "+": float.__add__,
    "-": float.__sub__,
    "*": float.__mul__,
    "/": float.__truediv__,
}

data_directory = 'data'


def calculate_from_str(calculation: str) -> float:
    """
    This function takes a string representing the calculation to compute and returns the answer
    :param calculation: the string, each value being separated by a space
    :return: a float, the computation made
    """
    calculation_list = calculation.split()
    for index, car in enumerate(calculation_list):
        if car not in operations:
            calculation_list[index] = float(car)
    try:
        result = _calculate_from_list(calculation_list)
    except StringInvalid:
        raise StringInvalid(calculation)
    _store_result_in_bdd(calculation, result)
    return result


def _calculate_from_list(calculation: list) -> float:

    pile = calculation[:2]
    for i in range(2, len(calculation)):
        if calculation[i] in operations:
            try:
                x, y = pile.pop(), pile.pop()
                pile.append(operations[calculation[i]](y, x))
            except IndexError:
                raise StringInvalid()
        else:
            pile.append(calculation[i])
    if len(pile) != 1 or pile[0] in operations:
        raise StringInvalid()
    return pile[0]


def _store_result_in_bdd(calculation: str, result: float) -> None:

    if not os.path.exists(data_directory):
        os.mkdir(data_directory)

    conn = sqlite3.connect(data_directory + '/calculation_results.db')
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


def _get_data_rows_from_bdd() -> list[tuple[str, float]]:
    conn = sqlite3.connect(data_directory + '/calculation_results.db')
    try:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT * FROM calculations"""
        )
        rows = cursor.fetchall()
    finally:
        conn.close()
    return rows


def create_csv_with_data() -> None:
    """
    This function creates a cvs file named 'data.csv'
    :return: None
    """
    rows = _get_data_rows_from_bdd()
    with open(data_directory + "/data.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
