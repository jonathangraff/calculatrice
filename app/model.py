from pydantic import BaseModel


class Calculation(BaseModel):
    calculation: str
