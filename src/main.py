import json
import os

from PyQt5.QtCore import QTime, QTimer
from win32api import GetSystemMetrics

from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from src import resources


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(resources.MAIN_WINDOW, self)
        self.start_timers()
        self.setup_ui()
        self.show()

        data = self.load_json()

        intro_string = ""
        dict_list = []
        for item in data["INTRO"]:
            dict_list.append(item)
        intro_string = "".join(dict_list)
        self.txtInput.setText(intro_string)

        self.btnStart.clicked.connect(self.start_training)

    def setup_ui(self):
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        self.imgBackground.setPixmap(QPixmap(resources.BACKGROUND))
        self.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
        self.btnStart.setIcon(QtGui.QIcon(resources.BTN_START))

    def start_timers(self):
        clock = QTimer(self)
        clock.timeout.connect(self.get_time)
        clock.start(1000)

        self.get_time()

    def get_time(self):
        time = QTime.currentTime().toString("hh:mm")

        if (time[:2] >= "00") and (time[:2] < "12"):
            self.lblGreeting.setText("Good Morning!")
        elif (time[:2] >= "12") and (time[:2] <= "17"):
            self.lblGreeting.setText("Good Afternoon!")
        elif (time[:2] > "17") and (time[:2] <= "23"):
            self.lblGreeting.setText("Good Evening!")

        self.lcdTime.display(time)

    def load_json(self):
        with open(resources.DATA, 'rt') as f_in:
            data = json.load(f_in)
        return data

    def start_training(self):
        self.btnStart.setVisible(False)
        self.btnStart.setEnabled(False)
        self.txtInput.setVisible(False)
        self.lblGreeting.setVisible(False)
        self.lcdTime.setVisible(False)
        self.lblTitle.setVisible(False)
        self.frame_menu.setVisible(False)

        self.rocket_timer()

    def rocket_timer(self):
        clock = QTimer(self)
        clock.timeout.connect(self.move_rocket)
        clock.start(80)

        self.move_rocket()

    def move_rocket(self):
        if self.lblShip.x() > 1200:
            self.txtInput.setVisible(True)
            self.lblGreeting.setVisible(True)
            self.lcdTime.setVisible(True)
            self.lblTitle.setVisible(True)
            self.frame_menu.setVisible(True)

            self.txtInput.setText("Blast off!")
        else:
            self.lblShip.move((self.lblShip.x() + 15), (self.lblShip.y() - 10))







