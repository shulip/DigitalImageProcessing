import cv2
import numpy as np

def dct(img):
    img_dct = cv2.dct(img.astype(np.float32))  # 进行离散余弦变换

    img_dct_log = np.log(abs(img_dct))  # 进行log处理
    return img_dct_log