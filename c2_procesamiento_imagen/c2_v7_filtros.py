import cv2
import numpy as np

img = cv2.imread("src/kernel_image.png")

kernel = np.array([
    [0.111, 0.111, 0.111],
    [0.111, 0.111, 0.111],
    [0.111, 0.111, 0.111],
])

filtered_img = cv2.filter2D(img, -1, kernel) 

blur = cv2.blur(img, (5, 5))
guassian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)

cv2.imshow("Imagen filtrada", guassian)
cv2.waitKey(0)
cv2.destroyAllWindows()
