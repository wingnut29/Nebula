import json
import os

from PyQt5.QtCore import QTime, QTimer
from win32api import GetSystemMetrics

from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtGui import QPixmap


from src import resources
from src import main
from src import functions


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(resources.SPLASH, self)
        self.start_timers()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        self.imgBackground.setPixmap(QPixmap(resources.BACKGROUND))
        self.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
        self.btnStart.clicked.connect(self.select_topic)
        self.btnInfo.clicked.connect(functions.feature_construction)
        self.btnRF.setEnabled(False)
        self.btnMod.setEnabled(False)
        self.btnRadar.setEnabled(False)
        self.btnWave.setEnabled(False)
        self.btnRF.setVisible(False)
        self.btnMod.setVisible(False)
        self.btnRadar.setVisible(False)
        self.btnWave.setVisible(False)

    def start_timers(self):
        clock = QTimer(self)
        clock.timeout.connect(self.get_time)
        clock.start(1000)

        self.get_time()

    def get_time(self):
        time = QTime.currentTime().toString("hh:mm")
        self.lcdTime.display(time)

    def select_topic(self):
        self.lblSubHeader.setVisible(False)
        self.btnStart.setVisible(False)
        self.btnStart.setEnabled(False)
        self.btnRF.setVisible(True)
        self.btnMod.setVisible(True)
        self.btnRadar.setVisible(True)
        self.btnWave.setVisible(True)
        self.btnWave.setEnabled(True)
        self.btnWave.clicked.connect(lambda: self.switch_window(main, "Wave Propagation"))
        # self.btnRadar.clicked.connect(lambda: self.switch_window(main, "Radar Principles"))
        # self.btnMod.clicked.connect(lambda: self.switch_window(main, "Modulation"))
        # self.btnRF.clicked.connect(lambda: self.switch_window(main, "Radio-Frequency Communication Principles"))

    def switch_window(self, ui, topic= None):
        self.window = ui.MainWindow(topic)
        self.window.show()
        self.close()
