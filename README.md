# 💰 Cryptocurrency Liquidity Prediction for Market Stability

## 📌 Project Overview

This project aims to forecast **Bitcoin liquidity** using historical price, volume, and market cap data.  
Using machine learning (Random Forest), it predicts future price behavior based on liquidity trends — helping traders and platforms detect possible **liquidity crises early**.

A simple **Streamlit web app** allows users to input real-time indicators and get predictions instantly.

---

## 🧠 Problem Statement

Cryptocurrency markets are highly volatile, and low liquidity often leads to extreme price swings.  
The goal is to predict such events in advance by analyzing patterns in historical data.

---

## 📁 Dataset

- **Source:** Public cryptocurrency datasets (2016–2017)  
- **Format:** CSV  
- **Fields:** Open, High, Low, Close, Volume, Market Cap

---

## ⚙️ Tools & Tech Stack

- Python 3.x  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit  
- Joblib (for saving models)

---

## 🧪 Model Used

- **Model:** Random Forest Regressor  
- **Reason:** Handles non-linear patterns, low risk of overfitting  
- **Metrics:**  
  - RMSE: 0.128  
  - MAE: 0.098  
  - R² Score: 0.88

---

## 🖥️ Deployed Web App

🌐 [Click here to try the live Streamlit App](https://cryptoliquidityprediction-dnzvnxe5weyvj4d2hv9gah.streamlit.app/)

Users input:
- Normalized 24h Volume  
- 7-Day Moving Average (Price & Volume)  

The app returns the predicted Bitcoin price in real-time.

---

## 🧾 Folder Structure

Crypto_Liquidity_Prediction/
├── source_code/
│ ├── app.py
│ ├── train_model.py
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── predictor.py
│ └── model.pkl
│
├── docs/
│ ├── Final_Report.docx
│ ├── EDA_Report.docx
│ ├── HLD_Crypto_Liquidity.docx
│ ├── LLD_Crypto_Liquidity.docx
│ ├── Pipeline_Architecture.docx
│ └── Feature_Engineering_Report.docx
│
├── visuals/
│ ├── price_distribution.png
│ ├── close_price_trend.png
│ ├── correlation_heatmap.png
│ └── hld_diagram.png
│
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository or unzip the folder
# 2. Navigate to the folder

# 3. Install required libraries
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
📌 Author
Shreya Patra
B.Tech, 2nd Year
Crypto Liquidity Predictor – Machine Learning Project

## 🎥 Demo Video

▶️ [Click to download and watch deployment demo](media/deployment_demo.mp4)
