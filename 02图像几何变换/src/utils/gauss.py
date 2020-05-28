#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
from numpy import *
from scipy.ndimage import filters
from matplotlib import pyplot as plt

def gaussian(im,sigma):
    """
    对图像进行高斯模糊
    :param im: 图像数组
    :param sigma: 二维高斯核
    :return: 高斯模糊后的图像
    """
    if(len(im.shape) == 2):
        im2 = filters.gaussian_filter(im,sigma)
    else:
        im2 = zeros(im.shape)
        for i in range(im.shape[2]):
            im2[:,:,i] = filters.gaussian_filter(im[:,:,i],sigma)
    im2 = array(im2,'uint8')
    return im2