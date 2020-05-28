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
        MainWindow.resize(898, 598)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(940, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_im1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_im1.setGeometry(QtCore.QRect(20, 50, 331, 231))
        self.graphicsView_im1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"")
        self.graphicsView_im1.setObjectName("graphicsView_im1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 101, 31))
        self.label_2.setStyleSheet("font: 11pt \"方正韵动粗黑简体\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_do = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_do.setGeometry(QtCore.QRect(780, 50, 93, 28))
        self.pushButton_do.setStyleSheet("font: 10pt \"方正韵动粗黑简体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_do.setObjectName("pushButton_do")
        self.graphicsView_im2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_im2.setGeometry(QtCore.QRect(20, 310, 331, 231))
        self.graphicsView_im2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"")
        self.graphicsView_im2.setObjectName("graphicsView_im2")
        self.graphicsView_mix = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_mix.setGeometry(QtCore.QRect(390, 100, 481, 341))
        self.graphicsView_mix.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"")
        self.graphicsView_mix.setObjectName("graphicsView_mix")
        self.comboBox_function = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_function.setGeometry(QtCore.QRect(570, 50, 181, 31))
        self.comboBox_function.setStyleSheet("font: 10pt \"方正韵动粗黑简体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_function.setObjectName("comboBox_function")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(780, 450, 81, 89))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_front = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_front.setStyleSheet("font: 20pt \"Adobe Arabic\";")
        self.radioButton_front.setObjectName("radioButton_front")
        self.verticalLayout.addWidget(self.radioButton_front)
        self.radioButton_back = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_back.setStyleSheet("font: 20pt \"Adobe Arabic\";")
        self.radioButton_back.setObjectName("radioButton_back")
        self.verticalLayout.addWidget(self.radioButton_back)
        self.horizontalSlider_mix = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_mix.setGeometry(QtCore.QRect(400, 470, 461, 41))
        self.horizontalSlider_mix.setStyleSheet("QSlider::groove:horizontal{ height: 10px; \n"
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
"                             background: #cd3426; \n"
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
        self.horizontalSlider_mix.setMaximum(1)
        self.horizontalSlider_mix.setSingleStep(1)
        self.horizontalSlider_mix.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_mix.setObjectName("horizontalSlider_mix")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(90, 10, 93, 28))
        self.pushButton_add.setStyleSheet("font: 10pt \"方正韵动粗黑简体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(205, 52, 38);")
        self.pushButton_add.setObjectName("pushButton_add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 26))
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
        self.label_2.setText(_translate("MainWindow", "原图像"))
        self.pushButton_do.setText(_translate("MainWindow", "执行"))
        self.radioButton_front.setText(_translate("MainWindow", "A-B"))
        self.radioButton_back.setText(_translate("MainWindow", "B-A"))
        self.pushButton_add.setText(_translate("MainWindow", "添加图像"))

