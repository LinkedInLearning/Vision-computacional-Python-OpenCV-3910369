import cv2

img = cv2.imread("src/Piggy bank_LIL_192070.jpeg")

img_rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

height, width, _ = img.shape
center = (width//2, height//2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)
img_rotation_matrix = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imshow("Imagen", img)
cv2.imshow("Imagen Rotada", img_rotate)
cv2.imshow("Imagen Rotada", img_rotation_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()
