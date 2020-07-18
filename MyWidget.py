# -*- coding: utf-8 -*-

import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.QtGui import  QPixmap
from GUI import Ui_MainWindow
from PIL import Image
import numpy as np

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()  #super(mywindow,self) 首先找到 mywindowd的父类(也就是类 QtWidgets.QMainWindow, Ui_MainWindow)
                                          #然后把类 mywindow 的对象转换为父类的对象 
        self.setupUi(self)
        self.setWindowTitle("同名核线标定")
        self.leftphoto = "./Resource/01-156_50mic.jpg"
        self.rightphoto = "./Resource/01-155_50mic.jpg"
        imgLeft = QPixmap(self.leftphoto)
        imgRight = QPixmap(self.rightphoto)
        self.LeftPhoto.setPixmap(imgLeft)
        self.RightPhoto.setPixmap(imgRight)
        self.LeftPhoto.setScaledContents(True)
        self.RightPhoto.setScaledContents(True)
        self.calButton.clicked.connect(self.onClickCalButton)
        self.clearButton.clicked.connect(self.onClickClearButton)

    def onClickCalButton(self):

        xPixel = eval(self.lineEdit.text())
        yPixel = eval(self.lineEdit_2.text())
        self.xFrame = self.Pixel2Frame(xPixel)-0.004              #像素坐标转换为像平面坐标，此为要求同名像点中的左像点
        self.yFrame = self.Pixel2Frame(yPixel)-0.008
        f = 152.720
        R1 = np.copy(self.rMat(-0.0081,0,-0.005))
        R2 = np.copy(self.rMat(-0.0066,-0.0067,0.0036))
        a = R1*np.mat([[self.xFrame],[self.yFrame],[f]])
        xaLeft = self.xFrame
        yaLeft = self.yFrame
        xbLeft = 50                       #随便给定一数值，获取过左像片核线中的另一点，进而确定左核线，两点确定一条直线
        xaRight = -100                    #同理获取右核线
        xbRight = 100
        #通过共面方程获取右像片任意点在核线上的y值
        ybLeft = (a[1,0]*R1[2,0]-a[2,0]*R1[1,0])*xbLeft/((a[2,0]*R1[1,1]-a[1,0]*R1[2,1]))+(a[2,0]*R1[1,2]-a[1,0]*R1[2,2])*f/(a[2,0]*R1[1,1]-a[1,0]*R1[1,1])
        yaRight = (a[1,0]*R2[2,0]-a[2,0]*R2[1,0])*xaRight/((a[2,0]*R2[1,1]-a[1,0]*R2[2,1]))+(a[2,0]*R2[1,2]-a[1,0]*R2[2,2])*f/(a[2,0]*R2[1,1]-a[1,0]*R2[1,1])
        ybRight = (a[1,0]*R2[2,0]-a[2,0]*R2[1,0])*xbRight/((a[2,0]*R2[1,1]-a[1,0]*R2[2,1]))+(a[2,0]*R2[1,2]-a[1,0]*R2[2,2])*f/(a[2,0]*R2[1,1]-a[1,0]*R2[1,1])
        k = int((ybLeft-yaLeft)/(xbLeft-xaLeft))
        b = yaLeft - k*xaLeft
        strLine = "y="+str(k) + "x+" + str(int(b))
        QMessageBox.information(self,"左核线方程",strLine)
        #沿着右像片的核线寻找同名像点，该函数一像素为单位
        self.areaVar = []
        self.areaIndex = []
        local = self.FindImagePoints(xaLeft,yaLeft,xaRight,yaRight,xbRight,ybRight)
        #print(local)
        strPoint = str(local[0])+str(local[1])
        QMessageBox.information(self,"同名像点",strPoint)


    def onClickClearButton(self):
        return

    def Pixel2Frame(self,x):
        xFrame = x/22-114
        return xFrame

    def rMat(self,f,w,k):
        a1 = np.cos(f)*np.cos(w)-np.sin(f)*np.sin(w)*np.sin(k)
        a2 = (-1)*np.cos(f)*np.sin(k)-np.sin(f)*np.sin(w)*np.sin(k)
        a3 = (-1)*np.sin(f)*np.cos(w)
        b1 = np.cos(w)*np.sin(k)
        b2 = np.cos(w)*np.cos(k)
        b3 = (-1)*np.sin(w)
        c1 = np.sin(f)*np.cos(k)+np.cos(f)*np.sin(w)*np.sin(k)
        c2 = (-1)*np.sin(f)*np.sin(k)+np.cos(f)*np.sin(w)*np.cos(k)
        c3 = np.cos(f)*np.cos(w)
        R = np.mat([[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]])
        return R

    def FindImagePoints(self,x,y,xaR,yaR,xbR,ybR):
        x = int((x+114)*22)
        y = int((y+114)*22)
        xaR = int((xaR+114)*22)
        yaR = int((yaR+114)*22)
        xbR = int((xbR+114)*22)
        ybR = int((ybR+114)*22)
        self.leftPhotoArray = np.array(Image.open(self.leftphoto))
        self.rightPhotoArray = np.array(Image.open(self.rightphoto))
        self.leftPixelArea = np.zeros((51,51,3))
        #首先以左像点为中心选取一块51✖51的区域，作为待匹配区域
        self.areaVar = []
        self.areaIndex = []
        for i in range(51):
            for j in range(51):
                self.leftPixelArea[i,j] = self.leftPhotoArray[x-25+i,y-25+j]
        k = (ybR-yaR)/(xbR-xaR)
        b = yaR - k*xaR
        strLine = strLine = "y="+str(int(k)) + "x+" + str(int(b))
        QMessageBox.information(self,"右核线方程",strLine)
        if abs(k)<=1:
            x1 = 0
            x2 = 5119
            y1 = b
            y2 = k*x2+b
            for i in range(100,4000):
                for j in range(int(5120-(k*i+b)-3),int(5120-(k*i+b)+3)):
                    temp = self.PixelVariance(i,j)
                    #print(temp)
                    self.areaVar.append(temp[0])
                    self.areaIndex.append(temp[1:])
            local = self.areaVar.index(min(self.areaVar))
            return self.areaIndex[local]

        elif abs(k)>1:
            y1 = 0
            y2 = 5119
            x1 = y1-b/k
            x2 = y2-b/k
            if x1<x2:
                for i in range(int(x1)+100,int(x2)-100):
                    for j in range(int(5102-(k*i+b)-3),int(5120+(k*i+b)+3)):
                        self.PixelVariance(i,j)
                        self.areaVar.append(self.PixelVariance(i,j)[0])
                        self.areaIndex.append(self.PixelVariance(i,j)[1:])
                local = self.areaVar.index(min(self.areaVar))
                return self.areaIndex[local]
            elif x1>x2:
                for i in range(int(x2)+100,int(x1)-100):
                    for j in range(int(5102-(k*i+b)-3),int(5120+(k*i+b)+3)):
                        self.PixelVariance(i,j)
                        self.areaVar.append(self.PixelVariance(i,j)[0])
                        self.areaIndex.append(self.PixelVariance(i,j)[1:])
                local = self.areaVar.index(min(self.areaVar))
                return self.areaIndex[local]
        #local = self.areaVar.index(self.areaVar)
        #print(self.areaIndex[local])

    def PixelVariance(self,x,y):
        onePixelArea = np.ones((51,51,3))   #一块与左像点匹配的区域
        oneList = []
        for i in range(51):
            for j in range(51):
                onePixelArea[i,j] = self.rightPhotoArray[x-25+i,y-25+j]    #将右核线上的每个点都生成一块51✖51的区域
        for m in range(51):
            for n in range(51):
                temp = np.var(self.leftPixelArea[m,n]-onePixelArea[m,n])
                oneList.append(temp)                                       #每个像素点的方差加入列表

        return (np.var(oneList),x,y)


if __name__ == '__main__': 
    
    app = QApplication(sys.argv)
    mainwindow = mywindow()
    mainwindow.show()
    sys.exit(app.exec_())