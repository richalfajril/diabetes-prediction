# 🚀 End-to-End Sistem Prediksi Diabetes  

Proyek ini merupakan **end-to-end machine learning pipeline** yang dikembangkan untuk memprediksi risiko diabetes berdasarkan indikator kesehatan. Model machine learning yang telah dioptimalkan dideploy menggunakan **Streamlit**, sehingga pengguna dapat dengan mudah mengakses prediksi melalui antarmuka web interaktif.  

## 🎯 Model Terbaik  

Setelah mengevaluasi berbagai algoritma yang tersedia di **Scikit-Learn**, model dengan performa terbaik adalah:  

🔹 **Model Terbaik**: Random Forest  
🔹 **Akurasi**: 0.8389  
🔹 **F1 Score**: 0.8386  
🔹 **AUC (Area Under Curve)**: 0.9148  

Model ini dipilih karena memberikan keseimbangan terbaik antara akurasi, generalisasi, dan interpretabilitas dalam memprediksi risiko diabetes. 

## 🚀 Fitur

- Prediksi risiko diabetes berdasarkan 8 indikator kesehatan
- Antarmuka web yang mudah digunakan
- Visualisasi hasil prediksi
- Penjelasan detail tentang setiap indikator yang digunakan

## 📋 Persyaratan Sistem

- Python 3.8 atau lebih tinggi
- pip (Python package installer)

## 📦 Dependensi

```plaintext
streamlit==1.29.0
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
joblib==1.3.2
matplotlib==3.7.2
```

## 🔍 Dataset yang Digunakan

Model machine learning dalam aplikasi ini dilatih menggunakan dataset **Pima Indians Diabetes Database**, yang tersedia di Kaggle:

📂 **Sumber Dataset**:  
[Kaggle - Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data)  

🔢 **Deskripsi Dataset**:
- Dataset ini berisi informasi kesehatan 768 perempuan dari suku Pima Indian, dengan label apakah mereka menderita diabetes atau tidak.
- Memiliki **8 fitur** sebagai input dan **1 label output** (diabetes: 1, tidak diabetes: 0).

📊 **Fitur dalam Dataset**:
1. **Pregnancies** – Jumlah kehamilan  
2. **Glucose** – Kadar glukosa dalam darah (mg/dL)  
3. **Blood Pressure** – Tekanan darah diastolik (mm Hg)  
4. **Skin Thickness** – Ketebalan lipatan kulit triceps (mm)  
5. **Insulin** – Kadar insulin dalam darah (mu U/ml)  
6. **BMI** – Indeks Massa Tubuh (kg/m²)  
7. **Diabetes Pedigree Function** – Skor risiko diabetes berdasarkan riwayat keluarga  
8. **Age** – Usia pasien (tahun)  

## 🔧 Instalasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/richalfajril/diabetes-prediction.git
   cd diabetes-prediction
   ```

2. Buat dan aktifkan virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk MacOS/Linux
   .\venv\Scripts\activate  # Untuk Windows
   ```

3. Install dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Cara Penggunaan

1. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

2. Buka browser dan akses `http://localhost:8501`

3. Masukkan data kesehatan yang diperlukan:
   - **Informasi Dasar** (usia, jumlah kehamilan, riwayat diabetes keluarga)
   - **Pengukuran Fisik** (IMT, tekanan darah, ketebalan kulit)
   - **Hasil Laboratorium** (kadar glukosa, insulin)

4. Klik tombol **"Analisis Risiko Diabetes"** untuk melihat hasil prediksi.

## 🔬 Teknologi yang Digunakan

- **Streamlit**: Framework web
- **Scikit-learn**: Machine learning
- **Pandas & NumPy**: Pengolahan data
- **Matplotlib**: Visualisasi data

## ⚠️ Catatan Penting

Aplikasi ini hanya untuk tujuan edukasi dan **tidak menggantikan diagnosis medis profesional**. Selalu konsultasikan dengan tenaga medis untuk diagnosis dan perawatan yang tepat.

## 📝 Lisensi

[MIT License](LICENSE)

## 👥 Kontributor

- [Richal Fajril](https://github.com/richalfajril)

## 🤝 Kontribusi

Kontribusi selalu diterima dengan senang hati. Silakan buat **pull request** atau **issue** untuk perbaikan atau saran.

## 📞 Kontak

Jika Anda memiliki pertanyaan atau saran, silakan hubungi:
- **Email**: richalfajril@gmail.com
- **GitHub**: [@richalfajril](https://github.com/richalfajril)