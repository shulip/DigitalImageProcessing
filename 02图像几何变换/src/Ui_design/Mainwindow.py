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
from PIL import Image, ImageFilter

from utils.load_img import load_img
from utils.img_translation import img_translation
from utils.map import map

import os
import time
import copy

from Ui_design.Createwindow import CreateWindow
from Ui_design.Ui.painBoard.MainWidget import MainWidget as PaintBoard


class MyFigure(FigureCanvas):
    def __init__(self, img):
        # index = [2, 1, 0]
        self.img = img
        self.fig = Figure(facecolor=(222/255.0, 222/255.0, 222/255.0))
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        self.axes = self.fig.add_subplot(111)
        self.axes.axis('off')

    def show_2d_array(self):
        self.axes.imshow(self.img)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # Slider设置值
        self.horizontalSlider_angle.setMaximum(360)
        self.horizontalSlider_angle.setMinimum(-360)
        self.horizontalSlider_angle.setSingleStep(1)

        self.horizontalSlider_x.valueChanged.connect(self.scale_img)
        self.horizontalSlider_y.valueChanged.connect(self.scale_img)
        self.horizontalSlider_angle.valueChanged.connect(self.rotate_img)



        # 全局变量
        self.paper_x = 0  # 画布长
        self.paper_y = 0  # 画布宽
        self.paper = None  # 画布矩阵
        self.img = None    # 原始图像
        self.img_new = None # 更改后图像
        self.mix_pro = 0.0  # 融合度
        self.sub_type = 'front'  # 相减选项
        self.paths = []  # 选择图像的路径

        # 子窗口
        self.createPaperWindow = CreateWindow()
        self.createPaperWindow.signal_create.connect(self.create_paper)

        self.cutWindow = PaintBoard(600,600)
        self.cutWindow.signal_cut.connect(self.show_cut)

        # 按钮
        self.pushButton_createPaper.clicked.connect(self.createPaperWindow.show)

        self.pushButton_add.clicked.connect(self.add_image)  # 加载图像
        self.pushButton_add.clicked.connect(self.load_image)  # 加载图像
        self.pushButton_add.clicked.connect(self.slider_scale)

        self.pushButton_scale.clicked.connect(self.slider_scale)

        self.pushButton_horizontal.clicked.connect(self.horizontal_mirror)
        self.pushButton_vertical.clicked.connect(self.vertical_mirror)

        self.pushButton_sure.clicked.connect(self.change_raw_img)
        self.pushButton_cut.clicked.connect(self.cut_img)

        # 显示窗口
        self.graphicsView_im1 = QGridLayout(self.graphicsView_im1)

        # Spinbox改变值
        self.spinBox_x.valueChanged.connect(self.translate_img)
        self.spinBox_y.valueChanged.connect(self.translate_img)

        # 改变方法
        self.pushButton_scale.clicked.connect(self.choose_scale)
        self.pushButton_rotate.clicked.connect(self.choose_rotate)
        self.pushButton_mirror.clicked.connect(self.choose_mirror)
        self.pushButton_translation.clicked.connect(self.choose_translation)

        # 设置可视
        self.label_1.setVisible(False)
        self.label_2.setVisible(False)
        self.pushButton_sure.setVisible(False)
        self.horizontalSlider_x.setVisible(False)
        self.horizontalSlider_y.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.horizontalSlider_angle.setVisible(False)
        self.pushButton_horizontal.setVisible(False)
        self.pushButton_vertical.setVisible(False)
        self.spinBox_x.setVisible(False)
        self.spinBox_y.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)

    def choose_scale(self):
        self.label_1.setVisible(True)
        self.label_2.setVisible(True)
        self.pushButton_sure.setVisible(True)
        self.horizontalSlider_x.setVisible(True)
        self.horizontalSlider_y.setVisible(True)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.horizontalSlider_angle.setVisible(False)
        self.pushButton_horizontal.setVisible(False)
        self.pushButton_vertical.setVisible(False)
        self.spinBox_x.setVisible(False)
        self.spinBox_y.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)

    def choose_rotate(self):
        self.label_1.setVisible(False)
        self.label_2.setVisible(False)
        self.pushButton_sure.setVisible(True)
        self.horizontalSlider_x.setVisible(False)
        self.horizontalSlider_y.setVisible(False)
        self.label_3.setVisible(True)
        self.label_4.setVisible(True)
        self.horizontalSlider_angle.setVisible(True)
        self.pushButton_horizontal.setVisible(False)
        self.pushButton_vertical.setVisible(False)
        self.spinBox_x.setVisible(False)
        self.spinBox_y.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)

    def choose_mirror(self):
        self.label_1.setVisible(False)
        self.label_2.setVisible(False)
        self.pushButton_sure.setVisible(False)
        self.horizontalSlider_x.setVisible(False)
        self.horizontalSlider_y.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.horizontalSlider_angle.setVisible(False)
        self.pushButton_horizontal.setVisible(True)
        self.pushButton_vertical.setVisible(True)
        self.spinBox_x.setVisible(False)
        self.spinBox_y.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)

    def choose_translation(self):
        self.label_1.setVisible(False)
        self.label_2.setVisible(False)
        self.pushButton_sure.setVisible(False)
        self.horizontalSlider_x.setVisible(False)
        self.horizontalSlider_y.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.horizontalSlider_angle.setVisible(False)
        self.pushButton_horizontal.setVisible(False)
        self.pushButton_vertical.setVisible(False)
        self.spinBox_x.setVisible(True)
        self.spinBox_y.setVisible(True)
        self.label_5.setVisible(True)
        self.label_6.setVisible(True)

    def create_paper(self):
        """
        创建画布
        :return: None
        """
        self.paper_x = self.createPaperWindow.spinBox_x.value()
        self.paper_y = self.createPaperWindow.spinBox_y.value()

        # 创建画布数组
        self.paper = np.full((self.paper_x, self.paper_y, 3), 255)

        fig = MyFigure(self.paper)
        fig.show_2d_array()

        self.graphicsView_im1.addWidget(fig, 0, 1)

    def slider_scale(self):
        """
        改变缩放拉条
        :return:
        """
        shape = self.img.shape
        print(shape)
        self.horizontalSlider_x.setMaximum(shape[0] + 400)
        self.horizontalSlider_x.setMinimum(1)
        self.horizontalSlider_x.setSingleStep(1)
        self.horizontalSlider_x.setValue(shape[0])

        self.horizontalSlider_y.setMaximum(shape[1] + 400)
        self.horizontalSlider_y.setMinimum(1)
        self.horizontalSlider_y.setSingleStep(1)
        self.horizontalSlider_y.setValue(shape[1])

    def add_image(self):
        """添加图像"""
        # print(1)
        self.paths, filetype = QFileDialog.getOpenFileNames(None,
                                                            "添加图像",
                                                            os.getcwd(),  # 起始路径
                                                            "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg)")

    def load_image(self):
        """加载图像"""
        self.img = load_img(self.paths[0])
        self.img_new = self.img


        self.mix_paper_img(self.img)

    def mix_paper_img(self, img):
        paper_shape = self.paper.shape
        img_shape = img.shape

        mixed = copy.deepcopy(self.paper)

        if img_shape[0] <= paper_shape[0] and img_shape[1] <= paper_shape[1]:
            mixed[:img_shape[0], :img_shape[1], :] = img

        elif img_shape[0] <= paper_shape[0] and img_shape[1] > paper_shape[1]:
            mixed[:img_shape[0], :, :] = img[:, :paper_shape[1], :]

        elif img_shape[0] > paper_shape[0] and img_shape[1] <= paper_shape[1]:
            mixed[:, :img_shape[1], :] = img[:paper_shape[0], :, :]

        elif img_shape[0] > paper_shape[0] and img_shape[1] > paper_shape[1]:
            mixed[:, :, :] = img[:paper_shape[0], :paper_shape[1], :]

        fig = MyFigure(mixed)
        fig.show_2d_array()

        self.graphicsView_im1.addWidget(fig, 0, 1)


    def scale_img(self):
        """
        改变图像尺寸
        :return:
        """
        print(self.horizontalSlider_x.value(),self.horizontalSlider_y.value())
        if self.horizontalSlider_x.value() * self.horizontalSlider_y.value() >0:
            self.img_new = Image.fromarray(self.img)
            self.img_new = self.img_new.resize((self.horizontalSlider_y.value(),self.horizontalSlider_x.value()))
            self.img_new = np.array(self.img_new)

            self.mix_paper_img(self.img_new)

    def rotate_img(self):
        """
        旋转图像
        :return:
        """

        self.img_new = Image.fromarray(self.img)
        self.img_new = self.img_new.rotate(self.horizontalSlider_angle.value(),expand=True,fillcolor=(255,255,255))
        self.img_new = np.array(self.img_new)

        self.mix_paper_img(self.img_new)

    def horizontal_mirror(self):
        """
        水平镜像图像
        :return:
        """
        self.img = self.img[:, ::-1, :]
        self.mix_paper_img(self.img)

    def vertical_mirror(self):
        """
        垂直镜像图像
        :return:
        """
        self.img = self.img[::-1, :, :]
        self.mix_paper_img(self.img)

    def change_raw_img(self):
        self.img = self.img_new

    def translate_img(self):
        """
        平移图像
        :return:
        """
        img = img_translation(self.img_new,self.spinBox_x.value(),self.spinBox_y.value())

        self.mix_paper_img(img)
        self.img = img

    def cut_img(self):
        self.cutWindow = PaintBoard(self.img.shape[1],self.img.shape[0])
        self.cutWindow.signal_cut.connect(self.show_cut)

        self.cutWindow.show()

    def show_cut(self):
        mask = self.cutWindow.paintBoard.board.toImage()
        mask.save('temp.png','png')
        mask = cv2.imread('temp.png')
        mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
        os.remove('temp.png')

        mask = map(mask,0,1).reshape([mask.shape[0],mask.shape[1],1])

        self.img = self.img * mask

        self.mix_paper_img(self.img)




