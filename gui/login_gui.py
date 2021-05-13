import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import ui_login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui_login.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
