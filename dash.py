import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMenu,QMenuBar, QWidget, QVBoxLayout,QDialog,QLineEdit
from PyQt6.QtGui import QPixmap,QAction,QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        # Set window properties
        self.setWindowTitle("DT DAY PLANNER")
        self.setGeometry(100, 100, 500, 210)
        self.setStyleSheet("background-color:#060d2e;color:#ffffff")
        self.app_icon=QIcon("images/time.png")
        self.setWindowIcon(self.app_icon)

        # Create widgets
        image_label = QLabel(self)
        pixmap = QPixmap("images/dashboard_image.png")
        image_label.setPixmap(pixmap)
        image_label.setGeometry(0, 0, 350, 300)

        normal_mode_button = QPushButton("Normal Mode", self)
        normal_mode_button.setGeometry(200, 50, 250, 45)
        normal_mode_button.clicked.connect(self.normal_mode_window)

        button2 = QPushButton("Advanced Mode", self)
        button2.setGeometry(200, 100, 250, 45)
        button2.clicked.connect(self.advanced_mode_window)

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

    def normal_mode_window(self):
        from sub_ui_tools import normal_mode_sub
        normal_mode_obj=normal_mode_sub()
        normal_mode_obj.exec()
        
    def advanced_mode_window(self):
        from sub_ui_tools import advanced_mode_sub
        advanced_mode_obj=advanced_mode_sub()
        advanced_mode_obj.exec()

    def open_window3(self):
        pass
    

    def show_about_dialog(self):
        about_dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel("Software Version: 0.0.1\nSoftware Type: Open Source\nDeveloper: DT Software Solutions")
        layout.addWidget(label)
        about_dialog.setLayout(layout)
        about_dialog.setWindowTitle("About Us")
        about_dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
