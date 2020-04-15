import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath="C:\\Users\\Angad Bajwa\\Downloads\\Messi.jpg"

img=cv2.imread(imgpath)

blur=cv2.blur(img,(5,5))  #Average Blur==arguments- src, kernel size
g_blur=cv2.GaussianBlur(img,(5,5),0) #Gaussian Blur==arguments- src, kernel size,standard devaition in x and y, nothing mentioned taken to be the same
m_blur=cv2.medianBlur(img,5) #Median Blur==arguments- src, kernel size(linear size) got Gaussian and median kernel size should be odd and postive
b_blur=cv2.bilateralFilter(img,9,75,75) # Bilateral Filter- to avoid blurring edges....arguments=src,diamter of pixel neighborhood,SIgmaColor(for the intensity matches),SIgmaSPace(for neighbourhood points)
cv2.imshow("input",img)
cv2.imshow("Average_blur",blur)
cv2.imshow("Gaussian_blur",g_blur)
cv2.imshow("Median_Blur",m_blur)
cv2.imshow("Bilateral_Filter_Blur",b_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
#https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html  - Reference docs
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
#Bilateral Filtering=As we noted, the filters we presented earlier tend to blur edges. This is not the case for the bilateral filter, cv2.bilateralFilter(), which was defined for, and is highly effective at noise removal while preserving edges. But the operation is slower compared to other filters. We already saw that a Gaussian filter takes the a neighborhood around the pixel and finds its Gaussian weighted average. This Gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It does not consider whether pixels have almost the same intensity value and does not consider whether the pixel lies on an edge or not. The resulting effect is that Gaussian filters tend to blur edges, which is undesirable.

#The bilateral filter also uses a Gaussian filter in the space domain, but it also uses one more (multiplicative) Gaussian filter component which is a function of pixel intensity differences. The Gaussian function of space makes sure that only pixels are ‘spatial neighbors’ are considered for filtering, while the Gaussian component applied in the intensity domain (a Gaussian function of intensity differences) ensures that only those pixels with intensities similar to that of the central pixel (‘intensity neighbors’) are included to compute the blurred intensity value. As a result, this method preserves edges, since for pixels lying near edges, neighboring pixels placed on the other side of the edge, and therefore exhibiting large intensity variations when compared to the central pixel, will not be included for blurring