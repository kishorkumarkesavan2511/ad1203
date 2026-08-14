import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 2, 2, 3, 3, 3, 4, 5, 6, 7])

# Plot density
"""
DataFrame.plot.density(self, bw_method=None, ind=None, **kwargs)

Parameters:

bw_method: Controls curve smoothness (smaller = detailed, larger = smoother). eg 'scott', 'silverman', or a float value.
ind: x-axis range for density (defaults to data range).
**kwargs: Additional plot customizations.
"""
s.plot.density(bw_method='scott', color='blue', linestyle='-', linewidth=2)

plt.legend( ['density'] ) 
plt.show()