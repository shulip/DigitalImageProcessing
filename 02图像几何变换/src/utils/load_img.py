#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def load_img(path):
    im = np.array(Image.open(path))

    return im