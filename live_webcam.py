# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:01:41 2020

@author: Angad Bajwa
"""

import cv2

cap=cv2.VideoCapture(0)

if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
    
while ret:
    
    output=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Live Feed",frame)
    cv2.imshow("Gray",output)
    if(waitKey(1))==27 :
        break
    
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()