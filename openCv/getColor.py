import cv2
import matplotlib.pyplot as plt

# apples_image = cv2.imread("resource/Images/apples.png")
# apples_image = cv2.cvtColor(apples_image, cv2.COLOR_BGR2RGB)
#
# red_channel_apples_image = apples_image.copy()
# red_channel_apples_image[:, :, 1] = 0
# red_channel_apples_image[:, :, 2] = 0
#
# green_channel_apples_image = apples_image.copy()
# green_channel_apples_image[:, :, 0] = 0
# green_channel_apples_image[:, :, 2] = 0
#
# blue_channel_apples_image = apples_image.copy()
# blue_channel_apples_image[:, :, 0] = 0
# blue_channel_apples_image[:, :, 1] = 0
#
# titles = ["original", "red", "green", "blue"]
# src = [apples_image, red_channel_apples_image, green_channel_apples_image, blue_channel_apples_image]
#
# for i in range(1, 5):
#     plt.subplot(1, 4, i), plt.imshow(src[i - 1]), plt.title(titles[i - 1])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()
#
# red = red_channel_apples_image[:, :, 0]
# green = green_channel_apples_image[:, :, 1]
# blue = blue_channel_apples_image[:, :, 2]
#
# print(red)
#
# cv2.imshow("red", red)
# cv2.imshow("green", green)
# cv2.imshow("blue", blue)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

red = cv2.imread("red.png")
red = red[:, :, 0]


def getColorAverage(color):
    for i in range(585):
       print(color[i])



print(getColorAverage(red))
# # print(getColorAverage(green_channel_apples_image))
# # print(getColorAverage(blue_channel_apples_image))

