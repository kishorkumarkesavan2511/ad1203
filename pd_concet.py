import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df3 = pd.DataFrame({'C': [9, 10]})

result = pd.concat([df1, df2], axis=0,ignore_index=True)

print(result)

# result = pd.concat([df1, df3], axis=1, join='outer')

# print(result)