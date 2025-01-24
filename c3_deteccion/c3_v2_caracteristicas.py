import cv2

img = cv2.imread("src/Tony.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detector Esquinas Harrys
corners = cv2.cornerHarris(img_gray, 2, 3, 0.04)
corners = cv2.dilate(corners, None)

img_corners = img.copy()
img_corners[corners > 0.01 * corners.max()] = [0, 0, 255]

# Detector SIFT
sift = cv2.SIFT_create()
keypoints = sift.detect(img_gray, None)

img_sift = img.copy()
img_sift = cv2.drawKeypoints(img_sift, keypoints, None)

# Detector ORB
orb = cv2.ORB_create()
keypoints = orb.detect(img_gray, None)

img_orb = img.copy()
img_orb = cv2.drawKeypoints(img_orb, keypoints, None)

cv2.imshow("Caracteristicas - Esquinas Harrys", img_corners)
cv2.imshow("Caracteristicas - SIFT", img_sift)
cv2.imshow("Caracteristicas - ORB", img_orb)
cv2.waitKey(0)
cv2.destroyAllWindows()
