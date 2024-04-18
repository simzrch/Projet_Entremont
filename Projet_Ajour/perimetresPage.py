from Page import Page
from PySide6.QtUiTools import QUiLoader
from gestionPage import GestionPage
from zonesPage import ZonesPage


class PerimetresPage(Page):
    def __init__(self, accueil_origine):

        super(Page, self).__init__()
        # Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("perimetres.ui")

        self.ui.setWindowTitle("Perimetres")
        self.accueilOrigine = accueil_origine
        self.setup_ui_connections()
        self.gestion_page = GestionPage(self, accueil_origine)
        self.zones_page = ZonesPage(self, accueil_origine)

    def setup_ui_connections(self):

        self.accueilOrigine
        self.ui.ButtonAccueil.clicked.connect(self.perimetres_vers_accueil)
        self.ui.ButtonGestion.clicked.connect(self.perimetres_vers_gestion)
        self.ui.ButtonZones.clicked.connect(self.perimetres_vers_zones)
        
    def perimetres_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def perimetres_vers_gestion(self):

        self.gestion_page.show()
        self.hide()

    def perimetres_vers_zones(self):

        self.zones_page.show()
        self.hide()
