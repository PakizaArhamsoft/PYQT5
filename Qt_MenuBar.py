from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        QMainWindow.setObjectName("QMainWindow")
        QMainWindow.resize(562, 600)
        self.centralwidget = QtWidgets.QWidget(QMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 60, 67, 17))
        self.label.setObjectName("label")
        QMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 22))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        QMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QMainWindow)
        self.statusbar.setObjectName("statusbar")
        QMainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(QMainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(QMainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(QMainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(QMainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFIle.addAction(self.actionNew)
        self.menuFIle.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(QMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)

        self.actionNew.triggered.connect(lambda: self.clicked("New File Created!"))
        self.actionSave.triggered.connect(lambda: self.clicked("Save the file!"))
        self.actionCopy.triggered.connect(lambda: self.clicked("Copy the file!"))
        self.actionPaste.triggered.connect(lambda: self.clicked("Paste the file!"))

    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("QMainWindow", "NotePad"))
        self.label.setText(_translate("QMainWindow", "Text Here"))
        self.menuFIle.setTitle(_translate("QMainWindow", "File"))
        self.menuEdit.setTitle(_translate("QMainWindow", "Edit"))
        self.actionNew.setText(_translate("QMainWindow", "New"))
        self.actionNew.setStatusTip(_translate("QMainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("QMainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("QMainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("QMainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("QMainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("QMainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("QMainWindow", "Copy a file"))
        self.actionCopy.setShortcut(_translate("QMainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("QMainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("QMainWindow", "Paste a file"))
        self.actionPaste.setShortcut(_translate("QMainWindow", "Ctrl+V"))

    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QMainWindow = QtWidgets.QMainWindow()
    ui = Ui_QMainWindow()
    ui.setupUi(QMainWindow)
    QMainWindow.show()
    sys.exit(app.exec_())
