import numpy as np
import cv2

def writeVideo():
    cap = cv2.VideoCapture(0)

    cap.set(3, 960)
    cap.set(4, 480)

    fps = 20
    width = int(cap.get(3))
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

    out = cv2.VideoWriter('../resource/video/DIVX.avi', fcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        cv2.imshow('divx', frame)
        out.write(frame)

        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

writeVideo()