import numpy as np
import cv2


def onChange():
    pass


def trackBar():
    img = np.zeros((200, 512, 3), np.uint8)
    cv2.namedWindow("color Track Bar")

    cv2.createTrackbar('B', 'color Track Bar', 0, 255, onChange)
    cv2.createTrackbar('G', 'color Track Bar', 0, 255, onChange)
    cv2.createTrackbar('R', 'color Track Bar', 0, 255, onChange)

    switch = "0: OFF\n1: ON"
    cv2.createTrackbar(switch, 'color Track Bar', 0, 1, onChange)

    while True:
        cv2.imshow('color Track Bar', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

        b = cv2.getTrackbarPos('B', 'color Track Bar')
        g = cv2.getTrackbarPos('G', 'color Track Bar')
        r = cv2.getTrackbarPos('R', 'color Track Bar')
        s = cv2.getTrackbarPos(switch, 'color Track Bar')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv2.destroyAllWindows()


trackBar()
