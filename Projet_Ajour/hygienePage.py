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

        self.PAG = PAG(self)
        self.RDR = RDR(self)

        #-----------
        self.populate_table()
        #----------

        self.setup_ui_connections()

        


    def setup_ui_connections(self):

        self.ui.tableWidget.cellClicked.connect(self.Recuperation_donne)
        self.ui.ButtonAccueil.clicked.connect(self.hygiene_vers_accueil)
        self.ui.ButtonQualiter.clicked.connect(self.hygiene_vers_qualiter)
        self.ui.ButtonRisques.clicked.connect(self.afficher_Risque)
        self.ui.ButtonUnique.clicked.connect(self.afficher_Unique)
        self.ui.ButtonVCSA.clicked.connect(self.afficher_VCSA)
        self.ui.ButtonPAG.clicked.connect(self.afficher_PAG)
        self.ui.ButtonRestriction.clicked.connect(self.logout)

    def populate_table(self):

        connection = self.Import_BDD.Connection_BDD()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM `Feuil1` WHERE 1")
        data = cursor.fetchall()

        # Définir le nombre de lignes et de colonnes du tableau
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))

         # Remplir le tableau avec les données
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_widget.setItem(row_idx, col_idx, item)

    def Recuperation_donne(self, row):


         ID = self.table_widget.item(row, 0)
         Datedebut = self.table_widget.item(row, 6)
         Fonction = self.table_widget.item(row, 10)
         Origine = self.table_widget.item(row, 4)
         Redacteur = self.table_widget.item(row, 12)
         Secteur = self.table_widget.item(row, 15)
         LignePoste = self.table_widget.item(row, 16)
         Fonction2 = self.table_widget.item(row, 13)
         Constat = self.table_widget.item(row, 25)
         Tâche = self.table_widget.item(row, 20)
         Commentaire = self.table_widget.item(row, 55)
         Responsablesecteur = self.table_widget.item(row, 17)
         Heure = self.table_widget.item(row, 7)
         Datefin = self.table_widget.item(row, 8)
         Groupe = self.table_widget.item(row, 1)
    
         
         self.PAG.Implemente_info(ID, Datedebut, Fonction, Origine, Redacteur, Secteur, LignePoste, Fonction2, Constat, Tâche, Commentaire, Responsablesecteur, Heure, Datefin, Groupe)
                

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
