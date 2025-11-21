import cv2

def is_blur(image_path, threshold=100):
    # Membaca gambar
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image file '{image_path}' not found.")

    # Mengonversi gambar ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Menggunakan transformasi Laplacian untuk mendeteksi ketajaman
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    print(f"Laplacian Variance: {laplacian_var}")

    # Membandingkan varians Laplacian dengan threshold untuk menentukan blur atau tidak
    if laplacian_var < threshold:
        print("Gambar blur")
        return True
    else:
        print("Gambar tidak blur")
        return False

# Uji dengan gambar
image_path = '2.jpeg'
is_blur(image_path)
