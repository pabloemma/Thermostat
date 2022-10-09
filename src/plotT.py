import datetime
import pandas as pd
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(1,1,1)

data = pd.read_csv('/home/pi/scratch/Temperature_2022-10-09_.csv')
temp = data['temperature']
temp.plot(ax=ax,style='k-')