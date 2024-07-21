import cv2
import numpy as np

img= cv2.imread("brains.jpeg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,100,200)
kernel = np.ones((5,5),np.float32)/25
texture = cv2.filter2D(gray,-1,kernel)
cv2.imshow('Original Image',img) 
cv2.imshow('Edges Image',edges) 
cv2.imshow('Texture Image',texture) 

cv2.waitKey(0)
cv2.destroyAllWindows()