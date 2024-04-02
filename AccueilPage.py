from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PySide6 import QtWidgets
import sys
from systeme_authentification import systemeAuthentification
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

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
    def __init__(self, ui_file, auth_system):
        super().__init__(ui_file)
        self.ui.setWindowTitle("Accueil")
        self.auth_system = auth_system
        self.login_window = None
    
        # Créer le bouton de déconnexion
        self.logout_button = QPushButton("Logout")
        self.logout_button.setFixedSize(60, 20)  # Définir une taille fixe pour le bouton
        self.logout_button.clicked.connect(self.logout)  # Connecter le bouton à la méthode logout

        # Ajouter le bouton à la disposition verticale existante
        self.ui.layout().addWidget(self.logout_button)

    def logout(self):
        if self.auth_system.logout():
            print("Déconnexion réussie")
            self.ui.ButtonRestriction.show()  # Afficher le bouton Restriction après la déconnexion
            
        #else:
            #print("Aucun utilisateur connecté")

    def setup_ui_connections(self):
        self.ui.ButtonQualiter.clicked.connect(self.domaine_qualiter)
        self.ui.ButtonHygiene.clicked.connect(self.domaine_hygiene)
        self.ui.ButtonRestriction.clicked.connect(self.login)

    def domaine_qualiter(self):
        qualite_page.show()
        self.hide()

    def domaine_hygiene(self):
        hygiene_page.show()
        self.hide()

    def login(self):
        print("gg")
        self.login_window = LoginWindow(self.auth_system, self)
        self.login_window.show()

    def hide_restriction_button(self):
        self.ui.ButtonRestriction.hide()
        self.restriction_button_hidden = True


class QualitePage(Page):
    def __init__(self, ui_file, auth_system):
        super().__init__(ui_file)
        self.ui.setWindowTitle("Qualité")
        self.auth_system = auth_system
      
        self.ui.ButtonRestriction.clicked.connect(self.logout)
        #print(self.auth_system.logged_in_user.role)
        QMessageBox.information(self, "Login réussie", f"Welcome,{self.auth_system.logged_in_user.role}")

    def setup_ui_connections(self):
        self.ui.ButtonAccueil.clicked.connect(self.qualiter_vers_accueil)
        self.ui.ButtonHygiene.clicked.connect(self.qualiter_vers_hygiene)
        

    def qualiter_vers_accueil(self):
        accueil_page.show()
        self.hide()

    def qualiter_vers_hygiene(self):
        hygiene_page.show()
        self.hide()

    def logout(self):
        if self.auth_system.logout():
            print("Déconnexion réussie")
    

class HygienePage(Page):
    def __init__(self, ui_file, auth_system):
        super().__init__(ui_file)
        self.ui.setWindowTitle("Hygiène")
        self.auth_system = auth_system

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


class LoginWindow(QWidget):
    def __init__(self, auth_system, accueil_page):
        super().__init__()

        self.auth_system = auth_system
        self.accueil_page = accueil_page  # Stocker la référence à AccueilPage

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label_username = QLabel("Username:")
        self.textbox_username = QLineEdit()
        layout.addWidget(self.label_username)
        layout.addWidget(self.textbox_username)

        self.label_password = QLabel("Password:")
        self.textbox_password = QLineEdit()
        self.textbox_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.textbox_password)

        self.button_login = QPushButton("Login")
        self.button_login.clicked.connect(self.check_login)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

    def check_login(self):
        username = self.textbox_username.text()
        password = self.textbox_password.text()

        if self.auth_system.verifier_authentification(username, password):
            QMessageBox.information(self, "Login réussie", f"Welcome, {username}! de {self.auth_system.logged_in_user.role}")
            self.close()  # Fermer la fenêtre de dialogue après le clic sur OK
            self.accueil_page.ui.ButtonRestriction.hide()  # Masquer le bouton de restriction dans AccueilPage

            return self.auth_system.logged_in_user.role 
                
        
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    auth_system = systemeAuthentification()

    accueil_page = AccueilPage("accueil.ui", auth_system)
    qualite_page = QualitePage("qualite.ui", auth_system )
    hygiene_page = HygienePage("hygiene.ui", auth_system)

    accueil_page.show()

    sys.exit(app.exec())

