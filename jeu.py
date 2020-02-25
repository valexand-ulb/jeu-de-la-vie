from random import randint
from os import name, system
from time import sleep


class Matrice:
    def __init__(self, n, parent=None):
        self.parent = parent
        self.len = n
        self.matrice = [[0 for i in range(n)] for j in range(n)]

    def getLen(self):
        return self.len

    def setMatcase(self, i, j, n):
        self.matrice[i][j] = n

    def printMat(self):
        if name == 'posix':
            system('clear')
        else:
            system('cls')
        s = ''
        for line in self.matrice:
            for elem in line:
                s += str(elem) + ' '
            s += '\n'
        print(s)

    def setrandomMat(self, pourc):
        len = self.getLen()
        num = int((len**2) * (pourc/100))
        for e in range(num):
            i = randint(0, len-1)
            j = randint(0, len-1)
            self.setMatcase(i, j, 1)

    def coef(self, i, j):
        coef = 0
        len = self.getLen()
        for ver in range(i-1, i+2):
            for hor in range(j-1, j+2):
                try:
                    if ver != i or hor != j:
                        if self.matrice[ver][hor] == 1:
                            coef += 1
                except:
                    coef = coef
        print(coef)
        return coef

    def rules(self):
        len = self.getLen()
        tda = []
        tdr = []
        for i in range(len):
            for j in range(len):
                coef = self.coef(i, j)

                if coef == 3 and self.matrice[i][j] == 0:
                    tda.append((i, j))
                elif self.matrice[i][j] == 1 and not ( 2 <= coef <= 3):
                    tdr.append((i, j))

        for elem in tda:
            self.setMatcase(elem[0], elem[1], 1)
        for elem in tdr:
            self.setMatcase(elem[0], elem[1], 0)

    def jeu(self, n, s):
        self.printMat()
        sleep(s)
        len = self.getLen()
        for i in range(n):
            self.rules()
            self.printMat()

            sleep(s)

