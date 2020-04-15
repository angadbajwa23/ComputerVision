import cv2
import numpy as np
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\Messi.jpg"

img=cv2.imread(imgpath)
rows,cols,ch = img.shape

M = np.float32([[1,0,+100],[0,1,50]]) #Translation is the shifting of object’s location. If you know the shift in (x,y) direction, let it be (t_x,t_y), you can create the transformation matrix:here t_x=100 and t_y=50


dst1 = cv2.warpAffine(img,M,(cols,rows))  #Third argument of the cv2.warpAffine() function is the size of the output image, which should be in the form of (width, height). Remember width = number of columns, and height = number of rows.

R=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)  #arguments- (centre,angle,scale)
dst2=cv2.warpAffine(img,R,(cols,rows))
cv2.imshow('output1',dst1)
cv2.imshow('output2',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()