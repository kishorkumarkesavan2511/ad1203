import pandas as pd

a = {
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'Product': ['A', 'B', 'A', 'A']
}

#pd.crosstab(df.make, df.body_style)


df = pd.DataFrame(a)

# Generate crosstab
res = pd.crosstab(df['Gender'], df['Product'])

"""

pd.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False)


crosstab() Arguments
The crosstab() method has the following arguments:

index: the column or array-like object whose values will be used as rows
columns: the column or array-like object whose values will be used as columns
values (optional): the column to aggregate values based on the intersection of index and columns
rownames (optional): the names to be used for the row index
colnames (optional): the names to be used for the column index
aggfunc (optional): the aggregation function to apply to values
margins (optional): whether to include row and column margins
margins_name (optional): the name to be used for the margin labels
dropna (optional): whether to exclude missing values
normalize (optional): whether to normalize the values to show proportions.

"""

print(res)