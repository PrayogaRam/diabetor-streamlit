import streamlit as st
import pickle
import numpy as np

model_path = 'diabetes_model(1)BISMILLAH.sav'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def main():
    # Membuat judul dan deskripsi aplikasi
    st.title("🩺 DIABETOR-Diabetes Detector")
    st.write("Selamat datang di aplikasi DIABETOR! Masukkan data kesehatan Anda untuk mengetahui kemungkinan terkena diabetes.")

    # Membuat sidebar untuk input data
    st.sidebar.header("Input Data Pasien")

    # Mengubah input biner menjadi pilihan "Ya" atau "Tidak"
    HighBP = st.sidebar.radio("Tekanan Darah Tinggi", ['Ya', 'Tidak'])
    HighChol = st.sidebar.radio("Kolesterol Tinggi", ['Ya', 'Tidak'])
    CholCheck = st.sidebar.radio("Pernah Pemeriksaan Kolesterol", ['Ya', 'Tidak'])
    Smoker = st.sidebar.radio("Perokok", ['Ya', 'Tidak'])
    Stroke = st.sidebar.radio("Pernah Stroke", ['Ya', 'Tidak'])
    Fruits = st.sidebar.radio("Konsumsi Buah Setiap Hari", ['Ya', 'Tidak'])
    PhysActivity = st.sidebar.radio("Kegiatan Fisik 30 Hari Terakhir", ['Ya', 'Tidak'])
    Veggies = st.sidebar.radio("Konsumsi Sayuran Setiap Hari", ['Ya', 'Tidak'])
    HvyAlcoholConsump = st.sidebar.radio("Pemabuk berat (pria dewasa minum lebih dari 14 minuman per minggu dan wanita dewasa minum lebih dari 7 minuman per minggu)", ['Ya', 'Tidak'])
    HeartDiseaseorAttack = st.sidebar.radio("Penyakit Jantung atau Serangan Jantung", ['Ya', 'Tidak'])
    AnyHealthcare = st.sidebar.radio("Pernah Mendapat Perawatan Kesehatan", ['Ya', 'Tidak'])
    NoDocbcCost = st.sidebar.radio("Tidak Ada Dokter karena Biaya", ['Ya', 'Tidak'])
    DiffWalk = st.sidebar.radio("Kesulitan Berjalan", ['Ya', 'Tidak'])
    Sex = st.sidebar.radio("Jenis Kelamin", ['Perempuan', 'Laki-Laki'])

    # Konversi pilihan "Ya" atau "Tidak" menjadi 1 atau 0
    HighBP = 1 if HighBP == 'Ya' else 0
    HighChol = 1 if HighChol == 'Ya' else 0
    CholCheck = 1 if CholCheck == 'Ya' else 0
    Smoker = 1 if Smoker == 'Ya' else 0
    Stroke = 1 if Stroke == 'Ya' else 0
    HeartDiseaseorAttack = 0 if HeartDiseaseorAttack == 'Ya' else 1
    AnyHealthcare = 1 if AnyHealthcare == 'Ya' else 0
    NoDocbcCost = 1 if NoDocbcCost == 'Ya' else 0
    DiffWalk = 1 if DiffWalk == 'Ya' else 0
    Sex = 1 if Sex == 'Laki-Laki' else 0
    Fruits = 0 if Fruits == 'Ya' else 1
    PhysActivity = 0 if PhysActivity == 'Ya' else 1
    Veggies = 0 if Veggies == 'Ya' else 1
    HvyAlcoholConsump = 0 if HvyAlcoholConsump == 'Ya' else 1 

    # Input BMI menggunakan input angka
    BMI = st.sidebar.number_input("Indeks Massa Tubuh (BMI)", min_value=0, max_value=80)
    GenHlth = st.sidebar.selectbox("Kesehatan Umum (1=Sangat Baik, 5=Sangat Buruk)", [1, 2, 3, 4, 5])
    MentHlth = st.sidebar.number_input("Jumlah Hari dengan Masalah Kesehatan Mental (30 hari terakhir)", min_value=0, max_value=30)
    PhysHlth = st.sidebar.number_input("Jumlah Hari dengan Masalah Kesehatan Fisik (30 hari terakhir)", min_value=0, max_value=30)
    Age = st.sidebar.number_input("Kategori Umur Berdasarkan AGEG5YR: FOURTEEN-LEVEL AGE CATEGORY", min_value=1, max_value=13)
    Education = st.sidebar.number_input("Level Edukasi Berdasarkan (EDUCA EDUCATION LEVEL) Skala 1-6", min_value=1, max_value=6)
    Income = st.sidebar.number_input("Skala Pendapatan Berdasarkan (INCOME2 INCOME LEVEL) Skala 1-8", min_value=1, max_value=8)

    # Mengambil data input
    input_data = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, Fruits, Veggies, PhysActivity, HvyAlcoholConsump, HeartDiseaseorAttack, 
                            AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income]])

    # Menampilkan prediksi setelah tombol diklik
    if st.button("Deteksi Diabetes"):
        prediction = model.predict(input_data)
        if prediction == 1:
            st.warning("⚠️ Anda mungkin sedang dalam tahap pre-diabetes. Harap perhatikan gaya hidup dan konsultasikan dengan dokter.")
        elif prediction == 2:
            st.warning("⚠️ Anda mungkin memiliki diabetes tipe 2. Harap perhatikan gaya hidup dan konsultasikan dengan dokter.")
        elif prediction == 0:
            st.success("✅ Anda kemungkinan besar tidak memiliki diabetes. Tetap jaga kesehatan Anda!")
            st.balloons()

if __name__ == "__main__":
    main()

