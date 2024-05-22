import cv2
import numpy as np
img=np.zeros((500,500,3),dtype='uint8')
image=cv2.line(img,(100,100),(400,400),(255,255,255),3)
arrow=cv2.arrowedLine(img,(400,400),(100,100),(255,255,255),3)
ellipse=cv2.ellipse(img,(100,100),(80,50),0,0,360,(255,255,255),3)
img1=np.zeros((500,500,3),dtype='uint8')
circle=cv2.circle(img,(300,300),15,(255,255,255),3)
rectangle=cv2.rectangle(img,(100,100),(200,400),(255,255,255),3)
#cv2.imwrite("rectangle.jpg",rectangle)
#cv2.imwrite('circle.jpg',circle)
#cv2.imwrite('ellipse.jpg',ellipse)
#cv2.imwrite('arrow.jpg',arrow)
#cv2.imwrite('line.jpg',image)
