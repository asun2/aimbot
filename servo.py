import serial
import numpy as np
import maestro

#will organize later, now is just getting some stuff done.


#x_axis = maestro.Controller(0)
#y_axis = maestro.Controller(1)



class control:
    #gotta understand how Maestro's servo controllers work.
    #
    #"Polulu protocols allow for multiple Maestros to be connected to a single
    # serial port. Each connected device is then indexed by number."
    #
    
    def __init__(self, up_down_port = "", left_right_port = ""): #unknown usb values
        self.servo1 = maestro.Controller(up_down_port)
        self.servo2 = maestro.Controller(left_right_port)
    
    #close handler method
    def close(self):
        self.servo1.close()
        self.servo2.close()
    
    def updatePos(x_move, y_move):
    #progressive speed ramping here?
