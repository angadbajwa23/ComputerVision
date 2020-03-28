# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:11:57 2020

@author: Angad Bajwa
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\Messi.jpg"

img=cv2.imread(imgpath)
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
plt.imshow(res)
plt.show()
