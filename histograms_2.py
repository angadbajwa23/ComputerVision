import numpy as np
import cv2
import matplotlib.pyplot as plt
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\Messi.jpg"
img=cv2.imread(imgpath)
print(img.shape)
plt.subplot(221),plt.imshow(img)
hsv=cv2.calcHist([img],[0,1],None,[180,256],[0,180,0,256]) # 2d histogram , hue - number of bins=180 and saturation - number of bins =256
plt.subplot(222),plt.imshow(hsv)
plt.show()
