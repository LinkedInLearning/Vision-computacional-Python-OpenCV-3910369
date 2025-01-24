import cv2

img = cv2.imread("src/Piggy bank_LIL_192070.jpeg", cv2.IMREAD_GRAYSCALE)

_, img_thresh = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)


apdaptive_img = cv2.adaptiveThreshold(
    img,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imshow("Result", apdaptive_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
