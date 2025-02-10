import cv2
import numpy as np

img = cv2.imread("src/Red fox_LIL_191706.jpeg")

(B, G, R) = cv2.split(img)

zeros = np.zeros(img.shape[:2], dtype="uint8")

red = cv2.merge([zeros, zeros, R])
cv2.imwrite("src/red_fox.png", red)

green = cv2.merge([zeros, G, zeros])
cv2.imwrite("src/green_fox.png", green)

blue = cv2.merge([B, zeros, zeros])
cv2.imwrite("src/blue_fox.png", blue)
