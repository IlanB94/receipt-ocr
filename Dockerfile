FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libgl1 tesseract-ocr \
    tesseract-ocr-heb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
