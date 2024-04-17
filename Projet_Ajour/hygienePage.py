from Page import Page
from PySide6.QtUiTools import QUiLoader


class HygienePage(Page):
    def __init__(self, auth_system, accueil_origine):

        super(Page, self).__init__()
        # Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("hygiene.ui")

        self.ui.setWindowTitle("Hygiene")
        self.auth_system = auth_system
        self.accueilOrigine = accueil_origine
        self.setup_ui_connections()

        #self.qualiter_page = accueil_origine.qualite_page

    def setup_ui_connections(self):
        self.ui.ButtonAccueil.clicked.connect(self.hygiene_vers_accueil)
        self.ui.ButtonQualiter.clicked.connect(self.hygiene_vers_qualiter)
        self.ui.ButtonRisques.clicked.connect(self.domaine_risques)
        self.ui.ButtonRestriction.clicked.connect(self.logout)

    def hygiene_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def hygiene_vers_qualiter(self):

        self.accueilOrigine.qualite_page.show()
        self.hide()

    def domaine_risques(self):
        print("test button")

    def logout(self):
        if self.auth_system.logout():
            print("Déconnexion réussie")
