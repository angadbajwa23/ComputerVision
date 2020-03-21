import cv2
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\Lena.tif"
img=cv2.imread(imgpath,0)

outpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\output\\Lena.jpg" #to convert img into jpg and store

cv2.imshow('Lena',img)  #to output image in window named Lena
cv2.imwrite(outpath,img)   # to save the image in  the given output path in terms of jpg format
cv2.waitKey(0)  # window is displayed till user presses another key
cv2.destroyWindow('Lena') #to close output window