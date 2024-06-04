from PySide6.QtWidgets import QPushButton
from systeme_authentification import systemeAuthentification
from PySide6.QtUiTools import QUiLoader
from Page import Page
from LoginWindow import LoginWindow
from qualitePage import QualitePage
from hygienePage import HygienePage
from perimetresPage import PerimetresPage
from DocumentPage import DocumentPage

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
         
        
        self.qualite_page = QualitePage(self)
        self.hygiene_page = HygienePage(self)
        self.perimetres_page = PerimetresPage(self)
        self.document_page = DocumentPage(self)


        self.ui.ButtonQualiter.clicked.connect(self.domaine_qualiter)
        self.ui.ButtonHygiene.clicked.connect(self.domaine_hygiene)
        self.ui.ButtonRestriction.clicked.connect(self.login)
        self.ui.ButtonParametres.clicked.connect(self.domaine_parametres)
        self.ui.ButtonDocuments.clicked.connect(self.domaine_document)

        self.acces_para()

    def logout(self):
        if self.auth_system.logout():
            print("Déconnexion réussie")
            self.ui.ButtonRestriction.show()  # Afficher le bouton Restriction après la déconnexion
            self.acces_para()
            
    #    else:
    #        print("Aucun utilisateur connecté")

    def domaine_qualiter(self):

        self.qualite_page.show()
        self.hide()
        self.qualite_page.affiche_niveau_qual()

    def domaine_hygiene(self):
        
        self.hygiene_page.show()
        self.hide() 
        self.hygiene_page.affiche_niveau_hyg()

    def domaine_document(self):
        
        self.document_page.show()
        self.hide() 
        self.document_page.authent_modif()
        self.document_page.afficher_bouton()
        

    def login(self):
        print("gg")
        self.login_window = LoginWindow(self.auth_system, self)
        self.login_window.show()

    def hide_restriction_button(self):
        self.ui.ButtonRestriction.hide()
        self.restriction_button_hidden = True

    def domaine_parametres(self):

        self.perimetres_page.show()
        self.hide()


    def acces_para(self):

        authorization_level = self.auth_system.is_authorized

        print(f"Autorisation de l'utilisateur de niveau {authorization_level}")
        button_widget = self.ui.ButtonParametres 

        if button_widget is not None:
            if authorization_level == 1 or authorization_level == 2:
                button_widget.setEnabled(False)
                print("désactivé")
            elif authorization_level == 3:
                button_widget.setEnabled(True)
                print("activé pour administrateur")
            else:
                button_widget.setEnabled(False)
                print("désactivé")
        else:
            print(f"Erreur: Widget introuvable.")

        print("fin") 