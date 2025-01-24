import cv2

img = cv2.imread("src/Tony.jpg", cv2.IMREAD_GRAYSCALE)

canny_edges = cv2.Canny(img, 100, 200)

cv2.imshow("Bordes - Canny", canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
