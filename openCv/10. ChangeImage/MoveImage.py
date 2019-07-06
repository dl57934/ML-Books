import cv2
import numpy as np


def transform():
    img = cv2.imread("../resource/Images/desktop.png")
    img = cv2.resize(img, None, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
    h, w = img.shape[:2]

    M = np.float32([[1, 0, 100], [0, 1, 50]])

    moveImg = cv2.warpAffine(img, M, (w, h))
    cv2.imshow("moveImage", moveImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


transform()



