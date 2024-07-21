#Rotation and scaling of image
import cv2
import numpy as np

def translate_image(image, dx, dy):
 rows, cols = image.shape[:2]
 translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
 translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
 return translated_image
# Read the image
image = cv2.imread('neutrality.jpg')
# Get image dimensions
height, width = image.shape[:2]
# Calculate the center coordinates of the image
center = (width // 2, height // 2)
rotation_value = int(input("Enter the degree of Rotation:"))
scaling_value = int(input("Enter the zooming factor:"))
# Create the 2D rotation matrix
rotated = cv2.getRotationMatrix2D(center=center, angle=rotation_value, scale=1)
rotated_image = cv2.warpAffine(src=image, M=rotated, dsize=(width, height))
scaled = cv2.getRotationMatrix2D(center=center, angle=0, scale=scaling_value)
scaled_image = cv2.warpAffine(src=rotated_image, M=scaled, dsize=(width, height))
h = int(input("How many pixels you want the image to be translated horizontally? "))
v = int(input("How many pixels you want the image to be translated vertically? "))
translated_image = translate_image(scaled_image, dx=h, dy=v)
cv2.imwrite('Final_image.png', translated_image)
