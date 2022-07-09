"""
脸部和眼睛追值踪
"""
import cv2

capture = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if capture.isOpened():
    while True:
        ret, frame = capture.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for eye in eyes:
                x, y, w, h = eye
                cv2.rectangle(frame, (x, y), (x + w + 5, y + h + 5), (0, 0, 255), 3)
            for face in faces:
                x, y, w, h = face
                cv2.rectangle(frame, (x, y), (x + w + 5, y + h + 5), (255, 0, 0), 3)
            cv2.imshow('camera', frame)
        key = cv2.waitKey(30)
        if key == ord('q'):
            break
