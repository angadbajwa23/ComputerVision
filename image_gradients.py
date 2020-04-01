import cv2
import numpy as np
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\sudoku.jpg"
img=cv2.imread(imgpath)
cv2.imshow("sample",img)

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

sobelx64f=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

laplacian=cv2.Laplacian(img,cv2.CV_64F)

cv2.imshow("sobel_x",sobelx)
cv2.imshow("sobel_x2",sobel_8u)
cv2.imshow("sobel_y",sobely)
cv2.imshow("laplacian",laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
