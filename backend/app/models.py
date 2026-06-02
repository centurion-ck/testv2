from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Threat(Base):
    __tablename__ = "threats"

    id = Column(Integer, primary_key=True, index=True)
    process_name = Column(String(100))
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    prediction = Column(String(50))
    score = Column(Float)