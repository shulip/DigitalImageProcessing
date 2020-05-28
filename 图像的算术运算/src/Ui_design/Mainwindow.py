#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.Qt import QButtonGroup
from PyQt5.Qt import QListView
from PyQt5.Qt import QSplashScreen, QDateTime
from Ui_design.Ui.mainwindow import Ui_MainWindow

import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import cv2
import numpy as np
from PIL import Image,ImageFilter

from utils.img_mix import load_imgs as mix_load
from utils.img_mix import mix_imgs

from utils.img_sub import load_imgs as sub_load
from utils.img_sub import sub_imgs

# from utils.gauss import gaussian
import os
import time


class MyFigure(FigureCanvas):
    def __init__(self, img):
        # index = [2, 1, 0]
        self.img = img
        self.fig = Figure(facecolor=(0, 0, 0))
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        self.axes = self.fig.add_subplot(111)
        self.axes.axis('off')

    def show_2d_array(self):
        self.axes.imshow(self.img)

class ThreadDynamic(QThread):
    # 定义一个信号
    signal_change = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.img = None
        self.gauss_img = None
        self.sess = True

    def run(self):
        rotate = 0  # 旋转角度
        im = Image.fromarray(self.img)
        w, h = im.size

        while self.sess:
            rotate += 10    # 旋转角度逐渐相加
            self.gauss_img = np.array(im.rotate(rotate))    # 执行旋转操作

            time.sleep(0.1)
            self.signal_change.emit(" ")  # 发送信号

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # combobox添加item
        self.comboBox_function.addItems(['融合','相减','动态'])

        # Slider设置值
        self.horizontalSlider_mix.setMaximum(100)
        self.horizontalSlider_mix.setMinimum(0)
        self.horizontalSlider_mix.setSingleStep(1)

        self.horizontalSlider_mix.valueChanged.connect(self.mix_pro_change)
        self.horizontalSlider_mix.valueChanged.connect(self.do_fun)

        # 全局变量
        self.img_1 = None
        self.img_2 = None
        self.mix_pro = 0.0      # 融合度
        self.sub_type = 'front' # 相减选项
        self.paths = []         # 选择图像的路径

        # 添加图像
        self.pushButton_add.clicked.connect(self.add_image)
        self.pushButton_add.clicked.connect(self.load_image)
        self.pushButton_add.clicked.connect(self.show_raw_imgs)

        # 显示窗口
        self.graphicsView_im1 = QGridLayout(self.graphicsView_im1)
        self.graphicsView_im2 = QGridLayout(self.graphicsView_im2)
        self.graphicsView_mix = QGridLayout(self.graphicsView_mix)

        # 显示原始图像
        # self.show_raw_imgs()

        # 动态图像
        self.threadDynamic = ThreadDynamic()
        # self.threadDynamic.graphicsView = self.graphicsView_mix
        # self.threadDynamic.main_window = self
        self.threadDynamic.signal_change.connect(self.show_dynamic)

        # 选定执行操作
        self.pushButton_do.clicked.connect(self.do_fun)

        # 改变方法
        self.comboBox_function.currentIndexChanged.connect(self.show_raw_imgs)
        self.comboBox_function.currentIndexChanged.connect(self.change_button)

        # 设置可视
        self.radioButton_front.setVisible(False)
        self.radioButton_back.setVisible(False)

        # 选择相减时选择A-B 或B-A
        self.radioButton_front.toggled.connect(self.set_type_front)
        self.radioButton_back.toggled.connect(self.set_type_back)


    def mix_pro_change(self):
        """融合度调整"""
        self.mix_pro = self.horizontalSlider_mix.value() / 100.0

    def set_type_front(self):
        self.sub_type = 'front'

    def set_type_back(self):
        self.sub_type = 'back'

    def show_raw_imgs(self):
        """显示原始图像"""
        if self.comboBox_function.currentIndex() == 1:
            self.img_1, self.img_2 = sub_load()
            fig_1 = MyFigure(self.img_1)
            fig_1.show_2d_array()

            self.graphicsView_im1.addWidget(fig_1, 0, 1)

            fig_2 = MyFigure(self.img_2)
            fig_2.show_2d_array()

            self.graphicsView_im2.addWidget(fig_2, 0, 1)
        else:
            # self.img_1, self.img_2 = mix_load()
            fig_1 = MyFigure(self.img_1)
            fig_1.show_2d_array()

            self.graphicsView_im1.addWidget(fig_1, 0, 1)

            fig_2 = MyFigure(self.img_2)
            fig_2.show_2d_array()

            self.graphicsView_im2.addWidget(fig_2, 0, 1)


    def change_button(self):
        if self.comboBox_function.currentIndex() == 0:
            self.horizontalSlider_mix.setVisible(True)
            self.radioButton_front.setVisible(False)
            self.radioButton_back.setVisible(False)

        elif self.comboBox_function.currentIndex() == 1:
            self.horizontalSlider_mix.setVisible(False)
            self.radioButton_front.setVisible(True)
            self.radioButton_back.setVisible(True)

    def do_fun(self):
        """执行相应的操作"""

        if self.comboBox_function.currentIndex() == 0:
            self.threadDynamic.sess = False
            mix_im = mix_imgs(self.img_1,self.img_2,self.mix_pro)

            fig = MyFigure(mix_im)
            fig.show_2d_array()

            self.graphicsView_mix.addWidget(fig, 0, 1)

        elif self.comboBox_function.currentIndex() == 1:
            self.threadDynamic.sess = False
            sub_im = sub_imgs(self.img_1,self.img_2,self.sub_type)

            fig = MyFigure(sub_im)
            fig.show_2d_array()

            self.graphicsView_mix.addWidget(fig, 0, 1)
        elif self.comboBox_function.currentIndex() == 2:
            print(1)
            self.gauss_change()

    def add_image(self):
        """添加图像"""
        # print(1)
        self.paths, filetype = QFileDialog.getOpenFileNames(None,
                                                            "添加图像",
                                                            os.getcwd(),  # 起始路径
                                                            "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg)")

    def load_image(self):
        """加载图像"""
        print(self.paths)
        # print(2)
        self.img_1 = np.array(Image.open(self.paths[0]))
        if len(self.paths) == 1:
            pass
        else:
            self.img_2 = np.array(Image.open(self.paths[1]))
            # print(4)
        # self.show_raw_imgs()

    def gauss_change(self):
        self.threadDynamic.img = self.img_1
        self.threadDynamic.sess = True
        self.threadDynamic.start()

    def show_dynamic(self):
        fig = MyFigure(self.threadDynamic.gauss_img)
        fig.show_2d_array()

        self.graphicsView_mix.addWidget(fig, 0, 1)