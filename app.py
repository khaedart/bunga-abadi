import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analisis Saham Perusahaan di Indonesia")

st.write("# Tugas Kelompok Bunga Abadi")

st.write("## Pendahuluan")
st.write('''Kami memilih menganalisis dataset saham Indonesia karena pasar modal di Indonesia menunjukkan potensi yang besar untuk pertumbuhan dan perkembangan ekonomi. Dalam beberapa tahun terakhir, minat masyarakat terhadap investasi saham semakin meningkat, seiring dengan kemudahan akses informasi dan teknologi yang memfasilitasi transaksi di pasar modal. Dengan lebih dari 700 perusahaan terdaftar di Bursa Efek Indonesia, terdapat beragam pilihan investasi yang dapat dieksplorasi. Melalui analisis dataset saham ini dapat memahami dinamika pergerakan harga, volume perdagangan, serta faktor-faktor yang mempengaruhi kinerja saham, seperti kondisi ekonomi makro, kebijakan pemerintah, dan sentimen pasar.
Selain itu, analisis dataset saham Indonesia juga penting untuk mengidentifikasi tren dan pola yang dapat membantu dalam pengembangan strategi investasi yang efektif. Dengan memanfaatkan data historis, maka dapat melakukan analisis teknikal dan fundamental yang mendalam, yang memungkinkan untuk meramalkan pergerakan harga saham di masa depan. ''')


st.write("## Deskripsi Data")
st.write(''' Dataset ini berisi data historis saham yang tercatat di IHSG dengan retan waktu per menit, per jam, dan per hari. sumber dataset diambil dari data publik Yahoo Finance dan situs web IDX. ''')

st.write("## Visualisasi")

import streamlit as st
import yfinance as yf
import plotly.express as px
import seaborn as sns

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

import numpy as np 

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
import pandas as pd
import warnings
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.subplots as ms
from plotly.offline import iplot
warnings.filterwarnings("ignore")

df=pd.read_csv('path/to/extract/minute/AALI.csv')
df = df.loc[df['timestamp']>='2018-04-16'].reset_index(drop=True)

st.write(df)
st.dataframe(df)
st.table(df)

#Window 1 bulan
WINDOW = 20
df['sma'] = df['close'].rolling(WINDOW).mean()
df['std'] = df['close'].rolling(WINDOW).std(ddof = 0)
display(df)

fig = make_subplots(specs=[[{"secondary_y": True}]])

# include candlestick with rangeselector
fig.add_trace(go.Candlestick(x=df['timestamp'],
                open=df['open'], high=df['high'],
                low=df['low'], close=df['close'], name='AALI'),
               secondary_y=False)
# Moving Average
fig.add_trace(go.Scatter(x = df['timestamp'],
                         y = df['sma'],
                         line_color = 'black',
                         name = 'Simple Moving Average'))

# Upper Bound
fig.add_trace(go.Scatter(x = df['timestamp'],
                         y = df['sma'] + (df['std'] * 2),
                         line_color = 'gray',
                         line = {'dash': 'dash'},
                         name = 'Bollinger Band',
                         opacity = 0.5))

# Lower Bound
fig.add_trace(go.Scatter(x = df['timestamp'],
                         y = df['sma'] - (df['std'] * 2),
                         line_color = 'gray',
                         line = {'dash': 'dash'},
                         showlegend=False,
                         opacity = 0.5))

# include a go.Bar trace for volumes
fig.add_trace(go.Bar(x=df['timestamp'], y=df['volume'], name='Volume'),
               secondary_y=True)
fig.update_xaxes(
    rangeslider_visible=True,
    rangebreaks=[
            dict(bounds=["sat", "mon"])  
#             dict(bounds=[16, 9], pattern="hour")
            ],
    rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1mo",
                     step="month",
                     stepmode="backward"),
                 dict(count=6,
                     label="6mo",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        )
)
fig.layout.yaxis2.showgrid=False
# Add figure title
fig.update_layout(
    title_text="Data Saham AALI"
)
# Set x-axis title
fig.update_xaxes(title_text="Date")
# Set y-axes titles
fig.update_yaxes(title_text="<b>Price</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Volume</b>", secondary_y=True)
fig.show()





st.write("## Analisis")
st.write(''' Dalam analisis ini, visualisasi untuk menggambarkan tren harga saham dari waktu ke waktu yang memungkinkan untuk mengidentifikasi pola yang signifikan. Misalnya, grafik garis yang menunjukkan pergerakan harga saham dapat menunjukkan periode volatilitas yang tinggi, dimana harga mengalami penurunan atau penurunan tajam, serta periode stabilitas dimana harga cenderung bergerak dalam rentang yang lebih sempit.''')

st.write("## Kesimpulan")
st.write("Data IHSG ini mencakup data historis yang mencakup harga pembukaan, penutupan, tertinggi, terendah, dan volume perdagangan ini memungkinkan untuk mengidentifikasi pola dan tren yang dapat mempengaruhi keputusan investasi. Melalui analisis dari visualisasi data tabel dan grafik ini dapat mengeksplorasi akumumulasi harga saham dari waktu ke waktu.")

st.write("## Referensi / Daftar Pustaka")
st.write("https://www.kaggle.com/datasets/muamkh/ihsgstockdata")

