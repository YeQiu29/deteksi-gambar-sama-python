import cv2
import os
import numpy as np

def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
            filenames.append(filename)
    return images, filenames

def resize_image(img, size=(500, 500)):
    return cv2.resize(img, size)

def compare_images(img1, img2):
    img1_resized = resize_image(img1)
    img2_resized = resize_image(img2)
    img1_gray = cv2.cvtColor(img1_resized, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2GRAY)
    score = cv2.matchTemplate(img1_gray, img2_gray, cv2.TM_CCOEFF_NORMED)
    return score

folder_path = 'C:\\Users\\Dennis\\OneDrive - Cubrews\\Documents\\PT. GEO GIVEN\\Deteksi_Gambar_sama\\apel'
images, filenames = load_images_from_folder(folder_path)

for i in range(len(images)):
    for j in range(i + 1, len(images)):
        score = compare_images(images[i], images[j])
        if np.max(score) >= 0.95:  # threshold to determine if images are similar
            print(f"Images {filenames[i]} and {filenames[j]} are similar with score {np.max(score)}")
