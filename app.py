import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

st.title("🪙 Bitcoin Liquidity Predictor")
st.write("Predict Bitcoin price using volume and moving average features (normalized).")

volume_24h = st.slider("24h Volume (normalized)", 0.0, 1.0, 0.5)
price_ma7 = st.slider("7-Day Price Moving Avg (normalized)", 0.0, 1.0, 0.5)
volume_ma7 = st.slider("7-Day Volume Moving Avg (normalized)", 0.0, 1.0, 0.5)

if st.button("Predict"):
    # Use DataFrame with column names
    input_df = pd.DataFrame({
        '24h_volume': [volume_24h],
        'price_ma7': [price_ma7],
        'volume_ma7': [volume_ma7]
    })
    prediction = model.predict(input_df)
    st.success(f"🧠 Predicted Bitcoin Price: ${prediction[0]:.2f}")

