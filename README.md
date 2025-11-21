# 📸 FastAPI Image Similarity Detector

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-009688?style=for-the-badge&logo=fastapi)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv)

Microservice sederhana dan efisien berbasis **FastAPI** untuk mendeteksi duplikasi atau kemiripan antar gambar menggunakan algoritma **SSIM (Structural Similarity Index)**.

API ini dirancang untuk menangani input *batch* (banyak gambar sekaligus), melakukan penyesuaian dimensi otomatis (*padding*), dan memberikan laporan jika ditemukan gambar yang identik.

## ✨ Fitur Utama

* **Batch Comparison:** Menerima upload minimal **2** hingga maksimal **10** gambar dalam satu request.
* **Smart Padding:** Menambahkan padding hitam secara otomatis agar dimensi gambar setara tanpa mendistorsi rasio aspek asli (memungkinkan perbandingan gambar beda resolusi).
* **SSIM Analysis:** Menggunakan `skimage.metrics.structural_similarity` untuk akurasi perbandingan struktur visual yang tinggi.
* **Threshold Alert:** Secara otomatis menandai "Similar" jika skor kemiripan mencapai **95% (0.95)** atau lebih.

## 🛠️ Teknologi

Project ini dibangun menggunakan library open-source yang handal:

* [FastAPI](https://fastapi.tiangolo.com/) - Framework web modern berkinerja tinggi.
* [OpenCV](https://opencv.org/) - Pemrosesan citra digital (decoding & manipulasi array).
* [Scikit-Image](https://scikit-image.org/) - Algoritma SSIM.
* [NumPy](https://numpy.org/) - Operasi matriks kecepatan tinggi.

## 🚀 Instalasi & Cara Pakai

### 1. Clone Repository
```bash
git clone https://github.com/YeQiu29/deteksi-gambar-sama-python
cd deteksi-gambar-sama-python
```
### 2. Install Dependencies
Buat virtual environment (opsional) dan install paket yang dibutuhkan. Kamu bisa membuat file requirements.txt dengan isi berikut:
```plaintext
fastapi
uvicorn
opencv-python-headless
scikit-image
python-multipart
numpy
```
Lalu Jalankan:
```bash
pip install -r requirements.txt
```
### 3. Jalankan Server
```bash
# Menjalankan server pada port 8000
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
## 📖 Dokumentasi API

Setelah server berjalan, dokumentasi interaktif tersedia di: 👉 Swagger UI: http://localhost:8000/docs 👉 ReDoc: http://localhost:8000/redoc

Endpoint: POST /compare-images/
Digunakan untuk membandingkan sekumpulan gambar yang diunggah.

Parameter Body:

files: Array of Files (multipart/form-data).

Validasi: Minimal 2 file, Maksimal 10 file.

Contoh Response (Jika ada kemiripan):
```JSON
{
  "similar": false,
  "message": "Images 1 and 2 are similar with score 0.9812"
}
```
Contoh Response (Jika semua unik):
```JSON
{
  "similar": true,
  "message": "Successful"
}
```
## 🧪 Contoh Testing via Terminal (cURL)
```bash
curl -X 'POST' \
  'http://localhost:8000/compare-images/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@foto_ktp_A.jpg' \
  -F 'files=@foto_ktp_A_duplikat.jpg' \
  -F 'files=@foto_selfie.jpg'
```
<div align="center">
  Created with ❤️ using Python and FastAPI by Dennis Putra Hilmansyah
</div>
