import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
image = cv2.imread("nature.jpeg")

# Convert the image to grayscale (contours work best on binary images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding (you can use other techniques like Sobel edges)
_, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Display the grayscale image
plt.figure()
plt.title("Grayscale Image")
plt.imshow(gray, cmap='gray')
cv2.imwrite("gray.png", gray)

# Display the binary image
plt.figure()
plt.title("Binary Image")
plt.imshow(binary_image, cmap='gray')
cv2.imwrite("binary_image.png", binary_image)

# Display the original image with contours
plt.figure()
plt.title("Contours on Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
cv2.imwrite("image_with_contours.png", image)

# Show all images
plt.show()
