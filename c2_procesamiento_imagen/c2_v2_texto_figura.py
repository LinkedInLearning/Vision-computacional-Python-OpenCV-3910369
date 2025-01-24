import cv2

img = cv2.imread("src/black.png")

cv2.putText(
    img,
    "Test",
    (300, 300),
    cv2.FONT_HERSHEY_SIMPLEX,
    5,
    (255, 255, 255),
    10
)

cv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
