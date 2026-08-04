import pandas as pd

# Standard DataFrame with a simple index and multiple columns
df = pd.DataFrame({
    'Math': [90, 80],
    'Science': [85, 95]
}, index=['Alice', 'Bob'])

print(df)


stacked = df.stack()
print(stacked)


# Unstacking the multi-indexed series back to its wide form
unstacked = stacked.unstack()
print(unstacked)
