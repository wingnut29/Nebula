import json

from PyQt5.QtWidgets import QMessageBox, QWidget

from src import resources


def reset_json():
    central_widget = QWidget()
    try:
        with open(resources.DATA, 'rt') as f_in:
            data = json.load(f_in)

            data["COUNTER"] = 0

        with open(resources.DATA, 'w') as json_file:
            json.dump(data, json_file, indent=4, sort_keys=True)
    except Exception as e:
        QMessageBox.warning(central_widget, "Error", "Cannot load backend. {}".format(e))


def feature_construction():
    central_widget = QWidget()
    QMessageBox.warning(central_widget, "In-Progress", "Feature still under construction.")