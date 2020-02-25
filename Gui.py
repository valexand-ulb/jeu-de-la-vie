import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from Box import settingsBox
from buttons import Playbutton
from jeu import Matrice


class Mainwin(QWidget):
    def __init__(self, matsize, matpos, remp=None, xpos=0, ypos=0, w=1920, h=1080):
        super().__init__()
        self.mat = Matrice(matsize, self)
        if remp is not None:
            self.mat.setrandomMat(remp)
        self.xpos = xpos
        self.ypos = ypos
        self.width = w
        self.height = h
        self.matsize = matsize
        self.matpos = matpos
        self.initui()

    def initui(self):
        #settingsbox
        setbox = settingsBox(self)
        setbox.setGeometry(0, 0, 1920, 80)
        #buttons
        for i in range(self.matsize):
            for j in range(self.matsize):
                x = self.matpos[0]
                y = self.matpos[1]
                b = Playbutton(x + i*25, y + j*25, str((i, j)), self)
                if self.mat.matrice[i][j] == 0:
                    b.setStyleSheet('background-color: #ffffff')
                else:
                    b.setStyleSheet('background-color: #000000')

        # Mainwin
        self.setGeometry(self.xpos, self.ypos, self.width, self.height)
        self.setWindowTitle('Test')
        self.show()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mainwin(50, (500,80))
    sys.exit(app.exec_())