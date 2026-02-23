from sqlalchemy import Column, Integer, String, Float, Date
from app.db import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    date = Column(Date, index=True)
    close = Column(Float)

class Signal(Base):
    __tablename__ = "signals"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    momentum_30d = Column(Float)
    volatility_30d = Column(Float)