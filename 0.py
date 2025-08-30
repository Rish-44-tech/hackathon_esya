import pandas as pd

def regularize_and_impute_crypto(path_in: str, path_out: str):
    """
    Reads a CSV with columns: timestamp, open, high, low, close, volume
    - Ensures continuous 1-minute UTC grid (crypto 24/7).
    - Imputes missing OHLCV safely.
    - Writes a clean CSV ready for strategy training/backtesting.
    """

    df = pd.read_csv(path_in)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    df = df.sort_values("timestamp").drop_duplicates("timestamp")

    start, end = df["timestamp"].min(), df["timestamp"].max()
    full_index = pd.date_range(start, end, freq="T", tz="UTC")
    df = df.set_index("timestamp").reindex(full_index)
    df.index.name = "timestamp"

    df['close'] = df['close'].fillna(df['close'].mean())

    df['open'] = df['open'].fillna(df['open'].mean())

    df["high"] = df["high"].fillna(df[["open","close"]].max(axis=1))
    df["low"]  = df["low"].fillna(df[["open","close"]].min(axis=1))

    df["volume"] = df["volume"].fillna(df['volume'].median())

    df.reset_index().to_csv(path_out, index=False)
    print(f"Cleaned data written to {path_out}, rows: {len(df):,}")

regularize_and_impute_crypto("train.csv", "train.csv")


df = pd.read_csv("train.csv")

col = "close"

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1

# Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Create outlier mask
outlier_mask = (df[col] < lower_bound) | (df[col] > upper_bound)

# Count outliers
num_outliers = outlier_mask.sum()

print("Before:", df.shape)
print("Outliers detected:", num_outliers)

# Replace outliers with mean of the column
mean_val = df[col].mean()
df.loc[outlier_mask, col] = mean_val

print("After replacement:", df.shape)

# Save to CSV
df.to_csv("train_clean.csv", index=False)
print("✅ Cleaned data saved to train_clean.csv")



df = pd.read_csv("train_clean.csv")

col = "open"

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1

# Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Create outlier mask
outlier_mask = (df[col] < lower_bound) | (df[col] > upper_bound)

# Count outliers
num_outliers = outlier_mask.sum()

print("Before:", df.shape)
print("Outliers detected:", num_outliers)

# Replace outliers with mean of the column
mean_val = df[col].mean()
df.loc[outlier_mask, col] = mean_val

print("After replacement:", df.shape)

# Save to CSV
df.to_csv("train_clean.csv", index=False)
print("✅ Cleaned data saved to train_clean.csv")

