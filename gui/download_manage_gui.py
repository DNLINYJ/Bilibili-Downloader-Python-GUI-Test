import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import ui_download_manage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui_download_manage.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
