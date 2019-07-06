import numpy as np
import cv2


def onMouse(x):
    pass


def bluring():
    img = cv2.imread("../resource/Images/kind.jpg")

    cv2.namedWindow("BlurPane")
    cv2.createTrackbar("BLUR_MODE", "BlurPane", 0, 3, onMouse)
    cv2.createTrackbar("BLUR", "BlurPane", 0, 5, onMouse)

    mode = cv2.getTrackbarPos("BLUR_MODE", "BlurPane")
    val = cv2.getTrackbarPos("BLUR", "BlurPane")

    while True:
        val = val * 2 + 1

        try:
            if mode == 0:
                blur = cv2.blur(img, (val, val))
            elif mode == 1:
                blur = cv2.GaussianBlur(img, (val, val), 0)
            elif mode == 2:
                blur = cv2.medianBlur(img, val)
            elif mode == 3:
                blur = cv2.bilateralFilter(img, 9, 75, 75)
            else:
                break
            cv2.imshow("BlurPane", blur)
        except:
            break

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        mode = cv2.getTrackbarPos("BLUR_MODE", "BlurPane")
        val = cv2.getTrackbarPos("BLUR", "BlurPane")

    cv2.destroyAllWindows()


bluring()
