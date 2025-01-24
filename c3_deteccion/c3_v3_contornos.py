import cv2

img = cv2.imread("src/Tony.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3) 

print(f"Cantidad de contornos {len(contours)}") 

cv2.imshow("Contornos", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
