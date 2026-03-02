import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel #added QLabel
from PyQt5.QtGui import QIcon, QFont #added QFont
from PyQt5.QtCore import Qt #added for text alignment

"""
sys: This is a built-in Python module that provides access to variables and functions that interact with the Python interpreter.
PyQt5.QtWidgets: This module contains all the main GUI “widgets” such as buttons, labels, and windows.
QApplication: This class manages the GUI application itself.
QMainWindow: This class provides a main application window that you can customize.
"""

#Created a custom window:


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("woah my frist window yippe :D")
        self.setGeometry(00, 00, 500, 500) #(x, y, width, hight)
        #x: distance from the left edge of your screen
        #y: distance from the top of your screen
        self.setWindowIcon(QIcon("images/lil fella.png"))
        #added - labl:
        self.label = QLabel("Hello", self)
        #added - change label font size:
        self.label.setFont(QFont("Arial", 40))
        #added - placing label
        self.label.setGeometry(0, 0, 500, 100)
        self.label.setStyleSheet(
            # This is CSS!
            "color: rgb(0,150,255); " #Supports HEX, RGB!!!, and ColorNames
            "background-color: rgb(0,0,150);" #Supports HEX, RGB!, and ColorNames
            "border: 5px solid black;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"

        )
        self.label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv) # Creates the main application and passes in an y command line arguments
    window = MainWindow() #Instariate our main window
    window.show() #Make the window visible
    # Starts the application loop. The program will keep running until you close the window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()