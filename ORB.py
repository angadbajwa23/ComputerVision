# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:00:34 2020

@author: Angad Bajwa
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

path="C:\\Users\\Angad Bajwa\\Downloads\\monuments.jpg"
img=cv2.imread(path)

# Initiate STAR detector
orb = cv2.ORB()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
plt.imshow(img2),plt.show()