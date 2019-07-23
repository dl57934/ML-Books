import cv2
import matplotlib.pyplot as plt
import numpy as np

apples_image = cv2.imread("resource/Images/apples.png")
apples_image = cv2.cvtColor(apples_image, cv2.COLOR_BGR2RGB)

red_channel_apples_image, green_channel_apples_image, blue_channel_apples_image = cv2.split(apples_image)

titles = ["original", "red", "green", "blue"]
src = [apples_image, red_channel_apples_image, green_channel_apples_image, blue_channel_apples_image]

zeros = np.zeros((apples_image.shape[0], apples_image.shape[1]), dtype="uint8")

for i in range(red_channel_apples_image.shape[0]):
    print(red_channel_apples_image[i])
