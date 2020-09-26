from PyQt5 import QtCore, QtGui, QtWidgets
from QuestionDial import Ui_Dialog
from StudyBuddy import Ui_MainWindow
import time
from scraper import convertArray
import random
import pandas as pd

df = convertArray("https://quizlet.com/2595436/stony-brook-university-flash-cards/")

for x in range(4):
    randomNumber = random.randint(0,len(df['Terms'])-1)
    print(df["Terms"][randomNumber],df["Definitions"][randomNumber])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())