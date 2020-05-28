import numpy as np
from PIL import Image
import cv2
from matplotlib import pyplot as plt

# https://blog.csdn.net/hujingshuang/article/details/47759579

def map(arr, max, min):
    x_min = np.min(arr)
    x_max = np.max(arr)
    return min + (max - min) / (x_max - x_min) * (arr - x_min)


def template_match_with_fourier(bw,feature,thresh=253):
    feature_ = np.zeros(bw.shape)
    feature_[:feature.shape[0], :feature.shape[1]] = feature

    C = np.real(np.fft.ifft2(np.fft.fft2(bw) *
                             np.fft.fft2(np.rot90(feature_,0), bw.shape)))
    C = map(C, 255.0, 0.0)

    return C # > thresh
