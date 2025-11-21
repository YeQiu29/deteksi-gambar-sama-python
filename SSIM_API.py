from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

app = FastAPI()

def pad_image(img, target_size):
    height, width = img.shape[:2]
    delta_w = target_size[1] - width
    delta_h = target_size[0] - height
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    color = [0, 0, 0]  # Padding hitam
    new_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return new_img

def compare_images_ssim(img1, img2):
    height1, width1 = img1.shape[:2]
    height2, width2 = img2.shape[:2]
    target_size = (max(height1, height2), max(width1, width2))
    
    img1_padded = pad_image(img1, target_size)
    img2_padded = pad_image(img2, target_size)
    
    img1_gray = cv2.cvtColor(img1_padded, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2_padded, cv2.COLOR_BGR2GRAY)
    
    score, diff = ssim(img1_gray, img2_gray, full=True)
    return score

@app.post("/compare-images/")
async def compare_images(files: List[UploadFile] = File(...)):
    if not (2 <= len(files) <= 10):
        raise HTTPException(status_code=400, detail="Image Minimum 2 foto & Maximum 10 foto")
    
    images = []
    for file in files:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is not None:
            images.append(img)
    
    for i in range(len(images)):
        for j in range(i + 1, len(images)):
            score = compare_images_ssim(images[i], images[j])
            if score >= 0.95:
                return {"similar": False, "message": f"Images {i+1} and {j+1} are similar with score {score:.4f}"}
    
    return {"similar": True, "message": "Successful"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
