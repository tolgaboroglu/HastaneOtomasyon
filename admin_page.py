from PyQt5.QtWidgets import *
from admin_page_python import Ui_Form



class AdminPage(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

