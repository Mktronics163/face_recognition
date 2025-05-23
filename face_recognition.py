import cv2
face_cascade = cv2.CascadeClassifier("haar_cascade/haar_cascade_frontal_face_default.xml")
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if not ret:
        break
    face = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.putText(frame,"Abdulmalik",(x//2,y),cv2.FONT_HERSHEY_COMPLEX,2,
                    (0,0,255),2)
    cv2.imshow("face",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
