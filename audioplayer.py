import sys
import os
from PySide6 import QtWidgets, QtCore, QtMultimedia


class Audioplayer(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.currentFiles = []
        self.setWindowTitle("Audioplayer")
        self.currentTrackIndex = 0
        self.mediaPlayer = QtMultimedia.QMediaPlayer()
        self.audioOutput = QtMultimedia.QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.audioOutput.setVolume(50)
        self.listTrack = QtWidgets.QListWidget()
        self.buttonPause = QtWidgets.QPushButton("pause")
        self.buttonPlay = QtWidgets.QPushButton("play")
        self.buttonPrev = QtWidgets.QPushButton("<")
        self.buttonNext = QtWidgets.QPushButton(">")
        self.buttonFiles = QtWidgets.QPushButton("files")
        self.baseLayout = QtWidgets.QVBoxLayout(self)
        self.progressBar = QtWidgets.QProgressBar()
        self.currentTrack = QtWidgets.QLabel()
        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.addWidget(self.buttonPrev)
        buttonLayout.addWidget(self.buttonPause)
        buttonLayout.addWidget(self.buttonPlay)
        buttonLayout.addWidget(self.buttonNext)
        buttonLayout.addWidget(self.buttonFiles)
        buttonLayout.addWidget(self.progressBar)
        self.buttonFiles.clicked.connect(self.getFiles)
        self.buttonNext.clicked.connect(lambda: self.nextTrack(1))
        self.buttonPrev.clicked.connect(lambda: self.nextTrack(-1))
        self.buttonPause.clicked.connect(self.pause)
        self.buttonPlay.clicked.connect(self.play)
        self.listTrack.itemDoubleClicked.connect(self.dummy)
        self.baseLayout.addLayout(buttonLayout)
        self.baseLayout.addWidget(self.currentTrack)
        self.baseLayout.addWidget(self.listTrack)

    @QtCore.Slot()
    def getFiles(self):
        files = QtWidgets.QFileDialog().getOpenFileNames()
        print(files[0])
        self.currentFiles.clear()
        self.listTrack.clear()
        self.currentTrackIndex = 0
        if files[0]:
            self.currentTrack.setText(files[0][0])
        self.currentFiles = list(filter(lambda x: x.endswith(".mp3"),
                                        files[0]))
        for file in self.currentFiles:
            self.listTrack.addItem(file)

    @QtCore.Slot()
    def dummy(self):
        self.currentTrack.setText(self.listTrack.currentItem().text())
        path = QtCore.QUrl.fromLocalFile(self.listTrack.currentItem().text())
        self.currentTrackIndex = self.listTrack.currentRow()
        self.mediaPlayer.setSource(path)
        print(self.mediaPlayer.source())
        self.mediaPlayer.play()

    @QtCore.Slot()
    def nextTrack(self, i):
        self.currentTrackIndex = (self.currentTrackIndex +
                                  i) % self.listTrack.count()
        self.listTrack.setCurrentRow(self.currentTrackIndex)
        self.currentTrack.setText(self.listTrack.currentItem().text())
        self.mediaPlayer.stop()
        self.dummy()

    @QtCore.Slot()
    def pause(self):
        self.mediaPlayer.pause()

    @QtCore.Slot()
    def play(self):
        self.mediaPlayer.play()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Audioplayer()
    # widget.resize(800, 400)
    widget.show()
    sys.exit(app.exec())
