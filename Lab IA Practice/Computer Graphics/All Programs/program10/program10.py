# Importing the modules 
import cv2 
import numpy as np 

# Reading the image 
image = cv2.imread("oceans.webp")
# Applying the filter 
    # Apply Bilateral Filter
bilateral = cv2.bilateralFilter(image, 9, 75, 75)

# Apply Average Blur
average_blur = cv2.blur(image, (5, 5))

# Apply Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Median Blur
median_blur = cv2.medianBlur(image, 5)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Bilateral Filter", bilateral)
cv2.imshow("Average Blur", average_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()