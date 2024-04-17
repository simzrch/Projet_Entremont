from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PySide6 import QtWidgets
import sys
from systeme_authentification import systemeAuthentification
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


auth_system = systemeAuthentification()


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

