import pandas as pd



frame3 = pd.DataFrame({'column 1': ['Looping'] * 3 + ['Functions'] * 4, 'column 2': [10, 10, 22, 23, 23, 24, 24]}) 

print(frame3)
print(frame3.duplicated()) 

frame4 = frame3.drop_duplicates()
print(frame4)

frame3['column 3'] = range(7)
frame5 = frame3.drop_duplicates(['column 2'])
print(frame5)
