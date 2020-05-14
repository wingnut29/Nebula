import sys

from PyQt5 import QtWidgets

from src import functions, main

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = main.MainWindow()
    app.exec_()
    functions.reset_json()
