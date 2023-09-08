import cv2
import numpy as np

# Load your image
image = cv2.imread('pattern.jpg')

# Define color range for red
lower_red = np.array([0, 0, 100])
upper_red = np.array([100, 100, 255])

# Create a red mask
red_mask = cv2.inRange(image, lower_red, upper_red)

# Apply the red mask to the original image to keep only the red pixels
rimage = cv2.bitwise_and(image, image, mask=red_mask)

# Display or save the red light image
cv2.imshow('Segmented image', rimage)
cv2.waitKey(0)
cv2.destroyAllWindows()