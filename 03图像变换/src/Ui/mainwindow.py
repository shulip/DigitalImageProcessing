# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 638)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svg/img_source/image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 20, 1121, 881))
        self.frame.setStyleSheet("background-color: rgb(250, 242, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_rotate = QtWidgets.QPushButton(self.frame)
        self.pushButton_rotate.setGeometry(QtCore.QRect(20, 130, 61, 28))
        self.pushButton_rotate.setStyleSheet("font: 10pt \"黑体\";\n"
"\n"
"border-radius: 10px;\n"
"background-color: rgb(228, 179, 99);\n"
"color: rgb(95, 51, 98);\n"
"color: rgb(49, 54, 56);")
        self.pushButton_rotate.setObjectName("pushButton_rotate")
        self.pushButton_translation = QtWidgets.QPushButton(self.frame)
        self.pushButton_translation.setGeometry(QtCore.QRect(20, 170, 61, 28))
        self.pushButton_translation.setStyleSheet("font: 10pt \"黑体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(228, 179, 99);\n"
"color: rgb(49, 54, 56);")
        self.pushButton_translation.setObjectName("pushButton_translation")
        self.pushButton_match = QtWidgets.QPushButton(self.frame)
        self.pushButton_match.setGeometry(QtCore.QRect(20, 210, 61, 28))
        self.pushButton_match.setStyleSheet("font: 10pt \"黑体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(228, 179, 99);\n"
"color: rgb(49, 54, 56);")
        self.pushButton_match.setObjectName("pushButton_match")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, -50, 1101, 111))
        self.frame_4.setStyleSheet("background-color: rgb(244, 227, 227);\n"
"background-color: rgb(244, 215, 215);\n"
"background-color: rgb(250, 245, 245);\n"
"border-radius:35px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalSlider_angle = QtWidgets.QSlider(self.frame_4)
        self.horizontalSlider_angle.setGeometry(QtCore.QRect(90, 70, 951, 21))
        self.horizontalSlider_angle.setStyleSheet("QSlider::groove:horizontal{ height: 10px; \n"
"                            left: 10px; \n"
"                            right: 10px; \n"
"                            background: #dcdcdc; \n"
"}\n"
"\n"
"QSlider::handle:horizontal{ \n"
"                             radius: 7px;\n"
"                             border-radius: 7px; \n"
"                             border: 3px solid rgb(255, 255, 255);\n"
"                             width:  9px; \n"
"                             margin: -5px -3px; \n"
"                             background: rgb(255, 183, 120); \n"
"} \n"
"\n"
"QSlider::sub-page:horizontalSlider:disabled {\n"
"\n"
"                             background: #6c6c6c; \n"
"                             border-color: #999;\n"
"                             border-radius: 2px;\n"
"} \n"
"\n"
"QSlider::add-page:horizontalSlider:disabled {\n"
" \n"
"                             background: #ffffff;\n"
"                             border-color: #999;\n"
"                             border-radius: 2px;\n"
"}")
        self.horizontalSlider_angle.setMaximum(1)
        self.horizontalSlider_angle.setSingleStep(1)
        self.horizontalSlider_angle.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_angle.setObjectName("horizontalSlider_angle")
        self.label_function = QtWidgets.QLabel(self.frame_4)
        self.label_function.setGeometry(QtCore.QRect(20, 60, 61, 41))
        self.label_function.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(49, 54, 56);")
        self.label_function.setObjectName("label_function")
        self.horizontalSlider_x = QtWidgets.QSlider(self.frame_4)
        self.horizontalSlider_x.setGeometry(QtCore.QRect(140, 70, 381, 21))
        self.horizontalSlider_x.setStyleSheet("QSlider::groove:horizontal{ height: 10px; \n"
"                            left: 10px; \n"
"                            right: 10px; \n"
"                            background: #dcdcdc; \n"
"}\n"
"\n"
"QSlider::handle:horizontal{ \n"
"                             radius: 7px;\n"
"                             border-radius: 7px; \n"
"                             border: 3px solid rgb(255, 255, 255);\n"
"                             width:  9px; \n"
"                             margin: -5px -3px; \n"
"                             background: rgb(255, 183, 120); \n"
"} \n"
"\n"
"QSlider::sub-page:horizontalSlider:disabled {\n"
"\n"
"                             background: #6c6c6c; \n"
"                             border-color: #999;\n"
"                             border-radius: 2px;\n"
"} \n"
"\n"
"QSlider::add-page:horizontalSlider:disabled {\n"
" \n"
"                             background: #ffffff;\n"
"                             border-color: #999;\n"
"                             border-radius: 2px;\n"
"}")
        self.horizontalSlider_x.setMaximum(1)
        self.horizontalSlider_x.setSingleStep(1)
        self.horizontalSlider_x.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_x.setObjectName("horizontalSlider_x")
        self.horizontalSlider_y = QtWidgets.QSlider(self.frame_4)
        self.horizontalSlider_y.setGeometry(QtCore.QRect(640, 70, 381, 21))
        self.horizontalSlider_y.setStyleSheet("QSlider::groove:horizontal{ height: 10px; \n"
"                            left: 10px; \n"
"                            right: 10px; \n"
"                            background: #dcdcdc; \n"
"}\n"
"\n"
"QSlider::handle:horizontal{ \n"
"                             radius: 7px;\n"
"                             border-radius: 7px; \n"
"                             border: 3px solid rgb(255, 255, 255);\n"
"                             width:  9px; \n"
"                             margin: -5px -3px; \n"
"                             background: rgb(255, 183, 120); \n"
"} \n"
"\n"
"QSlider::sub-page:horizontalSlider:disabled {\n"
"\n"
"                             background: #6c6c6c; \n"
"                             border-color: #999;\n"
"                             border-radius: 2px;\n"
"} \n"
"\n"
"QSlider::add-page:horizontalSlider:disabled {\n"
" \n"
"                             background: #ffffff;\n"
"                             border-color: #999;\n"
"                             border-radius: 2px;\n"
"}")
        self.horizontalSlider_y.setMaximum(1)
        self.horizontalSlider_y.setSingleStep(1)
        self.horizontalSlider_y.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_y.setObjectName("horizontalSlider_y")
        self.pushButton_match_run = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_match_run.setGeometry(QtCore.QRect(90, 70, 61, 28))
        self.pushButton_match_run.setStyleSheet("font: 10pt \"黑体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(228, 179, 99);\n"
"color: rgb(49, 54, 56);")
        self.pushButton_match_run.setObjectName("pushButton_match_run")
        self.label_function.raise_()
        self.horizontalSlider_angle.raise_()
        self.horizontalSlider_x.raise_()
        self.horizontalSlider_y.raise_()
        self.pushButton_match_run.raise_()
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(80, 90, 481, 491))
        self.frame_5.setStyleSheet("background-color: rgb(244, 227, 227);\n"
"background-color: rgb(239 ,100 ,97);\n"
"border-radius:15px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_kong = QtWidgets.QLabel(self.frame_5)
        self.label_kong.setGeometry(QtCore.QRect(40, 0, 81, 31))
        self.label_kong.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(49, 54, 56);")
        self.label_kong.setObjectName("label_kong")
        self.graphicsView_space = QtWidgets.QGraphicsView(self.frame_5)
        self.graphicsView_space.setGeometry(QtCore.QRect(0, 30, 481, 461))
        self.graphicsView_space.setStyleSheet("\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"background-color: rgb(223, 218, 218);\n"
"background-color: rgb(232, 233, 235);\n"
"\n"
"")
        self.graphicsView_space.setObjectName("graphicsView_space")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(590, 90, 481, 491))
        self.frame_6.setStyleSheet("background-color: rgb(244, 227, 227);\n"
"background-color: rgb(239 ,100 ,97);\n"
"border-radius:15px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_pin = QtWidgets.QLabel(self.frame_6)
        self.label_pin.setGeometry(QtCore.QRect(40, 0, 81, 31))
        self.label_pin.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(49, 54, 56);")
        self.label_pin.setObjectName("label_pin")
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setGeometry(QtCore.QRect(330, 10, 121, 21))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    \n"
"    font: 9pt \"黑体\";\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 0px solid gray;\n"
"    border-radius: 10px;\n"
"    \n"
"    color: #494949;\n"
"    padding: 0px 5px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; \n"
"    border-right-width: 8px;\n"
"    border-right-color: #e8e8e8;\n"
"    border-right-style: solid;\n"
"    border-top-right-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    font: 9pt \"黑体\";\n"
"    color: #494949;\n"
"}\n"
"\n"
"\n"
"QListView::item {\n"
"    background: #e8e8e8;\n"
"}\n"
" \n"
"QListView::item:hover {\n"
"    background: #bebebe;\n"
"    font: 8pt \"Consolas\";\n"
"    color: #494949;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected\n"
"{    \n"
"    background-color: #bebebe;\n"
"\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.graphicsView_frequency = QtWidgets.QGraphicsView(self.frame_6)
        self.graphicsView_frequency.setGeometry(QtCore.QRect(0, 30, 481, 461))
        self.graphicsView_frequency.setStyleSheet("\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"background-color: rgb(223, 218, 218);\n"
"background-color: rgb(232, 233, 235);\n"
"\n"
"")
        self.graphicsView_frequency.setObjectName("graphicsView_frequency")
        self.comboBox_match = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_match.setGeometry(QtCore.QRect(270, 10, 121, 21))
        self.comboBox_match.setStyleSheet("QComboBox {\n"
"    \n"
"    font: 9pt \"黑体\";\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 0px solid gray;\n"
"    border-radius: 10px;\n"
"    \n"
"    color: #494949;\n"
"    padding: 0px 5px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; \n"
"    border-right-width: 8px;\n"
"    border-right-color: #e8e8e8;\n"
"    border-right-style: solid;\n"
"    border-top-right-radius: 20px; \n"
"    border-bottom-right-radius: 20px;\n"
"    font: 9pt \"黑体\";\n"
"    color: #494949;\n"
"}\n"
"\n"
"\n"
"QListView::item {\n"
"    background: #e8e8e8;\n"
"}\n"
" \n"
"QListView::item:hover {\n"
"    background: #bebebe;\n"
"    font: 8pt \"Consolas\";\n"
"    color: #494949;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected\n"
"{    \n"
"    background-color: #bebebe;\n"
"\n"
"}")
        self.comboBox_match.setObjectName("comboBox_match")
        self.comboBox_match.addItem("")
        self.comboBox_match.addItem("")
        self.comboBox_match.addItem("")
        self.comboBox_match.addItem("")
        self.frame_match = QtWidgets.QFrame(self.centralwidget)
        self.frame_match.setGeometry(QtCore.QRect(450, 180, 271, 291))
        self.frame_match.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_match.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_match.setObjectName("frame_match")
        self.graphicsView_match = QtWidgets.QGraphicsView(self.frame_match)
        self.graphicsView_match.setGeometry(QtCore.QRect(20, 40, 211, 231))
        self.graphicsView_match.setStyleSheet("\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"background-color: rgb(250, 242, 240);\n"
"")
        self.graphicsView_match.setObjectName("graphicsView_match")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像处理"))
        self.pushButton_rotate.setText(_translate("MainWindow", "旋转"))
        self.pushButton_translation.setText(_translate("MainWindow", "平移"))
        self.pushButton_match.setText(_translate("MainWindow", "模板匹配"))
        self.label_function.setText(_translate("MainWindow", "旋转"))
        self.pushButton_match_run.setText(_translate("MainWindow", "执行"))
        self.label_kong.setText(_translate("MainWindow", "空域"))
        self.label_pin.setText(_translate("MainWindow", "频域"))
        self.comboBox.setItemText(0, _translate("MainWindow", "傅里叶变换"))
        self.comboBox.setItemText(1, _translate("MainWindow", "离散余弦变换"))
        self.comboBox_match.setItemText(0, _translate("MainWindow", "书上"))
        self.comboBox_match.setItemText(1, _translate("MainWindow", "平方差匹配"))
        self.comboBox_match.setItemText(2, _translate("MainWindow", "相关匹配"))
        self.comboBox_match.setItemText(3, _translate("MainWindow", "相关系数匹配"))
        self.actionopen.setText(_translate("MainWindow", "open"))

from .source import *
