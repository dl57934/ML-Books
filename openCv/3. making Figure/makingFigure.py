import numpy as np
import cv2


def drawing():
    img = np.zeros((512, 512, 3), np.uint8)
    print(img)
    img.fill(100)

    cv2.line(img, (243, 128), (511, 511), (255, 125, 125), 5)  # BGR
    cv2.line(img, (243, 128), (0, 511), (255, 125, 125), 5)
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    cv2.circle(img, (250, 400), 63, (160, 125, 255))
    cv2.ellipse(img, (248, 256), (78, 50), 0, 0, 270, (255, 0, 0), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "Feliz", (100, 100), font, 4, (200, 200, 200), 5)

    cv2.imshow("figure Test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


drawing()
