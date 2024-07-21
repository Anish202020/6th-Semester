# Importing the modules 
import cv2 
import numpy as np 

# Reading the image 
image = cv2.imread("oceans.webp")
# Applying the filter 
bilateral = cv2.bilateralFilter(image, 9, 75, 75) 

# Showing the image 
cv2.imshow('Original', image) 
cv2.imshow('Bilateral blur', bilateral) 

cv2.waitKey() 
cv2.destroyAllWindows() 
