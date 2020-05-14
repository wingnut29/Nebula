import json

from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from src import functions
from src import main
from src import resources


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, topic=None):
        super(MainWindow, self).__init__()
        uic.loadUi(resources.HOME, self)
        self.window = None
        self.start_timers()
        self.setup_ui(topic)
        self.show()

        data = self.load_json()

        self.btnStart.clicked.connect(lambda: self.start(data))
        # self.btnNext.clicked.connect(lambda: self.next_question(data))
        self.btnBack.clicked.connect(lambda: self.switch_window(main))
        self.btnChoiceA.clicked.connect(lambda: self.check_answer(data, self.btnChoiceA))
        self.btnChoiceB.clicked.connect(lambda: self.check_answer(data, self.btnChoiceB))
        self.btnChoiceC.clicked.connect(lambda: self.check_answer(data, self.btnChoiceC))
        self.btnChoiceD.clicked.connect(lambda: self.check_answer(data, self.btnChoiceD))

    def setup_ui(self, topic):
        self.lblSubHeader.setText(topic)

        self.frame_menu.setVisible(False)

        self.imgBackground.setPixmap(QPixmap(resources.BACKGROUND))
        self.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
        self.btnStart.setIcon(QtGui.QIcon(resources.BTN_START))
        self.btnBack.setIcon(QtGui.QIcon(resources.LEFT_ARROW))
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
        # self.btnNext.setEnabled(True)
        # self.btnNext.setVisible(True)

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

        elif count >= len(data["QUESTIONS"]):
            if data["SCORE"] == len(data["QUESTIONS"]):
                self.frame_menu.setVisible(False)
                msgBox = QMessageBox()
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
                msgBox.setWindowTitle("END")
                msgBox.setText("You finished and answered all question correctly!\n" +
                               "You won {} DOLLARS! (if only it were real)\n".format(data["MONEY"][data["SCORE"]]) +
                               "Would you like to play again?")
                answer_input = msgBox.exec_()

            if answer_input == QMessageBox.Yes:
                self.switch_window(main)
            elif answer_input == QMessageBox.No:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
                msgBox.setWindowTitle("Exit")
                msgBox.setText("Thank you for playing!")
                msgBox.exec_()
                self.close()

    def check_answer(self, data, button):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
        count = data["COUNTER"]
        money_label = self.check_money(data)

        if button.text() == data["Q_ANSWERS"][count]:
            msgBox.setWindowTitle("Correct")
            msgBox.setText("{}: Answer- '{}'".format("Correct!", button.text()))
            msgBox.exec_()
            money_label.setStyleSheet("QLabel{background-color: rgb(0, 255, 0);"
                                      "border-radius:10px;"
                                      "border: 2px solid #000000;}")
            count += 1
            data["COUNTER"] = count
            data["SCORE"] += 1
            self.save_json(data)
            self.next_question(data)

        elif button.text() != data["Q_ANSWERS"][count]:
            money_label.setStyleSheet("QLabel{background-color: rgb(255, 0, 0);"
                                      "border-radius:10px;"
                                      "border: 2px solid #000000;}")
            if count == 0:
                msgBox.setWindowTitle("Incorrect")
                msgBox.setText("Sorry that is incorrect.\n"
                               "You missed the first question.")
                msgBox.exec_()
            else:
                msgBox.setWindowTitle("Incorrect")
                msgBox.setText("Sorry that is incorrect.\n"
                               "You made it to {}".format(data["MONEY"][count]))
                msgBox.exec_()
            self.switch_window(main)

    def check_money(self, data):
        count = data["COUNTER"]
        if count == 0:
            return self.lbl100
        elif count == 1:
            return self.lbl200
        elif count == 2:
            return self.lbl300
        elif count == 3:
            return self.lbl400
        elif count == 4:
            return self.lbl500
        elif count == 5:
            return self.lbl1000
        elif count == 6:
            return self.lbl2000
        elif count == 7:
            return self.lbl4000
        elif count == 8:
            return self.lbl8000
        elif count == 9:
            return self.lbl16T
        elif count == 10:
            return self.lbl32T
        elif count == 11:
            return self.lbl64T
        elif count == 12:
            return self.lbl125T
        elif count == 13:
            return self.lbl250T
        elif count == 14:
            return self.lblMillion

    def switch_window(self, ui):
        self.window = ui.MainWindow()
        self.window.show()
        self.close()
        functions.reset_json()
