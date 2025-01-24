import cv2

img = cv2.imread("src/Piggy bank_LIL_192070.jpeg")

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print("BGR", img[200, 200])
print("RGB", rgb_img[200, 200])
print("Gray", gray_img[200, 200])
print("HSV", hsv_img[200, 200])

to_bgr = cv2.cvtColor(gray_img, cv2.COLOR_RGB2BGR)

cv2.imshow("BGR", img)
cv2.imshow("RGB", rgb_img)
cv2.imshow("Gray", gray_img)
cv2.imshow("HSV", hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
