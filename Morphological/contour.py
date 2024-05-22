import cv2
img=cv2.imread('wallpaper-night.jpg')
edges=cv2.Canny(img,100,200)
contours,_=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1,(0,255,0),1)
cv2.imwrite("contoured.jpg",img)
