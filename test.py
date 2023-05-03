import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

class ActivityWindow(QWidget):
    def __init__(self, activities, parent=None):
        super().__init__(parent)
        self.activities = activities
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        for i in range(24):
            hour_label = QLabel(f"{i}:00 - {i+1}:00")
            activity_label = QLabel(self.activities[i])
            grid.addWidget(hour_label, i % 12, i // 12 * 2)
            grid.addWidget(activity_label, i % 12, i // 12 * 2 + 1)
        
        self.setLayout(grid)
        self.setWindowTitle('Activities for the day')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    activities = ['Sleep', 'Work', 'Lunch', 'Meeting', 'Work', 'Work', 'Work', 'Break', 'Work', 'Work', 'Dinner', 'Relax',
                  'Sleep', 'Work', 'Lunch', 'Meeting', 'Work', 'Work', 'Work', 'Break', 'Work', 'Work', 'Dinner', 'Relax']
    activity_window = ActivityWindow(activities)
    sys.exit(app.exec())
