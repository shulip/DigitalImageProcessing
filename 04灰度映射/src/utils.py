import numpy as np
from matplotlib import pyplot as plt

def map(x, Max, Min):
    x_min = np.min(x)
    x_max = np.max(x)
    x = Min + (Max - Min) / (x_max - x_min) * (x - x_min)
    return x

def polynomial(X, x_, y_):
    X = X.astype(np.int32)
    num = x_.shape[0]
    Y = 0
    for i in range(num):
        temp = y_[i]
        for j in range(num):
            if i != j:
                temp = temp * (X - x_[j]) / (x_[i] - x_[j])
        Y += temp

    Y[Y < 0] = 0
    Y[Y > 255] = 255

    return Y


def line(x, a, b):
    x = x.astype(np.int32)
    Y = a * x + b

    Y[Y < 0] = 0
    Y[Y > 255] = 254

    return Y


def broken(X, x, y):
    X = X.astype(np.int32)
    x_y = np.vstack([x, y])
    x, y = x_y.T[np.lexsort(x_y[::-1, :])].T

    num = x.shape[0]
    Logics = np.zeros(X.shape).astype(np.bool)
    for i in range(num - 1):
        print(x[i], x[i + 1])
        k = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
        b = y[i] - x[i] * k

        logic = np.logical_and.reduce([X >= x[i], X < x[i + 1]])
        logic = np.logical_and(logic ^ Logics, logic)
        Logics = Logics + logic

        X[logic] = k * X[logic] + b

    return X


def histeq(im, nbr_bins=256):
    """
    对一幅灰度图像进行直方图均衡化
    :param im: 灰度图像
    :param nbr_bins: 直方图使用的小区间数目
    :return: 直方图均衡化后的图像，用来做像素值映射的累计分布函数
    """

    # 计算图像直方图
    imhist, bins = np.histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()  # cumulative distribution function
    cdf = 255 * cdf / cdf[-1]  # 归一化

    # 使用累计分布函数的线性差值，计算新的像素值
    im2 = np.interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape),cdf

def gamma_trans(X,gamma):
    X = map(X,1.0,0.0)
    Y = pow(X,gamma)
    Y = map(Y,255,0)
    return Y

if __name__ == '__main__':
    # a = np.array([1,100,235,255])
    # print(line(a,3,12))
    # a = np.array([13,41,1,23,2])
    # print(a)
    # b = np.array([1,2,3,4,5])
    # print(b)
    # c = np.vstack([a,b])
    # print(c)
    #
    # x,y = c.T[np.lexsort(c[::-1,:])].T
    # print(x)
    # print(y)

    x_ = np.array([0, 15, 90, 193, 255])
    y_ = np.array([0, 142, 112, 144, 255])

    x = np.arange(0, 255, 1)
    # y = polynomial(x, x_, y_)
    y = line(x,1.2,60)
    # plt.plot(x_, y_, "ob")
    plt.axis([-5, 260, -5, 260])
    plt.plot(x, y)
    plt.show()

    # plt.savefig("broken.png")

    # Logics = np.ones([3,4]).astype(np.bool)
    # Logics[0:1] = False
    # print(Logics)
    # print(Logics.dtype)
    #
    # Logics_ = np.zeros([3, 4]).astype(np.bool)
    # Logics_[:,1:3] = True
    # print(Logics_)
    # print(Logics_.dtype)
    #
    # print(Logics ^ Logics_)
