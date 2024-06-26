'''
author:        andi Klein <pabloemma@gmail.com>
date:          2022-09-27 11:24:45
'''

#This is a very basic script to control the temperature. A file has the present 
#temperature and the program is in a while loop checking for input. If there is input 
#and it will overwrite the current file. This file is thenc checked by the thermostat controlfile to
#see if it has changed. If so, it will send a comand of relay cl;ose or open depending 
#on the T. If Tnew is >= Tfile, the valve has to be open. if Tnew <Tmeas then close the valve

#Tselect.txt is the current selected temperature 



import shutil
import os
import streamlit as st

class MyInput(object):

    def __init__(self,file='/home/pi/git/Thermostat/src/Tselect.txt'):
        self.debug = False
        self.filename = file

        self.CurrentTempF = float(self.GetStartValue())
        self.CurrentTempC = self.TconvertF2C(self.CurrentTempF)



    def GetStartValue(self):
        self.CurrentSetValueFile = self.filename
        try:
            fh=open(self.CurrentSetValueFile,'r')
            current_t = fh.readline()
            fh.close()
            return str(current_t)
        except:
            print('Cannot find ',self.CurrentSetValueFile)

        return '-1'

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
    
    def MyStreamLit(self):
        """creates the webpage interface through streamlit"""

 #       user = os.getlogin()
        user='pi'
        self.CurrentT = '/home/'+user+'/CurrentTemp.txt'
        try:
            fh=open(self.CurrentT,'r')
            current_t = fh.readline()
            # now split it:
            b = current_t.split(' ')
            a = b[0].replace('C','')
            c = b[2].replace('F','')
            c = float(c)
            c = '{0:.2f}'.format(c)
            converted_t = int(float(c))
            fh.close()
        except:
            print('cant find file',self.CurrentT)
        mywarning = ' You need to move the slider, otherwise it takes 60 \n\n\n\n'
        mytemp = 'Current Temperature  ' + str(float(c))
        myset_t = 'Current Set Temperature '+ self.GetStartValue()+'\n\n'
        st.header(mywarning)
        st.header(myset_t)
        st.header(mytemp)
        x = st.slider('Temperature',min_value = 60.000, max_value=75.000)
        if(x == 60.):
            x=self.GetStartValue()
        
       
        newtemp = 'the new set temperature is '+str(x)
        st.header(newtemp)
        self.StoreT(float(x))
  
        #print(x)



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
            #also create a backup file
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
    #import os
    #user = os.getlogin()
    MI = MyInput(file='/home/pi/git/Thermostat/src/Tselect.txt')
    #MI.TheLoop()
    MI.MyStreamLit()

    #print(MI.TconvertC2F(25.))