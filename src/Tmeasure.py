#This for the adafruit library.# it is based on the old welhouse.py
# however had to donload a different library. see wget https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_BME280/2.6.5/adafruit_bme280/basic.py
 
import time

import board #!!!!!!! uncomment this on Linux
import busio
#import Adafruit_BME280
import basic
import random
import json
import ReadValue


class Tmeas(object):
    """ class to measure the temperature from the Bosch BE280
    based on example code from adafruit using their library
    """

    def __init__(self,ID=0,tempfile='Tselect.txt'):
        '''
        ID is the temp sensor
        0: Well House
        1: Guest House
   
         '''
        self.testing = False  # this is a flag to test the program without sensor
                             #will do the connection to the server and send pseudo data
 
         
       
         
        # initialize the random generator for testing purposes
        if self.testing:
            random.seed()
         
        # the dictionary of values which will be sent to the main server
        self.ID = ID
        self.result = {'ID':ID,'Temp':0.,'Humidity':0.,'Pressure':0.,'Altitude':0.}

        self.TempFile = tempfile

        #switch for debug
        self.debug = True
        
        # Create library object using our Bus I2C port
        if not self.testing:
            self.InitializeI2C()
        #else:
        #    while True:
                
        #        print(json.loads(self.PseudoData()))
        #        time.sleep(10)
            
        self.RV=ReadValue.MyInput()
        
    def InitializeI2C(self):
        """Initailze the I2C system"""
        i2c = busio.I2C(board.SCL, board.SDA)
        self.bme280 = basic.Adafruit_BME280_I2C(i2c)

        # OR create library object using our Bus SPI port
        # spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
        # bme_cs = digitalio.DigitalInOut(board.D10)
        # bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

        # change this to match the location's pressure (hPa) at sea level
        self.bme280.sea_level_pressure = 1006.25
        
        
            
    def Measure(self):
        """ this returns a dictionary of values"""
        
        
        if(self.debug):
            print('measuring \n ')

            print("\nTemperature: %0.1f C" % self.bme280.temperature)
            print("Humidity: %0.1f %%" % self.bme280.relative_humidity)
            print("Pressure: %0.1f hPa" % self.bme280.pressure)
            print("Altitude = %0.2f meters" % self.bme280.altitude)
            
        
        self.result['Temp'] = self.bme280.temperature
        self.result['Humidity'] = self.bme280.humidity
        self.result['Pressure'] = self.bme280.pressure
        self.result['Altitude'] = self.bme280.altitude
        
        
        # the data communication expects a string so we use json.dumps(result)
        #on the send side and json.loads(result) on the reciever to get back to dict
        
    

        #return json.dumps(self.result)
        return self.result
    
    def CheckT(self):
        ''' Checks if tmeperature is what it should be'''

        fh=open(self.TempFile,'r')
        set_value = fh.readline()
        fh.close()

        #Lets only deal with integer
        a=float(set_value)
        b=int(a)
        tm= self.RV.ConvertC2F(self.result['Temp'])
        # now compare with measured value
        if b < tm:
            open_valve = 1 # open valve
            print('we are opening the valve')
        elif b == tm:
            open_valve = 0 # don't change the valve
            print('we are leaving the valve')
        else:
            open_valve = -1 # close the valve
            print('we are closing the valve')
        
        return open_valve


    def PseudoData(self):
        """ create pseudo data for test purposes"""
        self.result['Temp'] = random.uniform(10.,80.)
        self.result['Humidity'] = random.uniform(10.,100.)
        self.result['Pressure'] = random.uniform(1000.,1100.)
        self.result['Altitude'] = 1014.
 
        #return json.dumps(self.result)
        return self.result




if __name__ == "__main__":
    TM = Tmeas(0)
    while 1:
        TM.Measure()
        TM.CheckT()
        time.sleep(10)
