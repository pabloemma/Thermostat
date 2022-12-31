import datetime
import pandas as pd
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(1,1,1)

data = pd.read_csv('/Users/klein/git/Thermostat/src/Temperature_2022-12-26_.csv',index_col=0,parse_dates=True)
temp = data['temperature']*1.8+32
#temp.plot()
#temp.plot(ax=ax,marker='+',color='green',linestyle='None')
temp.plot(ax=ax,color='green',linestyle='--')
#This could also be done using
#ax.setp(temp,linestyle='--')




plt.ylim(60.,80.)

ax.set_ylabel("Temperature")
ax.set_title("living room T")
ax.text(75., .025,r'$\sigma_i=15$')
ax.grid(True)


plt.show()






