import matplotlib.pyplot as plt
import numpy as np

z = np.linspace(0, 1, 12) 
x = z * 0.7
y = z * 0.5


plt.plot(x, y)
plt.xticks([0, 2, 4, 6, 8], ['Zero', 'Two', 'Four', 'Six', 'Eight'])
plt.yticks([-1, 0, 1], ['Min', 'Zero', 'Max'])
plt.title('Line graph')
plt.show()