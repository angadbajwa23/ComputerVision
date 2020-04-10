import cv2
import numpy as np
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\j.png"
img=cv2.imread(imgpath)

kernel=np.ones((5,5),np.uint8)
erode=cv2.erode(img,kernel,iterations=1)
dilate=cv2.dilate(img,kernel,iterations=1)
cv2.imshow('erode',erode)
cv2.imshow("hi",img)

cv2.imshow('dilate',dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()