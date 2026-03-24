from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel
import sys
#QApplication - Runs the GUI (Graphical User Interface)
#QMainWindow - Creates the main application window
#Qline Edit - Creates a text box
#QPushButton - Creates a clickable button
# DRY princable means Dont Reapet Yourself
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,400,400,200)
        #create a line edit widget:

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(10, 10, 210, 40)
        self.line_edit.setPlaceholderText("Enter your name:")
        self.assignStyleSheet(self.line_edit)

        self.button = QPushButton("Submit", self)
        self.button.setGeometry(220,10,100,40)
        self.assignStyleSheet(self.button)
        self.button.clicked.connect(self.submit)

        self.label = QLabel(self)
        self.label.setText("Hello World")
        self.label.setGeometry(10, 60, 200, 40)
        self.assignStyleSheet(self.label)


    def submit(self):
        text = self.line_edit.text()
        self.label.setText(f"Hello {text}!")    


    def assignStyleSheet(self, obj):
        obj.setStyleSheet("""
            font-size: 25px;
            font-family: Arial
        """)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())



"""
Create a new application called leet password generator.
The user will put a phrase in the line edit textbox, click a button and you will put a
"leet" encode string.
Include and image that sybolizes a password.

"""