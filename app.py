"""
Aplikasi web Streamlit untuk prediksi diabetes menggunakan machine learning.

Modul ini menyediakan antarmuka pengguna untuk memasukkan data kesehatan pasien dan
memprediksi risiko diabetes menggunakan model machine learning yang telah dilatih.
Termasuk fitur visualisasi data dan penjelasan detail hasil prediksi.
"""

import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Sistem Prediksi Diabetes", page_icon="🏥", layout="wide")


@st.cache_resource
def load_models():
    """Memuat model dan preprocessor yang telah disimpan."""
    try:
        model = joblib.load("best_diabetes_model.joblib")
        scaler = joblib.load("scaler.joblib")
        pca = joblib.load("pca.joblib")
        return model, scaler, pca
    except FileNotFoundError as e:
        st.error(f"Error saat memuat model: {str(e)}")
        st.error("Pastikan file model tersedia di direktori yang benar")
        st.stop()


def main():
    """
    Fungsi utama yang menjalankan aplikasi web prediksi diabetes menggunakan Streamlit.

    Fungsi ini:
    - Memuat model ML dan preprocessor yang telah dilatih
    - Membuat antarmuka web menggunakan Streamlit
    - Menangani pengumpulan input dari pengguna
    - Memproses input dan menampilkan hasil prediksi
    - Menyediakan informasi tentang model di sidebar

    Returns:
        None
    """
    # Memuat model
    model, scaler, pca = load_models()

    # Header
    st.title("Sistem Prediksi Diabetes")
    st.write(
        "Sistem ini memprediksi risiko diabetes berdasarkan berbagai indikator kesehatan."
    )

    # Informasi Dasar
    st.subheader("📋 Informasi Dasar")
    col_basic1, col_basic2 = st.columns(2)

    # Input data
    with col_basic1:
        age = st.number_input("Usia", 0, 120, 0, help="Usia dalam tahun")
        pregnancies = st.number_input(
            "Jumlah Kehamilan", 0, 20, 0, help="Jumlah kehamilan yang pernah dialami"
        )

    with col_basic2:
        has_family_diabetes = st.checkbox(
            "Riwayat Diabetes Keluarga",
            help="Centang jika memiliki anggota keluarga (orangtua/saudara) yang menderita diabetes",
        )
        diabetes_pedigree = 0.8 if has_family_diabetes else 0.1

    # Pengukuran Fisik
    st.subheader("📏 Pengukuran Fisik")
    col_physical1, col_physical2 = st.columns(2)

    with col_physical1:
        bmi = st.number_input(
            "IMT",
            0.0,
            70.0,
            0.0,
            help="Indeks Massa Tubuh (berat dalam kg/(tinggi dalam m)²)",
        )
        skin_thickness = st.number_input(
            "Ketebalan Kulit (mm)", 0, 100, 0, help="Ketebalan lipatan kulit trisep"
        )

    with col_physical2:
        blood_pressure = st.number_input(
            "Tekanan Darah (mm Hg)", 0, 200, 0, help="Tekanan darah diastolik"
        )

    # Hasil Laboratorium
    st.subheader("🔬 Hasil Laboratorium")
    col_lab1, col_lab2 = st.columns(2)

    with col_lab1:
        glucose = st.number_input(
            "Kadar Glukosa (mg/dL)",
            0,
            300,
            0,
            help="Konsentrasi glukosa plasma setelah 2 jam dalam tes toleransi glukosa oral",
        )

    with col_lab2:
        insulin = st.number_input(
            "Kadar Insulin (mu U/ml)", 0, 1000, 0, help="Insulin serum 2 jam"
        )

    # Hasil Prediksi
    st.subheader("🔄 Hasil Prediksi")

    # Menambahkan nama fitur ke input data
    feature_names = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
    ]

    input_data = np.array(
        [
            [
                pregnancies,
                glucose,
                blood_pressure,
                skin_thickness,
                insulin,
                bmi,
                diabetes_pedigree,
                age,
            ]
        ]
    )

    # Tombol untuk memprediksi
    if st.button("Analisis Risiko Diabetes", type="primary"):
        # Mengubah input data menjadi DataFrame dengan nama fitur
        input_df = pd.DataFrame(input_data, columns=feature_names)
        input_pca = pca.transform(input_df)
        input_scaled = scaler.transform(input_pca)

        prediction = model.predict(input_scaled)
        prediction_proba = model.predict_proba(input_scaled)

        if prediction[0] == 1:
            st.error("Risiko Tinggi Diabetes")
        else:
            st.success("Risiko Rendah Diabetes")

        st.write(f"Probabilitas terkena diabetes: {prediction_proba[0][1]:.2%}")
        st.progress(float(prediction_proba[0][1]))
    # Informasi Model dipindahkan ke sidebar
    with st.sidebar:
        st.title("ℹ️ Informasi")
        with st.expander("Tentang Model Ini"):
            st.write(
                """
            Model prediksi diabetes ini menggunakan machine learning untuk menilai 
            risiko diabetes berdasarkan beberapa indikator kesehatan. 
            
            Data yang diperlukan:
            1. Informasi Dasar
               - Usia
               - Jumlah kehamilan
               - Riwayat diabetes keluarga
            
            2. Pengukuran Fisik
               - IMT (Indeks Massa Tubuh)
               - Tekanan darah
               - Ketebalan kulit
            
            3. Hasil Laboratorium
               - Kadar glukosa
               - Kadar insulin
            
            Model ini menggunakan teknologi AI yang telah dioptimalkan untuk akurasi.
            """
            )


if __name__ == "__main__":
    main()
