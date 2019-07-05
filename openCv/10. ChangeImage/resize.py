import cv2
import numpy as np


def transform():
    baseImage = cv2.imread("../resource/Images/ipad.jpeg")
    h, w = baseImage.shape[:2]

    img2 = cv2.resize(baseImage, None, None, 0.1, 0.1, interpolation=cv2.INTER_AREA)

    cv2.imshow("img2", img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


transform()