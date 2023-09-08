import cv2
from matplotlib import pyplot as plt
import numpy as np



img=cv2.imread("C:/Users/OSLAB/Downloads/jellybean.jpg")
img1=cv2.imread("C:/Users/OSLAB/Downloads/jellybean.jpg",0)
half=cv2.resize(img,(0,0),fx=0.1, fy=0.10)
half1=cv2.resize(img1,(0,0),fx=0.1, fy=0.10)
plt.hist(half.ravel(),256,[0,256])
plt.show()
equ=cv2.equalizeHist(half1)
res=np.hstack((half1,equ))
plt.hist(res.ravel(),256,[0,256])
plt.show()
cv2.imshow('Output',res)
cv2.waitKey(0)
cv2.destroyAllWindows()