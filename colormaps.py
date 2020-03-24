# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import matplotlib.pyplot as plt

imgpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\Lena.tif"
img=cv2.imread(imgpath,0)

plt.imshow(img, )
plt.show()

