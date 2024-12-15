import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analisis Saham Perusahaan di Indonesia")

st.write("# Tugas Kelompok PasmingBased")

st.write("## Pendahuluan")
st.write('''Kami memilih menganalisis dataset saham Indonesia karena pasar modal di Indonesia menunjukkan potensi yang besar untuk pertumbuhan dan perkembangan ekonomi. Dalam beberapa tahun terakhir, minat masyarakat terhadap investasi saham semakin meningkat, seiring dengan kemudahan akses informasi dan teknologi yang memfasilitasi transaksi di pasar modal. Dengan lebih dari 700 perusahaan terdaftar di Bursa Efek Indonesia, terdapat beragam pilihan investasi yang dapat dieksplorasi. Melalui analisis dataset saham ini dapat memahami dinamika pergerakan harga, volume perdagangan, serta faktor-faktor yang mempengaruhi kinerja saham, seperti kondisi ekonomi makro, kebijakan pemerintah, dan sentimen pasar.
Selain itu, analisis dataset saham Indonesia juga penting untuk mengidentifikasi tren dan pola yang dapat membantu dalam pengembangan strategi investasi yang efektif. Dengan memanfaatkan data historis, maka dapat melakukan analisis teknikal dan fundamental yang mendalam, yang memungkinkan untuk meramalkan pergerakan harga saham di masa depan. ''')


st.write("## Deskripsi Data")
st.write('''Pertumbuhan ekonomi adalah sebuah proses dari perubahan kondisi perekonomian yang terjadi di suatu negara secara berkesinambungan untuk menuju keadaan yang dinilai lebih baik selama jangka waktu tertentu. ''')

st.write("## Visualisasi")

import streamlit as st
import yfinance as yf
import plotly.express as px

df = pd.read_csv('DaftarSaham.csv')

st.write("## menampilkan daftar saham")
st.write( df.head() )

# Dictionary of ticker symbols and company names
kamus_ticker = {
    'AALI': 'Astra Agro Lestari Tbk',
    'ABBA': 'Mahaka Media Tbk',
    'ABDA': 'Asuransi Bina Dana Arta Tbk',
    'ABMM': 'ABM Investama Tbk',
    'ACES': 'Ace Hardware Indonesia Tbk'
}

# Select box for ticker symbol with a unique key
tickerSymbol = st.selectbox(
    'Silakan pilih kode perusahaan',
    kamus_ticker.keys(),
    key='ticker_selectbox'  # Unique key for the ticker selectbox
)

# Display the full name of the selected company
st.write(f'Harga saham {kamus_ticker[tickerSymbol]}.')

# Fetch ticker data
tickerData = yf.Ticker(tickerSymbol)

# Select box for period with a unique key
pilihan_periode = st.selectbox(
    'Pilih periode:',
    ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y'],
    key='period_selectbox'  # Unique key for the period selectbox
)

# Fetch historical data
tickerDF = tickerData.history(
    period=pilihan_periode,
    start='2021-04-16',
    end='2022-04-15'
)

# Checkbox to display the table
flag_tampil = st.checkbox('Tampilkan tabel', key='show_table_checkbox')
if flag_tampil:
    st.write(tickerDF.head(10))

# Checkbox to display the graph
flag_grafik = st.checkbox('Tampilkan grafik', key='show_graph_checkbox')
if flag_grafik:
    pilihan_atribut = st.multiselect(
        'Silakan pilih atribut yang akan ditampilkan:',
        ['Low', 'High', 'Open', 'Close', 'Volume'],
        key='attributes_multiselect'  # Unique key for the multiselect
    )
    
    # Check if any attributes are selected
    if pilihan_atribut:
        # Create a line plot for the selected attributes
        grafik = px.line(
            tickerDF,
            title=f'Harga Saham {kamus_ticker[tickerSymbol]}',
            y=pilihan_atribut
        )
        st.plotly_chart(grafik)
    else:
        st.warning("Silakan pilih setidaknya satu atribut untuk ditampilkan.")



st.write("## Analisis")
st.write("Buat analisis sederhana dari visualisasi data yang muncul di bagian sebelumnya.")

st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmiah, dsb.")

