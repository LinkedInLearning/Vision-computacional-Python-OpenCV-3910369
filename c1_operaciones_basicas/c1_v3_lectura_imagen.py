import cv2

img = cv2.imread("src/Red fox_LIL_191706.jpeg")

cv2.imshow("Imagen", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
