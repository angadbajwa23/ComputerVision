import cv2
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\Lena.tif"
img1=cv2.imread(imgpath)

print(type(img1))   # data type of image
print(img1.dtype)   # data type of numbers in array
print(img1.size)    #size= 512*512*3
print(img1.ndim)    #number of dimensions=3 .....Blue Green Red
print(img1)         #image in form of an n dimension array
print(img1.shape)
