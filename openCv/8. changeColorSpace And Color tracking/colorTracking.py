import numpy as np
import cv2


def tracking():
    cap = cv2.VideoCapture(0)

    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])

    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])

    lower_red = np.array([-10, 100, 100])
    upper_red = np.array([10, 255, 255])

    while True:
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        blue_range = cv2.inRange(hsv, lower_blue, upper_blue)
        green_range = cv2.inRange(hsv, lower_green, upper_green)
        red_range = cv2.inRange(hsv, lower_red, upper_red)

        blue_result = cv2.bitwise_and(frame, frame, mask=blue_range)
        red_result = cv2.bitwise_and(frame, frame, mask=red_range)
        green_result = cv2.bitwise_and(frame, frame, mask=green_range)

        blue_result = cv2.resize(blue_result, (300, 300))
        green_result = cv2.resize(green_result, (300, 300))
        red_result = cv2.resize(red_result, (300, 300))
        frame = cv2.resize(frame, (300, 300))

        cv2.imshow("original", frame)
        cv2.imshow("blue", blue_result)
        cv2.imshow("red", red_result)
        cv2.imshow("green", green_result)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break

    cv2.destroyAllWindows()


tracking()
