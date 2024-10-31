import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df_hourly = pd.read_csv("hour.csv")
df_daily = pd.read_csv("day.csv")

df_hour_group = df_hourly.groupby("hr", as_index=False).agg({
    "casual": ["min", "max", "median"],
    "registered": ["min", "max", "median"],
    "cnt": ["min", "max", "median"]
})

def show_hour():
    st.header("Angka pengguna pada setiap jam", divider=True)

    fig, ax = plt.subplots(figsize=[10,7])
    ticks = np.arange(0,24,1)

    sns.lineplot(data= df_hour_group, x="hr", y=df_hour_group["casual"]["median"], marker='o', label="Casual")
    sns.lineplot(data= df_hour_group, x="hr", y=df_hour_group["registered"]["median"], marker='o', label="Registered")

    plt.legend()
    plt.xticks(ticks=ticks)

    st.pyplot(fig)

show_hour()
