import sys
from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt6.QtCore import Qt, QBasicTimer

class ProgressBarDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('Progress Bar Demo')

        self.progress = QProgressBar(self)
        self.progress.setGeometry(50, 50, 200, 20)

        self.start_button = QPushButton('Start', self)
        self.start_button.move(50, 90)
        self.start_button.clicked.connect(self.startProgress)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.move(160, 90)
        self.stop_button.clicked.connect(self.stopProgress)

        self.timer = QBasicTimer()
        self.step = 0

        self.show()

    def startProgress(self):
        if self.timer.isActive():
            return

        self.timer.start(100, self)

    def stopProgress(self):
        if self.timer.isActive():
            self.timer.stop()
            self.step = 0
            self.progress.setValue(0)

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            return

        self.step += 1
        self.progress.setValue(self.step)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ProgressBarDemo()
    sys.exit(app.exec())
