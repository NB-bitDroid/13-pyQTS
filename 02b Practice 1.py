import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel 
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello!")
        self.setGeometry(00, 00, 800, 600)
        self.setWindowIcon(QIcon("images/download.png"))
        self.label = QLabel("Hello", self)
        self.label2 = QLabel("Hi", self)
        self.label3 = QLabel("Text", self)
        self.label.setFont(QFont("Arial", 40))
        self.label.setGeometry(0, 0, 600, 100)
        self.label.setStyleSheet(
            "color: rgb(0,255,0); "
            "background-color: rgb(255,0,255);"
            "border: 5px solid red;"
            "font-weight: bold;"
            "font-style: italic;"


        )
        self.label2.setFont(QFont("Arial", 40))
        self.label2.setGeometry(00, 100, 200, 300)
        self.label2.setStyleSheet(
            "color: rgb(0,255,0); "
            "background-color: rgb(255,0,255);"
            "border: 5px solid red;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"

        )
        self.label3.setFont(QFont("Arial", 40))
        self.label3.setGeometry(200, 100, 400, 300)
        self.label3.setStyleSheet(
            "color: rgb(0,255,255); "
            "background-color: rgb(90,255,90);"
            "border: 5px solid red;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"

        )
        self.label.setAlignment(Qt.AlignCenter)

        self.piclabel = QLabel(self)
        self.piclabel.setGeometry(0, 200, 300, 250)
        self.pixmap = QPixmap("images/download.png")
        self.piclabel.setPixmap(self.pixmap)
        self.piclabel.setScaledContents(True) 
        self.piclabel.setGeometry(600, 0, 200, 600)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.label.setAlignment(Qt.AlignCenter)

        self.piclabel = QLabel(self)
        self.piclabel.setGeometry(0, 100, 300, 250)
        self.pixmap = QPixmap("images/NEONgreen (1).png")
        self.piclabel.setPixmap(self.pixmap)
        self.piclabel.setScaledContents(True) 
        self.piclabel.setGeometry(0, 550, 600, 50)
        self.label.setAlignment(Qt.AlignCenter)

        self.label.setAlignment(Qt.AlignCenter)

        self.piclabel = QLabel(self)
        self.piclabel.setGeometry(0, 100, 300, 250)
        self.pixmap = QPixmap("images/NEONPINK.jpg")
        self.piclabel.setPixmap(self.pixmap)
        self.piclabel.setScaledContents(True) 
        self.piclabel.setGeometry(0, 400, 600, 150)
        self.label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()