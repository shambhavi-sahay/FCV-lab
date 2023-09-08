import cv2
import numpy as np

img = cv2.imread("C:/Users/OSLAB/Desktop/lab.jpg")
for gamma in [0.1,0.5,1.2,2.2]:
    gamma_corrected=np.array(255*(img/255)** gamma, dtype='uint8')
    cv2.imshow('Gamma_Transformed'+str(gamma)+'.jpg',gamma_corrected)
    cv2.waitKey(0)