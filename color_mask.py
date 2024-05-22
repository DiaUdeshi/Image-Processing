import cv2
import numpy as np
img=cv2.imread('wallpaper-night.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower=np.array([110,50,50])
upper=np.array([130,255,255])
mask=cv2.inRange(hsv,lower,upper)
result=cv2.bitwise_and(img,img,mask=mask)
cv2.imwrite("blue_mask_output.jpg",result)
