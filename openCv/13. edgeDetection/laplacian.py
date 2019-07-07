import cv2
import numpy as np


img = cv2.imread("../resource/Images/receipt.png", cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(img, cv2.CV_32F)


cv2.imshow("original", img)
cv2.imshow("laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()