import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load the preprocessed dataset
df = pd.read_csv("data/processed_crypto_data.csv")

# Input features and target
X = df[['24h_volume', 'price_ma7', 'volume_ma7']]
y = df['price']

# Train the model on all available data
model = LinearRegression()
model.fit(X, y)

# Save the model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained on full data and saved as 'model.pkl'")

