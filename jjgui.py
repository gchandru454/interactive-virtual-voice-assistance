

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jjgui(object):
    def setupUi(self, jjgui):
        jjgui.setObjectName("jjgui")
        jjgui.resize(1956, 975)
        self.centralwidget = QtWidgets.QWidget(jjgui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1961, 981))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1580, 30, 161, 51))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("font: 90 8pt \"Constantia\";\n"
"background-color: rgb(170, 0, 0);\n"
"background-color: rgb(170, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1580, 100, 161, 51))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("font: 90 8pt \"Constantia\";\n"
"background-color: rgb(170, 0, 0);\n"
"background-color: rgb(170, 85, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 560, 301, 251))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../depositphotos_346456510-stock-illustration-letter-type-logo-design-vector.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 441, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../T8bahf.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1570, 570, 281, 331))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../lara.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(700, 7, 150, 60))
        self.textBrowser.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:blue;\n"
"font=size:120px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1000, 7, 150, 60))
        self.textBrowser_2 .setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"color:blue;\n"
"font=size:120px;");
        self.textBrowser_2.setObjectName("textBrowser_2")
        jjgui.setCentralWidget(self.centralwidget)

        self.retranslateUi(jjgui)
        QtCore.QMetaObject.connectSlotsByName(jjgui)

    def retranslateUi(self, jjgui):
        _translate = QtCore.QCoreApplication.translate
        jjgui.setWindowTitle(_translate("jjgui", "MainWindow"))
        self.pushButton.setText(_translate("jjgui", "START"))
        self.pushButton_2.setText(_translate("jjgui", "STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jjgui = QtWidgets.QMainWindow()
    ui = Ui_jjgui()
    ui.setupUi(jjgui)
    jjgui.show()
    sys.exit(app.exec_())
