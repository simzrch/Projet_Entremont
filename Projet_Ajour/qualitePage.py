from Page import Page
from PySide6.QtUiTools import QUiLoader


class QualitePage(Page):
    def __init__(self, auth_system, accueil_origine):

        super(Page, self).__init__()
        # Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("qualite.ui")

        self.ui.setWindowTitle("Qualite")
        self.auth_system = auth_system
        self.accueilOrigine = accueil_origine
        self.setup_ui_connections()

        #self.hygiene_page = accueil_origine.hygiene_page

    def setup_ui_connections(self):

        self.ui.ButtonAccueil.clicked.connect(self.hygiene_vers_accueil)
        self.ui.ButtonHygiene.clicked.connect(self.qualiter_vers_hygiene)
        self.ui.ButtonRestriction.clicked.connect(self.logout)

    def hygiene_vers_accueil(self):
        
        self.accueilOrigine.show()
        self.hide()

    def qualiter_vers_hygiene(self):
        
        self.accueilOrigine.hygiene_page.show()
        self.hide()

    def domaine_risques(self):
        print("test button")

    def logout(self):
        if self.auth_system.logout():
            print("Déconnexion réussie")
