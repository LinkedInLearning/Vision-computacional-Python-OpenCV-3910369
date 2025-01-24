import numpy as np
import matplotlib.pyplot as plt

height = 300
width = 300

np_img = np.zeros((height, width, 3), dtype=np.uint8)

np_img[0:50, 0:50, 0] = 255
np_img[0:50, 0:50, 1] = 20
np_img[0:50, 0:50, 2] = 147

plt.imshow(np_img)
plt.show()
