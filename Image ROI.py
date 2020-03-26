import cv2
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\Messi.jpg"

img=cv2.imread(imgpath)
img1=cv2.imread(imgpath)

ball=img[280:340, 330:390]
img[273:333, 100:160] = ball
cv2.imshow('Messi_1ball',img1)
cv2.imshow('Messi_2balls',img)
cv2.waitKey(0)
cv2.destroyAllWindows()