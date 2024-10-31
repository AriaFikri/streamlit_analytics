import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df_hourly = pd.read_csv("hour.csv")
df_daily = pd.read_csv("day.csv")

df_weather = df_hourly.groupby("weathersit", as_index=False).agg({
    "casual": ["min", "max", "median"],
    "registered": ["min", "max", "median"],
    "cnt": ["min", "max", "median"]
})

df_season = df_daily.groupby("season").agg({
    "casual": ["min", "max", "median"],
    "registered": ["min", "max", "median"],
    "cnt": ["min", "max", "median"]
})

def show_weather():
    st.header("Pengaruh musim dan cuaca")

    tab1, tab2 = st.tabs(["Jumlah pengguna tiap segmen terhadap cuaca", "Perbandingan pengguna setiap musim"])

    with tab1:
        st.subheader("Pengguna setiap segmen terhadap cuaca", divider=True)

        df_weather_1 = df_hourly.loc[df_hourly["weathersit"] == 1]
        df_weather_2 = df_hourly.loc[df_hourly["weathersit"] == 2]
        df_weather_3 = df_hourly.loc[df_hourly["weathersit"] == 3]
        df_weather_4 = df_hourly.loc[df_hourly["weathersit"] == 4]

        fig, ax = plt.subplots(figsize=[10, 8])
        plt.suptitle("Perbandingan jumlah pengguna terhadap cuaca")

        color = {
            "registered": "steelblue",
            "casual": "skyblue"
        }

        sns.barplot(data=df_weather_1, x="weathersit", y=df_weather_1["registered"], label="registered", color=color["registered"], estimator="median")
        sns.barplot(data=df_weather_2, x="weathersit", y=df_weather_2["registered"], color=color["registered"], estimator="median")
        sns.barplot(data=df_weather_3, x="weathersit", y=df_weather_3["registered"], color=color["registered"], estimator="median")
        sns.barplot(data=df_weather_4, x="weathersit", y=df_weather_4["registered"], color=color["registered"], estimator="median")


        sns.barplot(data=df_weather_1, x="weathersit", y=df_weather_1["casual"], label="casual", color=color["casual"], estimator="median")
        sns.barplot(data=df_weather_2, x="weathersit", y=df_weather_2["casual"], color=color["casual"])
        sns.barplot(data=df_weather_3, x="weathersit", y=df_weather_3["casual"], color=color["casual"])
        sns.barplot(data=df_weather_4, x="weathersit", y=df_weather_4["casual"], color=color["casual"], estimator="median")

        plt.ylabel("Jumlah Pengguna")
        plt.xticks([0, 1, 2, 3], ["Cerah", "Berkabut", "Presipitasi ringan", "presipitasi berat/Badai"])
        plt.xlabel("Kategori Cuaca")

        st.pyplot(fig)

    with tab2:
        st.subheader("Pengguna di setiap musim", divider=True)

        fig, ax = plt.subplots(figsize=[10,7])
        plt.suptitle("Angka pengguna setiap musim")

        color = {
            "registered": "steelblue",
            "casual": "skyblue"
        }

        sns.barplot(data=df_daily, x="season", y=df_daily["registered"], label="Registered", color=color["registered"], estimator="median")
        sns.barplot(data=df_daily, x="season", y=df_daily["casual"], label="casual", color=color["casual"], estimator="median")

        plt.ylabel("Median Pengguna")
        plt.xlabel("Musim")
        plt.xticks(ticks=[0,1,2,3], labels=["Spring", "Summer", "Fall", "Winter"])

        st.pyplot(fig)

show_weather()