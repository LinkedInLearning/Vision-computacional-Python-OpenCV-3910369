import cv2
import os

cwd = os.getcwd()
img_path = os.path.join(cwd, "src", "Red fox_LIL_191706.jpeg")

img = cv2.imread(img_path)

new_filename = "test.png"
new_path = os.path.join(cwd, "src", new_filename)

cv2.imwrite(new_path, img)
