# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(927, 564)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.definition = QtWidgets.QGroupBox(Form)
        self.definition.setGeometry(QtCore.QRect(20, 100, 611, 71))
        self.definition.setStyleSheet("background:rgba(0,0,0,0);color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.definition.setObjectName("definition")
        self.D_480P = QtWidgets.QRadioButton(self.definition)
        self.D_480P.setGeometry(QtCore.QRect(80, 30, 71, 21))
        self.D_480P.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.D_480P.setObjectName("D_480P")
        self.D_720P = QtWidgets.QRadioButton(self.definition)
        self.D_720P.setGeometry(QtCore.QRect(150, 30, 71, 21))
        self.D_720P.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.D_720P.setObjectName("D_720P")
        self.D_720P60FPS = QtWidgets.QRadioButton(self.definition)
        self.D_720P60FPS.setGeometry(QtCore.QRect(300, 30, 111, 21))
        self.D_720P60FPS.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.D_720P60FPS.setObjectName("D_720P60FPS")
        self.D_360P = QtWidgets.QRadioButton(self.definition)
        self.D_360P.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.D_360P.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.D_360P.setObjectName("D_360P")
        self.D_1080P = QtWidgets.QRadioButton(self.definition)
        self.D_1080P.setGeometry(QtCore.QRect(220, 30, 71, 21))
        self.D_1080P.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.D_1080P.setObjectName("D_1080P")
        self.D_4K = QtWidgets.QRadioButton(self.definition)
        self.D_4K.setGeometry(QtCore.QRect(540, 30, 71, 21))
        self.D_4K.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.D_4K.setObjectName("D_4K")
        self.D_1080P60FPS = QtWidgets.QRadioButton(self.definition)
        self.D_1080P60FPS.setGeometry(QtCore.QRect(410, 30, 111, 21))
        self.D_1080P60FPS.setStyleSheet("color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.D_1080P60FPS.setObjectName("D_1080P60FPS")
        self.Setting_Background = QtWidgets.QLabel(Form)
        self.Setting_Background.setGeometry(QtCore.QRect(10, 90, 901, 461))
        self.Setting_Background.setStyleSheet("background:rgba(0,0,0,60);")
        self.Setting_Background.setText("")
        self.Setting_Background.setObjectName("Setting_Background")
        self.Setting_Button = QtWidgets.QPushButton(Form)
        self.Setting_Button.setGeometry(QtCore.QRect(310, 20, 131, 41))
        self.Setting_Button.setStyleSheet("background:rgba(0,0,0,30);color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.Setting_Button.setObjectName("Setting_Button")
        self.Login_Username = QtWidgets.QLabel(Form)
        self.Login_Username.setGeometry(QtCore.QRect(760, 20, 131, 41))
        self.Login_Username.setStyleSheet("background:rgba(0,0,0,30);color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.Login_Username.setObjectName("Login_Username")
        self.Download_Manage_Button = QtWidgets.QPushButton(Form)
        self.Download_Manage_Button.setGeometry(QtCore.QRect(170, 20, 131, 41))
        self.Download_Manage_Button.setStyleSheet("background:rgba(0,0,0,30);color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.Download_Manage_Button.setObjectName("Download_Manage_Button")
        self.Sgin_out_Button = QtWidgets.QPushButton(Form)
        self.Sgin_out_Button.setGeometry(QtCore.QRect(610, 20, 131, 41))
        self.Sgin_out_Button.setStyleSheet("background:rgba(0,0,0,30);color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.Sgin_out_Button.setObjectName("Sgin_out_Button")
        self.Main_Button = QtWidgets.QPushButton(Form)
        self.Main_Button.setGeometry(QtCore.QRect(30, 20, 131, 41))
        self.Main_Button.setStyleSheet("background:rgba(0,0,0,30);color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.Main_Button.setObjectName("Main_Button")
        self.Background = QtWidgets.QLabel(Form)
        self.Background.setGeometry(QtCore.QRect(0, 0, 931, 571))
        self.Background.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap(":/jpg/background.jpg"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.Sgin_in_Button = QtWidgets.QPushButton(Form)
        self.Sgin_in_Button.setGeometry(QtCore.QRect(460, 20, 131, 41))
        self.Sgin_in_Button.setStyleSheet("background:rgba(0,0,0,30);color:white;\n"
"\n"
"font-family: 微软雅黑;\n"
"\n"
"font-size:15px")
        self.Sgin_in_Button.setObjectName("Sgin_in_Button")
        self.Background.raise_()
        self.Download_Manage_Button.raise_()
        self.Login_Username.raise_()
        self.Main_Button.raise_()
        self.Setting_Button.raise_()
        self.Sgin_in_Button.raise_()
        self.Sgin_out_Button.raise_()
        self.Setting_Background.raise_()
        self.definition.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "哔哩哔哩视频下载器 Beta v0.1 作者：菠萝小西瓜  φ(゜▽゜*)♪"))
        self.definition.setTitle(_translate("Form", "下载视频分辨率"))
        self.D_480P.setText(_translate("Form", "480P"))
        self.D_720P.setText(_translate("Form", "720P"))
        self.D_720P60FPS.setText(_translate("Form", "720P 60FPS"))
        self.D_360P.setText(_translate("Form", "360P"))
        self.D_1080P.setText(_translate("Form", "1080P"))
        self.D_4K.setText(_translate("Form", "4K"))
        self.D_1080P60FPS.setText(_translate("Form", "1080P 60FPS"))
        self.Setting_Button.setText(_translate("Form", "设置"))
        self.Login_Username.setText(_translate("Form", "TextLabel"))
        self.Download_Manage_Button.setText(_translate("Form", "下载管理"))
        self.Sgin_out_Button.setText(_translate("Form", "退出B站账号"))
        self.Main_Button.setText(_translate("Form", "首页"))
        self.Sgin_in_Button.setText(_translate("Form", "登录B站账号"))
import image_rc
