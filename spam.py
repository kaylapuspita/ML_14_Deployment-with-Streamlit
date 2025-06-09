import streamlit as st
import pickle
from PIL import Image

# Load model dan vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Konfigurasi halaman
st.set_page_config(page_title="Deteksi Spam", page_icon="📩", layout="centered")

# Header dan gaya
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #4a4a4a;
        }
        .subheader {
            font-size: 18px;
            color: #6c757d;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📩 Deteksi Pesan Spam</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Aplikasi sederhana untuk mendeteksi apakah sebuah pesan teks merupakan spam atau bukan.</div>', unsafe_allow_html=True)

# Input dari user
st.write("## Masukkan Pesan Anda")
user_input = st.text_area("", placeholder="Contoh: Dapatkan hadiah gratis sekarang juga!")

# Tombol deteksi
if st.button("🔍 Deteksi Sekarang"):
    if user_input:
        input_vect = vectorizer.transform([user_input])
        prediction = model.predict(input_vect)
        if prediction[0] == "spam":
            st.error("🚨 Pesan ini terdeteksi sebagai **SPAM**.")
        else:
            st.success("✅ Pesan ini **BUKAN SPAM**.")
    else:
        st.warning("⚠️ Silakan masukkan pesan terlebih dahulu.")

# Footer
st.markdown("""
---
<small>Developed with ❤️ by Kaylaaaa </small>
""", unsafe_allow_html=True)
