import sys
import os
from PySide6 import QtWidgets, QtCore, QtMultimedia


class Player(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.currentFiles = []
        self.listTrack = QtWidgets.QListWidget()
        self.buttonGet = QtWidgets.QPushButton("pause")
        self.buttonPrev = QtWidgets.QPushButton("<")
        self.buttonNext = QtWidgets.QPushButton(">")
        self.buttonFiles = QtWidgets.QPushButton("files")
        self.baseLayout = QtWidgets.QVBoxLayout(self)
        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.addWidget(self.buttonPrev)
        buttonLayout.addWidget(self.buttonGet)
        buttonLayout.addWidget(self.buttonNext)
        buttonLayout.addWidget(self.buttonFiles)
        self.buttonFiles.clicked.connect(self.getFiles)
        self.listTrack.itemDoubleClicked.connect(self.dummy)
        self.baseLayout.addLayout(buttonLayout)
        self.baseLayout.addWidget(self.listTrack)

    @QtCore.Slot()
    def getFiles(self):
        files = QtWidgets.QFileDialog().getOpenFileNames()
        print(files)
        self.currentFiles.clear()
        self.currentFiles = files[0]
        for file in self.currentFiles:
            self.listTrack.addItem(file)

    @QtCore.Slot()
    def dummy(self):
        print("hello")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Player()
    widget.resize(800, 400)
    widget.show()
    sys.exit(app.exec())
