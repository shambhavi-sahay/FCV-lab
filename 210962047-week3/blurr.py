import cv2
import numpy as np
image=cv2.imread('C:/Users/OSLAB/Downloads/tiger.jpg')

half=cv2.resize(image,(0,0),fx=0.1, fy=0.10)

cv2.imshow('Original image', half)
cv2.waitKey(0)

Gaussian=cv2.GaussianBlur(half,(7,7),0)
cv2.imshow('Gaussian Blurr',Gaussian)
cv2.waitKey(0)

median=cv2.medianBlur(half, 5)
cv2.imshow('Median Blurr',median)
cv2.waitKey(0)

bilateral=cv2.bilateralFilter(half,9,75,75)
cv2.imshow('Bilateral Blurr',bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()