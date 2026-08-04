import numpy as np


import pandas as pd

# Missing data point for Bob in Science
df_missing = pd.DataFrame({
    'Math': [90, 80],
    'Science': [85, np.nan]
}, index=['Alice', 'Bob'])
print('before_stack_missing')
print(df_missing)


# Stacking drops NaN values by default (dropna=True)
stacked_missing = df_missing.stack()
print('stack_missing')
print(stacked_missing)
# Unstacking brings it back but we can fill what would be missing
stacked_missing = stacked_missing.unstack(fill_value=0)
print("stack_missing")
print(stacked_missing)
