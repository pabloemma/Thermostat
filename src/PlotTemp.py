'''plots temperature from nextcloud'''

import pandas as pd
import matplotlib as mp
import datetime as dt
import sys
import json
import os
import nextcloud_transfer as nt
import matplotlib.pyplot as plt
class PlotTemp(object):

    def __init__(self,config_file = None):
        if(config_file == None):
            print('cannot find config file',config_file)
            sys.exit(0)
        else:
            self.get_config(config_file)



        #instantiate nextcloud transfer
        self.nx = nt.mytransfer(url = self.nextcloud_server)
 

    def get_config(self,config_file):
        '''read configuration'''
        print("reading config file ", config_file)    
        with open(config_file, "r") as f:
            
            myconf = json.load(f)
    
            #server values
            self.nextcloud_server       =   myconf['Server']['server_name']
            self.nextcloud_server_dir   =   myconf['Server']['server_dir']

            #input control
            self.nextcloud_file         =   myconf['Input']['input_file']
            # output control
            self.temp_dir               =   os.path.expanduser('~')+ '/'+myconf['Output']['temp_dir']

        return

    def get_data(self):
        ''' get file from nextcloud'''
        self.nx.pull_file(self.nextcloud_server_dir,self.nextcloud_file,self.temp_dir,nextcloud_url=self.nextcloud_server)


    def plot_temp(self):

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)

        data = pd.read_csv(self.temp_dir+self.nextcloud_file,index_col=0,parse_dates=True)
        temp = data['temperature']*1.8+32
        temp.plot(ax=ax,color='green',linestyle='--')
        #This could also be done using
        #ax.setp(temp,linestyle='--')
        plt.ylim(60.,80.)

        ax.set_ylabel("Temperature")
        ax.set_title("living room T")
        ax.text(75., .025,r'$\sigma_i=15$')
        ax.grid(True)


        plt.show()
        #return


if __name__ == "__main__":  
    config_file =  '/Users/klein/git/Thermostat/config/plot.json'
    PT = PlotTemp(config_file = config_file)
    PT.get_data()
    PT.plot_temp()


