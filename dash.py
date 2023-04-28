import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMenu,QMenuBar, QWidget, QVBoxLayout,QDialog,QLineEdit
from PyQt6.QtGui import QPixmap,QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle("DT DAY PLANNER")
        self.setGeometry(100, 100, 500, 210)
        self.setStyleSheet("background-color:#8a96f2;")

        # Create widgets
        image_label = QLabel(self)
        pixmap = QPixmap("dashboard_image.png").scaled(150,175)
        image_label.setPixmap(pixmap)
        image_label.setGeometry(0, 0, 350, 300)

        button1 = QPushButton("Normal Mode", self)
        button1.setGeometry(200, 50, 250, 45)
        button1.clicked.connect(self.open_window1)

        button2 = QPushButton("Advanced Mode", self)
        button2.setGeometry(200, 100, 250, 45)
        button2.clicked.connect(self.open_window2)

        button3 = QPushButton("View today", self)
        button3.setGeometry(200, 150, 250, 45)
        button3.clicked.connect(self.open_window3)

        # Create menu bar
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        help_menu = menu_bar.addMenu("Help")

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        about_action = QAction("About Us", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

        # Show main window
        self.show()

    def open_window1(self):
        window1 = QWidget()
        layout = QVBoxLayout()
        label = QLabel("This is Window 1")
        layout.addWidget(label)
        window1.setLayout(layout)
        window1.setGeometry(200, 200, 300, 200)
        window1.show()

    def open_window3(self):
        pass


    def open_window2(self):
        window2 = QDialog()
        layout = QVBoxLayout()

        # Add form fields
        name_label = QLabel("Name:")
        name_input = QLineEdit()
        layout.addWidget(name_label)
        layout.addWidget(name_input)

        email_label = QLabel("Email:")
        email_input = QLineEdit()
        layout.addWidget(email_label)
        layout.addWidget(email_input)

        phone_label = QLabel("Phone:")
        phone_input = QLineEdit()
        layout.addWidget(phone_label)
        layout.addWidget(phone_input)

        # Add submit button
        submit_button = QPushButton("Submit")
        layout.addWidget(submit_button)

        # Set layout
        window2.setLayout(layout)
        window2.setWindowTitle("Create day plan for tomorrow ")
        window2.setGeometry(200, 200, 300, 200)
        window2.exec()
    

    def show_about_dialog(self):
        about_dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel("This is the About Us dialog")
        layout.addWidget(label)
        about_dialog.setLayout(layout)
        about_dialog.setWindowTitle("About Us")
        about_dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
