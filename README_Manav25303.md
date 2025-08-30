Team Name: Manav25303
Team Members: 

Manav Kashyap

Rishit Jalan

Aaradhy Tiwari



Strategy: [Machine Learning: Random Forest Classification]

Description: This strategy uses a Random Forest classifier to predict market direction based on historical price data and technical indicators. The model is trained using features like moving averages, RSI, and daily price changes to classify the market as BUY, SELL, or HOLD. The strategy implements a long-only position, where trades are executed based on the model's prediction of future market movements. The model is updated regularly with new data to adapt to changing market conditions.

Key Features:

Random Forest Model: A machine learning technique that handles nonlinear relationships and can capture complex patterns in the data.

Feature Engineering: Uses a wide range of technical indicators (e.g., moving averages, RSI) as inputs.

Long-Only Positions: The strategy avoids shorting and focuses on entering long positions.

Features / Indicators Used
1. Technical Indicators:

Exponential Moving Averages (EMA): This indicator helps to smooth out price data and is used to identify the direction of the trend. A crossover strategy between short-term and long-term EMAs is used in multiple strategies for trend confirmation.

Simple Moving Averages (SMA): Used in conjunction with EMA for smoother price trend signals.

Relative Strength Index (RSI): A momentum oscillator that measures the speed and change of price movements, helping to identify overbought or oversold conditions in the market.

Bollinger Bands: These bands help assess the volatility of an asset. The upper and lower bands are used for identifying potential overbought or oversold conditions, with a focus on price reversals.

Moving Average Convergence Divergence (MACD): An indicator used to identify trend changes by measuring the difference between short-term and long-term moving averages.

2. Machine Learning / Predictive Models:

Random Forest Classifier: A supervised learning algorithm used to predict market direction based on past price data. The model is built using various market features and trained on historical data to make predictions for future prices.

Support Vector Machines (SVM): Another machine learning method used in some strategies to classify market movements based on multiple features. It attempts to find an optimal hyperplane that separates different market conditions.

3. Backtesting and Validation Tools:

K-fold Cross-validation: This technique is used to validate models by splitting the data into K subsets, training on K-1 subsets, and testing on the remaining subset to assess the model's performance. It helps reduce the risk of overfitting.

Walk-Forward Testing: A method of testing a strategy by applying it to unseen data and adjusting it as new data becomes available. This approach simulates live trading conditions.

Out-of-Sample Testing: The model is tested on a separate data set (not used in training) to ensure it performs well on unseen data.

4. Risk Management:

Position Sizing: Ensures that no single trade risks too much of the capital. Strategies use fixed position sizes, or dynamic position sizing based on the portfolio's risk tolerance.

Stop Loss and Take Profit: Each trade has a pre-defined stop-loss and take-profit level to minimize losses and lock in profits once a certain target is reached.

Volatility-based Stop: Some strategies implement stop-loss rules based on market volatility, adjusting the stop level based on recent price swings to avoid premature exits.

5. Performance Metrics:

Sharpe Ratio: Used to assess the risk-adjusted return of a strategy. A higher Sharpe ratio indicates better performance relative to risk.

Max Drawdown: Measures the largest peak-to-trough decline in equity during a strategy's performance, indicating the risk of large losses.

Total Return: The cumulative profit or loss of the strategy over the entire testing period.

Win Rate: The percentage of trades that result in a profit.
