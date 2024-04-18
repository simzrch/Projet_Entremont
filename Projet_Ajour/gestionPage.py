from Page import Page
from PySide6.QtUiTools import QUiLoader


class GestionPage(Page):
    def __init__(self, perimetre, accueil_origine):

        super(Page, self).__init__()
    #    Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("gestion.ui")

        self.ui.setWindowTitle("Gestion des acces")
        self.accueilOrigine = accueil_origine
        self.perimetre = perimetre
        self.setup_ui_connections()
    #    self.perimetres_page = PerimetresPage(self)

    def setup_ui_connections(self):

        self.ui.ButtonAccueil.clicked.connect(self.gestion_vers_accueil)
        self.ui.ButtonPerimetres.clicked.connect(self.gestion_vers_perimetres)
        self.ui.ButtonZones.clicked.connect(self.gestion_vers_zones)

    def gestion_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def gestion_vers_perimetres(self):

        self.accueilOrigine.perimetres_page.show()
        self.hide()

    def gestion_vers_zones(self):

        self.perimetre.zones_page.show()
        self.hide()
