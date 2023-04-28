import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

class Planner(QWidget):
    def __init__(self):
        super().__init__()

        # Create the grid layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Create three vertical columns of 8 rows by 6 columns each
        self.activities = {}
        for j in range(3):
            for i in range(8):
                time_label = QLabel(str(i + j*8) + ":00")
                grid.addWidget(time_label, i, j*2)
                input_box = QLineEdit()
                grid.addWidget(input_box, i, j*2 + 1)
                self.activities[(i + j*8)] = input_box

        # Create the submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_activities)
        grid.addWidget(submit_button, 24, 1)

        # Set the window title and show the widget
        self.setWindowTitle("Timetable for tomorrow!")
        self.setStyleSheet("background-color:#8a96f2;")
        self.show()

    def submit_activities(self):
        # Store the activities in a dictionary
        activities_dict = {}
        for i in range(24):
            activities_dict[i] = self.activities[i].text()

def start():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        planner = Planner()
        sys.exit(app.exec())

