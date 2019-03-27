from PyQt5 import QtGui, QtCore, QtWidgets

__supported_hosts__ = ("youtube.com", "youtu.be", "music.youtube.com")

class address_validator(QtGui.QValidator):
    def __init__(self, parent = None):
        super().__init__(parent)

    def validate(self, input, position):
        global __supported_hosts__
        url = QtCore.QUrl(input)
        
        if not url.isValid():
            return QtGui.QValidator.Invalid
        elif not url.host() in __supported_hosts__:
            QtWidgets.QErrorMessage(parent = self.parent()).showMessage(f"{url.host()} is not a supported domain.")
            return QtGui.QValidator.Invalid
        else:
            return QtGui.QValidato.Acceptable