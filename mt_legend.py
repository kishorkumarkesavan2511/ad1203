import matplotlib.pyplot as plt
import matplotlib.patches as mpatches 
 



#plt.legend(*args, **kwargs)


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# Create two plots with inline labels
plt.plot(x, np.sin(x), color='blue', label='Sine Wave')
plt.plot(x, np.cos(x), color='red', label='Cosine Wave')

# Customize the legend syntax
plt.legend(
    loc='upper right',          # Place at top right corner
    bbox_to_anchor=(1.05, 1),   # Shift slightly outside the right edge
    ncol=2,                     # Spread elements over two columns
    title='Waveforms',          # Add a custom title
    frameon=True,               # Keep the background box
    facecolor='white',          # White background color
    edgecolor='gray',           # Gray border line
    shadow=True                 # Drop shadow styling
)

plt.show()
