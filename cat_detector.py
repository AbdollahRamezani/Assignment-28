import cv2

image = cv2.imread("input/cats.jpg")

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
faces = face_detector.detectMultiScale(image) 

for face in faces:
    x, y, w, h = face
    cv2.rectangle(image, [x, y], [x+w, y+h], [255,255,255], 2)  

cv2.imshow("cat_detector", image)
cv2.imwrite("output/cats_detector.jpg", image)
cv2.waitKey()
