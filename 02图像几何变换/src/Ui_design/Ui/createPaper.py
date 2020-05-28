# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createPaper.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createPaper(object):
    def setupUi(self, createPaper):
        createPaper.setObjectName("createPaper")
        createPaper.resize(253, 212)
        self.label_3 = QtWidgets.QLabel(createPaper)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 71, 41))
        self.label_3.setStyleSheet("font: 17pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(createPaper)
        self.label_4.setGeometry(QtCore.QRect(40, 90, 71, 41))
        self.label_4.setStyleSheet("font: 17pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.spinBox_x = QtWidgets.QSpinBox(createPaper)
        self.spinBox_x.setGeometry(QtCore.QRect(90, 40, 101, 21))
        self.spinBox_x.setStyleSheet("border-radius: 10px;")
        self.spinBox_x.setMinimum(100)
        self.spinBox_x.setMaximum(5000)
        self.spinBox_x.setProperty("value", 600)
        self.spinBox_x.setObjectName("spinBox_x")
        self.spinBox_y = QtWidgets.QSpinBox(createPaper)
        self.spinBox_y.setGeometry(QtCore.QRect(90, 100, 101, 21))
        self.spinBox_y.setStyleSheet("border-radius: 10px;")
        self.spinBox_y.setMinimum(100)
        self.spinBox_y.setMaximum(5000)
        self.spinBox_y.setProperty("value", 600)
        self.spinBox_y.setObjectName("spinBox_y")
        self.pushButton_create = QtWidgets.QPushButton(createPaper)
        self.pushButton_create.setGeometry(QtCore.QRect(70, 160, 93, 28))
        self.pushButton_create.setStyleSheet("font: 10pt \"黑体\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(10, 189, 241);")
        self.pushButton_create.setObjectName("pushButton_create")

        self.retranslateUi(createPaper)
        QtCore.QMetaObject.connectSlotsByName(createPaper)

    def retranslateUi(self, createPaper):
        _translate = QtCore.QCoreApplication.translate
        createPaper.setWindowTitle(_translate("createPaper", "创建画布"))
        self.label_3.setText(_translate("createPaper", "长："))
        self.label_4.setText(_translate("createPaper", "宽："))
        self.pushButton_create.setText(_translate("createPaper", "确定"))

