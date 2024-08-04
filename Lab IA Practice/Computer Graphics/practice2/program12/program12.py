import cv2
import cv2.data
image = cv2.imread('phots_emotions.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

for (x,y,w,h) in faces:
    cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
    
cv2.imshow('Faces In Image',image)
cv2.imwrite('Faces_In_Image.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()