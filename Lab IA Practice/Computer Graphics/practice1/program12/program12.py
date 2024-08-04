import cv2
import cv2.data

image = cv2.imread("photo_emotions.jpg")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),( x + w, y + h),(255,0,0),2)
    
cv2.imshow("Detect Faces",image)
cv2.imwrite("Detect_Faces.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()