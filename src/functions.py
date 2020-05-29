import json

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
    with open("https://github.com/wingnut29/Nebula/blob/master/resources/backend/version.txt", 'rt') as in_file:
        version = in_file.read()
        for char in version:
            if char in ".":
                web_version = version.replace(char, "")
    return web_version
