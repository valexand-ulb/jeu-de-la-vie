from buttons import StartButton
from Combobox import Combo
from Layout import VerLayout, HorLayout
from Label import Label
from PyQt5.QtWidgets import QGroupBox


class settingsBox(QGroupBox):
    def __init__(self, parent):
        super().__init__(parent=parent)

        sb = StartButton('Start', self)

        tcombo = Combo(['1', '2', '3', '4'], self)
        label1 = Label('Time interval', self)

        scombo = Combo(['5*5', '10*10', '15*15', '20*20'], self)
        label2 = Label('Size', self)

        tocombo = Combo(['10', '30', '50', '100'])
        label3 = Label('Nombre de tours', self)

        v1 = VerLayout([label2, scombo])
        v2 = VerLayout([label1, tcombo])
        v3 = VerLayout([label3, tocombo])
        v4 = VerLayout([sb])

        hl = HorLayout([v1, v2, v3, v4])

        self.setLayout(hl)

