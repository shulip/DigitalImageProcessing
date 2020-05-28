import numpy as np
from PIL import Image
import cv2
from matplotlib import pyplot as plt

def test(img ,angle):
    img = img.rotate(angle)
    img = np.array(img)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    # fft结果是复数, 其绝对值结果是振幅
    fimg = np.log(np.abs(fshift))


    plt.subplot(121)
    plt.imshow(img ,"gray")
    plt.subplot(122)
    plt.imshow(fimg ,"gray")
    plt.show()

img = Image.open(r"imgs\test.jpg").convert("L")

test(img,0)
test(img,30)
test(img,60)
test(img,90)
test(img,180)
