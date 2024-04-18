from Page import Page
from PySide6.QtUiTools import QUiLoader

class HygienePage(Page):
    def __init__(self, auth_system, accueil_origine):

        super(Page, self).__init__()
        # Charger le fichier .ui

        loader = QUiLoader()
        self.ui = loader.load("hygiene.ui")
        self.ui.setWindowTitle("Hygiene")
        self.stackedWidget = self.ui.stackedWidget
        self.auth_system = auth_system
        self.accueilOrigine = accueil_origine
        self.setup_ui_connections()


    def setup_ui_connections(self):

        self.ui.ButtonAccueil.clicked.connect(self.hygiene_vers_accueil)
        self.ui.ButtonQualiter.clicked.connect(self.hygiene_vers_qualiter)
        self.ui.ButtonRisques.clicked.connect(self.afficher_Risque)
        self.ui.ButtonUnique.clicked.connect(self.afficher_Unique)
        self.ui.ButtonVCSA.clicked.connect(self.afficher_VCSA)
        self.ui.ButtonPAG.clicked.connect(self.afficher_PAG)
        self.ui.ButtonRestriction.clicked.connect(self.logout)

    def afficher_Risque(self):

        loader = QUiLoader()

        File = loader.load("RDR.ui")
        self.stackedWidget.addWidget(File)
        self.stackedWidget.setCurrentWidget(File)

    def afficher_Unique(self):
        pass

    def afficher_VCSA(self):
        pass
    
    def afficher_PAG(self):

        loader = QUiLoader()

        File = loader.load("PAG.ui")
        self.stackedWidget.addWidget(File)
        self.stackedWidget.setCurrentWidget(File)

    def hygiene_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def hygiene_vers_qualiter(self):

        self.accueilOrigine.qualite_page.show()
        self.hide()

    def logout(self):
        
        if self.auth_system.logout():
            print("Déconnexion réussie")
