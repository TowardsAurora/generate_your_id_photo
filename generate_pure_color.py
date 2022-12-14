import numpy as np
import cv2


def create_rgb_to_bgr(R, G, B):
    color = (B, G, R)
    return color


# mode B G R
def create_pure(h, w, COLOR):
    img = np.zeros((h, w, 3), np.uint8)
    imgRgb = img.copy()
    imgRgb[:, :, :] = COLOR
    return imgRgb


if __name__ == '__main__':
    bgr = create_rgb_to_bgr(255, 0, 0)
    color = bgr
    pure = create_pure(306, 236, color)
    # cv2.imwrite('./pure/pure1.png',pure)
    print(color)
    cv2.imshow('rgb', pure)
    cv2.waitKey()
    cv2.destroyAllWindows()
