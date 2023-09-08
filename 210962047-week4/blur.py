# importing opencv CV2 module
import cv2
img = cv2.imread("C:/Users/OSLAB/Documents/210962047/pattern.jpg")
gausBlur = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.waitKey(0)