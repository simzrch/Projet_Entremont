from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QMargins
import sys

class SimplePage(QMainWindow):
    def __init__(self):
        super(SimplePage, self).__init__()

        # Configurer la fenêtre principale
        self.setWindowTitle("Simple Page")
        
        # Créer le widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Créer un layout vertical
        layout = QVBoxLayout(central_widget)

        # Créer un bouton et l'ajouter au layout
        self.push_button = QPushButton("Click Me", self)
        layout.addWidget(self.push_button)

        # Créer un bouton de fermeture et l'ajouter au layout
        self.close_button = QPushButton("Close", self)
        layout.addWidget(self.close_button)

        # Connecter le clic des boutons aux méthodes correspondantes
        self.push_button.clicked.connect(self.on_button_click)
        self.close_button.clicked.connect(self.close)

        # Définir la fenêtre presque plein écran avec une marge
        self.show_near_full_screen()

    def show_near_full_screen(self):
        # Obtenir la taille de l'écran
        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        
        # Définir une marge (en pixels)
        margin = 50
        
        # Calculer les dimensions avec la marge
        new_width = screen_size.width() - 2 * margin
        new_height = screen_size.height() - 2 * margin

        # Définir la taille et la position de la fenêtre
        self.setGeometry(margin, margin, new_width, new_height)
        self.show()

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimplePage()
    window.show()
    sys.exit(app.exec())
