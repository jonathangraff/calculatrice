from models.calculation import Calculation
from models.calculation import Base
import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

data_directory = 'data'
database_name = 'calculation_results.db'
database_path = '/'.join([data_directory, database_name])
csv_data_name = 'data.csv'
csv_data_path = '/'.join([data_directory, csv_data_name])


def store_result_in_bdd(calculation: str, result: float) -> None:
    if not os.path.exists(data_directory):
        os.mkdir(data_directory)

    engine = create_engine('sqlite:///' + database_path)

    if not os.path.exists(database_path):
        Base.metadata.create_all(engine)
    with Session(engine) as session:
        calculation_line = Calculation(calculation=calculation, result=result)
        session.add(calculation_line)
        session.commit()


def create_csv_with_data() -> None:
    """
    This function creates a cvs file
    :return: None
    """
    calc_tuples = _get_data_tuples_from_bdd()
    with open(csv_data_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for calc_tuple in calc_tuples:
            writer.writerow(calc_tuple)


def _get_data_tuples_from_bdd() -> list[tuple[int, str, float]]:
    rows = _get_data_rows_from_bdd()
    tuples = []
    for row in rows:
        tuples.append((row.id, row.calculation, row.result))
    return tuples


def _get_data_rows_from_bdd() -> list[type(Calculation)]:
    engine = create_engine('sqlite:///' + database_path)
    with Session(engine) as session:
        query = session.query(Calculation)
        rows = query.all()
    return rows
