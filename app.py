'''

    @Author : Gökhan Özeloğlu
    @Date : 03.08.2018

'''


import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QLabel, QAction
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Name Creator Application"

        # Window's size and place
        self.left = 30
        self.top = 90
        self.width = 300
        self.height = 200

        # List definitions for storing names and surnames
        self.name_list = list()
        self.surname_list = list()
        self.read_files()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton("Create a new name", self)
        button.setToolTip("Create button")

        button.setGeometry(80, 75, 150, 60)     # Defines the place of button and sizes
        button.clicked.connect(self.on_click)   # Connects with on_click() function

        label = QLabel("Please push the button\n to create new name", self)
        label.setGeometry(80, 10, 200, 90)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")   # File menu is added

        # Exit button definition
        exit_button = QAction("Exit", self)
        exit_button.setShortcut("Ctrl+W")       # Shortcut is assigned
        exit_button.setStatusTip("Exit application")
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

        self.show()

    def main(self):
        name_list_length = len(self.name_list)          # Finds the number of names
        surname_list_length = len(self.surname_list)    # Finds the number of surnames

        random_name_number = random.randint(0, name_list_length)
        random_surname_number = random.randint(0, surname_list_length)

        return self.name_list[random_name_number][0] + " " + self.surname_list[random_surname_number][0]

    ''' This function just reads the input files '''
    def read_files(self):
        with open(sys.argv[1]) as name_file:
            for line in name_file:
                self.name_list.append(line.strip().split("\n"))

        with open(sys.argv[2]) as surname_file:
            for line in surname_file:
                self.surname_list.append(line.strip().split("\n"))

    @pyqtSlot()
    def on_click(self):
        print("Button is clicked")
        created_name = self.main()  # Calls main() function to create new names
        QMessageBox.question(self, "Result", "The created-name : " + created_name, QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())