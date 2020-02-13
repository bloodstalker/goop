#!/usr/bin/python3
# _*_ coding=utf-8 _*_

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window(xpos, ypos, width, height):
    app = QApplication(sys.argv)
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
    sys.exit(app.exec_())


def main():
    window(200, 200, 300, 300)


if __name__ == "__main__":
    main()
