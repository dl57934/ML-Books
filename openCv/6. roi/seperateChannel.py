import numpy as np
import cv2

img = cv2.imread("../resource/Images/ipad.jpeg")

b, g, r = cv2.split(img)


def showImage(window, img):
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.imshow(window, img)


showImage("original", img)
showImage("b", b)
showImage("g", g)
showImage("r", r)

mergeImage = cv2.merge((b, g, r))
showImage("merge", mergeImage)

cv2.waitKey(0)
cv2.destroyAllWindows()


b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]