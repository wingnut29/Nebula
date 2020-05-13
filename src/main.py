import json
import os

from PyQt5.QtCore import QTime, QTimer
from win32api import GetSystemMetrics

from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from src import resources


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, topic = ""):
        super(MainWindow, self).__init__()
        uic.loadUi(resources.MAIN_WINDOW, self)
        self.start_timers()
        self.setup_ui(topic)
        self.show()

        data = self.load_json()

        self.btnStart.clicked.connect(lambda : self.start(data))
        self.btnNext.clicked.connect(lambda: self.next_question(data))

    def setup_ui(self, topic):
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        self.lblSubHeader.setText(topic)

        self.frame_menu.setVisible(False)

        self.imgBackground.setPixmap(QPixmap(resources.BACKGROUND))
        self.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
        self.btnStart.setIcon(QtGui.QIcon(resources.BTN_START))
        self.btnNext.setIcon(QtGui.QIcon(resources.RIGHT_ARROW))
        self.btnNext.setEnabled(False)
        self.btnNext.setVisible(False)

        self.lbl100.setVisible(False)
        self.lbl200.setVisible(False)
        self.lbl300.setVisible(False)
        self.lbl400.setVisible(False)
        self.lbl500.setVisible(False)
        self.lbl1000.setVisible(False)
        self.lbl2000.setVisible(False)
        self.lbl4000.setVisible(False)
        self.lbl8000.setVisible(False)
        self.lbl16T.setVisible(False)
        self.lbl32T.setVisible(False)
        self.lbl64T.setVisible(False)
        self.lbl125T.setVisible(False)
        self.lbl250T.setVisible(False)
        self.lbl500T.setVisible(False)
        self.lblMillion.setVisible(False)

        self.btnChoiceA.setVisible(False)
        self.btnChoiceB.setVisible(False)
        self.btnChoiceC.setVisible(False)
        self.btnChoiceD.setVisible(False)

    def start_timers(self):
        clock = QTimer(self)
        clock.timeout.connect(self.get_time)
        clock.start(1000)

        self.get_time()

    def get_time(self):
        time = QTime.currentTime().toString("hh:mm")
        self.lcdTime.display(time)

    def load_json(self):
        try:
            with open(resources.DATA, 'rt') as f_in:
                data = json.load(f_in)
            return data
        except Exception as e:
            QMessageBox.warning(self, "Error", "Cannot load backend. {}".format(e))

    def save_json(self, data=None):
        try:
            with open(resources.DATA, 'w') as json_file:
                json.dump(data, json_file, indent=4, sort_keys=True)
        except Exception as e:
            QMessageBox.warning(self, "Error", "Cannot load backend. {}".format(e))

    def start(self, data=None):
        self.frame_menu.move(230, 140)
        self.frame_menu.setVisible(True)
        self.lbl100.setVisible(True)
        self.lbl200.setVisible(True)
        self.lbl300.setVisible(True)
        self.lbl400.setVisible(True)
        self.lbl500.setVisible(True)
        self.lbl1000.setVisible(True)
        self.lbl2000.setVisible(True)
        self.lbl4000.setVisible(True)
        self.lbl8000.setVisible(True)
        self.lbl16T.setVisible(True)
        self.lbl32T.setVisible(True)
        self.lbl64T.setVisible(True)
        self.lbl125T.setVisible(True)
        self.lbl250T.setVisible(True)
        self.lbl500T.setVisible(True)
        self.lblMillion.setVisible(True)

        self.btnStart.setVisible(False)
        self.btnStart.setEnabled(False)
        self.lblSubHeader.setVisible(False)
        self.btnNext.setEnabled(True)
        self.btnNext.setVisible(True)

        self.btnChoiceA.setVisible(True)
        self.btnChoiceB.setVisible(True)
        self.btnChoiceC.setVisible(True)
        self.btnChoiceD.setVisible(True)

        self.next_question(data)

    def next_question(self, data=None):
        count = data["COUNTER"]

        if count < len(data["QUESTIONS"]):
            for question in data["QUESTIONS"][count].keys():
                txt_question = question

            self.txtInput.setText(txt_question)

            for choices in data["QUESTIONS"][count].values():
                list_choices = choices

            self.btnChoiceA.setText(list_choices[0])
            self.btnChoiceB.setText(list_choices[1])
            self.btnChoiceC.setText(list_choices[2])
            self.btnChoiceD.setText(list_choices[3])

            count += 1
            data["COUNTER"] = count

            self.save_json(data)
        else:
            print("end")
