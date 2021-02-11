from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random
import pandas as pd



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,200,650,300)
        self.setWindowTitle("--Random Passwort Generator TuhinQ2--")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Generiere dein zufälliges Passwort:")
        self.label.setGeometry(10,5, 250,50)

        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText("Anzahl Stellen:")
        self.l1.setGeometry(10, 70, 250, 50)

        self.checkNumb = QtWidgets.QCheckBox(self)
        self.checkNumb.setGeometry(20,140,70,30)
        self.checkNumb.setText("Zahlen")
        self.checkNumb.setChecked(True)

        self.checkSonder = QtWidgets.QCheckBox(self)
        self.checkSonder.setGeometry(100, 140, 110, 30)
        self.checkSonder.setText("Sonderzeichen")
        self.checkSonder.setChecked(False)

        self.checkGros = QtWidgets.QCheckBox(self)
        self.checkGros.setGeometry(225, 140, 125, 30)
        self.checkGros.setText("Großbuchstaben")
        self.checkGros.setChecked(False)

        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.setGeometry(120, 80, 50, 30)
        self.textbox.setMaxLength(1)
        self.onlyInt = QtGui.QIntValidator()
        self.textbox.setValidator(self.onlyInt)

        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText("Generiertes Passwort:")
        self.l2.setGeometry(290, 70, 250, 50)

        self.pwt = QtWidgets.QLineEdit(self)
        self.pwt.setGeometry(450, 80, 100, 30)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setGeometry(170,190,120,50)
        self.b1.setText("Generieren")
        self.b1.clicked.connect(self.clicked)

        self.copy = QtWidgets.QPushButton(self)
        self.copy.setGeometry(300, 190, 120, 50)
        self.copy.setText("Kopieren")
        self.copy.clicked.connect(kopieren)



        global pw
        pw = ""

    def clicked(self):

        ##print(self.checkSonder.isChecked())

        zahlen = self.checkNumb.isChecked()

        sonder = self.checkSonder.isChecked()

        gros = self.checkGros.isChecked()

        add = ""


        if self.textbox.text() != '':

            x = int(self.textbox.text())

            y = 0

            pw = ""

            while y < x:

                r = random.randint(1,86)
                add = ""

                ##print(r)

                if r == 1:
                    add = "a"

                if r == 2:
                    add = "b"

                if r == 3:
                    add = "c"

                if r == 4:
                    add = "d"

                if r == 5:
                    add = "e"

                if r == 6:
                    add = "f"

                if r == 7:
                    add = "g"

                if r == 8:
                    add = "h"

                if r == 9:
                    add = "i"

                if r == 10:
                    add = "j"

                if r == 11:
                    add = "k"

                if r == 12:
                    add = "l"

                if r == 13:
                    add = "m"

                if r == 14:
                    add = "n"

                if r == 15:
                    add = "o"

                if r == 16:
                    add = "p"

                if r == 17:
                    add = "q"

                if r == 18:
                    add = "r"

                if r == 19:
                    add = "s"

                if r == 20:
                    add = "t"

                if r == 21:
                    add = "u"

                if r == 22:
                    add = "v"

                if r == 23:
                    add = "w"

                if r == 24:
                    add = "x"

                if r == 25:
                    add = "y"

                if r == 26:
                    add = "z"

                if r == 27 and sonder:
                    add = "!"

                if r == 28 and sonder:
                    add = "$"

                if r == 29 and sonder:
                    add = "%"

                if r == 30 and sonder:
                    add = "/"

                if r == 31 and sonder:
                    add = "("

                if r == 32 and sonder:
                    add = ")"

                if r == 33 and sonder:
                    add = "?"

                if r == 34 and sonder:
                    add = "*"

                if r == 35 and sonder:
                    add = "#"

                if r == 36 and sonder:
                    add = "+"

                if r == 37 and sonder:
                    add = "-"

                if r == 38 and sonder:
                    add = "_"

                if r == 39 and sonder:
                    add = "."

                if r == 40 and sonder:
                    add = ","

                if r == 41 and sonder:
                    add = ":"

                if r == 42 and sonder:
                    add = ";"

                if r == 43 and sonder:
                    add = "="

                if r == 44 and sonder:
                    add = "<"

                if r == 45 and sonder:
                    add = ">"

                if r == 46 and sonder:
                    add = "{"

                if r == 47 and sonder:
                    add = "}"

                if r == 48 and sonder:
                    add = "["

                if r == 49 and sonder:
                    add = "]"

                if r == 50 and zahlen:
                    add = "1"

                if r == 51 and zahlen:
                    add = "2"

                if r == 52 and zahlen:
                    add = "3"

                if r == 53 and zahlen:
                    add = "4"

                if r == 54 and zahlen:
                    add = "5"

                if r == 55 and zahlen:
                    add = "6"

                if r == 56 and zahlen:
                    add = "7"

                if r == 57 and zahlen:
                    add = "8"

                if r == 58 and zahlen:
                    add = "9"

                if r == 59 and zahlen:
                    add = "0"

                if r == 60 and gros:
                    add = "A"

                if r == 61 and gros:
                    add = "B"

                if r == 63 and gros:
                    add = "C"

                if r == 64 and gros:
                    add = "D"

                if r == 65 and gros:
                    add = "E"

                if r == 66 and gros:
                    add = "F"

                if r == 67 and gros:
                    add = "G"

                if r == 68 and gros:
                    add = "H"

                if r == 69 and gros:
                    add = "I"

                if r == 70 and gros:
                    add = "J"

                if r == 71 and gros:
                    add = "K"

                if r == 72 and gros:
                    add = "L"

                if r == 73 and gros:
                    add = "M"

                if r == 74 and gros:
                    add = "N"

                if r == 75 and gros:
                    add = "O"

                if r == 76 and gros:
                    add = "P"

                if r == 77 and gros:
                    add = "Q"

                if r == 78 and gros:
                    add = "R"

                if r == 79 and gros:
                    add = "S"

                if r == 80 and gros:
                    add = "T"

                if r == 81 and gros:
                    add = "U"

                if r == 82 and gros:
                    add = "V"

                if r == 83 and gros:
                    add = "W"

                if r == 84 and gros:
                    add = "X"

                if r == 85 and gros:
                    add = "Y"

                if r == 86 and gros:
                    add = "Z"

                if add != "":
                    pw = pw+add
                    add = ""
                    y = y+1



            self.pwt.setText(pw)
            self.textbox.setText("")

        else:
            self.pwt.setText("Keine Eingabe")



def kopieren():
    df = pd.DataFrame([pw])
    df.to_clipboard(index=False, header=False)



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())



window()


