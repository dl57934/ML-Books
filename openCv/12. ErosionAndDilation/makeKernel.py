import numpy as np
import cv2


def makekernel():
    rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

    print(rect)
    print(ellipse)
    print(cross)


makekernel()