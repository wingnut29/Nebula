import os
import sys
from pathlib import Path

from PyQt5 import QtWidgets

from src import splash
from src import functions


def get_os():
    """
    Check operating system, return string (e.g. 'linux' or 'win32')
    :return: sys.platform
    """
    return sys.platform


def check_permissions():
    """
    Check permissions of current directory and return path, error
    :return: path, errors
    """
    path = Path(__file__).parent.absolute()
    error = None

    try:
        os.access(path, os.R_OK)  # Check for read permissions
        os.access(path, os.W_OK)  # Check for write permissions
        os.access(path, os.X_OK)  # Check for execution permissions
    except PermissionError as e:
        error = e
        print("Permission Error (", error, ") exists. Try root?")
    finally:
        return path, error if error else None  # Return directory path and error if one exists

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = splash.MainWindow()
    app.exec_()
    functions.reset_json()
