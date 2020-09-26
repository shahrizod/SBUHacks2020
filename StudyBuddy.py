# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudyBuddy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from QuestionDial import Ui_Dialog
import time
import sys
import os
import random
from scraper import convertArray

global quizlet_reader
global numQuestions
global numQsDone
numQsDone = 0

def arrayconverter(scrapeUrl):
    global quizlet_reader
    quizlet_reader = convertArray(scrapeUrl)

def numQs(numq):
    global numQuestions
    numQuestions = numq

def createProblem():
    global quizlet_reader
    randRow = quizlet_reader.sample(1)  #pull random row from csv
    question = randRow.iat[0, 1]        #definition at random row
    answer = randRow.iat[0, 0]          #term at random row

    #pull 3 more random terms for incorrect choices
    choice1 = quizlet_reader.sample(1).iat[0,0] 
    choice2 = quizlet_reader.sample(1).iat[0,0]
    choice3 = quizlet_reader.sample(1).iat[0,0]

    #remove ':' from terms
    answer = answer[:-2]
    choice1 = choice1[:-2]
    choice2 = choice2[:-2]
    choice3 = choice3[:-2]

    List = [[question], [answer, choice1, choice2, choice3]]
    print(List)
    return List

class Ui_MainWindow(object):
    global List
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
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
        arrayconverter(self.lineEdit.text())
        numQs(self.NumberQuestions.value())
        global List
        List = createProblem()
        choices = List[1]
        random.shuffle(choices)
        time.sleep(self.TimeAmount.value())
        qUi.inputChoice(Dialog, 1, choices[0])
        qUi.inputChoice(Dialog, 2, choices[1])
        qUi.inputChoice(Dialog, 3, choices[2])
        qUi.inputChoice(Dialog, 4, choices[3])
        qUi.inputChoice(Dialog, 5, List[0][0])
        
        Dialog.show()
        Dialog.exec_()

class Ui_Dialog(object):
    global List
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 800)
        Dialog.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint
        )
        self.choice2 = QtWidgets.QCheckBox(Dialog)
        self.choice2.setGeometry(QtCore.QRect(80, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.choice2.setFont(font)
        self.choice2.setObjectName("choice2")
        self.choice4 = QtWidgets.QCheckBox(Dialog)
        self.choice4.setGeometry(QtCore.QRect(80, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.choice4.setFont(font)
        self.choice4.setObjectName("choice4")
        self.choice1 = QtWidgets.QCheckBox(Dialog)
        self.choice1.setGeometry(QtCore.QRect(80, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.choice1.setFont(font)
        self.choice1.setObjectName("choice1")
        self.defQuestions = QtWidgets.QLabel(Dialog)
        self.defQuestions.setGeometry(QtCore.QRect(10, 0, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.defQuestions.setFont(font)
        self.defQuestions.setObjectName("defQuestions")
        self.defQuestions.setWordWrap(True)
        self.choice3 = QtWidgets.QCheckBox(Dialog)
        self.choice3.setGeometry(QtCore.QRect(80, 370, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.choice3.setFont(font)
        self.choice3.setObjectName("choice3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.choice1.stateChanged.connect(lambda: self.checkClick(Dialog, 1))
        self.choice2.stateChanged.connect(lambda: self.checkClick(Dialog, 2))
        self.choice3.stateChanged.connect(lambda: self.checkClick(Dialog, 3))
        self.choice4.stateChanged.connect(lambda: self.checkClick(Dialog, 4))

    def checkClick(self, Dialog, choice):
        if choice == 1:
            chosen = self.choice1.text()
        if choice == 2:
            chosen = self.choice2.text()
        if choice == 3:
            chosen = self.choice3.text()
        if choice == 4:
            chosen = self.choice4.text()
        print(chosen)
        print(List[1][0])

        if chosen == List[1][0]:
            self.nextSlide(chosen)
        else:
            print("try again")

    def nextSlide(self, chosen):
        global numQsDone
        numQsDone+=1
        global numQuestions
        global List
        List = createProblem()
        choices = List[1]
        random.shuffle(choices)
        print(choices)
        self.inputChoice(Dialog, 1, choices[0])
        self.inputChoice(Dialog, 2, choices[1])
        self.inputChoice(Dialog, 3, choices[2])
        self.inputChoice(Dialog, 4, choices[3])
        self.inputChoice(Dialog, 5, List[0][0])

        self.choice1.setChecked(False)
        self.choice2.setChecked(False)
        self.choice3.setChecked(False)    
        self.choice4.setChecked(False)
        if numQuestions == numQsDone:
            sys.exit()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.choice2.setText(_translate("Dialog", "Choice 2"))
        self.choice4.setText(_translate("Dialog", "Choice 4"))
        self.choice1.setText(_translate("Dialog", "Choice 1"))
        self.defQuestions.setText(_translate("Dialog", "Definition: "))
        self.choice3.setText(_translate("Dialog", "Choice 3"))

    def inputChoice(self, Dialog, choice, text):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        if choice == 1:
            self.choice1.setText(_translate("Dialog", text))
            self.choice1.adjustSize()
        if choice == 2:
            self.choice2.setText(_translate("Dialog", text))
            self.choice2.adjustSize()
        if choice == 3:
            self.choice3.setText(_translate("Dialog", text))
            self.choice3.adjustSize()
        if choice == 4:
            self.choice4.setText(_translate("Dialog", text))
            self.choice4.adjustSize()
        if choice == 5:
            self.defQuestions.setText(_translate("Dialog", "Definition: " + text))
            self.defQuestions.adjustSize()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    Dialog = QtWidgets.QDialog()
    qUi = Ui_Dialog()
    qUi.setupUi(Dialog)
    MainWindow.show()
    sys.exit(app.exec_())
