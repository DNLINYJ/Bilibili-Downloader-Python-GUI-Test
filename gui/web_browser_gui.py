import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import ui_web_browser

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui_web_browser.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
