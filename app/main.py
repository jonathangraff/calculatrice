from app.calculatrice import calculate_from_str
from app.calc_data import create_csv_with_data
from app.model import Calculation

from fastapi import FastAPI


app = FastAPI()


@app.get("/get_data")
async def get_data() -> None:
    create_csv_with_data()


@app.post("/calculate")
async def calculate(calculation: Calculation) -> float:
    return calculate_from_str(calculation.calculation)
