# 说明 #

- 1 使用Qt5进行的界面设计（GUI.ui），使用NumPy进行矩阵运算
- 2 使用Python3.7及以上翻译MyWidget.py文件（Python需已经安装NumPy、PyQt5、Pillow）
- 3 在Ui中输入左像点坐标（像素坐标），点击“查找”获取左右像片核线的直线方程式后，程序会沿着右像片的核线进行灰度匹配，遍历整个核线后选取方差最小值，作为右像片上的像点

  

# 问题 #
- 1 核线所占像元数量在5000x6 = 30000个点左右，除此之外每个像点匹配到的范围为51x51的方位，即总时间复杂度：78030000，这导致需要较长的运行时长，大约1200s，所以若像看到最终的同名像点需要等，此处应该可以优化
- 2 界面方面没有对同名核线和像点进行标定，以后（我有时间）会添加进去