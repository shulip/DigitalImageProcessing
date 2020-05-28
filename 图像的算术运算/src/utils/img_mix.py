#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def load_imgs():
    im_1 = np.array(Image.open(r'imgs\cyber.jpg'))
    im_2 = np.array(Image.open(r'imgs\Lena.jpg'))

    return im_1, im_2


def mix_imgs(im_1, im_2, proportion):
    """
    图像融合（叠加）
    :param im_1:图像1
    :param im_2: 图像2
    :param proportion:融合度
    :return: 融合后图像
    """

    # 获取图像大小
    im_1_x, im_1_y,im_1_z = im_1.shape
    im_2_x, im_2_y,im_2_z = im_2.shape

    # 比较图像大小，找出最大尺寸
    if im_1_x > im_2_x:
        max_x = im_1_x
    else:
        max_x = im_2_x

    if im_1_y > im_2_y:
        max_y = im_1_y
    else:
        max_y = im_2_y

    # 创建两个符合最大尺寸的矩阵
    im_1_filled_with_0 = np.zeros((max_x,max_y,3))
    im_2_filled_with_0 = np.zeros((max_x,max_y,3))

    # 在矩阵中添加图片
    im_1_filled_with_0[0:im_1.shape[0], 0:im_1.shape[1], :] = im_1
    im_2_filled_with_0[0:im_2.shape[0], 0:im_2.shape[1], :] = im_2

    # 根据融合度相加
    mix_im = proportion * im_1_filled_with_0 + (1 - proportion) * im_2_filled_with_0
    mix_im = mix_im.astype(np.uint8)

    return mix_im


if __name__ == '__main__':
    im_1, im_2 = load_imgs()

    mix_im = mix_imgs(im_1, im_2, proportion=0.5)

    im = Image.fromarray(mix_im)

    plt.imshow(im)

    plt.show()
