#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.Qt import QButtonGroup
from PyQt5.Qt import QListView
from PyQt5.Qt import QSplashScreen, QDateTime
from Ui.mainwindow import Ui_MainWindow

import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation

import cv2
import numpy as np
from PIL import Image, ImageFilter

import os
import time
import copy

from utils import polynomial, line, broken, histeq,gamma_trans


class MyFigure(FigureCanvas):
    def __init__(self, img):
        self.img = img
        self.fig = Figure(facecolor=(232 / 255.0, 233 / 255.0, 235 / 255.0))
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        self.axes = self.fig.add_subplot(111)
        self.axes.axis('off')
        # plt.xlim(0, 255)

    def show_2d_array(self):
        self.axes.imshow(self.img, cmap='gray')


class TwoImgFigure(FigureCanvas):
    def __init__(self, img,raw_img):
        self.img = img
        self.raw_img = raw_img
        self.fig = Figure(facecolor=(232 / 255.0, 233 / 255.0, 235 / 255.0))
        super(TwoImgFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        self.axes1 = self.fig.add_subplot(121)
        self.axes2 = self.fig.add_subplot(122)
        self.axes1.axis('off')
        self.axes2.axis('off')
        # plt.xlim(0, 255)

    def show_2d_array(self):
        self.axes1.imshow(self.raw_img, cmap='gray')
        self.axes2.imshow(self.img, cmap='gray')

class HisFigure(FigureCanvas):
    def __init__(self, img,raw_img,cdf):
        self.img = img
        self.raw_img = raw_img
        self.cdf = cdf
        self.fig = Figure(facecolor=(232 / 255.0, 233 / 255.0, 235 / 255.0))
        super(HisFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        self.axes = self.fig.add_subplot(221)
        self.axes1 = self.fig.add_subplot(222)
        self.axes2 = self.fig.add_subplot(223)
        # self.axes.axis('off')

    def show_2d_array(self):
        self.axes.hist(self.raw_img.flatten(), 128)
        x_ = [i for i in range(len(self.cdf))]
        self.axes1.plot(x_, self.cdf)
        self.axes2.hist(self.img.flatten(), 128)


class PointChanging(QObject):
    signal_change = pyqtSignal()

    def on_press(self, event):
        MainWindow.whether_click = True
        MainWindow.press_down = (event.xdata, event.ydata)
        MainWindow.min_index = self.calculate_min_distance(MainWindow.press_down)
        print(MainWindow.min_index)
        print("my down position:", event.button, MainWindow.press_down)
        if MainWindow.min_index == -1:
            MainWindow.X = np.append(MainWindow.X, event.xdata)
            MainWindow.Y = np.append(MainWindow.Y, event.ydata)
            self.signal_change.emit()
            print("emit")
            # cls.signal_change.emit()
        else:
            MainWindow.X = np.delete(MainWindow.X, MainWindow.min_index)
            MainWindow.Y = np.delete(MainWindow.Y, MainWindow.min_index)
            MainWindow.X = np.append(MainWindow.X, event.xdata)
            MainWindow.Y = np.append(MainWindow.Y, event.ydata)

    def on_motion_notify(self, event):
        if MainWindow.whether_click:
            MainWindow.press_move = (event.xdata, event.ydata)
            print("my move position:", event.button, MainWindow.press_move)

            # if MainWindow.min_index == -1:
            MainWindow.X = np.delete(MainWindow.X, -1)
            MainWindow.X = np.append(MainWindow.X, event.xdata)
            MainWindow.Y = np.delete(MainWindow.Y, -1)
            MainWindow.Y = np.append(MainWindow.Y, event.ydata)
            self.signal_change.emit()
            print("emit")

    def on_release(self, event):
        MainWindow.whether_click = False
        MainWindow.min_index = -1
        MainWindow.press_up = (event.xdata, event.ydata)
        print("my up position:", event.button, MainWindow.press_up)

    def calculate_min_distance(self, location):
        index = -1
        min_distance = 9999999
        distances = np.sqrt(pow((MainWindow.X - location[0]), 2) + pow((MainWindow.Y - location[1]), 2))
        min_distance = np.min(distances)
        min_index = np.where(distances == np.min(distances))[0][0]
        if min_distance < 5:
            return min_index
        else:
            return -1


class CurveFigure(FigureCanvas):
    pc = PointChanging()

    def __init__(self, X, Y, type):
        self.X = X
        self.Y = Y
        self.type = type
        self.fig = Figure(facecolor=(232 / 255.0, 233 / 255.0, 235 / 255.0))
        super(CurveFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        self.axes = self.fig.add_subplot(111)
        # self.axes.axis('off')
        self.axes.axis([-5, 260, -5, 260])
        # self.fig.canvas.mpl_connect('button_press_event', self.pc.on_press)
        # self.fig.canvas.mpl_connect('button_release_event', self.pc.on_release)
        # self.fig.canvas.mpl_connect('motion_notify_event', self.pc.on_motion_notify)

    def show_curve(self):
        if self.type == "curve":
            x = np.arange(0, 255, 1)
            y = polynomial(x, self.X, self.Y)
            self.axes.plot(x, y)
            self.axes.plot(self.X, self.Y, "ob")
        elif self.type == "line":
            x = np.arange(0, 255, 1)
            y = line(x, self.X, self.Y)
            self.axes.plot(x, y)
        elif self.type == "broken":
            x = np.arange(0, 255, 1)
            y = broken(x, self.X, self.Y)
            self.axes.plot(x, y)
            self.axes.plot(self.X, self.Y, "ob")
        elif self.type == "gamma":
            x = np.arange(0, 255, 1)
            y = gamma_trans(x, self.X)
            self.axes.plot(x, y)



class MainWindow(QMainWindow, Ui_MainWindow):
    # 定义一个信号
    signal_change = pyqtSignal()
    # sigarr = [pyqtSignal()]

    # 有关鼠标点击和曲线绘制的全局变量
    press_down = None
    press_move = None
    press_up = None
    whether_click = False
    min_index = -1

    X = np.array([0, 125, 255])
    Y = np.array([0, 150, 255])
    a = 1
    b = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 添加阴影
        self.add_shadow()

        # 实例化主窗口的QMenuBar对象
        self.file = self.menubar.addMenu("文件")
        self.openFile = QAction("打开", self)
        self.file.addAction(self.openFile)
        self.openFile.triggered.connect(self.add_image)

        # 全局变量
        self.type = "line"
        self.raw_img = None  # 原始图像
        self.img = None  # 空域图像
        self.frequency_img = None  # 频域图像
        self.cdf = None
        self.gamma = 1

        # 拉条
        self.horizontalSlider_a.setMinimum(-100)
        self.horizontalSlider_a.setMaximum(100)
        self.horizontalSlider_a.setSingleStep(0.1)
        self.horizontalSlider_b.setMinimum(-255)
        self.horizontalSlider_b.setMaximum(255)
        self.horizontalSlider_b.setSingleStep(1)
        self.horizontalSlider_a.setValue(self.a)
        self.horizontalSlider_b.setValue(self.b)
        self.horizontalSlider_gamma.setMinimum(1)
        self.horizontalSlider_gamma.setMaximum(2500)
        self.horizontalSlider_gamma.setValue(100)

        # 拉条改变
        self.horizontalSlider_a.valueChanged.connect(self.change_a)
        self.horizontalSlider_b.valueChanged.connect(self.change_b)
        self.horizontalSlider_gamma.valueChanged.connect(self.change_gamma)

        # 显示窗口
        self.graphicsView_image = QGridLayout(self.graphicsView_image)
        self.graphicsView_curve = QGridLayout(self.graphicsView_curve)

        # 改变方法
        self.pushButton_line.clicked.connect(self.choose_line)
        self.pushButton_broken.clicked.connect(self.choose_broken)
        self.pushButton_curve.clicked.connect(self.choose_curve)
        self.pushButton_histeq.clicked.connect(self.choose_histeq)
        self.pushButton_gamma.clicked.connect(self.choose_gamma)

        # 设置不可视
        self.label_a.setVisible(False)
        self.label_b.setVisible(False)
        self.horizontalSlider_a.setVisible(False)
        self.horizontalSlider_b.setVisible(False)
        self.label_gamma.setVisible(False)
        self.horizontalSlider_gamma.setVisible(False)

        # 鼠标点击重绘曲线
        self.pc = PointChanging()
        self.pc.signal_change.connect(self.updata_img)

    def change_a(self):
        self.a = self.horizontalSlider_a.value()/10.
        self.updata_img()

    def change_b(self):
        self.b = self.horizontalSlider_b.value()
        self.updata_img()

    def change_gamma(self):
        self.gamma = self.horizontalSlider_gamma.value()/100.0
        self.updata_img()

    def choose_line(self):
        self.type = "line"
        self.label_a.setVisible(True)
        self.label_b.setVisible(True)
        self.horizontalSlider_a.setVisible(True)
        self.horizontalSlider_b.setVisible(True)
        self.label_gamma.setVisible(False)
        self.horizontalSlider_gamma.setVisible(False)
        self.updata_img()

    def choose_broken(self):
        self.type = "broken"
        # self.X = np.array([0, 125, 255])
        # self.Y = np.array([0, 150, 255])
        self.label_a.setVisible(False)
        self.label_b.setVisible(False)
        self.horizontalSlider_a.setVisible(False)
        self.horizontalSlider_b.setVisible(False)
        self.label_gamma.setVisible(False)
        self.horizontalSlider_gamma.setVisible(False)
        self.updata_img()

    def choose_curve(self):
        self.type = "curve"
        # self.X = np.array([0, 125, 255])
        # self.Y = np.array([0, 150, 255])
        self.label_a.setVisible(False)
        self.label_b.setVisible(False)
        self.horizontalSlider_a.setVisible(False)
        self.horizontalSlider_b.setVisible(False)
        self.label_gamma.setVisible(False)
        self.horizontalSlider_gamma.setVisible(False)
        self.updata_img()

        # self.show_curve()

    def choose_histeq(self):
        self.type = "histeq"
        self.label_a.setVisible(False)
        self.label_b.setVisible(False)
        self.horizontalSlider_a.setVisible(False)
        self.horizontalSlider_b.setVisible(False)
        self.label_gamma.setVisible(False)
        self.horizontalSlider_gamma.setVisible(False)
        self.updata_img()

    def choose_gamma(self):
        self.type = "gamma"
        self.label_a.setVisible(False)
        self.label_b.setVisible(False)
        self.horizontalSlider_a.setVisible(False)
        self.horizontalSlider_b.setVisible(False)
        self.label_gamma.setVisible(True)
        self.horizontalSlider_gamma.setVisible(True)
        self.updata_img()

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(16)
        shadow.setColor(QColor(0, 0, 0, 500))
        shadow.setOffset(1, 1)
        self.frame_top1.setGraphicsEffect(shadow)

        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(16)
        shadow1.setColor(QColor(0, 0, 0, 500))
        shadow1.setOffset(1, 1)
        self.frame_image.setGraphicsEffect(shadow1)

        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(16)
        shadow2.setColor(QColor(110, 110, 110, 500))
        shadow2.setOffset(1, 1)
        self.frame_curve.setGraphicsEffect(shadow2)

    def show_line(self):
        fig = CurveFigure(self.a, self.b, self.type)
        fig.show_curve()

        self.graphicsView_curve.addWidget(fig, 0, 1)

    def show_curve(self):
        print('show_curve')
        fig = CurveFigure(self.X, self.Y, self.type)
        fig.fig.canvas.mpl_connect('button_press_event', self.pc.on_press)
        fig.fig.canvas.mpl_connect('button_release_event', self.pc.on_release)
        fig.fig.canvas.mpl_connect('motion_notify_event', self.pc.on_motion_notify)
        fig.show_curve()

        self.graphicsView_curve.addWidget(fig, 0, 1)

    def show_histeq(self):
        fig = HisFigure(self.img,self.raw_img,self.cdf)
        fig.show_2d_array()

        self.graphicsView_curve.addWidget(fig, 0, 1)

    def show_gamma(self):
        fig = CurveFigure(self.gamma, self.b, self.type)
        fig.show_curve()
        self.graphicsView_curve.addWidget(fig, 0, 1)

    def show_img(self):
        if self.type == "histeq":
            fig = TwoImgFigure(self.img,self.raw_img)
            fig.show_2d_array()
            self.graphicsView_image.addWidget(fig, 0, 1)
        else:
            fig = MyFigure(self.img)
            fig.show_2d_array()
            self.graphicsView_image.addWidget(fig, 0, 1)

    def add_image(self):
        """添加图像"""
        self.paths, filetype = QFileDialog.getOpenFileNames(None,
                                                            "添加图像",
                                                            os.getcwd(),  # 起始路径
                                                            "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg)")
        self.img = np.array(Image.open(self.paths[0]).convert("L"))
        self.raw_img = self.img

        self.show_img()

    def updata_img(self):
        if self.type == "curve":
            self.img = polynomial(self.raw_img, self.X, self.Y)
            self.show_img()
            self.show_curve()

        elif self.type == "line":
            self.img = line(self.raw_img, self.a, self.b)
            self.show_line()
            self.show_img()

        elif self.type == "broken":
            self.img = polynomial(self.raw_img, self.X, self.Y)
            self.show_img()
            self.show_curve()

        elif self.type == "histeq":
            self.img,self.cdf = histeq(self.raw_img)
            self.show_img()
            self.show_histeq()

        elif self.type == "gamma":
            self.img = gamma_trans(self.raw_img,self.gamma)
            self.show_img()
            self.show_gamma()
