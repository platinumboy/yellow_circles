import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QPolygon
from PyQt5.QtCore import Qt, QPoint
from random import choice, randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.makeflag)

    def makeflag(self):
        self.draw = True

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('Yellow'))
            radius = randint(20, 200)
            self.x = randint(20, 1000)
            self.y = randint(20, 700)
            qp.drawEllipse(self.x - radius, self.y - radius, 2 * radius, 2 * radius)
            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
