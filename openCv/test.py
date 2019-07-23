import cv2
import numpy as np

img = cv2.imread("resource/Images/apples.png", -1)

rgb_planes = cv2.split(img)

result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    print(diff_img)
    result_planes.append(diff_img)

result = cv2.merge(result_planes)

cv2.imwrite('shadows_out.png', result)
