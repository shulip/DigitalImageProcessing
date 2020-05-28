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
import multiprocessing
import matplotlib

from Mainwindow import MainWindow
import sys

matplotlib.use("Qt5Agg")  # 声明使用QT5

if __name__ == '__main__':
    # 解决多线程无限自启问题
    multiprocessing.freeze_support()
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = MainWindow()

    MainWindow.show()
    MainWindow.move(int((QApplication.desktop().width() - MainWindow.width()) / 2),
                    int((QApplication.desktop().height() - MainWindow.height()) / 2 - 50))
    sys.exit(app.exec_())
