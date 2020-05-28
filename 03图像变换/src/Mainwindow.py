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
from Ui.mainwindow import Ui_MainWindow

import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import cv2
import numpy as np
from PIL import Image, ImageFilter

import os
import time
import copy
from utils.fourier_transform import fourier_transform
from utils.dct import dct
from utils.template_match_with_fourier import template_match_with_fourier


class MyFigure(FigureCanvas):
    def __init__(self, img,R=232,G=233,B=235):
        # index = [2, 1, 0]
        self.img = img
        self.fig = Figure(facecolor=(R/255.0, G/255.0, B/255.0))
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        self.axes = self.fig.add_subplot(111)
        self.axes.axis('off')

    def show_2d_array(self):
        self.axes.imshow(self.img,cmap='gray')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #
        # Slider设置值
        self.horizontalSlider_angle.setMaximum(360)
        self.horizontalSlider_angle.setMinimum(-360)
        self.horizontalSlider_angle.setSingleStep(1)
        self.horizontalSlider_angle.setValue(0)
        self.horizontalSlider_x.setMaximum(100)
        self.horizontalSlider_x.setMinimum(-100)
        self.horizontalSlider_x.setSingleStep(1)
        self.horizontalSlider_x.setValue(0)
        self.horizontalSlider_y.setMaximum(100)
        self.horizontalSlider_y.setMinimum(-100)
        self.horizontalSlider_y.setSingleStep(1)
        self.horizontalSlider_y.setValue(0)
        #
        #     self.horizontalSlider_x.valueChanged.connect(self.scale_img)
        #     self.horizontalSlider_y.valueChanged.connect(self.scale_img)
        #     self.horizontalSlider_angle.valueChanged.connect(self.rotate_img)

        # 实例化主窗口的QMenuBar对象
        self.file = self.menubar.addMenu("文件")
        self.openFile = QAction("打开", self)
        self.file.addAction(self.openFile)
        self.openFile.triggered.connect(self.add_image)

        self.position = self.menubar.addMenu("匹配定位")
        self.loadRaw = QAction("打开原图像", self)
        self.loadFeature = QAction("打开匹配图", self)
        self.position.addAction(self.loadRaw)
        self.position.addAction(self.loadFeature)
        self.loadRaw.triggered.connect(self.add_raw_image)
        self.loadFeature.triggered.connect(self.add_feature_image)


        # 全局变量
        self.raw_img = None         # 原始图像
        self.img = None             # 空域图像
        self.frequency_img = None   # 频域图像
        self.feature_img = None     # 匹配图像

        # 按钮
        self.pushButton_match_run.clicked.connect(self.run_match)

        # 拉条
        self.horizontalSlider_angle.valueChanged.connect(self.img_change_by_angle)
        self.horizontalSlider_x.valueChanged.connect(self.img_change_by_coordinate)
        self.horizontalSlider_y.valueChanged.connect(self.img_change_by_coordinate)

        # 显示窗口
        self.graphicsView_space = QGridLayout(self.graphicsView_space)
        self.graphicsView_frequency = QGridLayout(self.graphicsView_frequency)
        self.graphicsView_match = QGridLayout(self.graphicsView_match)

        # 改变方法
        self.pushButton_translation.clicked.connect(self.choose_translation)
        self.pushButton_rotate.clicked.connect(self.choose_rotate)
        self.pushButton_match.clicked.connect(self.choose_match)
        self.comboBox.currentIndexChanged.connect(self.change_frequency)

        # 设置不可视
        self.label_function.setVisible(False)
        self.horizontalSlider_x.setVisible(False)
        self.horizontalSlider_y.setVisible(False)
        self.horizontalSlider_angle.setVisible(False)
        self.frame_match.setVisible(False)
        self.pushButton_match_run.setVisible(False)
        self.comboBox_match.setVisible(False)
        self.add_shadow()

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(16)
        shadow.setColor(QColor(0, 0, 0, 500))
        shadow.setOffset(1, 1)
        self.frame_4.setGraphicsEffect(shadow)

        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(16)
        shadow1.setColor(QColor(0, 0, 0, 500))
        shadow1.setOffset(1, 1)
        self.frame_5.setGraphicsEffect(shadow1)

        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(16)
        shadow2.setColor(QColor(110, 110, 110, 500))
        shadow2.setOffset(1, 1)
        self.frame_6.setGraphicsEffect(shadow2)


    def choose_translation(self):
        self.label_function.setVisible(True)
        self.comboBox.setVisible(True)
        self.comboBox_match.setVisible(False)
        self.label_pin.setText("频域")
        self.label_function.setText("平移")
        self.horizontalSlider_x.setVisible(True)
        self.horizontalSlider_y.setVisible(True)
        self.horizontalSlider_angle.setVisible(False)
        self.frame_match.setVisible(False)
        self.pushButton_match_run.setVisible(False)

        if self.raw_img is not None:
            self.horizontalSlider_x.setMaximum(self.raw_img.shape[0])
            self.horizontalSlider_x.setMinimum(-self.raw_img.shape[0])
            self.horizontalSlider_x.setSingleStep(1)
            self.horizontalSlider_x.setValue(0)
            self.horizontalSlider_y.setMaximum(self.raw_img.shape[1])
            self.horizontalSlider_y.setMinimum(-self.raw_img.shape[1])
            self.horizontalSlider_y.setSingleStep(1)
            self.horizontalSlider_y.setValue(0)

    def choose_rotate(self):
        self.label_function.setVisible(True)
        self.comboBox.setVisible(True)
        self.comboBox_match.setVisible(False)
        self.label_pin.setText("频域")
        self.label_function.setText("旋转")
        self.horizontalSlider_x.setVisible(False)
        self.horizontalSlider_y.setVisible(False)
        self.horizontalSlider_angle.setVisible(True)
        self.frame_match.setVisible(False)
        self.pushButton_match_run.setVisible(False)

    def choose_match(self):
        self.label_function.setVisible(False)
        self.comboBox.setVisible(False)
        self.comboBox_match.setVisible(True)
        self.label_pin.setText("匹配")
        self.horizontalSlider_x.setVisible(False)
        self.horizontalSlider_y.setVisible(False)
        self.horizontalSlider_angle.setVisible(False)
        self.frame_match.setVisible(True)
        self.pushButton_match_run.setVisible(True)

    def show_space(self):
        fig = MyFigure(self.img)
        fig.show_2d_array()

        self.graphicsView_space.addWidget(fig, 0, 1)

    def show_frequency(self):
        fig = MyFigure(self.frequency_img)
        fig.show_2d_array()

        self.graphicsView_frequency.addWidget(fig, 0, 1)

    def show_feature(self):
        fig = MyFigure(self.feature_img,250,242,240)
        fig.show_2d_array()

        self.graphicsView_match.addWidget(fig, 0, 1)

    def update_frequency(self):
        if self.comboBox.currentIndex()==0:
            self.frequency_img = fourier_transform(self.img)
        elif self.comboBox.currentIndex()==1:
            self.frequency_img = dct(self.img)

    def add_image(self):
        """添加图像"""
        self.paths, filetype = QFileDialog.getOpenFileNames(None,
                                                            "添加图像",
                                                            os.getcwd(),  # 起始路径
                                                            "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg)")
        self.img = np.array(Image.open(self.paths[0]).convert("L"))
        self.raw_img = self.img

        self.show_space()
        self.update_frequency()
        self.show_frequency()

    def add_raw_image(self):
        """添加原图像"""
        self.paths, filetype = QFileDialog.getOpenFileNames(None,
                                                            "添加原图像",
                                                            os.getcwd(),  # 起始路径
                                                            "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg)")
        self.img = np.array(Image.open(self.paths[0]).convert("L"))

        self.show_space()

    def add_feature_image(self):
        """添加匹配图像"""
        self.paths, filetype = QFileDialog.getOpenFileNames(None,
                                                            "添加匹配图",
                                                            os.getcwd(),  # 起始路径
                                                            "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg)")
        self.feature_img = np.array(Image.open(self.paths[0]).convert("L"))

        self.show_feature()

    def change_frequency(self):
        self.update_frequency()
        self.show_frequency()

    def img_change_by_angle(self):
        self.img = Image.fromarray(self.raw_img).rotate(self.horizontalSlider_angle.value())
        self.img = np.array(self.img)
        self.show_space()
        self.update_frequency()
        self.show_frequency()

    def img_change_by_coordinate(self):
        x = self.horizontalSlider_x.value()
        y = self.horizontalSlider_y.value()
        print(self.raw_img[x:,:].shape,self.raw_img[:x,:].shape)

        self.img = np.vstack([self.img[x:,:],self.img[:x,:]])
        print(self.img.shape)
        self.img = np.hstack([self.img[:, y:], self.img[:, :y]])
        self.show_space()
        self.update_frequency()
        self.show_frequency()

    def run_match(self):
        import copy
        if self.comboBox_match.currentIndex()==0:
            self.frequency_img = template_match_with_fourier(self.img,self.feature_img)
        elif self.comboBox_match.currentIndex()==1:
            self.frequency_img = cv2.matchTemplate(self.img,self.feature_img, cv2.TM_CCOEFF)
        elif self.comboBox_match.currentIndex()==2:
            self.frequency_img = cv2.matchTemplate(self.img,self.feature_img, cv2.TM_CCORR)
        elif self.comboBox_match.currentIndex()==3:
            self.frequency_img = cv2.matchTemplate(self.img,self.feature_img, cv2.TM_CCOEFF)

        # 相关系数匹配方法：cv2.TM_CCOEFF
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(self.frequency_img)
        h, w = self.feature_img.shape[:2]

        self.frequency_img = copy.deepcopy(self.img)
        left_top = max_loc  # 左上角
        right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
        cv2.rectangle(self.frequency_img, left_top, right_bottom, 255, 2)  # 画出矩形位置

        self.show_frequency()

