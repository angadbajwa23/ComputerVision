import numpy as np
import cv2
import matplotlib.pyplot as plt
imgpath="C:\\Users\\Angad Bajwa\\Downloads\\standard_test_images\\mandril_color.tif"
img=cv2.imread(imgpath,0)
print(img.shape)


plt.subplot(221),plt.imshow(img)
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img=cv2.bitwise_and(img,img,mask=mask)

plt.subplot(222),plt.imshow(masked_img)
hist_1 = cv2.calcHist([img],[0],None,[256],[0,256])  #arguments-(src, channel, masks, bins, range)
hist_2 = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(223),plt.plot(hist_1)
plt.subplot(224),plt.plot(hist_2)
cv2.imshow('mask',mask)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()