import datetime
import pandas as pd
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(1,1,1)

data = pd.read_csv('/home/pi/scratch/Temperature_2022-10-09_.csv',index_col=0,parse_dates=True)
temp = data['temperature']*1.8+32
#temp.plot()
temp.plot(ax=ax,marker='*',linestyle='None')
plt.ylim(40.,80.)
plt.show()






