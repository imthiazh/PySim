# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:56:22 2018

@author: Abhishek
"""

import cv2
import numpy as np

def menu():
    windowName="preview"
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
    
    while ret:
        ret,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        #BLUE COLOR
        low=np.array([100,50,50])
        high=np.array([140,255,255])
        
        image_mask=cv2.inRange(hsv,low,high)
        output=cv2.bitwise_and(frame,frame,mask=image_mask)
        print(image_mask)
        cv2.imshow("mask_image",image_mask)
        cv2.imshow(windowName,frame)
        cv2.imshow("mask",output)
        if cv2.waitKey(1)==27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__=="__main__":
    menu()