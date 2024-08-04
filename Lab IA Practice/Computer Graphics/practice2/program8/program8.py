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

rotating_factor = float(input("Enter rotating factor"))
scaling_factor = float(input("Enter scaling factor"))

rotated = cv2.getRotationMatrix2D(center=center,angle=rotating_factor,scale=1)
rotated_image = cv2.warpAffine(src=image,M=rotated,dsize=(width,height))

scaled = cv2.getRotationMatrix2D(center=center,angle=0,scale=scaling_factor)
scaled_image = cv2.warpAffine(src=rotated_image,M=scaled,dsize=(width,height))

dx = float(input("Enter the dx value"))
dy = float(input("Enter the dy value"))
translated_image = translate_image(scaled_image,dx,dy)

cv2.imwrite("Final.png",translated_image)
cv2.imshow("Final",translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
