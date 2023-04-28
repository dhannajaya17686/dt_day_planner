import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class Form(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Form')
        self.setGeometry(100, 100, 400, 200)

        self.name_label = QLabel('Name:', self)
        self.name_label.move(50, 50)
        self.name_input = QLineEdit(self)
        self.name_input.move(150, 50)

        self.email_label = QLabel('Email:', self)
        self.email_label.move(50, 80)
        self.email_input = QLineEdit(self)
        self.email_input.move(150, 80)


        self.submit_button = QPushButton('Submit', self)
        self.submit_button.move(150, 120)
        self.submit_button.clicked.connect(self.submit)

    def submit(self):
        name = self.name_input.text()
        email = self.email_input.text()
        print(f"Name: {name}\nEmail: {email}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
