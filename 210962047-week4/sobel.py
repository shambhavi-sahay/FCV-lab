import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("C:/Users/OSLAB/Documents/210962047/pattern.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img1 = cv2.GaussianBlur(gray,(3,3),0)
# convolute with proper kernels
laplacian = cv2.Laplacian(img1,cv2.CV_64F,ksize=5)
sobelx = cv2.Sobel(img1,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img1,cv2.CV_64F,0,1,ksize=5)  # y

plt.subplot(2,2,1),plt.imshow(img1,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()