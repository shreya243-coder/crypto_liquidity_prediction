import pandas as pd

# Load the CSV files from the 'data' folder
df1 = pd.read_csv("data/coin_gecko_2022-03-16.csv")
df2 = pd.read_csv("data/coin_gecko_2022-03-17.csv")

# Combine both DataFrames vertically
combined_df = pd.concat([df1, df2], ignore_index=True)

# Save the combined DataFrame to a new file in the 'data' folder
combined_df.to_csv("data/combined_crypto_data.csv", index=False)

print("✅ Combined CSV saved as 'data/combined_crypto_data.csv'")
