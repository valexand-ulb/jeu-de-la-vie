from PyQt5.QtWidgets import QComboBox


class Combo(QComboBox):
    def __init__(self, param_list, parent=None):
        super().__init__(parent=parent)
        for elem in param_list:
            self.addItem(elem)