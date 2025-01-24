import cv2

img = cv2.imread("src/Piggy bank_LIL_192070.jpeg")

crop_img = img[100:300, 100:300]

cv2.imshow("Imagen", img)
cv2.imshow("Imagen recortada", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
