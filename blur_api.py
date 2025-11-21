from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import cv2
import numpy as np

app = FastAPI()

def is_blur(image: np.ndarray, threshold: int = 100) -> (bool, float):
    # Mengonversi gambar ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Menggunakan transformasi Laplacian untuk mendeteksi ketajaman
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    # Membandingkan varians Laplacian dengan threshold untuk menentukan blur atau tidak
    return laplacian_var < threshold, laplacian_var

@app.post("/detect-blur/")
async def detect_blur(file: UploadFile = File(...), threshold: int = 100):
    # Membaca file gambar yang diunggah
    try:
        image = await file.read()
        np_image = np.frombuffer(image, np.uint8)
        image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
        
        if image is None:
            raise HTTPException(status_code=400, detail="Invalid image file.")
        
        # Deteksi blur
        is_blurred, score = is_blur(image, threshold)
        
        # Mengembalikan hasil deteksi sebagai JSON
        result = {
            "Deteksi": not is_blurred,  # true jika tidak blur, false jika blur
            "message": "Gambar jelas" if not is_blurred else "Gambar blur",
            "scores": score
        }
        return JSONResponse(content=result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
