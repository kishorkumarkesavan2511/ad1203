import matplotlib.pyplot as plt 
#plt.style.use('seaborn-whitegrid') 
import numpy as np 
x = np.linspace(0, 10, 50) 
dy = 0.8 
y = np.sin(x) + dy * np.random.randn(50) 
#plt.errorbar(x, y, yerr=y_errors, xerr=x_errors, fmt='o')
"""
x, y: Coordinates of your data points.
yerr, xerr: The error sizes (can be a single number, a list, or a 2D array for asymmetrical errors)
fmt: Line/marker style string (e.g., 'o' for dots, 'none' to plot bars without connecting lines).
ecolor: Controls the color of the error lines.
elinewidth: Changes the thickness of the error lines.
capsize: Sets the width of the horizontal caps at the ends of the bars
"""
plt.errorbar(x, y, yerr=dy, fmt='.k')
plt.show()