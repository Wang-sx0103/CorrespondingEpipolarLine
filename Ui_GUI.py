# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Desktop\CorrespondingEpipolarLine\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1188, 815)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LeftPhoto = QtWidgets.QLabel(self.centralwidget)
        self.LeftPhoto.setMinimumSize(QtCore.QSize(500, 400))
        self.LeftPhoto.setMaximumSize(QtCore.QSize(960, 1040))
        self.LeftPhoto.setText("")
        self.LeftPhoto.setObjectName("LeftPhoto")
        self.gridLayout.addWidget(self.LeftPhoto, 0, 0, 1, 1)
        self.RightPhoto = QtWidgets.QLabel(self.centralwidget)
        self.RightPhoto.setMinimumSize(QtCore.QSize(500, 400))
        self.RightPhoto.setMaximumSize(QtCore.QSize(960, 1040))
        self.RightPhoto.setText("")
        self.RightPhoto.setObjectName("RightPhoto")
        self.gridLayout.addWidget(self.RightPhoto, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(1679999, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(167999, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.calButton = QtWidgets.QPushButton(self.centralwidget)
        self.calButton.setMinimumSize(QtCore.QSize(140, 40))
        self.calButton.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.calButton.setFont(font)
        self.calButton.setObjectName("calButton")
        self.gridLayout_2.addWidget(self.calButton, 1, 4, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setMinimumSize(QtCore.QSize(140, 40))
        self.clearButton.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_2.addWidget(self.clearButton, 1, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">x</p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "2000"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">y</p></body></html>"))
        self.lineEdit_2.setText(_translate("MainWindow", "2000"))
        self.calButton.setText(_translate("MainWindow", "查找"))
        self.clearButton.setText(_translate("MainWindow", "清空"))
