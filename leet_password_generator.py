from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
import sys



class Window(QMainWindow):
    leet_table = {
        "A":("4", "@"),
        "B":("8", "|3"),
        "C":("(", "<"),
        "D":("|)", "[)"),
        "E":("3", "€"),
        "F":("|=", "ph"),
        "G":("6", "9"),
        "H":("|-|", "#"),
        "I":("1", "!"),
        "J":("_|", "_/"),
        "K":("|<", "|{"),
        "L":("1", "|_"),
        "M":("//\\", "|/|"),
        "N":("||", "//"),
        "O":("0", "()"),
        "P":("|*", "|o"),
        "Q":("0_", "(,)"),
        "R":("|2", "12"),
        "S":("5", "$"),
        "T":("7", "+"),
        "U":("|_|", "(_)"),
        "V":("/", "|"),
        "W":("//", "vv"),
        "X":("><", "}{"),
        "Y":("'/", "j"),
        "Z":("2", "7_"),
    }

    def __init__(self):
        super().__init__()
        self.setGeometry(300,400,700,395)
        self.index = 0
        #create a line edit widget:

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(10, 10, 270, 40)
        self.line_edit.setPlaceholderText("Enter your password:")
        self.assignStyleSheet(self.line_edit)

        self.button = QPushButton("Submit", self)
        self.button.setGeometry(280,10,100,40)
        self.assignStyleSheet(self.button)
        self.button.clicked.connect(self.submit)

        self.button1 = QPushButton("option1", self)
        self.button1.setGeometry(385,10,100,40)
        self.assignStyleSheet(self.button1)

        self.button2 = QPushButton("option2", self)
        self.button2.setGeometry(485,10,100,40)
        self.assignStyleSheet(self.button2)
        self.button2.clicked.connect(self.option2)

        self.label = QLabel(self)
        self.label.setText("Leek speak password:")
        self.label.setGeometry(10, 60, 1000, 40)
        self.assignStyleSheet(self.label)

        self.piclabel = QLabel(self)
        self.piclabel.setGeometry(0, 100, 300, 300)
        self.pixmap = QPixmap("images/lock.png")
        self.piclabel.setPixmap(self.pixmap)

    def option2(self):
        self.index = 1

    def submit(self):
        text = self.line_edit.text()
        text = text.upper()
        for letter in text:    
            try:
                text = text.replace(letter, self.leet_table[letter][int(self.index)])
            except KeyError:
                continue
        self.label.setText(f"{text}")
        self.index = 0

    def assignStyleSheet(self, obj):
        obj.setStyleSheet("""
            font-size: 25px;
            font-family: Arial
        """)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())