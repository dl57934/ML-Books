import numpy as np
import cv2
import matplotlib.pyplot as plt


def transform():
    img = cv2.imread("../resource/Images/trainRoad.jpg")
    h, w = img.shape[:2]

    pts1 = np.float32([[455, 350], [540, 350], [300, h], [730, h]])
    pts2 = np.float32([[0, 0], [1024, 0], [0, h], [1024, h]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    img2 = cv2.warpPerspective(img, M, (w, h))

    cv2.circle(img, (455, 350), 20, (255, 0, 0), -1)
    cv2.circle(img, (540, 350), 20, (0, 255, 0), -1)
    cv2.circle(img, (300, h), 20, (0, 0, 255), -1)
    cv2.circle(img, (730, h), 20, (0, 0, 0), -1)

    cv2.circle(img2, (0, 0), 20, (255, 0, 0), -1)
    cv2.circle(img2, (1024, 0), 20, (0, 255, 0), -1)
    cv2.circle(img2, (0, h), 20, (0, 0, 255), -1)
    cv2.circle(img2, (1024, h), 20, (0, 0, 0), -1)

    plt.subplot(1, 2, 1), plt.imshow(img), plt.title('image')
    plt.subplot(1, 2, 2), plt.imshow(img2), plt.title('perspective')
    plt.show()


transform()
