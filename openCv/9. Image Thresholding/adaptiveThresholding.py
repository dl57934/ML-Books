import numpy as np
import cv2

img = cv2.imread("../resource/images/ipad.jpeg", cv2.IMREAD_GRAYSCALE)

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thr2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thr3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

title = ['original', 'Global Threshold', 'Adaptive Mean', 'Adaptive Gaussian']
images = [img, thr1, thr2, thr3]

for i in range(4):
    cv2.namedWindow(title[i], cv2.WINDOW_NORMAL)
    cv2.imshow(title[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

