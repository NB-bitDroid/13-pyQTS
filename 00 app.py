import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
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

def main():
    app = QApplication(sys.argv) # Creates the main application and passes in an y command line arguments
    window = MainWindow() #Instariate our main window
    window.show() #Make the window visible
    # Starts the application loop. The program will keep running until you close the window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()