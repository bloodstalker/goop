#!/usr/bin/python3
# _*_ coding=utf-8 _*_

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QWidget, QLineEdit
import sys

class Goop(QWidget):
    def __init__(self, xpos, ypos, width, height):
        super().__init__()
        self.title = "Goop"
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.xpos, self.ypos, self.width, self.height)
        self.mainWindow(200, 200, 300, 300)
        #self.getText("Input String", "Input String")
        #self.getText("RegEx", "RegEx")
        self.show()

    def getText(self, DialogueTitle, BoxText):
        text, okPressed = QInputDialog.getText(self, DialogueTitle, BoxText, QLineEdit.Normal, "")
        if okPressed and text != "":
            print(text)

    def mainWindow(self, xpos, ypos, width, height):
        #app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(xpos, ypos, width, height)
        win.setWindowTitle("Wedgie")

        InLabel = QtWidgets.QLabel(win)
        InLabel.setText("Input Text")
        InLabel.move(10, 10)

        OutLabel = QtWidgets.QLabel(win)
        OutLabel.setText("Output Text")
        OutLabel.move(10, 140)

        win.show()
        #sys.exit(app.exec_())


def main():
    app = QApplication(sys.argv)
    goop = Goop(200,200,300,300)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
