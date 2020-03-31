import cv2
import numpy as np
import matplotlib.pyplot as plt
#img should be in grayscale for thresholding
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\Messi.jpg"
img=cv2.imread(imgpath,0)

ret,thres1=cv2.threshold(img,127,255,cv2.THRESH_BINARY) #global thresholding
thres2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) #Adaptive Mean
thres3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)   # Adaptive Gaussian
ret3,thres4 = cv2.threshold(img,100,200,cv2.THRESH_BINARY++cv2.THRESH_OTSU)    #OTSU Binarization
plt.title('Binary'),plt.imshow(thres1)
plt.show()
plt.title('adaptive_mean'),plt.imshow(thres2)
plt.show()
plt.title('adaptive_gaussian'),plt.imshow(thres3)
plt.show()
plt.title('otsu'),plt.imshow(thres4)
plt.show()