import cv2
import matplotlib.pyplot as plt

image = cv2.imread("nature.jpeg")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_,binary_image = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(binary_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image,contours,-1,(0,255,0),3)

plt.figure()
plt.title("GrayScale Image")
plt.imshow(gray,cmap='gray')
cv2.imwrite('gray.png',gray)
plt.figure()
plt.title("Binary Image")
plt.imshow(binary_image,cmap='gray')
cv2.imwrite('binary_image.png',binary_image)

plt.figure()
plt.title("Contours on Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
cv2.imwrite("image_with_contours.png", image)

# Show all images
plt.show()