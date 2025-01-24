import cv2

img = cv2.imread("src/Piggy bank_LIL_192070.jpeg")

height, width, _ = img.shape
ratio = height / width

fixed_width = 300
calculated_height = int(fixed_width*ratio)

fixed_value_img = cv2.resize(img, dsize=(fixed_width, calculated_height))


scale_factor_img = cv2.resize(img, None, fx= 0.5, fy=0.5)


interpolated_img = cv2.resize(img, dsize=(fixed_width, calculated_height), interpolation=cv2.INTER_LANCZOS4)


cv2.imshow("Imagen escalada valor fijo", fixed_value_img)
cv2.imshow("Imagen escalada factor", scale_factor_img)
cv2.imshow("Imagen interpolada", interpolated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
