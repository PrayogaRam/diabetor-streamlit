import streamlit as st
import pickle
import numpy as np

# Memuat model machine learning
model = pickle.load(open('diabetes_model(0.1,1).sav', 'rb'))

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
    HeartDiseaseorAttack = st.sidebar.radio("Penyakit Jantung atau Serangan Jantung", ['Ya', 'Tidak'])
    AnyHealthcare = st.sidebar.radio("Pernah Mendapat Perawatan Kesehatan", ['Ya', 'Tidak'])
    NoDocbcCost = st.sidebar.radio("Tidak Ada Dokter karena Biaya", ['Ya', 'Tidak'])
    DiffWalk = st.sidebar.radio("Kesulitan Berjalan", ['Ya', 'Tidak'])
    Sex = st.sidebar.radio("Jenis Kelamin (0=Perempuan, 1=Laki-laki)", [0, 1])

    # Konversi pilihan "Ya" atau "Tidak" menjadi 1 atau 0
    HighBP = 1 if HighBP == 'Ya' else 0
    HighChol = 1 if HighChol == 'Ya' else 0
    CholCheck = 1 if CholCheck == 'Ya' else 0
    Smoker = 1 if Smoker == 'Ya' else 0
    Stroke = 1 if Stroke == 'Ya' else 0
    HeartDiseaseorAttack = 1 if HeartDiseaseorAttack == 'Ya' else 0
    AnyHealthcare = 1 if AnyHealthcare == 'Ya' else 0
    NoDocbcCost = 1 if NoDocbcCost == 'Ya' else 0
    DiffWalk = 1 if DiffWalk == 'Ya' else 0

    # Input data tambahan
    BMI = st.sidebar.slider("Indeks Massa Tubuh (BMI)", 0, 80, 25)
    GenHlth = st.sidebar.selectbox("Kesehatan Umum (1=Sangat Baik, 5=Sangat Buruk)", [1, 2, 3, 4, 5])
    MentHlth = st.sidebar.slider("Jumlah Hari dengan Masalah Kesehatan Mental (30 hari terakhir)", 0, 30, 0)
    PhysHlth = st.sidebar.slider("Jumlah Hari dengan Masalah Kesehatan Fisik (30 hari terakhir)", 0, 30, 0)
    Age = st.sidebar.slider("Kategori Umur", 1, 100, 5)

    # Mengambil data input
    input_data = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, 
                            AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age]])

    # Menampilkan prediksi setelah tombol diklik
    if st.button("Deteksi Diabetes"):
        prediction = model.predict(input_data)
        if prediction == 2:
            st.error("⚠️ Anda mungkin memiliki diabetes tipe 2. Harap segera konsultasikan dengan dokter.")
        elif prediction == 1:
            st.warning("⚠️ Anda mungkin berada dalam tahap pre-diabetes. Harap perhatikan gaya hidup dan konsultasikan dengan dokter.")
        elif prediction == 0:
            st.success("✅ Anda kemungkinan besar tidak memiliki diabetes. Tetap jaga kesehatan Anda!")

        st.balloons()  # Menampilkan animasi balon untuk hasil non-diabetes

if __name__ == "__main__":
    main()
