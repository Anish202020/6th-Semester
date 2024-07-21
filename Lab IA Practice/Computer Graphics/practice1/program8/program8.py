import cv2
import numpy as np

def translate_image(image,dx,dy):
    rows,cols = image.shape[:2]
    translation_matrix = np.float32([[1,0,dx],[0,1,dy]])
    translated_image = cv2.warpAffine(image,translation_matrix,(cols,rows))
    return translated_image

image = cv2.imread('neutrality.jpg')
height,width = image.shape[:2]
center = (width//2,height//2)
rotation_value = float(input("Rotation Factor"))
scaling_value = float(input("Scaling Factor"))
# 
rotated = cv2.getRotationMatrix2D(center=center,angle=rotation_value,scale=1)
rotated_image = cv2.warpAffine(src=image, M=rotated, dsize=(width,height))
# 
scaled = cv2.getRotationMatrix2D(center=center,angle=0,scale=scaling_value)
scaled_image = cv2.warpAffine(src=rotated_image, M=scaled ,dsize=(width,height))

h=float(input("Translate X"))
w=float(input("Translate Y"))
translated_image = translate_image(scaled_image,dx=h,dy=w)
cv2.imwrite("Final_Image.png",translated_image)