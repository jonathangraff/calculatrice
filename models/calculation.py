from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Calculation(Base):
    __tablename__ = 'calculation'
    id = Column(Integer, primary_key=True)
    calculation = Column(String)
    result = Column(Float)
