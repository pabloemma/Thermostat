import usbrelay_py

class MyRelay(object):

    def __init__(self):

        #this initializes the usb relay
        count = usbrelay_py.board_count()
        print("Count: ",count)

        boards = usbrelay_py.board_details()
        print("Boards: ",boards)


    def SetRelayOn(self,boards):
        relay = 1
        result = usbrelay_py.board_control(boards[0],relay,1)
        return

    def SetRelayOff(self,boards):
        relay = 1
        result = usbrelay_py.board_control(boards[0],relay,0)
        return

if __name__ == "__main__":

    MR = MyRelay()
    MR.SetRelayOn('3X9XI_1')