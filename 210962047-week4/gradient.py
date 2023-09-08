import cv2
import numpy as np

image=cv2.imread("pattern.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gradx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)  # x
grady = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)  # y

gradmag=np.sqrt(gradx**2+grady**2)
gradphase=np.arctan2(grady,gradx)
gradphasedeg=np.degrees(gradphase)

cv2.imshow('Gradient magnitude',gradmag.astype(np.uint8))
cv2.imshow('Gradient phase',gradphasedeg.astype(np.uint8))
cv2.waitKey(0)