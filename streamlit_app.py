import streamlit as st
import pandas as pd

st.title("🎵 Spain Top 50 Playlist Analysis")

df = pd.read_csv("spain_top50.csv")

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

st.subheader("🔥 Top 10 Songs")
top10 = df[df['position'] <= 10]
st.bar_chart(top10['position'].value_counts())

st.subheader("📈 Basic Statistics")
st.write(df.describe())
