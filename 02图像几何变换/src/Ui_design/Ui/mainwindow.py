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
        MainWindow.resize(940, 720)
        MainWindow.setMinimumSize(QtCore.QSize(940, 720))
        MainWindow.setMaximumSize(QtCore.QSize(940, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_im1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_im1.setGeometry(QtCore.QRect(110, 80, 801, 581))
        self.graphicsView_im1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"background-color: rgb(222, 222, 222);\n"
"")
        self.graphicsView_im1.setObjectName("graphicsView_im1")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(220, 10, 93, 28))
        self.pushButton_add.setStyleSheet("font: 10pt \"黑体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(10, 189, 241);\n"
"background-color: rgb(255, 183, 120);\n"
"\n"
"")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_createPaper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_createPaper.setGeometry(QtCore.QRect(120, 10, 93, 28))
        self.pushButton_createPaper.setStyleSheet("border-radius: 10px;\n"
"font: 10pt \"黑体\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_createPaper.setObjectName("pushButton_createPaper")
        self.pushButton_scale = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_scale.setGeometry(QtCore.QRect(20, 90, 61, 28))
        self.pushButton_scale.setStyleSheet("font: 10pt \"黑体\";\n"
"\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_scale.setObjectName("pushButton_scale")
        self.pushButton_rotate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rotate.setGeometry(QtCore.QRect(20, 140, 61, 28))
        self.pushButton_rotate.setStyleSheet("font: 10pt \"黑体\";\n"
"\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_rotate.setObjectName("pushButton_rotate")
        self.pushButton_mirror = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mirror.setGeometry(QtCore.QRect(20, 190, 61, 28))
        self.pushButton_mirror.setStyleSheet("font: 10pt \"黑体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_mirror.setObjectName("pushButton_mirror")
        self.horizontalSlider_x = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_x.setGeometry(QtCore.QRect(90, 50, 351, 21))
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
        self.horizontalSlider_y = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_y.setGeometry(QtCore.QRect(490, 50, 371, 21))
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
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 50, 41, 16))
        self.label_1.setStyleSheet("font: 10pt \"黑体\";")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 50, 71, 20))
        self.label_2.setStyleSheet("font: 10pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalSlider_angle = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_angle.setGeometry(QtCore.QRect(100, 50, 721, 21))
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
        self.pushButton_horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_horizontal.setGeometry(QtCore.QRect(680, 50, 93, 28))
        self.pushButton_horizontal.setStyleSheet("border-radius: 10px;\n"
"font: 10pt \"黑体\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_horizontal.setObjectName("pushButton_horizontal")
        self.pushButton_vertical = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vertical.setGeometry(QtCore.QRect(810, 50, 93, 28))
        self.pushButton_vertical.setStyleSheet("border-radius: 10px;\n"
"font: 10pt \"黑体\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_vertical.setObjectName("pushButton_vertical")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 50, 61, 16))
        self.label_3.setStyleSheet("font: 10pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(830, 50, 141, 20))
        self.label_4.setStyleSheet("font: 10pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_sure = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sure.setGeometry(QtCore.QRect(870, 50, 51, 21))
        self.pushButton_sure.setStyleSheet("border-radius: 10px;\n"
"font: 10pt \"黑体\";\n"
"background-color: rgb(255, 183, 120);\n"
"")
        self.pushButton_sure.setObjectName("pushButton_sure")
        self.pushButton_translation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_translation.setGeometry(QtCore.QRect(20, 240, 61, 28))
        self.pushButton_translation.setStyleSheet("font: 10pt \"黑体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_translation.setObjectName("pushButton_translation")
        self.spinBox_x = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_x.setGeometry(QtCore.QRect(660, 50, 101, 21))
        self.spinBox_x.setStyleSheet("border-radius: 10px;")
        self.spinBox_x.setMinimum(-2000)
        self.spinBox_x.setMaximum(2000)
        self.spinBox_x.setSingleStep(10)
        self.spinBox_x.setProperty("value", 0)
        self.spinBox_x.setObjectName("spinBox_x")
        self.spinBox_y = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_y.setGeometry(QtCore.QRect(800, 50, 101, 21))
        self.spinBox_y.setStyleSheet("border-radius: 10px;")
        self.spinBox_y.setMinimum(-2000)
        self.spinBox_y.setMaximum(2000)
        self.spinBox_y.setSingleStep(10)
        self.spinBox_y.setProperty("value", 0)
        self.spinBox_y.setObjectName("spinBox_y")
        self.pushButton_cut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cut.setGeometry(QtCore.QRect(20, 290, 61, 28))
        self.pushButton_cut.setStyleSheet("font: 10pt \"黑体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_cut.setObjectName("pushButton_cut")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-30, 80, 141, 661))
        self.frame.setStyleSheet("background-color: rgb(244, 236, 234);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 50, 61, 16))
        self.label_5.setStyleSheet("font: 10pt \"黑体\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(780, 50, 61, 16))
        self.label_6.setStyleSheet("font: 10pt \"黑体\";")
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(110, 80, 861, 661))
        self.frame_2.setStyleSheet("background-color: rgb(245, 234, 228);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(-60, 0, 1011, 80))
        self.frame_4.setStyleSheet("background-color: rgb(244, 227, 227);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.graphicsView_im1.raise_()
        self.pushButton_add.raise_()
        self.pushButton_createPaper.raise_()
        self.pushButton_scale.raise_()
        self.pushButton_rotate.raise_()
        self.pushButton_mirror.raise_()
        self.horizontalSlider_x.raise_()
        self.horizontalSlider_y.raise_()
        self.label_1.raise_()
        self.label_2.raise_()
        self.horizontalSlider_angle.raise_()
        self.pushButton_horizontal.raise_()
        self.pushButton_vertical.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_sure.raise_()
        self.pushButton_translation.raise_()
        self.spinBox_x.raise_()
        self.spinBox_y.raise_()
        self.pushButton_cut.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImageProcessing"))
        self.pushButton_add.setText(_translate("MainWindow", "添加图像"))
        self.pushButton_createPaper.setText(_translate("MainWindow", "创建画布"))
        self.pushButton_scale.setText(_translate("MainWindow", "缩放"))
        self.pushButton_rotate.setText(_translate("MainWindow", "旋转"))
        self.pushButton_mirror.setText(_translate("MainWindow", "镜像"))
        self.label_1.setText(_translate("MainWindow", "X:"))
        self.label_2.setText(_translate("MainWindow", "Y:"))
        self.pushButton_horizontal.setText(_translate("MainWindow", "水平镜像"))
        self.pushButton_vertical.setText(_translate("MainWindow", "垂直镜像"))
        self.label_3.setText(_translate("MainWindow", "-360"))
        self.label_4.setText(_translate("MainWindow", "360"))
        self.pushButton_sure.setText(_translate("MainWindow", "确认"))
        self.pushButton_translation.setText(_translate("MainWindow", "平移"))
        self.pushButton_cut.setText(_translate("MainWindow", "切割"))
        self.label_5.setText(_translate("MainWindow", "x:"))
        self.label_6.setText(_translate("MainWindow", "y:"))

