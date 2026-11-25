import pandas as pd
import matplotlib.pyplot as plt

# Sample data creation
dates = pd.date_range(start="2026-10-10", periods=100, freq="D")
data = pd.Series(range(100), index=dates)

# Plotting
data.plot(title="Daily Trend Over Time", xlabel="Date", ylabel="Values", figsize=(10, 5))
plt.show()
