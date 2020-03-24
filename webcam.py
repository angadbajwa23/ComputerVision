# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 21:56:30 2020

@author: Angad Bajwa
"""

import cv2
import matplotlib.pyplot as plt
cap=cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame=cap.read()
    print(ret)
    print(frame)
else:
    ret=False

img=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
cv2.imshow("Photo",img)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()