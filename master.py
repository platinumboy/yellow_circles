import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 500, 1149, 794)
        self.setWindowTitle('Жёлтые круги')
        self.draw = False
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown']

        self.pushButton = QPushButton('Кнопка', self)
        self.pushButton.resize(50, 50)
        self.pushButton.move(140, 140)
        self.pushButton.clicked.connect(self.makeflag)

    def makeflag(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            for i in range(6):
                qp.setBrush(QColor(choice(self.colors)))
                radius = randint(20, 200)
                self.x = randint(20, 1000)
                self.y = randint(20, 700)
                qp.drawEllipse(self.x - radius, self.y - radius, 2 * radius, 2 * radius)
            qp.end()
            self.draw = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
