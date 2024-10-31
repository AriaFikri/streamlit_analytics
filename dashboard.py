import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

with st.container(border=True):
    st.header("Penjelasan dataset", divider="gray")
    st.write(
        "Bike sharing merupakan salah satu moda transportasi yang memungkinkan para penggunanya untuk menjadi member, menyewa, hingga mengembalikan sepeda secara otomatis. Dengan otomatisasi sistem bike sharing, data yang dihasilkan dari sistem ini pun dapat lebih mudah direkam dan menjadi hal yang menarik sehingga lahirlah dataset bike sharing untuk kepentingan analisa"
        )
    st.write("""
Data dari bike_dataset memiliki beberapa kolom yaitu:
    \n
    * Instant (No. perekaman data)
    * dteday (Tanggal)
    * Season (Angka sebagai penanda musim [1: Spring, 2: Summer, 3: Fall, 4: Winter
    * Year (Tahun, [0: 2011, 1: 2012]
    * mnth (Bulan dari 1 hingga 12)
    * hr (Jam dari 0 hingga 23)
    * Holiday (Menandakan apakah tanggal tersebut termasuk dalam holiday schedule/hari libur nasional)
    * Weekday (hari dalam satu minggu dari 0 hingga 6)
    * Workingday (menandakan apakah tanggal yang terekam adalah hari kerja. 1 untuk workday dan 0 untuk weekend atau holiday)
    * Weathersit (Menandakan cuaca)
        - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + 
    * temp (suhu yang telah dinormalis di 41 maksi)al)
    * atemp (feeling temperature yang telah dinormalis. Dibagi di 50 maksi mal)
    * hum (nilai kelembaban yang telah dinormalisasi. Dibagi menjadi 100 maksimal)
    * windspeed (kecepatan angin yang telah dinormalisasi. Nilai dibagi menjadi 67 maksimal)
    * casual (pengguna/pelanggan kasual)
    * registered (pengguna yang telah terdaftar)
    * cnt (total casual dan registered)
    """)

st.sidebar.title("Dashboard Bike Sharing Data :bike:")
select = st.sidebar.radio("Select page", ["About Dataset :newspaper:", "Perkembangan angka pengguna :chart_with_upwards_trend:", "Pengaruh hari kerja :office_worker:", "Pengaruh cuaca dan musim :sun_small_cloud:", "Angka pengguna setiap jam :clock8:", "Additional analysis"])

if select == "Pengaruh hari kerja :office_worker:":
    exec(open("workingday.py").read())
if select == "Perkembangan angka pengguna :chart_with_upwards_trend:":
    exec(open("development.py").read())
if select == "Angka pengguna setiap jam :clock8:":
    exec(open("hour.py").read())
if select == "Pengaruh cuaca dan musim :sun_small_cloud:":
    exec(open("weather.py").read())
if select == "Additional analysis":
    exec(open("additional.py").read())