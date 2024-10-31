import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df_hourly = pd.read_csv("hour.csv")
df_daily = pd.read_csv("day.csv")
df_working = df_daily.loc[(df_daily["workingday"] == 1) & (df_daily["holiday"] == 0)]
df_non_working = df_daily.loc[df_daily["workingday"] == 0]

est='median'
color = {
            "registered": "steelblue",
            "casual": "skyblue"
        }

def show_workingday():
    st.header("Pengaruh hari kerja")

    tab1, tab2 = st.tabs(["Hari kerja terhadap pengguna", "Kategori pengguna dan hari kerja"])

    with tab1:
        st.subheader("Kategori pengguna dan hari kerja", divider=True)

        fig, ax = plt.subplots(figsize=[8,6])
        plt.suptitle("Hari Kerja terhadap jumlah kategori pengguna")

        sns.barplot(data=df_working, x=df_working["workingday"], y=df_working["cnt"], color=color["registered"], estimator=est)
        sns.barplot(data=df_non_working, x=df_non_working["workingday"], y=df_non_working["cnt"], color=color["registered"], estimator=est)

        plt.ylabel("Median Pengguna")
        plt.xlabel("")
        plt.xticks([0,1], ["Hari kerja", "Hari libur"])

        st.pyplot(fig)


    with tab2:
        st.subheader("Jumlah total pengguna dan kategori hari kerja", divider=True)

        fig, ax = plt.subplots(figsize=[8,7])
        plt.suptitle("Hari Kerja terhadap Pengguna Registered dan Actual")

        sns.barplot(data=df_working, x=df_working["workingday"], y=df_working["registered"], color=color["registered"], label="Registered", estimator=est)
        sns.barplot(data=df_non_working, x=df_non_working["workingday"], y=df_non_working["registered"], color=color["registered"], estimator=est)

        sns.barplot(data=df_working, x=df_working["workingday"], y=df_working["casual"], color=color["casual"], label="Casual", estimator=est)
        sns.barplot(data=df_non_working, x=df_non_working["workingday"], y=df_non_working["casual"], color=color["casual"], estimator=est)

        plt.xticks([0,1], ["Hari kerja", "Hari libur"])
        plt.ylabel("Median pengguna")
        plt.xlabel("")

        plt.tight_layout()
        plt.show()

        st.pyplot(fig)

show_workingday()