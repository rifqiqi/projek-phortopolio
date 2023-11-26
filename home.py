import streamlit as st


st.set_page_config(
    page_title="Portfolio | Rifqi Maulana",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("rifqi.png", width= 190)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : Moh Rifqi Maulana")
   st.caption("NIM : 0402201100")
   st.write(
            """
            - Tempat Tanggal Lahir   : Brebes 12 April 2002 
            - Alamat                 : Lumpur Limangan Losari Brebes
            - Hobi                   : Main bola, Melukis, Membaca
            - Cita-cita              : Harus Bisa Mewarnai Bukan Di Warnai
            - Hal yang disukai       : Membuat orang Terseyum
            - Status                 : Sedang Belajar 
            - Hal yang tidak disukai : Makana-makan Pedas
            """
        )

st.header("*Call Me If You Want*")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("wahstapp")
   
with col2:
    st.subheader("Facebook")
    
with col3:
    st.subheader("Instagram")
   
with col4:
    st.subheader("blogg")
   
st.container()
st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
   
    st.image("wa.jpeg", width= 50)
with col2:
   
    st.image("facebook.jpeg", width= 50)
with col3:
    
    st.image("instagram.jpeg", width= 50)
with col4:
    
    st.image("blog.jpeg", width= 50)
