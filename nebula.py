import sys

from PyQt5 import QtWidgets

from src import functions, main


def check_for_updates():
    if functions.check_app_version() == functions.check_hosted_version():
        functions.message_up_to_date()
    elif functions.check_app_version() < functions.check_hosted_version():
        value = functions.message_update_available()

        if value is not False:
            update_path = functions.update_app()
            functions.is_file_downloaded(update_path)
    # todo: finish checking for updates


def start():
    app = QtWidgets.QApplication(sys.argv)
    window = main.MainWindow()
    check_for_updates()
    app.exec_()
    functions.reset_json()


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(str(e))
