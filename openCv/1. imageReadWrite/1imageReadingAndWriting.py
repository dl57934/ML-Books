import cv2


def showImage():
    imgFile = "resource/ipad.jpeg"
    img = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

    cv2.namedWindow('ipad', cv2.WINDOW_NORMAL)
    cv2.imshow('ipad', img)
    cv2.waitKey(10000000)
    cv2.destroyAllWindows()
    cv2.imwrite("resource/ipad_copy.jpeg", img)

showImage()
