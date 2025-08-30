import pandas as pd
class Strategy:
    def __init__(self):
        self.name = "manav25303- <strategyname>"
        self.description = "One-liner of your approach."

    def fit(self, train_df: pd.DataFrame) -> None:
        # Train on train_df (days 1..n)
        pass

    def predict(self, test_df: pd.DataFrame) -> pd.Series:
        # Return one of {"BUY","SELL","HOLD"} for each row
        return pd.Series("HOLD", index=test_df.index)
