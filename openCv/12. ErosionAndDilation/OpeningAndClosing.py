import numpy as np
import cv2


def morph():
    img1 = cv2.imread("../resource/Images/nike.jpg", cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((5, 5), np.uint8)

    gaussian = cv2.medianBlur(img1, 5)

    closing = cv2.morphologyEx(gaussian, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(gaussian, cv2.MORPH_OPEN, kernel)
    gradient = cv2.morphologyEx(gaussian, cv2.MORPH_GRADIENT, kernel)
    diff = cv2.morphologyEx(gaussian, cv2.MORPH_BLACKHAT, kernel)
    diff2 = cv2.morphologyEx(gaussian, cv2.MORPH_TOPHAT, kernel)
    

    cv2.imshow("closing", closing)
    cv2.imshow("open", opening)
    cv2.imshow("gradient", gradient)
    cv2.imshow("BLACK", diff)
    cv2.imshow("TOPHAT", diff2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


morph()