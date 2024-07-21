import cv2
# from google.colab.patches import cv2_imshow
image = cv2.imread('colors.png',)
B, G, R = cv2.split(image)
# Corresponding channels are separated
cv2.imshow('Original Image',image)
cv2.imshow("Blue Image",B)
cv2.imshow("Green Image",G)
cv2.imshow("Red Image",R)
cv2.waitKey(0)
cv2.destroyAllWindows()