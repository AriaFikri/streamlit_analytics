import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df_hourly = pd.read_csv("hour.csv")
df_daily = pd.read_csv("day.csv")

def create_monthly_df (df):

    df_monthly = df.groupby(["yr", "mnth"], as_index=False).agg({
        "casual": ["min", "max", "median", "sum"],
        "registered": ["min", "max", "median", "sum"],
        "cnt": ["min", "max", "median", "sum"],
    })

    return df_monthly

df_daily = df_daily.drop("instant", axis=1)
df_hourly = df_hourly.drop("instant", axis=1)

df_daily["dteday"] = pd.to_datetime(df_daily["dteday"], format="%Y-%m-%d")
df_hourly["dteday"] = pd.to_datetime(df_hourly["dteday"], format="%Y-%m-%d")

df_monthly = create_monthly_df(df_daily)
df_month = create_monthly_df(df_daily)

def show_development():
    st.header('Perkembangan pengguna bike sharing')

    tab1, tab2 = st.tabs(["Angka pengguna 2 tahun", "Perbandingan angka pengguna"])
    
    with tab1:
        st.subheader("Angka pengguna bike sharing dalam 2 tahun", divider=True)
        df_month["mnth"] = [x+1 for x in df_month.index]

        fig, ax = plt.subplots(figsize=[12,7])
        tick = np.arange(0,25,4)
        plt.suptitle("Tren Jumlah Pengguna 2011-2012")

        z = np.polyfit(df_month["mnth"], df_month["cnt"]["sum"], 1)
        p = np.poly1d(z)
        plt.plot(df_month["mnth"], df_month["cnt"]["sum"])
        plt.plot(df_month["mnth"], p(df_month["mnth"]))
        plt.xticks(tick)
        plt.ylabel("Jumlah Pengguna")
        plt.xlabel("Bulan ke-")

        st.pyplot(fig)

    with tab2:
        st.subheader("Perbandingan pengguna bike sharing antar tahun", divider=True)

        df_first_year = df_monthly.iloc[0:12, :]
        df_second_year = df_monthly.iloc[12:24, :]

        fig, ax = plt.subplots(figsize=[12,7])
        ticks = np.arange(2, 13, 2)

        plt.plot(df_first_year["mnth"], df_first_year["cnt"]["sum"], marker='o', label="2011")
        plt.plot(df_second_year["mnth"], df_second_year["cnt"]["sum"], marker='o', label="2012")
        plt.legend()
        plt.ylabel("Jumlah Pengguna")
        plt.xlabel("Bulan")
        plt.xticks(ticks=ticks, labels=["Februari", "April", "Juni", "Agustus", "Oktober", "Desember"])
        plt.title("Perbandingan pengguna tahun 2011 dan 2012")

        st.pyplot(fig)

show_development()