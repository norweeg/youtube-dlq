from PyQt5 import QtGui, QtCore, QtWidgets

__supported_hosts__ = ("youtube.com", "youtu.be", "music.youtube.com")

class address_validator(QtGui.QValidator):
    def __init__(self, parent = None):
        super().__init__(parent)

    def validate(self, input, position):
        global __supported_hosts__
        url = QtCore.QUrl(input)
        
        if url.isValid() and url.host() in __supported_hosts__:
            return self.Acceptable
        elif url.isValid() and url.host() not in __supported_hosts__:
            return self.Intermediate
        else:
            return self.Invalid
