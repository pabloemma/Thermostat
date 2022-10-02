import usbrelay_py

class MyRelay(object):

    def __init__(self):

        #this initializes the usb relay
        count = usbrelay_py.board_count()
        print("Count: ",count)

        self.boards = usbrelay_py.board_details()
        print("Boards: ",self.boards)
        

    def SetRelayOn(self,relay_number):
        '''This sets the relay to closed
        The relay_number is the number of the relay you wasnt to control
        But note : its starts counting from 1 and NOT 0
        '''

        relay = relay_number
        
        print(self.boards[0][0])
        result = usbrelay_py.board_control(self.boards[0][0],relay,1)
        return

    def SetRelayOff(self,relay_number):
        relay = relay_number
        result = usbrelay_py.board_control(self.boards[0][0],relay,0)
        return

if __name__ == "__main__":

    MR = MyRelay()
    MR.SetRelayOn(2)
    MR.SetRelayOff(2)