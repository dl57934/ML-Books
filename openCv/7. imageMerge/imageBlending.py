import cv2
import numpy as np


def onMouse(x):
    pass


def imageBlending(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.namedWindow("blending", cv2.WINDOW_NORMAL)
    cv2.createTrackbar('weight', 'blending', 0, 100, onMouse)
    mix = 0

    img1 = cv2.resize(img1, (1200, 600))
    img2 = cv2.resize(img2, (1200, 600))

    while True:
        weighted_img = cv2.addWeighted(img1, float(mix)/100, img2, float(100 - mix)/100, 0)
        cv2.imshow("blending", weighted_img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        mix = cv2.getTrackbarPos("weight", "blending")

    cv2.destroyAllWindows()


imageBlending("../resource/Images/ipad.jpeg", "../resource/Images/desktop.png")
