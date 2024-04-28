from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float


class Base(DeclarativeBase):
    pass


class Calculation(Base):
    __tablename__ = 'calculation'
    id = Column(Integer, primary_key=True)
    calculation = Column(String)
    result = Column(Float)

    def __repr__(self) -> str:
        return f"Calculation(id={self.id}, calculation={self.calculation}, result={self.result})"
