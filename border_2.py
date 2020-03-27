# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:26:18 2020

@author: Angad Bajwa
"""

import cv2
import matplotlib.pyplot as plt
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\Lena.tif"
img=cv2.imread(imgpath,0)



border1=cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_CONSTANT)
border2=cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_REFLECT)
border3=cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_WRAP)

plt.imshow(img),plt.title("Original")
plt.show()
plt.imshow(border1),plt.title("Constant Border")
plt.show()
plt.imshow(border2),plt.title("Reflect Border")
plt.show()
plt.imshow(border3),plt.title("Wrap Border")
plt.show()