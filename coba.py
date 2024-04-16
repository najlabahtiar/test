import streamlit as st

st.title("Nama Senyawa Dalam Kimia")
kode_unsur = st.text_input("Silahkan masukan kode unsur senyawa")
cari = st.button("Mencari deskripsi")

if cari :
        if (kode_unsur =="H" or kode_unsur =="h" ): 
             st.write('Hidrogen ')
        elif (kode_unsur =="NH4"): 
             st.write('amonium ')
        elif (kode_unsur =="Au"): 
             st.write('Emas ')
        elif (kode_unsur =="K"): 
             st.write('Kalium ')
        elif (kode_unsur =="Li"): 
             st.write('Litium ') 
        elif (kode_unsur =="Cu"): 
             st.write('Tembaga ')
        elif (kode_unsur =="Na"): 
             st.write('Natrium ')
        elif (kode_unsur =="Ag"): 
             st.write('Perak') 
        elif (kode_unsur =="Hg"): 
             st.write('Raksa')                            
        else  : 
            st.write('Salah memasukan nama unsur')  