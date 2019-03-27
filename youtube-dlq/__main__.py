import sys

from PyQt5 import QtWidgets

from main_window import create_ui

if __name__ == '__main__':
    # create the QApplication that will manage this window
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("youtube-dlq")

    # create a window
    main_window = create_ui()
    main_window.show()

    # execute the application
    sys.exit(app.exec_())
