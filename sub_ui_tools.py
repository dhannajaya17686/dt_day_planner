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
        backend_cur.tomorrow_checker()
        if backend_cur.tomorrow_checker()==True:
            reply=ui_message_api().ask_message_box('Warning!','Another record found for this date would you like to delte it?')
            if reply==QMessageBox.StandardButton.Yes:
                backend_cur.tomorrow_remover()
                backend_cur.normal_mode_submitter()
            else:
                pass
        else:
            backend_cur.normal_mode_submitter()
            if backend_cur.normal_mode_submitter()==True:
                ui_message_api().info_msg('Success!','Data Inserted correctly!')
            else:
                ui_message_api().warning_msg('Warning','Data not inserted!')
        
        


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
            backend_cur.advanced_mode_activity_dict[i] = self.activities[i].text()
        for key,value in backend_cur.advanced_mode_activity_dict.items():
            if backend_cur.advanced_mode_activity_dict[key]=='':
                backend_cur.advanced_mode_activity_dict[key]='no_activity'
            else:
                pass
        try:
            if backend_cur.advanced_mode_submitter()==True:
                ui_message_api().info_msg('Success!','Data inserted successfully!')
        except KeyError:
            ui_message_api().warning_msg('Warning!','Please pick a date before submitting!')
        
    
    def date_picker_function(self):
        #store a date to my activities
        date_picker_app=DatePicker()
        date_picker_app.exec()
        backend_cur.advanced_mode_activity_dict['selected_date']=date_picker_app.return_selected_date()
    


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

class ui_message_api():
    def __init__(self):
        self.msg_obj=QMessageBox()
    
    def info_msg(self,title:str,text:str)->True:
        self.msg_obj.setIcon(QMessageBox.Icon.Information)
        self.msg_obj.setWindowTitle(title)
        self.msg_obj.setText(text)
        self.msg_obj.exec()
        return True
    
    def warning_msg(self,title:str,text:str)->True:
        self.msg_obj.setIcon(QMessageBox.Icon.Warning)
        self.msg_obj.setWindowTitle(title)
        self.msg_obj.setText(text)
        self.msg_obj.exec()
        return True
    
    def ask_message_box(self,title:str,text:str)->True:
        msg_box = QMessageBox(QMessageBox.Icon.Question,title,text)
        msg_box.addButton(QMessageBox.StandardButton.Yes)
        msg_box.addButton(QMessageBox.StandardButton.No)
        return msg_box.exec()

    
class View_activity_today(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        try:           
            for i in range(24):
                self.activities_normal = backend_cur.normal_mode_show()[0][2:26]
                hour_label = QLabel(f"{i}:00 - {i+1}:00")
                activity_label = QLabel(self.activities_normal[i])
                grid.addWidget(hour_label, i % 12, i // 12 * 2)
                grid.addWidget(activity_label, i % 12, i // 12 * 2 + 1)
        except IndexError:
            try:
                for i in range(24):
                    self.activities_override=backend_cur.today_activities_show()[0][2:26]
                    hour_label = QLabel(f"{i}:00 - {i+1}:00")
                    activity_label = QLabel(self.activities_override[i])
                    grid.addWidget(hour_label, i % 12, i // 12 * 2)
                    grid.addWidget(activity_label, i % 12, i // 12 * 2 + 1)
            except IndexError:
                ui_message_api().warning_msg('Warning','You have no activities for today!\nIn case if you have forgotten to add activities to today do it using advanced mode')

        self.setLayout(grid)
        self.setWindowTitle('Activities for the day')
        self.show()