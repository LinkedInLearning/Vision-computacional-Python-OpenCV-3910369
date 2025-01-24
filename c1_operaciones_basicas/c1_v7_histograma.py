import cv2
import matplotlib.pyplot as plt

# Imagen en escala de grises
path = "src/Red fox_LIL_191706.jpeg"
gray_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

hist_gray= cv2.calcHist([gray_img], [0], None, [256], [0, 256])
plt.plot(hist_gray)
plt.show()


# Imagen a color
color_img = cv2.imread(path)

channels = ("b", "g", "r")
for i, color in enumerate(channels):
    hist = cv2.calcHist([color_img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

plt.show()
