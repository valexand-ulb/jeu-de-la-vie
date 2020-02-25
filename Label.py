from PyQt5.QtWidgets import QLabel


class Label(QLabel):
    """
    initie un label
    """
    def __init__(self, text, parent):
        super().__init__(parent=parent)
        self.setText(text)