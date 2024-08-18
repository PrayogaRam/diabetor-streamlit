import pickle
import streamlit as st

model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Diabetor: Diabetes Detector')

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input ('Masukkan Jumlah Kehamilan( Jika laki-laki maka kehamilan = 0)')
with col2:
    Glucose = st.text_input ('Masukkan Nilai Glukosa(Hasil Uji Glukosa Puasa 8 Jam)')
with col1:
    BloodPressure = st.text_input ('Masukkan Nilai Tekanan Darah')
with col2:
    SkinThickness = st.text_input ('Masukkan Nilai Ketebalan Kulit')
with col1:
    Insulin = st.text_input ('Masukkan Nilai Insulin')
with col2:
    BMI = st.text_input ('Masukkan Nilai BMI( Body Mass Index )')
with col1:
    DiabetesPedigreeFunction = st.text_input ('Masukkan Nilai DPF( DiabetesPedigreeFunction )')
with col2:
    Age = st.text_input ('Masukkan Umur')

diab_diagnosis = ''

if st.button('Lihat Hasil Prediksi'):
    diab_pred = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_pred[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes Tipe 1'
    elif(diab_pred[0] == 2):
        diab_diagnosis = 'Pasien terkena Diabetes Tipe 2'
    else :
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
    
st.success(diab_diagnosis)
