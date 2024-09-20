import cv2
import numpy as np

def detect_shapes(frame):
    # Convert to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Blur image
    blur = cv2.GaussianBlur(hsv, (11, 11), 0)

    # Thresholding
    thresh = cv2.inRange(blur, (0, 113, 150), (180, 255, 255))

    # Find contours
    contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours
    for i in contours:
        M = cv2.moments(i)
        if M['m00'] > 1000:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.drawContours(frame, [i], -1, (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 4, (255, 255, 255), -1)
            cv2.putText(frame, "center", (cx - 15, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
            cv2.putText(frame, f"x: {cx} y: {cy}", (cx - 50, cy + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    return frame