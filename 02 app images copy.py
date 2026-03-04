import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel 
from PyQt5.QtGui import QIcon, QFont, QPixmap #QPixmap loads and manages the image file before
from PyQt5.QtCore import Qt 

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
        self.setWindowIcon(QIcon("images/download.png"))
        self.label = QLabel("Hello", self)
        self.label.setFont(QFont("Arial", 40))
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

        self.piclabel = QLabel(self)
        self.piclabel.setGeometry(0, 100, 300, 250)
        self.pixmap = QPixmap("images/download.png")
        #put the image (pixmap) into the label
        self.piclabel.setPixmap(self.pixmap)
        #if image is too big or too small, we can make it fit our container.
        self.piclabel.setScaledContents(True) 
        #let's try putting the lil fella in the bottom right corner - we'll use MATH
        self.piclabel.setGeometry(self.width(
        ) - self.piclabel.width(), self.height() - self.piclabel.height(), 300, 250)

        # % is mod, // is integer division
        #let's try putting greg in the middle - we'll use MATH



def main():
    app = QApplication(sys.argv) # Creates the main application and passes in an y command line arguments
    window = MainWindow() #Instariate our main window
    window.show() #Make the window visible
    # Starts the application loop. The program will keep running until you close the window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()