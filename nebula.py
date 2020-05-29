import sys

from PyQt5 import QtWidgets

from src import functions, main


def check_for_updates():
    pass
    # todo: finish checking for updates


def start():
    print(functions.check_app_version())
    print(functions.check_hosted_version())
    app = QtWidgets.QApplication(sys.argv)
    window = main.MainWindow()
    # check_for_updates()
    app.exec_()
    functions.reset_json()


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(str(e))
