# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudyBuddy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from QuestionDial import Ui_Dialog
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(140, 20, 151, 141))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("study buddy.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(80, 130, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.NumberQuestions = QtWidgets.QSpinBox(self.centralwidget)
        self.NumberQuestions.setGeometry(QtCore.QRect(290, 270, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.NumberQuestions.setFont(font)
        self.NumberQuestions.setObjectName("NumberQuestions")
        self.QuestionsLabel = QtWidgets.QLabel(self.centralwidget)
        self.QuestionsLabel.setGeometry(QtCore.QRect(30, 260, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.QuestionsLabel.setFont(font)
        self.QuestionsLabel.setObjectName("QuestionsLabel")
        self.TimeAmount = QtWidgets.QSpinBox(self.centralwidget)
        self.TimeAmount.setGeometry(QtCore.QRect(370, 330, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.TimeAmount.setFont(font)
        self.TimeAmount.setObjectName("TimeAmount")
        self.TimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(30, 320, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setObjectName("TimeLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 390, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.urlLabel = QtWidgets.QLabel(self.centralwidget)
        self.urlLabel.setGeometry(QtCore.QRect(30, 380, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 440, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.study)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "Study Bully"))
        self.QuestionsLabel.setText(_translate("MainWindow", "Number of questions each round"))
        self.TimeLabel.setText(_translate("MainWindow", "Amount of time between each round in min."))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Please enter the URL here..."))
        self.urlLabel.setText(_translate("MainWindow", "Quizlet Link"))
        self.pushButton.setText(_translate("MainWindow", "STUDY"))

    def study(self):
        #time.sleep(5)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.inputChoice(Dialog, 2, "Lick My Balls")
        Dialog.show()
        Dialog.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

