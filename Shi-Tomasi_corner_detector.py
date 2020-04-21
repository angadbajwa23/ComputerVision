import cv2
import numpy as np
cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:
    ret, frame = cap.read()
    cv2.imshow("Live Feed", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, 125, 0.01, 10) #finds 125 best corners
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)

    cv2.imshow("output", frame)



    if (cv2.waitKey(1)) == 27:
        break
cv2.destroyAllWindows()
cap.release()
