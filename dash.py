import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QMenuBar,QAction
from PyQt6.QtGui import QPixmap

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'DT DAY PLANNER VERSION 0.0.1'
        self.left = 100
        self.top = 100
        self.width =700
        self.height = 400

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel(self)
        pixmap = QPixmap('image.jpeg').scaled(100,100) 
        label.setPixmap(pixmap)
        label.move(100, 100)

        menu_bar = QMenuBar(self)

        file_menu = menu_bar.addMenu('Help')

        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        
        self.setMenuBar(menu_bar)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
