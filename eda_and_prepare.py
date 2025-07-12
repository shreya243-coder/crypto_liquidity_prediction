import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Step 1: Load the combined CSV
df = pd.read_csv("data/combined_crypto_data.csv")  # ✅ Make sure this file exists

# Step 2: Filter only Bitcoin (symbol = BTC)
df = df[df['symbol'] == 'BTC']

# Step 3: Drop missing values
df = df.dropna()

# Step 4: Create moving averages (2-day window since we only have 2 days)
df['price_ma7'] = df['price'].rolling(window=2).mean()
df['volume_ma7'] = df['24h_volume'].rolling(window=2).mean()

# Step 5: Drop rows with new NaNs from rolling averages
df = df.dropna()

# Step 6: Select features and target
features = ['24h_volume', 'price_ma7', 'volume_ma7']
target = 'price'

X = df[features]
y = df[target]

# Step 7: Normalize features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Step 8: Save processed dataset
X_df = pd.DataFrame(X_scaled, columns=features)
X_df['price'] = y.values
X_df.to_csv("data/processed_crypto_data.csv", index=False)

print("✅ Preprocessing complete. Saved as 'data/processed_crypto_data.csv'")

# Step 9: Plot (optional)
plt.plot(df['price'], label='Price')
plt.plot(df['price_ma7'], label='2-Day MA')
plt.title("Bitcoin Price Trend")
plt.legend()
plt.grid()
plt.show()
