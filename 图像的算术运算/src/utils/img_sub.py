#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def load_imgs():
    im_1 = np.array(Image.open(r'imgs\Lena.jpg'))
    im_2 = np.array(Image.open(r'imgs\Lena_points.jpg'))

    return im_1,im_2

def sub_imgs(im_1,im_2,type="front"):
    """
    图像相减
    :param im_1: 图像1
    :param im_2: 图像2
    :param type: 相减顺序   front: im_1-im_2    back:im_2-im_1
    :return:
    """
    im_1 = im_1.astype(np.int16)
    im_2 = im_2.astype(np.int16)

    if type=='front':
        subed_img = np.abs(im_1 - im_2)

    elif type=='back':
        subed_img = np.abs(im_2 - im_1)

    subed_img = subed_img.astype(np.uint8)

    return subed_img