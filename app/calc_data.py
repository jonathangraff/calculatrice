from models.calculation import Calculation

import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

data_directory = 'data'
database_name = 'calculation_results.db'
database_path = '/'.join([data_directory, database_name])
csv_data_name = 'data.csv'
csv_data_path = '/'.join([data_directory, csv_data_name])


def store_result_in_bdd(calculation: str, result: float) -> None:
    if not os.path.exists(data_directory):
        os.mkdir(data_directory)

    engine = create_engine('sqlite://' + database_path)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        calculation = Calculation(calculation=calculation, result=result)
        session.add(calculation)
        session.commit()
    finally:
        session.close()
        engine.dispose()

def create_csv_with_data() -> None:
    """
    This function creates a cvs file named 'data.csv'
    :return: None
    """
    rows = _get_data_rows_from_bdd()
    with open(data_directory + csv_data_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)


def _get_data_rows_from_bdd() -> list[type(Calculation)]:

    engine = create_engine('sqlite://' + database_path)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        query = session.query(Calculation)
        rows = query.all()
    finally:
        session.close()
        engine.dispose()
    return rows
