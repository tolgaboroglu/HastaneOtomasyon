from PyQt5.QtWidgets import *
from qt_designer_python import Ui_MainWindow
from admin_page import AdminPage
from hastaPage import HastaPage

class Otomation(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.adminGiris_Button.clicked.connect(self.adminGiris)
        self.admin_page = AdminPage()

        self.ui.hastaGiris_Button.clicked.connect(self.hastaGiris)
        self.hastaPage = HastaPage()

    def adminGiris(self):
        self.admin_page.show()
        self.close()

    def hastaGiris(self):
        self.hastaPage.show()
        self.close()















