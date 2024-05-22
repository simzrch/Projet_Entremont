from Page import Page
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from Import_Base import Import_Base
from PAG import PAG
from RDR import RDR

class HygienePage(Page):
    def __init__(self, accueil_origine):

        super(Page, self).__init__()
        # Charger le fichier .ui

        loader = QUiLoader()
        self.ui = loader.load("hygiene.ui")
        self.ui.setWindowTitle("Hygiene")
        self.stackedWidget = self.ui.stackedWidget
        self.table_widget = self.ui.tableWidget
        self.auth_system = accueil_origine.auth_system
        self.accueilOrigine = accueil_origine
        self.Import_BDD = Import_Base()

        connection = self.Import_BDD.Connection_BDD()
        cursor = connection.cursor()

        #-----------
        
        self.populate_table(cursor)
        #----------

        self.setup_ui_connections()

        self.PAG = PAG(self)
        self.RDR = RDR(self)


    def setup_ui_connections(self):

        self.ui.ButtonAccueil.clicked.connect(self.hygiene_vers_accueil)
        self.ui.ButtonQualiter.clicked.connect(self.hygiene_vers_qualiter)
        self.ui.ButtonRisques.clicked.connect(self.afficher_Risque)
        self.ui.ButtonUnique.clicked.connect(self.afficher_Unique)
        self.ui.ButtonVCSA.clicked.connect(self.afficher_VCSA)
        self.ui.ButtonPAG.clicked.connect(self.afficher_PAG)
        self.ui.ButtonRestriction.clicked.connect(self.logout)

    def populate_table(self, cursor):

        
        cursor.execute("SELECT * FROM visiteurs")
        data = cursor.fetchall()

        # Définir le nombre de lignes et de colonnes du tableau
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))

         # Remplir le tableau avec les données
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_widget.setItem(row_idx, col_idx, item)

    def afficher_Risque(self):

        self.RDR.Affichage()

    def afficher_Unique(self):
        pass

    def afficher_VCSA(self):
        pass
    
    def afficher_PAG(self):

        self.PAG.Affichage()
        self.PAG.Implementation_ComboBox()

    def hygiene_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def hygiene_vers_qualiter(self):

        self.accueilOrigine.qualite_page.show()
        self.hide()

    def logout(self):

        if self.auth_system.logout():
            print("Déconnexion réussie")
