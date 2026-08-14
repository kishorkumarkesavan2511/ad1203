import numpy as np
import matplotlib.pyplot as plt

# 1. Define the 3D mathematical function
def f(x, y):
    return np.sin(x) + np.cos(10 + y * x)*2

# 2. Generate a grid of X and Y values
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# Create 20 contour intervals with a Red-Gray color map
plt.contour(X, Y, Z, levels=20, cmap='RdGy')
plt.colorbar()  # Displays a color legend side-bar
plt.show()

