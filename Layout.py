from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class HorLayout(QHBoxLayout):
    """
    initie les layout horizontaux
    """
    def __init__(self, widgets_list):
        super().__init__()
        if len(widgets_list) > 1:
            for widget in widgets_list:
                try:
                    self.addWidget(widget)
                except TypeError:
                    self.addLayout(widget)
        else:
            try:
                self.addWidget(widgets_list[0])
            except TypeError:
                self.addLayout(widgets_list[0])


class VerLayout(QVBoxLayout):
    """
        initie les layouts verticaux
    """
    def __init__(self, widgets_list):
        super().__init__()
        for widget in widgets_list:
            try:
                self.addWidget(widget)
            except TypeError:
                self.addLayout(widget)
