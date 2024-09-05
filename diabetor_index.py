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
    HighBP = 1.0 if HighBP == 'Ya' else 0.0
    HighChol = 1.0 if HighChol == 'Ya' else 0.0
    CholCheck = 1.0 if CholCheck == 'Ya' else 0.0
    Smoker = 1.0 if Smoker == 'Ya' else 0.0
    Stroke = 1.0 if Stroke == 'Ya' else 0.0
    HeartDiseaseorAttack = 1.0 if HeartDiseaseorAttack == 'Ya' else 0.0
    AnyHealthcare = 1.0 if AnyHealthcare == 'Ya' else 0.0
    NoDocbcCost = 1.0 if NoDocbcCost == 'Ya' else 0.0
    DiffWalk = 1.0 if DiffWalk == 'Ya' else 0.0
    Sex = 1.0 if Sex == 'Laki-Laki' else 0.0
    Fruits = 1.0 if Fruits == 'Ya' else 0.0
    PhysActivity = 1.0 if PhysActivity == 'Ya' else 0.0
    Veggies = 1.0 if Veggies == 'Ya' else 0.0 
    HvyAlcoholConsump = 1.0 if Veggies == 'Ya' else 0.0 

    # Input BMI menggunakan slider dengan nilai desimal
    BMI = st.sidebar.slider("Indeks Massa Tubuh (BMI)", 0, 80, 0)
    GenHlth = st.sidebar.selectbox("Kesehatan Umum (1=Sangat Baik, 5=Sangat Buruk)", [1, 2, 3, 4, 5])
    MentHlth = st.sidebar.slider("Jumlah Hari dengan Masalah Kesehatan Mental (30 hari terakhir)", 0, 30, 0)
    PhysHlth = st.sidebar.slider("Jumlah Hari dengan Masalah Kesehatan Fisik (30 hari terakhir)", 0, 30, 0)
    Age = st.sidebar.slider("Kategori Umur Berdasarkan AGEG5YR: FOURTEEN-LEVEL AGE CATEGORY", 1, 13, 5)
    Education = st.sidebar.slider("Level Edukasi Berdasarkan (EDUCA EDUCATION LEVEL) Skala 1-6", 1, 6, 1)
    Income = st.sidebar.slider("Skala Pendapatan Berdasarkan (INCOME2 INCOME LEVEL) Skala 1-8", 1, 8, 1)

    # Mengambil data input
    input_data = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, Fruits, Veggies, PhysActivity, HvyAlcoholConsump, HeartDiseaseorAttack, 
                            AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income]])

    # Menampilkan prediksi setelah tombol diklik
    if st.button("Deteksi Diabetes"):
        prediction = model.predict(input_data)
        if prediction => 0.5:
            st.warning("⚠️ Anda mungkin sedang dalam tahap pre-diabetes. Harap perhatikan gaya hidup dan konsultasikan dengan dokter.")
        elif prediction => 1:
            st.warning("⚠️ Anda mungkin memiliki diabetes tipe 2. Harap perhatikan gaya hidup dan konsultasikan dengan dokter.")
        elif prediction => 0:
            st.success("✅ Anda kemungkinan besar tidak memiliki diabetes. Tetap jaga kesehatan Anda!")
            st.balloons()

if __name__ == "__main__":
    main()
