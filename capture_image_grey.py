# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:49:56 2018

@author: southorn
"""
import numpy as np
import cv2

#cap = cv2.VideoCapture(0)
## (0) for laptop webcam, (1) for external webcam
#
#while(True):
#    # Capture frame-by-frame
#    ret, image = cap.read()
#    # ret, frame = cap.read()
#
#    # Our operations on the frame come here
#    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#    # Display the resulting frame
#    cv2.imshow("My Webcam", image)
#    #cv2.imshow('frame',gray)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#
## When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
#


def show_webcam(mirror=False):
    webcam = cv2.VideoCapture(0)
    while True:
        ret, image = webcam.read()
        if mirror:
            image = cv2.flip(image, 1)
        cv2.imshow('My_webcam', image)
        if cv2.waitKey(1) == 27:
            break # Esc to quit
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()            
    