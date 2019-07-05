import numpy as np
import cv2

def showVideo():
    cap = cv2.VideoCapture(0)

    cap.set(3, 960)
    cap.set(4, 640)

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video', gray)

        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


showVideo()
