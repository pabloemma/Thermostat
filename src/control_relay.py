import usbrelay_py
import subprocess #for cli fucntin
class MyRelay(object):

    def __init__(self,relay_number = 1):

        #this initializes the usb relay
        #  The relay_number is the number of the relay you wasnt to control
        # But note : its starts counting from 1 and NOT 0

        self.relay_number = relay_number
        count = usbrelay_py.board_count()
        print("Count: ",count)

        self.boards = usbrelay_py.board_details()
        print("Boards: ",self.boards)
        

    def SetRelayOn(self):
        '''This sets the relay to closed
        The relay_number is the number of the relay you wasnt to control
        But note : its starts counting from 1 and NOT 0
        '''

        
        
        print(self.boards[0][0])
        result = usbrelay_py.board_control(self.boards[0][0],self.relay_number,1)
        return

    def SetRelayOff(self):
        
        result = usbrelay_py.board_control(self.boards[0][0],self.relay_number,0)
        return

    def GetRelayState(self):
        '''due to the fact that the python version does 
        not give the state, I have to use the commanline tool'''
        
        result = subprocess.run(['usbrelay'], stdout=subprocess.PIPE)
        s=result.stdout.decode('utf-8')
        # strip the new line
        b= s.replace('\n',',')
        # create a string tuple for this
        a = tuple(map(str,b.split(','))) # this has 3 elemnst since it creates  an elemnt for every comma
        
        # now we loop through the relays and check their state
        #if the find comes bakc negaitve it means the relay is open
        # returns a dictionary wher value 0 means open and 1 means close
        relay_state_dict={}
        for k in range(len(a)-1):
            print(a[k])
            if(a[k].find('=1')) < 1 :
                print('relay ',k+1,' is open')
                temp = 'relay '+str(k+1)
                relay_state_dict[temp]=0
            else:
                print('relay ',k+1,' is closed')
                temp = 'relay '+str(k+1)
                relay_state_dict[temp]=1

        print (relay_state_dict)
        return relay_state_dict



if __name__ == "__main__":

    MR = MyRelay(relay_number = 1)
    MR.SetRelayOn()
    MR.GetRelayState()
    #MR.SetRelayOff()