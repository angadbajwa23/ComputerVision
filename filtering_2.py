# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 01:55:38 2020

@author: Angad Bajwa
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
#imgpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\peppers_color.tiff"

#img=cv2.imread(imgpath,0)

imgpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\Lena.tif"
img=cv2.imread(imgpath)
img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

k=np.array(([0,0,0],
           [0,1,0],
           [0,0,0]),np.uint8)

q=np.array(np.ones((11,11),np.float32))/121

g=np.array(([1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]),np.float32)/256

e=np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),np.float32)

identity=cv2.filter2D(img1,-1,k)
average=cv2.filter2D(img1,-1,q)
gaussian=cv2.filter2D(img1,-1,g)
edge=cv2.filter2D(img1,-1,e)

plt.imshow(img1)
plt.title("Orignial Image")
plt.show()
plt.imshow(identity)
plt.title("Identity")
plt.show()
plt.imshow(average)
plt.title("Average(mean) filter(11X11)")
plt.show()
plt.imshow(gaussian)
plt.title("Gaussian filter(5X5)")
plt.show()
plt.imshow(edge)
plt.title("Edge detector")
plt.show()