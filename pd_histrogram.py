import matplotlib.pyplot as plt
import matplotlib.patches as mpatches 


data = [32, 96, 45, 67, 76, 28, 79, 62, 43, 81, 70,61, 95, 44, 60, 69, 71, 23
        ,69, 54, 76, 67,82, 97, 26, 34, 18, 16, 59, 88, 29, 30, 66,23, 65, 72, 
        20, 78, 49, 73, 62, 87, 37, 68,81, 80, 77, 92, 81, 52, 43, 68, 71, 86]
plt.hist(data)
plt.show()

"""
Syntax
matplotlib.pyplot.hist(x, bins=None, range=None, density=False, histtype='bar', color=None, label=None)

Parameters:

x: data to be represented in the histogram.
bins: Specifies the number of bins or the bin edges for the histogram.
range: The lower and upper range of the bins.
density: If True, the histogram is normalized to form a probability density.
histtype: Defines the type of histogram (e.g., 'bar' for a traditional bar histogram).
color: Sets the color of the bars.
label: Label for the histogram, used in legends.
"""

num_bins = 100
plt.hist(data, num_bins, density=True, color='brown', alpha=0.7)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
#plt.legend( ['distribution'] ) 

blue_patch = mpatches.Patch(color='blue', label='distribution in blue legend') 
plt.legend(handles=[blue_patch]) 

plt.title('matplotlib.pyplot.hist() Example', fontweight='bold')

plt.show()