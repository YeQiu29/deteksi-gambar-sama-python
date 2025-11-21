import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as ssim

def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
            filenames.append(filename)
    return images, filenames

def pad_image(img, target_size):
    height, width = img.shape[:2]
    delta_w = target_size[1] - width
    delta_h = target_size[0] - height
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    color = [0, 0, 0]  # Black padding
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

folder_path = 'C:\\Users\\Dennis\\OneDrive - Cubrews\\Documents\\PT. GEO GIVEN\\Deteksi_Gambar_sama\\apel'
images, filenames = load_images_from_folder(folder_path)

for i in range(len(images)):
    for j in range(i + 1, len(images)):
        score = compare_images_ssim(images[i], images[j])
        if score >= 0.95:  # threshold to determine if images are similar
            print(f"Images {filenames[i]} and {filenames[j]} are similar with score {score}")
