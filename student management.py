import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(900,600)
    w.move(500,500)
    w.setWindowTitle("pyqt")
    w.show()

    #进入程序的主循环
    sys.exit(app.exec_())
