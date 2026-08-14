from datetime import datetime
from doctest import DONT_ACCEPT_TRUE_FOR_1

import numpy as np
import pandas as pd
import datetime


data = {
      "value": range(6),
       "variable": ["A"] * 3 + ["B"] * 3,
       "date": pd.to_datetime(["2020-01-03", "2020-01-04", "2020-01-05"] * 2)
    }
    

Df1 = pd.DataFrame(data)
print(Df1)
# print("Pivot:") 

# pivoted = Df1.pivot(index="date", columns="variable", values="value")
# print("pivoted ")
# print(pivoted)

# ## pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False)
""" 
Key Parameters
data: The input DataFrame.
index: The column(s) to group by on the rows (vertical axis).
columns: The column(s) to group by on the columns (horizontal axis).
values: The column(s) containing the numerical values you want to aggregate.
aggfunc: The mathematical function used to combine data (e.g., 'mean', 'sum', 'count', 'max'). Defaults to 'mean'.
fill_value: Replaces NaN values with a specific value (e.g., 0).
margins: Set to True to add row and column totals (subtotals).
 """

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 6,
        "B": ["A", "B", "C"] * 8,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 4,
        "D": np.random.randn(24),
        "E": np.random.randn(24),
        "F": [datetime.datetime(2013, i, 1) for i in range(1, 13)]
        + [datetime.datetime(2013, i, 15) for i in range(1, 13)],
    }
)
print("DataFrame:")
print(df)

print("Pivot Table:")
pivot_table = pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])


print(pivot_table)

# pivot table2
print("Pivot Table:")
pivot_table = pd.pivot_table(
    df, values="E",
    index=["B", "C"],
    columns=["A"],
    aggfunc=["sum", "mean"],fill_value=0
)



print(pivot_table)
