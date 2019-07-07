import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("resource/Images/nike.jpg", cv2.IMREAD_GRAYSCALE)

canny = cv2.Canny(img, 50, 200)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
laplacian = cv2.Laplacian(img, cv2.CV_64F)

images = [canny, sobelx, sobely, laplacian]
titles = ['canny', 'sobelx', 'sobely', 'laplacian']

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

