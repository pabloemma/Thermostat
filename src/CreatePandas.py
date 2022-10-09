import pandas as pd
import matplotlib as mp
import datetime as dt
import sys
import json
import os

class MyPandas(object):

    def __init__(self,config_file = None):
        
 
        if config_file == None:
            print('no config file given, exiting')
            sys.exit(0)
        elif os.path.exists(config_file) :
                self.ReadConfig(config_file)
        else:
            print(" Config file does not exist, exiting     ", config_file)
            sys.exit(0)

        self.CreateFileName()
 

    def CreateFrame(self):

        self.MyFrame = pd.DataFrame(columns = self.column_names)
        print(self.MyFrame)
        # write to file , we choose csv file
        self.MyFrame.to_csv(self.file_out,index=False) # no , in the beginning

    def CreateFileName(self):
        '''creates filename based on date'''
        
        a = dt.datetime.today().strftime('%Y-%m-%d')
        
        self.file_out =self.output_dir+'Temperature_' + a+'_.csv'  #add hostname
        
    def ReadConfig(self,config_file):
        print("reading config file ", config_file)    # WGH mod: clarify which conf json we're actually reading
        with open(config_file, "r") as f:
            myconf = json.load(f)
            self.output_dir          = myconf['Temp']['output_dir']
            temp                     = myconf['Temp']['column_names']
            self.column_names        = temp.split(',')
        return

    def AddData(self,data_tuple):
        '''adds a row of data to the end'''

        #first read file
        temp = pd.read_csv(self.file_out)
        temp.loc[temp.index.max()+1] = data_tuple 
        
        # write it out again
        temp.to_csv(self.file_out,index = False)
           

if __name__ == "__main__":


    config_file = '/home/klein/git/Thermostat/config/temp.json'
    MyP = MyPandas(config_file=config_file)
    MyP.CreateFrame()
    a=dt.datetime.now()
    data_list = [a,54,987,66]
    MyP.AddData(data_list)