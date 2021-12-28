from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        xpos, ypos = 500, 500
        width, height = 500, 700
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("PyQt5 Tutorial")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.move(20, 60)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.move(20, 20)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Succesfully Clicked!")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()

