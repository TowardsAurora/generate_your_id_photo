import cv2
import numpy as np


def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """

    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道

    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道
    return img_new


def merge_img(img, png_trans_img, y1, y2, x1, x2):
    """ 将png透明图像与jpg图像叠加
        y1,y2,x1,x2为叠加位置坐标值
    """

    # 判断jpg图像是否已经为4通道
    if img.shape[2] == 3:
        img = add_alpha_channel(img)

    '''
    当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
    这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
    '''
    yy1 = 0
    yy2 = png_trans_img.shape[0]
    xx1 = 0
    xx2 = png_trans_img.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > img.shape[1]:
        xx2 = png_trans_img.shape[1] - (x2 - img.shape[1])
        x2 = img.shape[1]
    if y2 > img.shape[0]:
        yy2 = png_trans_img.shape[0] - (y2 - img.shape[0])
        y2 = img.shape[0]

    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_png = png_trans_img[yy1:yy2, xx1:xx2, 3] / 255.0
    alpha_jpg = 1 - alpha_png

    # 开始叠加
    for c in range(0, 3):
        img[y1:y2, x1:x2, c] = ((alpha_jpg * img[y1:y2, x1:x2, c]) + (alpha_png * png_trans_img[yy1:yy2, xx1:xx2, c]))

    return img


def operate(bg_img, transparent_img):
    bg_img = cv2.imread(bg_img, cv2.IMREAD_UNCHANGED)
    transparent_img = cv2.imread(transparent_img, cv2.IMREAD_UNCHANGED)

    x_ori = 0
    y_ori = 0
    x_f = x_ori + transparent_img.shape[1]
    y_f = y_ori + transparent_img.shape[0]

    res_img = merge_img(bg_img, transparent_img, y_ori, y_f, x_ori, x_f)

    cv2.imshow('result', res_img)

    return res_img
