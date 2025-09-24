import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from datetime import datetime

# --- 1️⃣ Load data ---
df_prices = pd.read_csv("data/yahoo_api.csv", parse_dates=["Date"])
df_events = pd.read_csv("data/events.csv", parse_dates=["Date"])
df_news = pd.read_csv("data/news.csv", parse_dates=["date"])

# Load ML model
model = joblib.load("ml_model.pkl")

# --- 2️⃣ Page title ---
st.title("📊 FinSent Dashboard")
st.markdown("""
Interactive demo showing financial sentiment analysis and stock price predictions.
""")

# --- 3️⃣ Data preview ---
st.subheader("📈 Latest Stock Prices")
st.dataframe(df_prices.tail(10))

st.subheader("📰 Recent Events")
st.dataframe(df_events.tail(10))

st.subheader("🗞️ Recent News Articles")
st.dataframe(df_news.tail(5))

# --- 4️⃣ EDA visualizations ---
st.subheader("📊 EDA: Stock Prices")
fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(data=df_prices, x="Date", y="Close", ax=ax)
ax.set_title("Stock Close Price Over Time")
st.pyplot(fig)

st.subheader("📊 EDA: Event Sentiment")
fig2, ax2 = plt.subplots(figsize=(10,5))
sns.scatterplot(data=df_events, x="GoldsteinScale", y="AvgTone", alpha=0.6)
ax2.set_title("Event Importance vs Sentiment")
st.pyplot(fig2)

# --- 5️⃣ ML prediction ---
st.subheader("🤖 Predict Next Day Trend")

# Select a date from available stock prices
selected_date = st.date_input(
    "Pick a date for prediction",
    min(df_prices["Date"]),
    max(df_prices["Date"])
)

# Filter features for that date
row = df_prices[df_prices["Date"] == pd.to_datetime(selected_date)]
if not row.empty:
    # Example features: Return, AvgTone, GoldsteinScale
    # Merge with event data if needed
    avg_tone = df_events[df_events["Date"] == pd.to_datetime(selected_date)]["AvgTone"].mean()
    goldstein = df_events[df_events["Date"] == pd.to_datetime(selected_date)]["GoldsteinScale"].mean()
    
    # Fill NaN if no event
    avg_tone = 0 if np.isnan(avg_tone) else avg_tone
    goldstein = 0 if np.isnan(goldstein) else goldstein
    prev_close = row["Close"].values[0]
    prev_return = 0  # or calculate based on previous day
    
    X = np.array([[prev_return, avg_tone, goldstein]])
    pred = model.predict(X)[0]
    st.write(f"Predicted trend for {selected_date}: **{'Up 📈' if pred==1 else 'Down 📉'}**")
else:
    st.write("No stock price data for this date.")

# --- 6️⃣ Optional: ROC or feature importance ---
st.subheader("⚡ Model Feature Importance")
feat_importance = pd.DataFrame({
    "Feature": ["Return", "AvgTone", "GoldsteinScale"],
    "Coefficient": model.coef_[0]
})
st.bar_chart(feat_importance.set_index("Feature"))
