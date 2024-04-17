from PySide6 import QtWidgets
import sys
from systeme_authentification import systemeAuthentification
from accueilPage import AccueilPage

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    auth_system = systemeAuthentification()

    accueil_page = AccueilPage(auth_system)

    accueil_page.show()

    sys.exit(app.exec())
