import easyocr

reader = easyocr.Reader(['he', 'en'])

def extract_text(image):
    result = reader.readtext(image, detail=0)
    return "\n".join(result)