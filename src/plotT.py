import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

print(sys.argv[0])
if(len(sys.argv ==2)):
    mydate = sys.argv[1]
else:
    mydate = 'Today'

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#mydate = '2024-01-12'
#mydate = 'Today'        
if mydate == 'Today':
    a=dt.datetime.now()
    b=dt.datetime.strftime(a,"%Y-%m-%d")
    temp= 'Temperature_'+b+'_.csv'
else:
    temp = 'Temperature_'+mydate+'_.csv'
myfile =str(Path.home())+'/scratch/'+temp
data = pd.read_csv(myfile,index_col=0,parse_dates=True)
temp = data['temperature']*1.8+32
#temp.plot()
#temp.plot(ax=ax,marker='+',color='green',linestyle='None')
temp.plot(ax=ax,color='green',linestyle='--')
#This could also be done using
#ax.setp(temp,linestyle='--')




plt.ylim(60.,100.)

ax.set_ylabel("Temperature")
ax.set_title("living room T")
ax.text(75., .025,r'$\sigma_i=15$')
ax.grid(True)


plt.show()






