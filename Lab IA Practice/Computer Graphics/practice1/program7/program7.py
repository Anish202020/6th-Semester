import cv2
import matplotlib.pyplot as plt

img  =cv2.imread("neutrality.jpg")
height,width = img.shape[:2]

quad1 = img[:height//2,:width//2]
quad2 = img[:height//2,width//2:]
quad3 = img[height//2:,:width//2]
quad4 = img[height//2:,width//2:]

plt.figure(figsize=(10,5))
# Plt 1 and 2
plt.subplot(1,2,1)
plt.imshow(quad1)
plt.title("1")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(quad2)
plt.title("2")
plt.axis("off")
# Plt 3 and 4
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(quad3)
plt.title("3")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(quad4)
plt.title("4")
plt.axis("off")
plt.show()