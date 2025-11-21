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
git clone [https://github.com/username-anda/repo-anda.git](https://github.com/username-anda/repo-anda.git)
cd repo-anda

