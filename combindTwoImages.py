import cv2
import numpy as np

# Read image1
image = cv2.imread("images/mike.jpg")

horizontalMerge = np.hstack((image, image))

verticalMerge = np.vstack((image, image))

cv2.imshow("Image", image)
cv2.imshow("Horizontal Merge", horizontalMerge)
cv2.imshow("Vertical Merge", verticalMerge)
cv2.waitKey(0)