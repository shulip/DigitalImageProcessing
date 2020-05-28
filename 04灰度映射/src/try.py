from PIL import Image
from numpy import *
from matplotlib import pyplot as plt

def histeq(im,nbr_bins=256):
    """
    对一幅灰度图像进行直方图均衡化
    :param im: 灰度图像
    :param nbr_bins: 直方图使用的小区间数目
    :return: 直方图均衡化后的图像，用来做像素值映射的累计分布函数
    """

    # 计算图像直方图
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum()   # cumulative distribution function
    cdf = 255 * cdf / cdf[-1]   #归一化

    # 使用累计分布函数的线性差值，计算新的像素值
    im2 =interp(im.flatten(),bins[:-1],cdf)

    return im2.reshape(im.shape),cdf


im = array(Image.open(r'imgs\Lena.jpg').convert('L'))
im2,cdf = histeq(im)

x_ = [i for i in range(len(cdf))]

plt.figure(figsize=(15,8),dpi=150)

plt.subplot(231),plt.hist(im.flatten(),128)
plt.subplot(232),plt.title('transformation function'),plt.plot(x_,cdf)
plt.subplot(233),plt.hist(im2.flatten(),128)
plt.subplot(234),plt.title('before'),plt.imshow(Image.fromarray(im))
plt.subplot(236),plt.title('after'),plt.imshow(Image.fromarray(im2))

plt.show()