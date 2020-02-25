from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSlot


class Playbutton(QPushButton):
    def __init__(self, xpos, ypos, name, parent=None, w=25, h=25):
        super().__init__(parent=parent)
        self.name = name
        self.move(xpos, ypos)
        self.setFixedSize(w, h)
        self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print(self.name)


class StartButton(QPushButton):
    def __init__(self, name, parent=None):
        super().__init__(parent=parent)
        self.setText(name)
        self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        self.parent().parent().mat.jeu()

