from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtGui import QPixmap

from src import functions
from src import resources, main


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, topic=None):
        super(MainWindow, self).__init__()
        uic.loadUi(resources.STUDY, self)
        self.window = None
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.imgBackground.setPixmap(QPixmap(resources.BACKGROUND))
        self.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
        self.btnBack.setIcon(QtGui.QIcon(resources.LEFT_ARROW))
        self.btnBack.clicked.connect(lambda: self.switch_window(main))

    def switch_window(self, ui):
        self.window = ui.MainWindow()
        self.window.show()
        self.close()
        functions.reset_json()
