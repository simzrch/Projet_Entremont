from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
import sys
from PySide6 import QtWidgets


class Page:
    def __init__(self, ui_file):
        self.loader = QUiLoader()
        self.ui = self.loader.load(ui_file, None)
        self.setup_ui_connections()

    def setup_ui_connections(self):
        raise NotImplementedError("La méthode setup_ui_connections doit être implémentée dans les sous-classes.")

    def show(self):
        self.ui.show()

    def hide(self):
        self.ui.hide()

class AccueilPage(Page):
    def __init__(self, ui_file):
        super().__init__(ui_file)
        self.ui.setWindowTitle("Accueil")

    def setup_ui_connections(self):
        self.ui.ButtonQualiter.clicked.connect(self.domaine_qualiter)
        self.ui.ButtonHygiene.clicked.connect(self.domaine_hygiene)

    def domaine_qualiter(self):
        qualite_page.show()
        self.hide()

    def domaine_hygiene(self):
        hygiene_page.show()
        self.hide()

class QualitePage(Page):
    def __init__(self, ui_file):
        super().__init__(ui_file)
        self.ui.setWindowTitle("Qualité")

    def setup_ui_connections(self):
        self.ui.ButtonAccueil.clicked.connect(self.qualiter_vers_accueil)
        self.ui.ButtonHygiene.clicked.connect(self.qualiter_vers_hygiene)

    def qualiter_vers_accueil(self):
        accueil_page.show()
        self.hide()

    def qualiter_vers_hygiene(self):
        hygiene_page.show()
        self.hide()

class HygienePage(Page):
    def __init__(self, ui_file):
        super().__init__(ui_file)
        self.ui.setWindowTitle("Hygiène")

    def setup_ui_connections(self):
        self.ui.ButtonAccueil.clicked.connect(self.hygiene_vers_accueil)
        self.ui.ButtonQualiter.clicked.connect(self.hygiene_vers_qualiter)
        self.ui.ButtonRisques.clicked.connect(self.domaine_risques)

    def hygiene_vers_accueil(self):
        accueil_page.show()
        self.hide()

    def hygiene_vers_qualiter(self):
        qualite_page.show()
        self.hide()

    def domaine_risques(self):
        print("test button")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    accueil_page = AccueilPage("accueil.ui")
    qualite_page = QualitePage("qualite.ui")
    hygiene_page = HygienePage("hygiene.ui")

    accueil_page.show()

    sys.exit(app.exec())

