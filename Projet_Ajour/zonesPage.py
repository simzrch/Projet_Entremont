from Page import Page
from PySide6.QtUiTools import QUiLoader


class ZonesPage(Page):
    def __init__(self, perimetre, accueil_origine):

        super(Page, self).__init__()
    #    Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("zones.ui")

        self.ui.setWindowTitle("Identification zones")
        self.accueilOrigine = accueil_origine
        self.perimetre = perimetre
        self.setup_ui_connections()
    #    self.perimetres_page = PerimetresPage(self)

    def setup_ui_connections(self):

        self.ui.ButtonAccueil.clicked.connect(self.zones_vers_accueil)
        self.ui.ButtonPerimetres.clicked.connect(self.zones_vers_perimetres)
        self.ui.ButtonGestion.clicked.connect(self.zones_vers_gestion)

    def zones_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def zones_vers_perimetres(self):

        self.accueilOrigine.perimetres_page.show()
        self.hide()

    def zones_vers_gestion(self):

        self.perimetre.gestion_page.show()
        self.hide()
