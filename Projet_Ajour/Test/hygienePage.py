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

        #-------
        self.Num = 0
        #-------

        self.populate_table()

        self.setup_ui_connections()

        
    def setup_ui_connections(self):

        self.ui.tableWidget.cellClicked.connect(self.Recuperation_donne)
        self.ui.ButtonAccueil.clicked.connect(self.hygiene_vers_accueil)
        self.ui.ButtonQualiter.clicked.connect(self.hygiene_vers_qualiter)
        self.ui.ButtonRisques.clicked.connect(self.afficher_Risque)
        self.ui.ButtonUnique.clicked.connect(self.afficher_Unique)
        self.ui.ButtonVCSA.clicked.connect(self.afficher_VCSA)
        self.ui.ButtonPAG.clicked.connect(self.afficher_PAG)
        self.ui.Filtre.currentIndexChanged.connect(self.filtre)

    def populate_table(self):

        connection = self.Import_BDD.Connection_BDD()
        cursor = connection.cursor()
        i = self.Num
        print(i)

        if (i == 0):
            cursor.execute("SELECT * FROM `Feuil1` WHERE 1")
            data = cursor.fetchall()
        elif (i == 1):
            cursor.execute("SELECT `ID`, `Groupe`, `BU`, `Site`, `Origine`, `Origine2`, `Datedebut`, `Heure`, `Datefin`, `Visité` FROM `Feuil1` WHERE 1")
            data = cursor.fetchall()
        elif (i == 2):
            cursor.execute("SELECT `ID`, `Groupe`, `BU`, `Site` FROM `Feuil1` WHERE 1")
            data = cursor.fetchall()
        elif (i == 3):
            cursor.execute("SELECT `ID`, `Groupe`, `BU`, `Site`, `Origine` FROM `Feuil1` WHERE 1")
            data = cursor.fetchall()
        elif (i == 4):
            cursor.execute("SELECT `ID`, `Groupe`, `BU`, `Site`, `Datedebut`, `Fonction`, `Origine`, `Rédacteur/Rédactrice`, `Secteur`, `Ligne/Poste`, `Fonction2`, `Constat`, `Tâche`, `Commentaire(s)`, `Responsablesecteur`, `Datederéalisation`, `Datefin` FROM `Feuil1` WHERE 1")
            data = cursor.fetchall()

        #self.filtre(i)
        self.Table(data)

    def Table(self, data):
            # Définir le nombre de lignes et de colonnes du tableau
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))

        # Remplir le tableau avec les données
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_widget.setItem(row_idx, col_idx, item)

    def filtre(self):
        
        connection = self.Import_BDD.Connection_BDD()
        cursor = connection.cursor()
        i = self.Num

        if (i == 0):
            sql = "SELECT `ID`, `Groupe`, `BU`, `Site`, `Datedebut`, `Fonction`, `Origine`, `Rédacteur/Rédactrice`, `Secteur`, `Ligne/Poste`, `Fonction2`, `Constat`, `Tâche`, `Commentaire(s)`, `Responsablesecteur`, `Datederéalisation`, `Datefin` FROM `Feuil1` WHERE Secteur = %s"
        elif (i == 1):
            sql = "SELECT `ID`, `Groupe`, `BU`, `Site`, `Origine`, `Origine2`, `Datedebut`, `Heure`, `Datefin`, `Visité` FROM `Feuil1` WHERE Secteur = %s"    
        elif (i == 2):
             sql = "SELECT `ID`, `Groupe`, `BU`, `Site` FROM `Feuil1` WHERE Secteur = %s"   
        elif (i == 3):
            sql = "SELECT `ID`, `Groupe`, `BU`, `Site`, `Origine` FROM `Feuil1` WHERE Secteur = %s" 
        elif (i == 4):
            sql = "SELECT `ID`, `Groupe`, `BU`, `Site`, `Datedebut`, `Fonction`, `Origine`, `Rédacteur/Rédactrice`, `Secteur`, `Ligne/Poste`, `Fonction2`, `Constat`, `Tâche`, `Commentaire(s)`, `Responsablesecteur`, `Datederéalisation`, `Datefin` FROM `Feuil1` WHERE Secteur = %s"        
        
        print("Numéro : ", i)
        values = (self.ui.Filtre.currentText(),)
        print("Valeur : ", values)
        print("SQL : ", sql)
        cursor.execute(sql, values)
        data = cursor.fetchall()
        print("Data : ", data)
        self.Table(data)


    def Recuperation_donne(self, row):

        ID = self.table_widget.item(row, 0)
        Groupe = self.table_widget.item(row, 1)
        BU = self.table_widget.item(row, 2)
        Site = self.table_widget.item(row, 3)


        Datedebut = self.table_widget.item(row, 4)
        Fonction = self.table_widget.item(row, 5)
        Origine = self.table_widget.item(row, 6)
        Rédacteur_Rédactrice = self.table_widget.item(row, 7)
        Secteur = self.table_widget.item(row, 8)
        Ligne_Poste = self.table_widget.item(row, 9)
        Fonction2 = self.table_widget.item(row, 10)
        Constat = self.table_widget.item(row, 11)
        Tâche = self.table_widget.item(row, 12)
        Commentaires = self.table_widget.item(row, 13)
        Responsablesecteur = self.table_widget.item(row, 14)
        Heure = self.table_widget.item(row, 15)
        Datefin = self.table_widget.item(row, 16)

         
        self.PAG.Implemente_info(ID, Groupe, Datedebut, Fonction, Origine, Rédacteur_Rédactrice, Secteur, Ligne_Poste, Fonction2, Constat, Tâche, Commentaires, Responsablesecteur, Heure, Datefin)
        self.RDR.Implemente_info(ID, Groupe, Datedebut, Fonction, Origine, Rédacteur_Rédactrice, Secteur, Ligne_Poste, Fonction2, Constat, Tâche, Commentaires, Responsablesecteur, Heure, Datefin)


    def afficher_Risque(self):

        self.RDR.Affichage()
        self.Num = 1
        self.populate_table()
        self.RDR.Implementation_ComboBox()

    def afficher_Unique(self):

        self.Num = 2
        self.populate_table()

    def afficher_VCSA(self):

        self.Num = 3
        self.populate_table()
    
    def afficher_PAG(self):

        self.PAG.Affichage()
        self.PAG.ui.BouttonModifier.hide()
        self.Num = 4
        self.populate_table()
        self.PAG.Implementation_ComboBox()

    def hygiene_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def hygiene_vers_qualiter(self):

        self.accueilOrigine.qualite_page.show()
        self.hide()
        self.accueilOrigine.qualite_page.affiche_niveau_qual()

    def affiche_niveau_hyg(self):
        authorization_level = self.auth_system.is_authorized("")
        print("je suis niveau", authorization_level)

        button_restriction = self.ui.ButtonRestriction1 
        if button_restriction:
            button_restriction.setText(f"Niveau: {authorization_level}")  # Sinon, affiche le niveau actuel
        else:
            print("Erreur: Widget button_restriction introuvable.")
