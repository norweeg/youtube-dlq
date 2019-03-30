import sys
from pathlib import Path
import platform

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.uic import loadUi

from validators import address_validator

_about = f"""
A Youtube-dlg work-alike.
"""

def _toggle_browser_control_buttons(main_window):
    history = main_window.webEngineView.history()

    main_window.back_button.setEnabled(history.canGoBack())
    main_window.forward_button.setEnabled(history.canGoForward())

    main_window.back_button.update()
    main_window.forward_button.update()

def create_ui():
    """Loads the UI from the .ui file and instantiates it and connects any signals which could not be connected in designer

    Returns:
        QMainWindow: The main window of the application
    """
    main_window = loadUi(Path(__file__).parent/"main_window.ui")
    try:
        if platform.system() == 'Darwin':
            style = QtWidgets.QStyleFactory.create('Macintosh')
        elif platform.system() == 'Windows':
            style = QtWidgets.QStyleFactory.create('Windows')
        elif platform.system() == 'Linux':
            if 'QtCurve' in QtWidgets.QStyleFactory.keys():
                style = QtWidgets.QStyleFactory.create('QtCurve')
            elif 'Breeze' in QtWidgets.QStyleFactory.keys():
                style = QtWidgets.QStyleFactory.create('Breeze')
            elif 'Oxygen' in QtWidgets.QStyleFactory.keys():
                style = QtWidgets.QStyleFactory.create('Oxygen')
            elif 'gtk2' in QtWidgets.QStyleFactory.keys():
                style = QtWidgets.QStyleFactory.create('gtk2')
            else:
                style = QtWidgets.QStyleFactory.create('Fusion')
        else:
            style = QtWidgets.QStyleFactory.create('Fusion')
    except:
        style = QtWidgets.QStyleFactory.create('Fusion')
    assert style
    QtWidgets.QApplication.instance().setStyle(style)
    style.polish(QtWidgets.QApplication.instance())
    #connect the about actions to the corresponding about message they should display when triggered
    main_window.actionAbout_Qt.triggered.connect(QtWidgets.QApplication.instance().aboutQt)
    main_window.actionAbout.triggered.connect(lambda: QtWidgets.QMessageBox.about(main_window, "Youtube-dlq", _about))
    #main_window.address_bar.setValidator(address_validator(parent = main_window.address_bar))
    main_window.address_bar.returnPressed.connect(lambda: main_window.webEngineView.load(QtCore.QUrl(main_window.address_bar.text())))
    main_window.back_button.setIcon(style.standardIcon(style.SP_ArrowBack))
    main_window.forward_button.setIcon(style.standardIcon(style.SP_ArrowForward))
    main_window.reload_button.setIcon(style.standardIcon(style.SP_BrowserReload))
    main_window.browse_button.setIcon(style.standardIcon(style.SP_FileDialogStart))
    main_window.add_button.setIcon(style.standardIcon(style.SP_ArrowDown))
    main_window.webEngineView.urlChanged.connect(lambda url: main_window.address_bar.setText(url.toString()))
    main_window.webEngineView.loadStarted.connect(lambda: _toggle_browser_control_buttons(main_window))
    main_window.webEngineView.loadFinished.connect(lambda x: _toggle_browser_control_buttons(main_window))
    return main_window
