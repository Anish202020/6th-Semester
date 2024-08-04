import matplotlib.pyplot as plt
import numpy as np
import cv2
image = cv2.imread('nature.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Imp
_,binary_image=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)

# 
contours,_ = cv2.findContours(binary_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image,contours,-1,(0,255,0),3)

plt.figure()
plt.title('Gray Image')
plt.imshow(gray,cmap='Gray')
cv2.imwrite('gray.jpg',gray)

plt.figure()
plt.title('Binary Image')
plt.imshow(binary_image,cmap='Gray')
cv2.imwrite('binary_image.jpg',binary_image)

plt.figure()
plt.title('Contours Image')
plt.imshow(cv2.cvtColor(image,cv2.COLOR_RGB2BGR))
cv2.imwrite('countrs_image.jpg',binary_image)

