import cv2
import numpy as np


def transform():
    img = cv2.imread("../resource/Images/trainRoad.jpg")
    h, w = img.shape[:2]

    pts1 = np.float32([[50, 50], [200, 100], [20, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(pts1, pts2)

    print(M)

    img2 = cv2.warpAffine(img, M, (w, h))

    cv2.imshow("original", img)
    cv2.imshow("perspective", img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


transform()
