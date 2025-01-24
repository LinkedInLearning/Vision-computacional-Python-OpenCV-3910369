import cv2

img_1 = cv2.imread("src/Dark chocolate pieces_LIL_191458.jpeg", cv2.IMREAD_GRAYSCALE)
img_2 = cv2.imread("src/Piggy bank_LIL_192070.jpeg", cv2.IMREAD_GRAYSCALE)

img_1 = cv2.resize(img_1, (1024, 768))
img_2 = cv2.resize(img_2, (1024, 768))

add_img = cv2.add(img_1, img_2)
print("Img1", img_1[0, 0])
print("Img2", img_2[0, 0])
print("Add", add_img[0, 0])

weight_img = cv2.addWeighted(img_1, 0.5, img_2, 0.5, 0)
print("Add weight", weight_img[0, 0])

sub_img = cv2.subtract(img_1, img_2)
print("Subtract", sub_img[0, 0])

mult_img = cv2.subtract(img_1, img_2)
print("Multiply", mult_img[0, 0])

div_img = cv2.subtract(img_1, img_2)
print("Divide", div_img[0, 0])


and_bitwise = cv2.bitwise_and(img_1, img_2)

not_bitwise = cv2.bitwise_not(img_1)

cv2.imshow("Result", weight_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
