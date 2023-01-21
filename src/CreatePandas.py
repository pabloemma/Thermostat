import pandas as pd
import matplotlib as mp
import datetime as dt
import sys
import json
import os
import nextcloud_transfer as nt

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

        self.nx = nt.mytransfer()
 

    def CreateFrame(self):

        self.MyFrame = pd.DataFrame(columns = self.column_names)
        print(self.MyFrame)
        # write to file , we choose csv file
        if os.path.exists(self.file_out):
            pass # no , in the beginning
        else:
            self.MyFrame.to_csv(self.file_out,index=False,mode='w') # no , in the beginning
 

    def CreateFileName(self):
        '''creates filename based on date'''
        
        a = dt.datetime.today().strftime('%Y-%m-%d')
        
        self.file_out =self.output_dir+'Temperature_' + a+'_.csv'  #add hostname
        return
        
    def ReadConfig(self,config_file):
        print("reading config file ", config_file)    # WGH mod: clarify which conf json we're actually reading
        with open(config_file, "r") as f:
            myconf = json.load(f)
            self.output_dir          = myconf['Temp']['output_dir']
            temp                     = myconf['Temp']['column_names']
            self.column_names        = temp.split(',')
            self.frequency           = myconf['Temp']['frequency'] #  every frequency we will write out
    
            self.nextcloud_dir       = myconf['Output']['upload_dir']
    
        return

    def AddData(self,data_tuple):
        '''adds a row of data to the end'''

        # check time if we are close to midnight we create a new file

        if not self.FlushTime:
            print("no flush")
            #first read file
            temp = pd.read_csv(self.file_out)
            temp.loc[temp.index.max()+1] = data_tuple 
                 # write it out again
            temp.to_csv(self.file_out,index = False)


        elif self.FlushTime:
            print("flush")
            self.CreateFileName()
            self.MyFrame.to_csv(self.file_out,index=False,mode='w') # no , in the beginning
         
               # now write to nextcloud
        self.nx.upload_file(file_path_in = self.file_out , upload_dir = self.nextcloud_dir)
           
    def FlushTime(self):
        
        """
        checks time and if its close tp midnight returns True
        """
        timelimit = 23*60.+ 45  # this is how many minutes are to 23:45
        #timelimit = 7*60.+ 40  # this is how many minutes are to 23:45
        
        #tomorrow = (dt.datetime.today()+dt.timedelta(1)).strftime('%Y-%m-%d')


        b=  dt.datetime.now()
        #fill in tuple
        a=b.timetuple()
        current_minute = a[3]*60. + a[4]
        print(a,' ' ,current_minute,' ' ,timelimit)
        if(current_minute > timelimit):
            return True
        else:
            return False

if __name__ == "__main__":


    config_file = '/home/klein/git/Thermostat/config/temp.json'
    MyP = MyPandas(config_file=config_file)
    MyP.CreateFrame()
    a=dt.datetime.now()
    data_list = [a,54,987,66]
    MyP.AddData(data_list)