import cv2
import numpy as py
image=cv2.imread('wallpaper-night.jpg')
height,width=image.shape[:2]
qheight,qwidth=height/4,width/4
m=py.float32([[1,0,qwidth],[0,1,qheight]])
translate=cv2.warpAffine(image,m,(width,height))

cv2.imshow('translation',translate)
cv2.waitKey(0)
cv2.destroyAllWindows()
