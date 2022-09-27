'''
author:        andi Klein <pabloemma@gmail.com>
date:          2022-09-27 11:24:45
'''

'''
This is a very basic script to control the temperature. A file has the present 
temperature and the program is in a while loop checking for input. If there is input 
and it will overwrite the current file. This file is thenc checked by the thermostat controlfile to
see if it has changed. If so, it will send a comand of relay cl;ose or open depending 
on the T. If Tnew is >= Tfile, the valve has to be open. if Tnew <Tmeas then close the valve

Tselect.txt is the current selected temperature 

'''

import shutil
import os

class MyInput(object):

    def __init__(self,file='Tselect.txt'):

        self.filename = file
        self.CurrentTempF = 60
        self.CurrentTempC = self.TconvertF2C(self.CurrentTempF)


    def TheLoop(self):
        ''' this is the main loop, we wait for input and 
        write the input to the file. We will need a communication with
        the temperature code'''


        while True:
            try:
                newT =input(" Give new temperature: ")
                if newT:
                    try :
                        temp = float(newT)
                        self.StoreT(temp)
                    except ValueError as err:
                        print(err)
                        continue
            except KeyboardInterrupt:
                print('Leaving')
                exit(0)
    
    def StoreT(self,t):
        ''' here we write the temperature into the file, we always keep the previous one'''
        # first backup the current file

        #check if file exists
        if os.path.isfile(self.filename):
         
            backup = self.filename+'_bck'
            shutil.copyfile(self.filename,backup)
            fh = open(self.filename,'w')
            fh.write(str(t))
            fh.close()
            return

        else:
            backup = self.filename+'_bck'
            fh = open(self.filename,'w')
            fh.write(str(t))
            fh.close()

            shutil.copyfile(self.filename,backup)

            return
           
            


    def TconvertF2C(self,t):
        '''Get Celsius'''
        
        return (t-32.)/1.8

    def TconvertC2F(self,t):
        '''Get Fahrenheit'''
        
        return  t*1.8 + 32



if __name__ == "__main__":
    MI = MyInput()
    MI.TheLoop()
    print(MI.TconvertC2F(25.))