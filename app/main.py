# app/main.py
from fastapi import FastAPI, UploadFile
import shutil
from app.ocr.preprocess import preprocess_image
from app.ocr.extract_text import extract_text
from app.ocr.parse_fields import extract_total

app = FastAPI()

@app.post("/ocr")
async def ocr_receipt(file: UploadFile):
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    image = preprocess_image(path)
    text = extract_text(image)
    total = extract_total(text)

    return {
        "text": text,
        "total": total
    }
