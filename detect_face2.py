import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0) #0 is to use webcam,it will capture the frame from webcam
while True:
    _, img=cap.read()#_, is flag that is used to indicate the frame was read currently or not and img is frame itself
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#This method works on gray scale image only
    faces=face_cascade.detectMultiScale(gray,1.3,4)

    for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       #to detect the face ,rectangle coordinates is used here
       #(255,0,0)means rectangle color will be blue and 2 is the thickness of rectangle
    cv2.imshow('img',img) 
    k=cv2.waitKey(30) & 0xff 
    if k==27: # if ESC key is clicked it will break the loop
      break
cap.release()
 