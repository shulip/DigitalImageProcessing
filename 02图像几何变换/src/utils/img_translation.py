#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2


def img_translation(im, dx, dy):
    """
    图像平移
    :param im: 图像平移
    :param dx: x轴位移
    :param dy: y轴位移
    :return:
    """
    H = np.float32([[1, 0, dx], [0, 1, dy]])
    rows, cols = im.shape[:2]
    res = cv2.warpAffine(im, H, (cols + dx, rows + dy), borderValue=(255, 255, 255))  # 需要图像、变换矩阵、变换后的大小

    return res


if __name__ == '__main__':
    import os

    path = r'..\imgs\2007_000925.jpg'
    print(os.path.exists(path))
    img = cv2.imread(path)
    # print(img)
    img2 = img_translation(img, 100, -100)

    print(img.shape)
    print(img2.shape)

    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(img2)

    plt.show()
