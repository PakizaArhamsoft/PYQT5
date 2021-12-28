from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    xpos, ypos = 500, 500
    width, height = 500, 700
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("PyQt5 Tutorial")

    label = QtWidgets.QLabel(win)
    label.setText("Basic GUI Application")
    label.move(20, 20)

    win.show()
    sys.exit(app.exec_())


window()
