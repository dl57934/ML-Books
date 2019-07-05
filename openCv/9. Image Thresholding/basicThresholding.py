import numpy as np
import cv2


def setNamedWindow(windowName, type):
    cv2.namedWindow(windowName, type)


def show(windowName, src):
    cv2.imshow(windowName, src)


img = cv2.imread("../resource/Images/ipad.jpeg", cv2.IMREAD_GRAYSCALE)

setNamedWindow("original", cv2.WINDOW_NORMAL)
setNamedWindow("BINARY", cv2.WINDOW_NORMAL)
setNamedWindow("BINARY_INV", cv2.WINDOW_NORMAL)
setNamedWindow("TRUNC", cv2.WINDOW_NORMAL)
setNamedWindow("TOZERO", cv2.WINDOW_NORMAL)
setNamedWindow("TOZERO_INV", cv2.WINDOW_NORMAL)

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

show("original", img)
show("BINARY", thr1)
show("BINARY_INV", thr2)
show("TRUNC", thr3)
show("TOZERO", thr4)
show("TOZERO_INV", thr5)

cv2.waitKey(0)
cv2.destroyAllWindows()

