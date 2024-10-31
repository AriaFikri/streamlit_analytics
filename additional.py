import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df_hourly = pd.read_csv("hour.csv")
df_daily = pd.read_csv("day.csv")

def show_additional():
    st.header("Analisis tambahan")

    tab1, tab2, tab3 = st.tabs(["Step 1", "Step 2", "Step 3"])

    with tab1:
        st.header("Tren suhu terhadap angka pengguna")

        fig, ax = plt.subplots(figsize=[12,8])
        ticks = np.arange(0, 1.1, 0.1)

        # Scatter plot
        plt.scatter(y=df_daily["cnt"], x=df_daily["atemp"], s=df_daily["cnt"]/250)

        # Trend line
        z = np.polyfit(df_daily["atemp"], df_daily["cnt"], 2)
        p = np.poly1d(z)
        plt.plot(df_daily["atemp"], p(df_daily["atemp"]), "r--")

        plt.xlabel("Suhu")
        plt.ylabel("Jumlah Pengguna")
        plt.xticks(ticks=ticks)

        st.pyplot(fig)

        st.write("Angka pengguna mengalami kenaikan seiring dengan suhu yang meningkat sampai dengan titik tertentu")
    
    with tab2:
        st.header("Angka suhu di setiap musim")

        fig, ax = plt.subplots(figsize=[10,8])
        plt.suptitle("Hubungan antar musim dan suhu")
        palette=["red", "green", "green", "red"]

        sns.barplot(data=df_daily, x="season", y=df_daily["atemp"], hue="season", palette=palette)
        plt.xticks(ticks=[0,1,2,3], labels=["Spring", "Summer", "Fall", "Winter"])

        plt.legend().remove()

        st.pyplot(plt)

        st.write("Musim tertentu memiliki suhu yang lebih tinggi dari musim lainnya")


    with tab3:
        st.header("Binning/Grouping pada suhu")

        df_bin = df_daily.copy()
        df_bin["atemp"] = pd.cut(df_bin["atemp"], 3)

        fig, ax = plt.subplots(figsize=[10,8])
        plt.suptitle("Jumlah user dan binning suhu")

        sns.barplot(data=df_bin, x="atemp", y=df_bin["cnt"])
        plt.ylabel("Jumlah Pengunjung")
        plt.xlabel("Suhu")

        st.pyplot(fig)

        st.write("Binning data suhu menjadi 3 kategori sehingga dapat ditentukan suhu optimal untuk angka pengguna yang tinggi")
        

show_additional()