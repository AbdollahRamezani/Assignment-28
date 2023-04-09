import cv2
cap = cv2.VideoCapture(0) 
sticker = cv2.imread("input/sticker2.png")
glasses = cv2.imread("input/glasses.png")

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")


def chees_face(image):
    frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3)
    for face in faces:
        x, y, w, h = face
        face_image = image[y:y+h, x:x+w]
        face_image_small = cv2.resize(face_image, [10, 10]) 
        face_image_big = cv2.resize(face_image_small, [w, h], interpolation=cv2.INTER_NEAREST)
        image[y:y+h, x:x+w] = face_image_big
 
    return image

def sticker_face(image):
    frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3) #جای چهره یا مکان چهره را برمیگرداند
    for face in faces:
        x, y, w, h = face
        sticker = cv2.resize(sticker, [w, h])
        image[y:y+h, x:x+w ] = sticker  
        
    return image    

def glasses_face(image):
    eyes = eye_detector.detectMultiScale(image, 1.3)
    frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3)

    for face in faces:
          face_x, face_y, face_w, face_h= face

    for eye in eyes:
        x, y, w, h = eye
        
        glasses = cv2.resize(glasses, [face_w, h])
        image[y:y+h, face_x:face_x+face_w ] = glasses  


 
choice = 0
while True:
    _, frame = cap.read()

    if choice==1:
        frame=chees_face(frame)

    elif choice==2:
        frame=sticker_face(frame)
    elif choice==3:
        frame=glasses_face(frame)    
    
    cv2.imshow('result',frame)

    if cv2.waitKey(5) & 0XFF == ord('q'):
        break
    elif cv2.waitKey(5) & 0XFF==ord('1'):
       choice=1
    elif cv2.waitKey(5) & 0XFF==ord('2'):
       choice=2
    elif cv2.waitKey(5) & 0XFF==ord('3'):
       choice=3   
    
    

    
 
    
    
