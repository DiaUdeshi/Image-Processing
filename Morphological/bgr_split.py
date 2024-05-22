import cv2
img=cv2.imread('rgb.jpg')
b,g,r=cv2.split(img)
cv2.imwrite("blue_image.jpg",b)
cv2.imwrite("green_image.jpg",g)
cv2.imwrite("red_image.jpg",r)
