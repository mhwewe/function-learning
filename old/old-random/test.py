# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitest.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1199, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dont = QtWidgets.QPushButton(self.centralwidget)
        self.dont.setGeometry(QtCore.QRect(590, 400, 93, 28))
        self.dont.setObjectName("dont")
        self.rando = QtWidgets.QLabel(self.centralwidget)
        self.rando.setGeometry(QtCore.QRect(434, 140, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.rando.setFont(font)
        self.rando.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rando.setAlignment(QtCore.Qt.AlignCenter)
        self.rando.setObjectName("rando")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dont.setText(_translate("MainWindow", "dont push me"))
        self.rando.setText(_translate("MainWindow", "Yo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())