import getpass
import json
import os
from urllib.request import urlopen

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox, QWidget

from src import resources


def reset_json():
    central_widget = QWidget()
    try:
        with open(resources.DATA, 'rt') as f_in:
            data = json.load(f_in)

            data["COUNTER"] = 0
            data["SCORE"] = 0

        with open(resources.DATA, 'w') as json_file:
            json.dump(data, json_file, indent=4, sort_keys=True)
    except Exception as e:
        QMessageBox.warning(central_widget, "Error", "Cannot load backend. {}".format(e))


def load_json():
    central_widget = QWidget()
    try:
        with open(resources.DATA, 'rt') as f_in:
            data = json.load(f_in)
        return data
    except Exception as e:
        QMessageBox.warning(central_widget, "Error", "Cannot load backend. {}".format(e))


def save_json(data=None):
    central_widget = QWidget()
    try:
        with open(resources.DATA, 'w') as json_file:
            json.dump(data, json_file, indent=4, sort_keys=True)
    except Exception as e:
        QMessageBox.warning(central_widget, "Error", "Cannot load backend. {}".format(e))


def feature_construction():
    central_widget = QWidget()
    QMessageBox.warning(central_widget, "In-Progress", "Feature still under construction.")


def check_app_version():
    with open(resources.VERSION, 'rt') as in_file:
        version = in_file.read()
        for char in version:
            if char in ".":
                app_version = version.replace(char, "")
    return app_version


def check_hosted_version():
    try:
        with urlopen(
                "https://raw.githubusercontent.com/wingnut29/Nebula/master/resources/backend/version.txt") as web_file:
            version = (web_file.read()).decode()
            for char in version:
                if char in ".":
                    web_version = version.replace(char, "")
        return web_version
    except Exception:
        central_widget = QWidget()
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
        msg_box.setWindowTitle("Connection error")
        msg_box.setText("Cannot connect to the internet to check for updates."
                        "\nTo check for updates please check your connection.")
        msg_box.exec_()


def message_up_to_date():
    central_widget = QWidget()
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
    msg_box.setWindowTitle("Up to Date")
    msg_box.setText("This is the most up to date version.")
    msg_box.exec_()


def message_update_available():
    central_widget = QWidget()
    msg_box = QMessageBox()
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setWindowIcon(QtGui.QIcon(resources.WINDOW_ICON))
    msg_box.setWindowTitle("Update Available")
    msg_box.setText("Update available."
                    "\nWould you like to update now?")
    answer_input = msg_box.exec_()

    if answer_input == QMessageBox.Yes:
        # pass
        update_app()
    elif answer_input == QMessageBox.No:
        pass


def update_app():
    import requests
    central_widget = QWidget()
    user = getpass.getuser()
    working_dir = os.getcwd()

    os.chdir(('{}{}{}'.format('/Users/', user, '/Downloads')))

    url = "https://github.com/wingnut29/Nebula/raw/master/setup/nebula_setup.exe"
    r = requests.get(url, allow_redirects=True)
    open('nebula_updater.exe', 'wb').write(r.content)

    os.chdir(working_dir)

    # todo: pull updated version from github
