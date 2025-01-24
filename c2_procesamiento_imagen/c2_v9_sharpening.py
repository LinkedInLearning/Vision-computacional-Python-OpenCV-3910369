import cv2
import numpy as np

img = cv2.imread("src/kernel_image.png")

kernel = np.array([
    [0, -1, 0],
    [-1, 9, -1],
    [0, -1, 0],
])

img_sharpen = cv2.filter2D(img, -1, kernel)

cv2.imshow("Result", img_sharpen)
cv2.waitKey(0)
cv2.destroyAllWindows()
