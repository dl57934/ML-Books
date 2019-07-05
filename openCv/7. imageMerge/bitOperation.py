import numpy as np
import cv2


def bitOperation(hpos, vpos):
    img1 = cv2.imread("../resource/Images/desktop.png")
    img2 = cv2.imread("../resource/Images/ipad.jpeg")

    # 결과 값을 보여줄 namedWindow 지정
    cv2.namedWindow('result', cv2.WINDOW_NORMAL)
    cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
    cv2.namedWindow('mask_inv', cv2.WINDOW_NORMAL)
    cv2.namedWindow('img_fg', cv2.WINDOW_NORMAL)
    cv2.namedWindow('img_bg', cv2.WINDOW_NORMAL)

    # img2 resize해준다.
    img2 = cv2.resize(img2, (800, 500))

    # 이미지의 가로길이 세로길이 가져온다.
    rows, cols, channel = img2.shape
    # 입력받은 roi지정
    roi = img1[vpos:vpos + rows, hpos: hpos + cols]

    # 마스크 만들기
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    cv2.imshow("mask", mask)
    cv2.imshow("mask_inv", mask_inv)

    # 0이면 그대로 두고 아니면 그대로 mask를 씌웁니다.
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    cv2.imshow("img_fg", img2_fg)
    cv2.imshow("img_bg", img1_bg)

    # 두 이미지를 더해서 검은 부분과 색이 있는 부분이 더해져서 없어집니다.
    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos: vpos + rows, hpos: hpos + cols] = dst

    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


bitOperation(10, 10)
