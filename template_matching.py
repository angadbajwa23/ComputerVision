import cv2
import matplotlib.pyplot as plt
import numpy as np

path1="C:\\Users\\Angad Bajwa\\Downloads\\messi_face.jpg"
path2="C:\\Users\\Angad Bajwa\\Downloads\\Messi.jpg"

temp=cv2.imread(path1,0)
img=cv2.imread(path2,0)

w, h = temp.shape[::-1]
res = cv2.matchTemplate(img,temp,cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img,top_left, bottom_right, 255, 2)

plt.subplot(221),plt.imshow(temp)
plt.subplot(222),plt.imshow(img)


plt.show()
cv2.waitKey(0)