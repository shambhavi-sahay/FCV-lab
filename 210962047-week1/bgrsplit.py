import cv2
import numpy as np
im1=cv2.imread("C:/Users/OSLAB/Desktop/lab.jpg")

b,g,r=cv2.split(im1)
zeros=np.zeros(b.shape,np.uint8)

img_red=cv2.merge((zeros,zeros,r))
img_green=cv2.merge((zeros,g,zeros))
img_blue=cv2.merge((b,zeros,zeros))

cv2.waitKey(0)
cv2.imshow('red image',img_red)

cv2.waitKey(0)
cv2.imshow('green image',img_green)

cv2.waitKey(0)
cv2.imshow('blue image',img_blue)