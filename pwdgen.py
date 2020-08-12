from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = string.punctuation

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 313)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 170, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textbrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textbrowser.setGeometry(QtCore.QRect(120, 220, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.textbrowser.setStyleSheet('color:Red')
        self.textbrowser.setAlignment(QtCore.Qt.AlignCenter)
        self.textbrowser.setFont(font)
        self.textbrowser.setText("")
        self.textbrowser.setObjectName("textbrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.textbrowser.setText("")
        self.pushButton.clicked.connect(self.poorpwd)
        self.pushButton_2.clicked.connect(self.goodpwd)
        self.pushButton_3.clicked.connect(self.strongpwd)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Poor"))
        self.pushButton_2.setText(_translate("MainWindow", "Good"))
        self.pushButton_3.setText(_translate("MainWindow", "Strong"))
        self.label.setText(_translate("MainWindow", "Password Generator"))


    def poorpwd(self):
        poorpass = ''.join(random.choice(lowercase) for i in range(0,9))
        self.textbrowser.setText(poorpass)


    def goodpwd(self):
        goodpass = ''.join(random.choice(lowercase+uppercase+digits) for i in range(0,11))
        self.textbrowser.setText(goodpass)

    def strongpwd(self):
        strongpass =''.join(random.choice(lowercase+uppercase+digits+special) for i in range(0,13))
        self.textbrowser.setText(strongpass)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
