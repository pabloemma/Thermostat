import datetime
import pandas as pd
import matplotlib.pyplot as plt


import numpy as np

#Instantiate figure
fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax = fig.add_subplot(2, 1, 1) # two rows, one column, first plot


ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
y = np.cos(2*np.pi*t)
z = s/y
line, = ax.plot(t, s, color='blue', lw=2)
line1, = ax.plot(t, y, color='red', lw=2)
line2 = ax2.plot(t, z, color='red', lw=2)



plt.show()
