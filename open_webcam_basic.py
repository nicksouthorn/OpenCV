# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:49:56 2018
Basic opening of webcam.
Esc to exit
@author: Nick Southorn
"""

import cv2

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
    