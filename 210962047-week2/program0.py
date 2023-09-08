import cv2
import numpy as np
import matplotlib.pyplot as plt
im1=cv2.imread("C:/Users/OSLAB/Desktop/lab.jpg")
img_neg = 255 - im1
cv2.imshow('negative',img_neg)
cv2.waitKey(0)

im2 = cv2.rotate(im1, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('90 degrees', im2)
cv2.waitKey(0)

half = cv2.resize(im1, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(im1, (1050, 1610))
stretch_near = cv2.resize(im1, (780, 540), interpolation = cv2.INTER_LINEAR)

Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[im1, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()