import sys
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.uic import loadUi

from validators import address_validator

_about = f"""
A Youtube-dlg work-alike.
"""


def create_ui():
    """Loads the UI from the .ui file and instantiates it and connects any signals which could not be connected in designer

    Returns:
        QMainWindow: The main window of the application
    """
    main_window = loadUi(Path(__file__).parent/"main_window.ui")
    #connect the about actions to the corresponding about message they should display when triggered
    main_window.actionAbout_Qt.triggered.connect(QtWidgets.QApplication.instance().aboutQt)
    main_window.actionAbout.triggered.connect(lambda: QtWidgets.QMessageBox.about(main_window, "Youtube-dlq", _about))
    main_window.address_bar.setValidator(address_validator(parent = main_window))
    main_window.address_bar.returnPressed.connect(lambda: main_window.webEngineView.load(QtCore.QUrl(main_window.address_bar.text())))
    return main_window