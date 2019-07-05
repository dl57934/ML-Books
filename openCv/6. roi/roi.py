import numpy as np
import cv2

img = cv2.imread("../resource/Images/ipad.jpeg")
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original', img)

subImg = img[300:400, 350:750]
cv2.namedWindow('cutting', cv2.WINDOW_NORMAL)
cv2.imshow('cutting', subImg)

print(img.shape)
print(subImg.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()