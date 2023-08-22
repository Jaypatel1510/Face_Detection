import cv2
import math 

# load data
dataset = cv2.CascadeClassifier('face.xml')

# choose image
webcam = cv2.VideoCapture(0)

while True:
    success, frame = webcam.read()
    
    grayimage = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

# detect image
    faces = dataset.detectMultiScale(grayimage)
    print(faces)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


    cv2.imshow('single_person',frame)

    key = cv2.waitKey(1)
    if (key==81 or key==113):
        break

webcam.release()

print('end program')