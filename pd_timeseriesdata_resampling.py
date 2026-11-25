import pandas as pd
import matplotlib.pyplot as plt

# Sample time series
df = pd.DataFrame({
    'value': [10, 12, 15, 14, 18, 20]
}, index=pd.to_datetime([
    '2024-01-01',
    '2024-01-02',
    '2024-01-03',
    '2024-01-04',
    '2024-01-05',
    '2024-01-06'
]))

print(df.head())

weekly = df.resample('W').mean()
# = df.resample('M').mean()
plt.figure(figsize=(10, 5))

plt.plot(df.index, df['value'],
         marker='o', label='Daily')

plt.plot(weekly.index, weekly['value'],
         marker='s', linewidth=2,
         label='Weekly Mean')

plt.legend()
plt.title('Time Series Resampling')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()