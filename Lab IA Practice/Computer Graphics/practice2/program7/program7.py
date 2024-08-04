import cv2
import matplotlib.pyplot as plt

image = cv2.imread('neutrality.jpg')

height,width = image.shape[:2]

quad1 = image[:height//2,:width//2]
quad2 = image[:height//2,width//2:]
quad3 = image[height//2:,:width//2]
quad4 = image[height//2:,width//2:]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title('1')
plt.imshow(quad1)
plt.axis('off')
plt.subplot(1,2,2)
plt.title('2')
plt.imshow(quad2)
plt.axis('off')

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title('3')
plt.imshow(quad3)
plt.axis('off')
plt.subplot(1,2,2)
plt.title('4')
plt.imshow(quad4)
plt.axis('off')

plt.show()