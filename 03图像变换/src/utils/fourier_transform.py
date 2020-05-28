import numpy as np
from PIL import Image
import cv2
from matplotlib import pyplot as plt

def fourier_transform(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    # fft结果是复数, 其绝对值结果是振幅
    fimg = np.log(np.abs(fshift))

    return fimg



