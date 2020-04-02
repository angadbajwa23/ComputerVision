import cv2
import numpy as np
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\Messi.jpg"
img=cv2.imread(imgpath)

edges=cv2.Canny(img,100,200)  # lower threshold-100, upper threshold 200
cv2.imshow("input",img)
cv2.imshow("output",edges)



cv2.imshow('output_2', res)
cv2.waitKey(0)
cv2.destroyAllWindows()