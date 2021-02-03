import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('test.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

faces=face_cascade.detectMultiScale(gray,1.3,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       #to detect the face ,rectangle coordinates is used here
       #(255,0,0)means rectangle color will be blue and 2 is the thickness of rectangle
cv2.imshow('img',img) # for the image
cv2.waitKey() #This will wait for a keypress to close the image

