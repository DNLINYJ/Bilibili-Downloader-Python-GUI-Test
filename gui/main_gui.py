import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel , QWidget, QDialog
# from PyQt5.QtCore import pyqtSignal
import ui_web_browser as login
import ui_download_manage as download
import ui_setting as setting
import ui_main as main
import threading
import os
import requests
import base64 as b64
import ui_login_message

# 加解密代码来自：https://blog.csdn.net/u010649766/article/details/79174580
def xor_encrypt(tips,key):
    ltips=len(tips)
    lkey=len(key)
    secret=[]
    num=0
    for each in tips:
        if num>=lkey:
            num=num%lkey
        secret.append(chr(ord(each)^ord(key[num])))
        num+=1

    return b64.b64encode("".join(secret).encode()).decode()

def xor_decrypt(secret,key):

    tips = b64.b64decode(secret.encode()).decode()

    ltips=len(tips)
    lkey=len(key)
    secret=[]
    num=0
    for each in tips:
        if num>=lkey:
            num=num%lkey

        secret.append(chr(ord(each)^ord(key[num])))
        num+=1

    return "".join(secret)

#关闭requests模块的InsecureRequestWarning警告提示
#from：https://www.cnblogs.com/milian0711/p/6836384.html
#此处 VS Code 报错为正常现象
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {
            'cookie': "",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://www.bilibili.com'
          }

def get_cookie_def(dialog):
    #正常登录               
    not_login_url = "https://passport.bilibili.com/login"
    not_login_cookie = dialog.widget.get_cookie()
    v1 = 0
    while v1 != 1:
        now_login_url = str(dialog.widget.page().url()).replace("PyQt5.QtCore.QUrl('","").replace("')","")
        now_login_cookie = dialog.widget.get_cookie()
        if not_login_url == now_login_url: # url 无变化，说明未登录
            if not_login_cookie == now_login_cookie: # cookie 无变化，说明未登录
                pass
        else: # url 已变化
            headers["cookie"] = now_login_cookie
            v2 = requests.get(url="https://space.bilibili.com/", headers=headers, verify=False)
            if v2.status_code == 200:
                if "https://passport.bilibili.com" not in v2.request.url: 
                    v1 = 1 # 未跳转登录页面，说明登录成功
                    if os.path.exists("User Data") != True:
                        os.makedirs("User Data")
                    with open("User Data\\Cookie.dat","w+") as f:
                        key = "bilibili_downloader"
                        f.write(xor_encrypt(now_login_cookie,key))
                        

class MainWin(QMainWindow, main.Ui_MainWindow):
    # show_sub_win_signal = pyqtSignal()  # 该信号用于展示子窗体
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class SubWin_Login_Message(QDialog, ui_login_message.Ui_Dialog):
    # 自定义信号
    def __init__(self):
        super(SubWin_Login_Message, self).__init__()
        self.setupUi(self)

class SubWin_Login(QDialog, login.Ui_Dialog):
    # 自定义信号
    def __init__(self):
        super(SubWin_Login, self).__init__()
        self.setupUi(self)
        # self.show()

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
        # 防重复登录检查
        if os.path.exists("User Data\\Cookie.dat") == True:
            key = "bilibili_downloader"
            with open("User Data\\Cookie.dat","r+") as f:
                encrypted_cookie = f.read()
                old_login_cookie = xor_decrypt(encrypted_cookie,key)
                headers["cookie"] = old_login_cookie
                v3 = requests.get(url="https://space.bilibili.com/", headers=headers, verify=False)
                if v3.status_code == 200:
                    if "https://passport.bilibili.com" not in v3.request.url: 
                        temp_dialog = SubWin_Login_Message()
                        temp_dialog.show()
                        temp_dialog.exec_()
                    else:
                        pass
        else:
            # 解决方案 : https://blog.csdn.net/weixin_43350361/article/details/104842332
            dialog = SubWin_Login()
            dialog.show()
            chcek_login_thread = threading.Thread(target=get_cookie_def,args=(dialog,))
            chcek_login_thread.start()
            dialog.exec_()
    elif num == 2: #Download Manage
        SubWin_Download_Manage.show()
        myWin.hide()
        SubWin_Setting.hide()
        # SubWin_Login.hide()
    elif num == 3: #Setting
        SubWin_Setting.show()
        myWin.hide()
        SubWin_Download_Manage.hide()
        # SubWin_Login.hide()

def show_main():
    myWin.show()
    # SubWin_Login.hide()
    SubWin_Download_Manage.hide()
    SubWin_Setting.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWin()
    myWin.show()
    # SubWin_Login = SubWin_Login()
    SubWin_Download_Manage = SubWin_Download_Manage()
    SubWin_Setting = SubWin_Setting()

    myWin.Sgin_in_Button.clicked.connect(lambda:show_sub(1))
    myWin.Download_Manage_Button.clicked.connect(lambda:show_sub(2))
    myWin.Setting_Button.clicked.connect(lambda:show_sub(3))

    # SubWin_Login.Main_Button.clicked.connect(lambda:show_main())
    # SubWin_Login.Download_Manage_Button.clicked.connect(lambda:show_sub(2))
    # SubWin_Login.Setting_Button.clicked.connect(lambda:show_sub(3))

    SubWin_Download_Manage.Main_Button.clicked.connect(lambda:show_main())
    SubWin_Download_Manage.Sgin_in_Button.clicked.connect(lambda:show_sub(1))
    SubWin_Download_Manage.Setting_Button.clicked.connect(lambda:show_sub(3))

    SubWin_Setting.Main_Button.clicked.connect(lambda:show_main())
    SubWin_Setting.Sgin_in_Button.clicked.connect(lambda:show_sub(1))
    SubWin_Setting.Download_Manage_Button.clicked.connect(lambda:show_sub(2))

    sys.exit(app.exec_())