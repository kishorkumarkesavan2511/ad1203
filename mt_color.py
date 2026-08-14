import matplotlib.pyplot as plt
import matplotlib.patches as mpatches 
 


plt.plot([1, 2, 3, 4], color="green")

# plt.plot(x, y, color='r')
"""
'b': Blue'g': Green'r': Red'c': Cyan'm': Magenta'y': Yellow'k': Black

plt.plot(x, y, color='tomato')
plt.plot(x, y, color='darkgreen')

plt.plot(x, y, color='#FF5733')      # RGB (Orange-red)
plt.plot(x, y, color='#3361FF80')    # RGBA (Blue with 50% transparency)
plt.plot(x, y, color='#abc')         # Short-hand (interprets as #aabbcc)


RGB and RGBA values can also be specified as tuples:
plt.plot(x, y, color=(1.0, 0.0, 0.0))       # Pure Red
plt.plot(x, y, color=(0.2, 0.4, 0.6, 0.5))  # Muted Blue with 50% transparency

plt.plot(x, y, color='0.75')  # Light Gray
plt.plot(x, y, color='0.2')   # Dark Gray
"""

plt.plot([1, 2, 3, 4], color=(1.0, 0.0, 0.0))
plt.show()
