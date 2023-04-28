import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel

class Timetable(QWidget):
    def __init__(self):
        super().__init__()

        # Create the grid layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Create the time labels
        for i in range(24):
            label = QLabel(str(i) + ":00")
            grid.addWidget(label, i, 0)

        # Create the event labels
        for i in range(24):
            label = QLabel("No event")
            grid.addWidget(label, i, 1)

        # Set the window title and show the widget
        self.setWindowTitle("Timetable")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    timetable = Timetable()
    sys.exit(app.exec())
