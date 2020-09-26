# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestionDial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import random
from scraper import convertArray
class Ui_Dialog(object):

    def createProblem(self):
        quizlet_reader = convertArray("https://quizlet.com/2595436/stony-brook-university-flash-cards/")
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
        return List

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 1080)
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
        font.setPointSize(30)
        self.choice2.setFont(font)
        self.choice2.setObjectName("choice2")
        self.choice4 = QtWidgets.QCheckBox(Dialog)
        self.choice4.setGeometry(QtCore.QRect(80, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(30)
        self.choice4.setFont(font)
        self.choice4.setObjectName("choice4")
        self.Instructions = QtWidgets.QLabel(Dialog)
        self.Instructions.setGeometry(QtCore.QRect(30, 130, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        self.Instructions.setFont(font)
        self.Instructions.setObjectName("Instructions")
        self.choice1 = QtWidgets.QCheckBox(Dialog)
        self.choice1.setGeometry(QtCore.QRect(80, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(30)
        self.choice1.setFont(font)
        self.choice1.setObjectName("choice1")
        self.defQuestions = QtWidgets.QLabel(Dialog)
        self.defQuestions.setGeometry(QtCore.QRect(10, 0, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(50)
        self.defQuestions.setFont(font)
        self.defQuestions.setObjectName("defQuestions")
        self.choice3 = QtWidgets.QCheckBox(Dialog)
        self.choice3.setGeometry(QtCore.QRect(80, 370, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(30)
        self.choice3.setFont(font)
        self.choice3.setObjectName("choice3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.displayQ(Dialog, "The powerhouse of the cell")
        self.choice2.stateChanged.connect(self.checkClick)

    def checkClick(self, Dialog):
        print("Correct")

    def retranslateUi(self, Dialog):
        List = self.createProblem()
        choices = List[1]
        for i in range(len(choices)-1, 0, -1):
            j = random.randint(0, i+1)

            choices[i], choices[j] = choices[j], choices[i]
        
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.choice2.setText(_translate("Dialog", choices[0]))
        self.choice4.setText(_translate("Dialog", choices[1]))
        self.Instructions.setText(_translate("Dialog", "Please select a choice"))
        self.choice1.setText(_translate("Dialog", choices[2]))
        self.defQuestions.setText(_translate("Dialog", List[0][0]))
        self.choice3.setText(_translate("Dialog", choices[3]))

    def inputChoice(self, Dialog, choice, text,):
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

    def displayQ(self, Dialog, text):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.defQuestions.setText(_translate("Dialog", "Definition: " + text))
        self.defQuestions.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

