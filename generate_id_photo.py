import cv2

from generate_pure_color import create_pure
import numpy as np


def resize_one_inch(img):
    one_inch = cv2.resize(img, (295, 413))
    return one_inch


def resize_two_inch(img):
    two_inch = cv2.resize(img, (413, 626))
    return two_inch


def lay_pos(img, bg, x, y, x1, y1):
    bg[x:x1, y:y1] = img
    return bg


def lay_one_inch(img, bg, num):
    if num > 8:
        print("1寸照片不能超过8张")
        return
    img = resize_one_inch(img)
    img = rotate_bound(img, -90)
    t = num // 2
    count = 0
    for i in range(2):
        for j in range(t):
            count += 1
            pos = lay_pos(img, bg, 20 + (20 + 295) * j, 20 + (20 + 413) * i, (20 + 295) * (j + 1), (20 + 413) * (i + 1))
    return pos


def lay_two_inch(img, bg, num):
    if num > 4:
        print("2寸照片不能超过4张")
        return
    img = resize_two_inch(img)
    t = num // 2
    count = 0
    for i in range(2):
        for j in range(t):
            count += 1
            pos = lay_pos(img, bg, 20 + (20 + 626) * j, 20 + (20 + 413) * i, (20 + 626) * (j + 1), (20 + 413) * (i + 1))
    return pos


def rotate_bound(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv2.warpAffine(image, M, (nW, nH))


if __name__ == '__main__':
    # path = './result/id_photo.png'
    path = './result/2id_photo2.png'
    oriImg = cv2.imread(path)

    pure = create_pure(1300, 886, (255, 255, 255))

    # 输入数字应为大于0，小于8的偶数效果最佳
    inch1 = lay_one_inch(oriImg, pure, 8)
    cv2.imshow('inc1', inch1)

    # name = input("请输入文件名：")
    name = 'boy'
    cv2.imwrite('./one_inch/' + name + '.png', inch1)

    inch2 = lay_two_inch(oriImg, pure, 4)
    cv2.imshow('inch2', inch2)

    cv2.imwrite('./two_inch/' + name + '.png', inch2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
