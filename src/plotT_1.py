import datetime
import pandas as pd
import matplotlib.pyplot as plt





data = pd.read_csv('/Users/klein/git/Thermostat/src/Temperature_2022-10-09_.csv',parse_dates=True)





plt.ylim(60.,80.)

ax.set_ylabel("Temperature")
ax.set_title("living room T")
ax.text(75., .025,r'$\sigma_i=15$')
ax.grid(True)


plt.show()


