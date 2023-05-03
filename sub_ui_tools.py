import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton,QDialog,QMessageBox,QVBoxLayout,QCalendarWidget
from PyQt6.QtCore import QDate
from backend_core import Backend_core_module
backend_cur=Backend_core_module()
class normal_mode_sub(QDialog):

    def __init__(self):
        super().__init__()

        # Create the grid layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Create three vertical columns of 8 rows by 6 columns each
        self.activities = {}
        for j in range(3):
            for i in range(8):
                time_label = QLabel(str(i + j*8) +":00")
                grid.addWidget(time_label, i, j*2)
                input_box = QLineEdit()
                grid.addWidget(input_box, i, j*2 + 1)
                self.activities[(i + j*8)] = input_box
        
        
                

        # Create the submit butto
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_activities)
        grid.addWidget(submit_button, 24, 1)

        # Set the window title and show the widget
        self.setWindowTitle("Timetable for tomorrow!")
        self.setStyleSheet("background-color:#060d2e;color:#ffffff")
        self.show()


    def submit_activities(self):
        # Store the activities in a dictionary
        for i in range(24):
            backend_cur.normal_mode_activity_dict[i] = self.activities[i].text()
        import datetime
        current_date = QDate.currentDate()
        tomorrow_date = current_date.addDays(1)
        tomorrow_datetime = datetime.datetime(tomorrow_date.year(), tomorrow_date.month(), tomorrow_date.day())
        tomorrow_string = tomorrow_datetime.strftime('%Y-%m-%d')
        backend_cur.normal_mode_activity_dict['tomorrow_date']=tomorrow_string
        for key,value in backend_cur.normal_mode_activity_dict.items():
            if backend_cur.normal_mode_activity_dict[key]=='':
                backend_cur.normal_mode_activity_dict[key]='no_activity'
            else:
                pass
        print(backend_cur.normal_mode_activity_dict)
        backend_cur.test_table_submitter()

class advanced_mode_sub(QDialog):
    def __init__(self):
        super().__init__()
        self.advanced_mode_activities_dict={}
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

        #create a select date button
        date_button=QPushButton("Select Date")
        date_button.clicked.connect(self.date_picker_function)
        grid.addWidget(date_button,23,1)
        # Create the submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_activities)
        grid.addWidget(submit_button, 24, 1)

        # Set the window title and show the widget
        self.setWindowTitle("Timetable for a selected day")
        self.setStyleSheet("background-color:#060d2e;color:#ffffff")
        self.show()
    
    def submit_activities(self):
        # Store the activities in a dictionary
        for i in range(24):
            self.advanced_mode_activities_dict[i] = self.activities[i].text()
        for key,value in self.advanced_mode_activities_dict.items():
            if self.advanced_mode_activities_dict[key]=='':
                self.advanced_mode_activities_dict[key]='no_activity'
            else:
                pass
        print(self.advanced_mode_activities_dict)
        backend_cur.advanced_mode_submitter(self.advanced_mode_activities_dict)
        
    
    def date_picker_function(self):
        #store a date to my activities
        date_picker_app=DatePicker()
        date_picker_app.exec()
        self.advanced_mode_activities_dict['selected_date']=date_picker_app.return_selected_date()
        

class DatePicker(QDialog):

    def __init__(self):
        super().__init__()

        # Create a QCalendarWidget widget
        self.calendar = QCalendarWidget(self)

        # Set the current date as the selected date in the calendar
        self.calendar.setSelectedDate(QDate.currentDate())

        # Connect the selectionChanged signal to a slot
        self.calendar.selectionChanged.connect(self.return_selected_date)
        self.setStyleSheet("background-color:#060d2e;color:#ffffff")
        # Create a layout and add the QCalendarWidget widget to it
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        self.setLayout(layout)

    def return_selected_date(self):
        # Get the selected date from the calendar
        self.selected_date = self.calendar.selectedDate()
        msg_box = QMessageBox(QMessageBox.Icon.Question, "Date conformation!", f"Would you like to select the date {self.selected_date.toString('yyyy-MM-dd')}?")
        msg_box.addButton(QMessageBox.StandardButton.Yes)
        msg_box.addButton(QMessageBox.StandardButton.No)
        reply = msg_box.exec()
        
        
        # Check the user's response
        if reply == QMessageBox.StandardButton.Yes:
            return self.selected_date.toString('yyyy-MM-dd')
        else:
            pass