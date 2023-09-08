import cv2
img_grayscale=cv2.imread("C:/Users/OSLAB/Desktop/lab.jpg",0)
cv2.imshow('grayscale image', img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("C:/Users/OSLAB/Desktop/grayscale.jpg",img_grayscale)