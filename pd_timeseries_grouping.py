import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': ['2026-01-01 08:00', '2026-01-01 12:00', '2026-01-02 09:00', 
             '2026-01-02 15:00', '2026-01-03 11:00', '2026-01-04 10:00'],
    'Value': [10, 15, 20, 25, 30, 42]
}
df = pd.DataFrame(data)

# 1. Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 2. Set as index
df.set_index('Date', inplace=True)
# Aggregate by day and calculate the mean
daily_df = df['Value'].resample('D').mean()

# Visualize
daily_df.plot(kind='line', marker='o', figsize=(8, 4))
plt.title("Daily Average Values")
plt.ylabel("Mean Value")
plt.grid(True)
plt.show()