import cv2
import numpy as py
import matplotlib.pyplot as plt

def getEroded(img,kernel):
    erosion=cv2.erode(img,kernel,iterations=1)
    plt.imsave("eroded.jpg",erosion,cmap='gray')

def getDilated(img,kernel):
    dilation=cv2.dilate(img,kernel,iterations=1)
    plt.imsave("dilated.jpg",dilation,cmap='gray')

def getOpening(img,kernel):
    opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    plt.imsave("opening.jpg",opening,cmap='gray')

def getClosing(img,kernel):
    closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
    plt.imsave("closing.jpg",closing,cmap='gray')

def getGrayScale(img):
    plt.imsave("grayscale.jpg",img,cmap='gray')

def getContoured(img1):
    edges=cv2.Canny(img1,100,200)
    contours,_=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img1,contours,-1,(0,255,0),1)
    cv2.imwrite("contoured.jpg",img1)

img=cv2.imread('wallpaper-night.jpg',0)
img1=cv2.imread('wallpaper-night.jpg')
kernel=py.ones((5,5),py.uint8)
getEroded(img,kernel)
getDilated(img,kernel)
getClosing(img,kernel)
getOpening(img,kernel)
getGrayScale(img)
getContoured(img1)
