from PySide6.QtWidgets import QPushButton
from systeme_authentification import systemeAuthentification
from PySide6.QtUiTools import QUiLoader
from Page import Page
from LoginWindow import LoginWindow
from qualitePage import QualitePage
from hygienePage import HygienePage

class AccueilPage(Page):


    def __init__(self, auth_system):
        super(Page, self).__init__()
        # Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("accueil.ui")

        self.ui.setWindowTitle("Accueil")
        self.auth_system = auth_system
        self.login_window = None
    
        print("Test init accueilpage")
        # Créer le bouton de déconnexion
        self.logout_button = QPushButton("Logout")
        self.logout_button.setFixedSize(60, 20)  # Définir une taille fixe pour le bouton
        self.logout_button.clicked.connect(self.logout)  # Connecter le bouton à la méthode logout

        # Ajouter le bouton à la disposition verticale existante
        self.ui.layout().addWidget(self.logout_button)
         
        

        self.qualite_page = QualitePage(auth_system, self)
        self.hygiene_page = HygienePage(auth_system, self)


        self.ui.ButtonQualiter.clicked.connect(self.domaine_qualiter)
        self.ui.ButtonHygiene.clicked.connect(self.domaine_hygiene)
        self.ui.ButtonRestriction.clicked.connect(self.login)

    def logout(self):
        if self.auth_system.logout():
            print("Déconnexion réussie")
            self.ui.ButtonRestriction.show()  # Afficher le bouton Restriction après la déconnexion
            
        #else:
            #print("Aucun utilisateur connecté")

    def domaine_qualiter(self):

        self.qualite_page.show()
        self.hide()

    def domaine_hygiene(self):
        
        self.hygiene_page.show()
        self.hide() 

    def login(self):
        print("gg")
        self.login_window = LoginWindow(self.auth_system, self)
        self.login_window.show()

    def hide_restriction_button(self):
        self.ui.ButtonRestriction.hide()
        self.restriction_button_hidden = True