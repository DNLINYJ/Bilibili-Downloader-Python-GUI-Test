import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# from PyQt5.QtCore import pyqtSignal
import ui_login as login
import ui_download_manage as download
import ui_setting as setting
import ui_main as main


class MainWin(QMainWindow, main.Ui_MainWindow):
    # show_sub_win_signal = pyqtSignal()  # 该信号用于展示子窗体

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SubWin_Login(QWidget, login.Ui_Form):
    # 自定义信号

    def __init__(self):
        super(SubWin_Login, self).__init__()
        self.setupUi(self)

class SubWin_Download_Manage(QWidget, download.Ui_Form):
    # 自定义信号

    def __init__(self):
        super(SubWin_Download_Manage, self).__init__()
        self.setupUi(self)

class SubWin_Setting(QWidget, setting.Ui_Form):
    # 自定义信号

    def __init__(self):
        super(SubWin_Setting, self).__init__()
        self.setupUi(self)

def show_sub(num):
    if num == 1: #Login 
        SubWin_Login.show()
        myWin.hide()
        SubWin_Download_Manage.hide()
        SubWin_Setting.hide()
    elif num == 2: #Download Manage
        SubWin_Download_Manage.show()
        myWin.hide()
        SubWin_Setting.hide()
        SubWin_Login.hide()
    elif num == 3: #Setting
        SubWin_Setting.show()
        myWin.hide()
        SubWin_Download_Manage.hide()
        SubWin_Login.hide()

def show_main():
    myWin.show()
    SubWin_Login.hide()
    SubWin_Download_Manage.hide()
    SubWin_Setting.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWin()
    myWin.show()
    SubWin_Login = SubWin_Login()
    SubWin_Download_Manage = SubWin_Download_Manage()
    SubWin_Setting = SubWin_Setting()

    myWin.Sgin_in_Button.clicked.connect(lambda:show_sub(1))
    myWin.Download_Manage_Button.clicked.connect(lambda:show_sub(2))
    myWin.Setting_Button.clicked.connect(lambda:show_sub(3))

    SubWin_Login.Main_Button.clicked.connect(lambda:show_main())
    SubWin_Login.Download_Manage_Button.clicked.connect(lambda:show_sub(2))
    SubWin_Login.Setting_Button.clicked.connect(lambda:show_sub(3))

    SubWin_Download_Manage.Main_Button.clicked.connect(lambda:show_main())
    SubWin_Download_Manage.Sgin_in_Button.clicked.connect(lambda:show_sub(1))
    SubWin_Download_Manage.Setting_Button.clicked.connect(lambda:show_sub(3))

    SubWin_Setting.Main_Button.clicked.connect(lambda:show_main())
    SubWin_Setting.Sgin_in_Button.clicked.connect(lambda:show_sub(1))
    SubWin_Setting.Download_Manage_Button.clicked.connect(lambda:show_sub(2))

    sys.exit(app.exec_())