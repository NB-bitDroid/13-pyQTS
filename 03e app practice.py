import sys
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QFont, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid stuff")
        self.setGeometry(700, 300, 400, 400)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        label1 = QLabel()
        self.pixmap = QPixmap("images/download.png")
        label1.setPixmap(self.pixmap)
        label1
        label2 = QLabel()
        self.pixmap = QPixmap("images/NEONgreen.png")
        label2.setPixmap(self.pixmap)
        label3 = QLabel()
        self.pixmap = QPixmap("images/download.png")
        label3.setPixmap(self.pixmap)
        label4 = QLabel()
        self.pixmap = QPixmap("images/NEONgreen.png")
        label4.setPixmap(self.pixmap)
        label5 = QLabel()
        self.pixmap = QPixmap("images/Mr._T.png")
        label5.setPixmap(self.pixmap)

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 1, 2)
        grid.addWidget(label3, 0, 2)
        grid.addWidget(label4, 1, 0)
        grid.addWidget(label5, 0, 1)
        self.central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()