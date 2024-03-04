import streamlit as st
import datetime
import matplotlib.pyplot as plt
import numpy as np

with st.sidebar:
    
    st.text('Bike Share Administrator')
    
    name = st.text_input(label='Nama lengkap', value='')

    number = st.number_input(label='Umur')

    name = st.text_input(label='Alamat', value='')

    date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))

    if st.button('Register'):
        st.write('Selamat, Anda telah terdaftar di Bike Share Company')

st.title('Selamat Datang di Dashboard Bike Share')
tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])

with tab1:
    st.header("Bagaimana perbandingan antara jumlah peminjam sepeda yang sudah teregistrasi dengan peminjam sepeda tanpa akun ? lebih banyak yang mana ?")
 
    with st.expander("Kesimpulan 1"):
        st.write(
        "Berdasarkan hasil dari proses pengolahan dan visualisasi data diatas, menghasilkan kesimpulan bahwa jumlah peminjam sepeda yang sudah ter registrasi lebih banyak jika dibandingkan dengan jumlah peminjam sepeda yang belum memiliki akun."
    )

with tab2:
    st.header("Apakah cuaca berpengaruh terhadap jumlah peminjaman sepeda yang dilakukan ?")

    with st.expander("Kesimpulan 2"):
        st.write(
        "Berdasarkan hasil dari proses pengolahan dan visualisasi data diatas, menghasilkan kesimpulan bahwa cuaca berpengaruh terhadap jumlah peminjaman sepeda. Hal tersebut dapat dilihat jika cuaca dalam keadaan baik (1) banyak jumlah peminjamnya, jika cuaca dalam keadaan buruk (4) jumlah peminjam mengalami penurunan. hal itu sejalan dengan jenis cuaca dari nomor 1 sampai nomor 4 yang terus mengalami penurunan jumlah peminjam sepeda."
    )
