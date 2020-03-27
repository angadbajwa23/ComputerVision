# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:44:03 2020

@author: Angad Bajwa
"""

import cv2
import matplotlib.pyplot as plt
imgpath1="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\jetplane.tif"
imgpath2="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\Lena.tif"
img1=cv2.imread(imgpath1)
img2=cv2.imread(imgpath2)

mer=cv2.addWeighted(img1,0.5,img2,0.5,0) # merge= p*(img1) + (1-p)*(img2) + z  , here z=0

cv2.imshow("Merged",mer)
cv2.waitKey(0)
#make sure the image sizes are the same i.e. not have same number of channels