import cv2
import numpy as np

# Read the image
image = cv2.imread("photo_emotions.jpg")


# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# image = cv2.imread("C:/Users/AI06GF13/Desktop/p12input.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
# Draw rectangles around detected faces
for (x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imwrite('detected_faces.jpg', image)  # Save the result
cv2.imshow('Detected Faces', image)  # Display the result
cv2.waitKey(0)
cv2.destroyAllWindows()
