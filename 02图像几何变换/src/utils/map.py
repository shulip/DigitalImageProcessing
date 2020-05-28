#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np

def map(arr,min,max):
    """
    映射
    :param arr: 矩阵
    :param min: 最小值
    :param max: 最大值
    :return:
    """
        # https://blog.csdn.net/Touch_Dream/article/details/62076236
    arr = arr.astype(np.float32)
    arr_max = np.max(arr)
    arr_min = np.min(arr)

    maped_arr = min + (max - min)/(arr_max-arr_min) * (arr - arr_min)
    return maped_arr





if __name__ == '__main__':
    a = np.array([1,7,7,7,7,7,7])

    maped_a = map(a,0,1)

    print(a)

    print(maped_a)
