import cv2
import matplotlib.pyplot as plt
import numpy as np
#imgpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\peppers_color.tiff"

#img=cv2.imread(imgpath,0)

imgpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\Lena.tif"
img=cv2.imread(imgpath,0)

k=np.array(([1,0,0],
           [0,1,0],
           [0,0,1]),np.uint8)
print(k)
output=cv2.filter2D(img,-1,k)
plt.imshow(img)
plt.title("Sample")
plt.show()
plt.imshow(output)
plt.title("Sample")
plt.show()
