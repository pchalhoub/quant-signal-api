FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV ENV=prod

CMD ["sh", "-c", "python app/create_tables.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]