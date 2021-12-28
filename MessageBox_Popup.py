from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 200, 89, 25))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Show Popup"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message Box!")
        msg.setText("Have a nice day!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Retry | QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Ignore)
        msg.setInformativeText("Information here.")
        msg.setDetailedText("Here's info details...")
        msg.buttonClicked.connect(self.popup_button)
        # msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def popup_button(self,i):
        print(i.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
