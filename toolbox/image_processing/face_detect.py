""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/jsutker/SoftDesSp15/toolbox/image_processing/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    #print str(faces)
    for (x,y,w,h) in faces:
        frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
        cv2.circle(frame, (x+(w/3),y+(w/3)), w/8, (255,255,255),-w/8)
        cv2.circle(frame, (x+(2*w/3),y+(w/3)), w/8, (255,255,255),-w/8)
        cv2.circle(frame, (x+(w/3),y+(w/3)), w/16, (0,0,0),-w/8)
        cv2.circle(frame, (x+(2*w/3),y+(w/3)), w/16, (0,0,0),-w/8)
        cv2.circle(frame, (x+(w/2),y+(5*w/6)), w/10, (0,0,0),-w/8)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()