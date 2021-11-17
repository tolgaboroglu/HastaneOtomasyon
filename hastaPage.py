from PyQt5.QtWidgets import*
from hastaPage_python import Ui_Form


class HastaPage(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)