import cv2
import numpy as np


img = cv2.imread("../resource/Images/nike.jpg", cv2.IMREAD_GRAYSCALE)
img_sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
img_sobel_x = cv2.convertScaleAbs(img_sobel_x)

img_sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
img_sobel_y = cv2.convertScaleAbs(img_sobel_y)

img_sobel = cv2.addWeighted(img_sobel_x, 1, img_sobel_y, 1, 0)


cv2.imshow("sobel_x", img_sobel_x)
cv2.imshow("sobel_y", img_sobel_y)
cv2.imshow("sobel", img_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
