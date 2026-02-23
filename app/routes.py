from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app import models
from app.signals import fetch_daily_prices#, compute_signals

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/signals/{ticker}")
def get_signals(ticker: str, db: Session = Depends(get_db)):
    
    existing = db.query(models.Signal).filter(models.Signal.ticker == ticker).first()
    
    if existing:
        return {
            "ticker": ticker,
            "momentum_30d": existing.momentum_30d,
            "volatility_30d": existing.volatility_30d
        }

    df = fetch_daily_prices(ticker)
    signal_data = compute_signals(df)

    new_signal = models.Signal(
        ticker=ticker,
        momentum_30d=signal_data["momentum_30d"],
        volatility_30d=signal_data["volatility_30d"]
    )

    db.add(new_signal)
    db.commit()
    db.refresh(new_signal)

    return {
        "ticker": ticker,
        **signal_data
    }