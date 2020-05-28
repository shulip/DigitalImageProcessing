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
        MainWindow.resize(1200, 765)
        MainWindow.setMinimumSize(QtCore.QSize(940, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1500, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/SVG/img/smile.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 40, 1211, 711))
        self.frame.setStyleSheet("background-color: rgb(250, 242, 240);\n"
"background-color: rgb(232, 233, 235);\n"
"background-color: rgb(250, 245, 245);\n"
"background-color: rgb(232, 231, 223);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_image = QtWidgets.QFrame(self.frame)
        self.frame_image.setGeometry(QtCore.QRect(70, 70, 501, 501))
        self.frame_image.setStyleSheet("background-color: rgb(239 ,100 ,97);\n"
"border-radius:15px;")
        self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.label_camera = QtWidgets.QLabel(self.frame_image)
        self.label_camera.setGeometry(QtCore.QRect(40, 10, 81, 31))
        self.label_camera.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(49, 54, 56);")
        self.label_camera.setObjectName("label_camera")
        self.graphicsView_image = QtWidgets.QGraphicsView(self.frame_image)
        self.graphicsView_image.setGeometry(QtCore.QRect(0, 40, 501, 461))
        self.graphicsView_image.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"background-color: rgb(227, 222, 222);\n"
"background-color: rgb(224, 223, 213);\n"
"background-color: rgb(232, 233, 235);\n"
"\n"
"\n"
"")
        self.graphicsView_image.setObjectName("graphicsView_image")
        self.frame_curve = QtWidgets.QFrame(self.frame)
        self.frame_curve.setGeometry(QtCore.QRect(610, 70, 521, 501))
        self.frame_curve.setStyleSheet("background-color: rgb(239 ,100 ,97);\n"
"border-radius:15px;")
        self.frame_curve.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_curve.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_curve.setObjectName("frame_curve")
        self.label_detect = QtWidgets.QLabel(self.frame_curve)
        self.label_detect.setGeometry(QtCore.QRect(40, 10, 121, 31))
        self.label_detect.setStyleSheet("font: 11pt \"黑体\";\n"
"color: rgb(49, 54, 56);")
        self.label_detect.setObjectName("label_detect")
        self.graphicsView_curve = QtWidgets.QGraphicsView(self.frame_curve)
        self.graphicsView_curve.setGeometry(QtCore.QRect(0, 40, 521, 461))
        self.graphicsView_curve.setStyleSheet("background-color: rgb(227, 222, 222);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"background-color: rgb(224, 223, 213);\n"
"background-color: rgb(232, 233, 235);\n"
"\n"
"")
        self.graphicsView_curve.setObjectName("graphicsView_curve")
        self.frame_down = QtWidgets.QFrame(self.frame)
        self.frame_down.setGeometry(QtCore.QRect(0, 600, 1211, 121))
        self.frame_down.setStyleSheet("\n"
"background-color: rgb(244, 215, 215);\n"
"background-color: rgb(239, 151, 96);\n"
"background-color: rgb(239, 163, 115);\n"
"background-color: rgb(224, 223, 213);\n"
"background-color: rgb(229, 230, 230);\n"
"background-color: rgb(224, 223, 213);\n"
"background-color: rgb(250, 245, 245);\n"
"border-radius:35px;")
        self.frame_down.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_down.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_down.setObjectName("frame_down")
        self.horizontalSlider_a = QtWidgets.QSlider(self.frame_down)
        self.horizontalSlider_a.setGeometry(QtCore.QRect(90, 30, 481, 21))
        self.horizontalSlider_a.setStyleSheet("QSlider::groove:horizontal{ height: 10px; \n"
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
        self.horizontalSlider_a.setMaximum(1)
        self.horizontalSlider_a.setSingleStep(1)
        self.horizontalSlider_a.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_a.setObjectName("horizontalSlider_a")
        self.horizontalSlider_b = QtWidgets.QSlider(self.frame_down)
        self.horizontalSlider_b.setGeometry(QtCore.QRect(640, 30, 491, 21))
        self.horizontalSlider_b.setStyleSheet("QSlider::groove:horizontal{ height: 10px; \n"
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
        self.horizontalSlider_b.setMaximum(1)
        self.horizontalSlider_b.setSingleStep(1)
        self.horizontalSlider_b.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_b.setObjectName("horizontalSlider_b")
        self.label_a = QtWidgets.QLabel(self.frame_down)
        self.label_a.setGeometry(QtCore.QRect(40, 20, 101, 41))
        self.label_a.setStyleSheet("font: 19pt \"黑体\";\n"
"color: rgb(49, 54, 56);")
        self.label_a.setObjectName("label_a")
        self.label_b = QtWidgets.QLabel(self.frame_down)
        self.label_b.setGeometry(QtCore.QRect(600, 20, 101, 41))
        self.label_b.setStyleSheet("font: 19pt \"黑体\";\n"
"color: rgb(49, 54, 56);")
        self.label_b.setObjectName("label_b")
        self.horizontalSlider_gamma = QtWidgets.QSlider(self.frame_down)
        self.horizontalSlider_gamma.setGeometry(QtCore.QRect(140, 30, 941, 21))
        self.horizontalSlider_gamma.setStyleSheet("QSlider::groove:horizontal{ height: 10px; \n"
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
        self.horizontalSlider_gamma.setMaximum(1)
        self.horizontalSlider_gamma.setSingleStep(1)
        self.horizontalSlider_gamma.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_gamma.setObjectName("horizontalSlider_gamma")
        self.label_gamma = QtWidgets.QLabel(self.frame_down)
        self.label_gamma.setGeometry(QtCore.QRect(30, 20, 101, 41))
        self.label_gamma.setStyleSheet("font: 19pt \"黑体\";\n"
"color: rgb(49, 54, 56);")
        self.label_gamma.setObjectName("label_gamma")
        self.label_a.raise_()
        self.horizontalSlider_a.raise_()
        self.label_b.raise_()
        self.horizontalSlider_b.raise_()
        self.horizontalSlider_gamma.raise_()
        self.label_gamma.raise_()
        self.frame_top1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_top1.setGeometry(QtCore.QRect(-10, -50, 1211, 121))
        self.frame_top1.setStyleSheet("\n"
"background-color: rgb(244, 215, 215);\n"
"background-color: rgb(239, 151, 96);\n"
"background-color: rgb(239, 163, 115);\n"
"background-color: rgb(224, 223, 213);\n"
"background-color: rgb(229, 230, 230);\n"
"background-color: rgb(224, 223, 213);\n"
"background-color: rgb(250, 245, 245);\n"
"border-radius:35px;")
        self.frame_top1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top1.setObjectName("frame_top1")
        self.pushButton_line = QtWidgets.QPushButton(self.frame_top1)
        self.pushButton_line.setGeometry(QtCore.QRect(50, 60, 90, 45))
        self.pushButton_line.setStyleSheet("font: 12pt \"黑体\";\n"
"border-radius: 20px;\n"
"background-color: rgb(254, 180, 160);\n"
"background-color: rgb(239 ,100 ,97);\n"
"background-color: rgb(228, 179, 99);\n"
"color: rgb(49, 54, 56);")
        self.pushButton_line.setObjectName("pushButton_line")
        self.pushButton_broken = QtWidgets.QPushButton(self.frame_top1)
        self.pushButton_broken.setGeometry(QtCore.QRect(180, 60, 90, 45))
        self.pushButton_broken.setStyleSheet("font: 12pt \"黑体\";\n"
"border-radius: 20px;\n"
"background-color: rgb(254, 180, 160);\n"
"background-color: rgb(239 ,100 ,97);\n"
"background-color: rgb(228, 179, 99);\n"
"color: rgb(49, 54, 56);")
        self.pushButton_broken.setObjectName("pushButton_broken")
        self.pushButton_curve = QtWidgets.QPushButton(self.frame_top1)
        self.pushButton_curve.setGeometry(QtCore.QRect(300, 60, 90, 45))
        self.pushButton_curve.setStyleSheet("font: 12pt \"黑体\";\n"
"border-radius: 20px;\n"
"background-color: rgb(254, 180, 160);\n"
"background-color: rgb(239 ,100 ,97);\n"
"background-color: rgb(228, 179, 99);\n"
"color: rgb(49, 54, 56);")
        self.pushButton_curve.setObjectName("pushButton_curve")
        self.pushButton_histeq = QtWidgets.QPushButton(self.frame_top1)
        self.pushButton_histeq.setGeometry(QtCore.QRect(430, 60, 141, 45))
        self.pushButton_histeq.setStyleSheet("font: 12pt \"黑体\";\n"
"border-radius: 20px;\n"
"background-color: rgb(254, 180, 160);\n"
"background-color: rgb(239 ,100 ,97);\n"
"background-color: rgb(228, 179, 99);\n"
"color: rgb(49, 54, 56);")
        self.pushButton_histeq.setObjectName("pushButton_histeq")
        self.pushButton_gamma = QtWidgets.QPushButton(self.frame_top1)
        self.pushButton_gamma.setGeometry(QtCore.QRect(600, 60, 101, 45))
        self.pushButton_gamma.setStyleSheet("font: 12pt \"黑体\";\n"
"border-radius: 20px;\n"
"background-color: rgb(254, 180, 160);\n"
"background-color: rgb(239 ,100 ,97);\n"
"background-color: rgb(228, 179, 99);\n"
"color: rgb(49, 54, 56);")
        self.pushButton_gamma.setObjectName("pushButton_gamma")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像处理"))
        self.label_camera.setText(_translate("MainWindow", "图像"))
        self.label_detect.setText(_translate("MainWindow", "曲线"))
        self.label_a.setText(_translate("MainWindow", "a:"))
        self.label_b.setText(_translate("MainWindow", "b:"))
        self.label_gamma.setText(_translate("MainWindow", "γ:"))
        self.pushButton_line.setText(_translate("MainWindow", "线性"))
        self.pushButton_broken.setText(_translate("MainWindow", "折线"))
        self.pushButton_curve.setText(_translate("MainWindow", "曲线"))
        self.pushButton_histeq.setText(_translate("MainWindow", "直方图均衡化"))
        self.pushButton_gamma.setText(_translate("MainWindow", "伽马变换"))

