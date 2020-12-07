import cv2
import numpy as np

import "servo.py"

cam = cv2.VideoCapture(0) #port number for cam (will need to change)

#messy code and comments but gotta start somewhere, in the future, expect to see everything tidied up


#main program body.
#  this loop is supposed to continually get position of a blob from the image feed and
#  send information to the servos
while(1):
    #gonna need some blob detetction.
    #which means creating a blob
    
    #blob will be an object, probably through masking the image feed
    
    pos_x = blob.getXPos() #make getPos return a range of values for x and y
    pos_y = blob.getYPos()
    #below section is definitely refactorable, change later
    x_move = pos_x.avg
    y_move = pos_y.avg
    
    #gonna have to check for if the blob is going to be out of frame, probably want to create a
    #buffer zone
    
    #currently these set of if statements see if the blob is within the center of the screen,
    #contradicts the above comments
    if (0 > pos_x.low and 0 < pos_x.high): #assuming that xhair x position is 0
        x_move = 0
    if (0 > pos_y.low and 0 < pos_y.high):
        y_move = 0
    
    # speed might have to be determined by distance from
    # center of image feed to blob, done progressively
    
    control.updatePos(x_move, y_move)
    
