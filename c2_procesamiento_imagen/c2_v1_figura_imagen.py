import cv2

img = cv2.imread("src/black.png")

cv2.line(img, (0,0), (200, 200), (0, 0, 255), 2)
cv2.circle(img, (200, 200), 5, (255, 0, 0), 25)
cv2.rectangle(img, (300, 300), (500, 500), (0, 255, 0), 10)
cv2.ellipse(img, (800, 600), (150, 300), 0, 0, 360, (255, 255, 255), 5)

cv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
