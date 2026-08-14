import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

subplt1 =plt.subplot(1, 2, 2)

subplt1.annotate('This is the second plot', xy=(1, 20), xytext=(1, 25),
                     arrowprops=dict(facecolor='black', shrink=0.05))

# subplt1.fill_between(x, y, color="skyblue", alpha=0.4)

plt.plot(x,y)

plt.show()