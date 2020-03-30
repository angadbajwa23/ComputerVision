import cv2
import numpy as np
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\Messi.jpg"
img=cv2.imread(imgpath)
img1=cv2.imread(imgpath)



pts1 = np.float32([[56,65],[368,52],[28,187],[389,290]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])


M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))
cv2.imshow('output',dst)
cv2.imshow('input',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()