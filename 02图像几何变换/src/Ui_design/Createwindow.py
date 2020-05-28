#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.Qt import QButtonGroup
from PyQt5.Qt import QListView
from PyQt5.Qt import QSplashScreen, QDateTime


import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QCoreApplication

from Ui_design.Ui.createPaper import Ui_createPaper


class CreateWindow(QWidget, Ui_createPaper):
    signal_create = pyqtSignal(str)
    def __init__(self, parent=None):
        super(CreateWindow, self).__init__(parent)
        self.setupUi(self)

        # 关闭窗口
        self.pushButton_create.clicked.connect(self.create)

    def create(self):
        self.close()
        self.signal_create.emit(" ")
