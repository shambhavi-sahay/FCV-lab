import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("C:/Users/OSLAB/Documents/210962047/pattern.jpg")
gausBlur = cv2.GaussianBlur(img, (7, 7), 0)

cv2.imshow('Original', img)

cv2.imshow('Blurred', gausBlur)

edges=img-gausBlur

cv2.imshow('Edges', edges)

img1=img+edges

cv2.imshow('Sharpened', img1)

cv2.waitKey(0)