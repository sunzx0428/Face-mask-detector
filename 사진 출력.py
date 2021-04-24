import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap('NIER.jpg')

        self.label = QLabel(self)

        self.btn1 = QPushButton('NIER', self)
        self.btn1.clicked.connect(self.showImage)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn1)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


    def showImage(self):
        self.label.setPixmap(self.pixmap)
        self.label.setContentsMargins(10, 10, 10, 10)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
