from shapedetection import detect_shapes
import cv2

image = cv2.imread("PennAir 2024 App Static.png")
cv2.imwrite("image.png", detect_shapes(image))