from shapedetection import detect_shapes
import cv2

cap = cv2.VideoCapture('PennAir 2024 App Dynamic.mp4')
 
while cap.isOpened():
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame', detect_shapes(frame))
    if cv2.waitKey(1) == ord('q'):
        break