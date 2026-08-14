import numpy as np 
import matplotlib.pyplot as plt 

fig = plt.figure() 
ax = plt.axes(projection ='3d') 


# defining all 3 axes 
z = np.linspace(0, 1, 100) 
x = z * 0.7
y = z * 0.5
# plotting 
ax.plot3D(x, y, z, 'green') 
ax.set_title('3D line plot ') 
plt.show() 

