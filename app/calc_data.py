import csv
import sqlite3
import os
from sqlalchemy import create_engine

data_directory = 'data'


def store_result_in_bdd(calculation: str, result: float) -> None:

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
