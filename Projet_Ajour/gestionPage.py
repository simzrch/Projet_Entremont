from Page import Page
from Import_Base import Import_Base
from PySide6.QtWidgets import QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
import mysql.connector


class GestionPage(Page):
    def __init__(self, perimetre, accueil_origine):

        super(Page, self).__init__()
    #    Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("gestion.ui")

        self.ui.setWindowTitle("Gestion des acces")
        self.accueilOrigine = accueil_origine
        self.perimetre = perimetre
        self.Import_BDD = Import_Base()
        self.table_widget = self.ui.tableWidgetAcces
        self.populate_table()
        self.setup_ui_connections()
    #    self.vider_les_LineEdit()
    #    self.perimetres_page = PerimetresPage(self)
        


    def setup_ui_connections(self):

        self.ui.ButtonAccueil.clicked.connect(self.gestion_vers_accueil)
        self.ui.ButtonPerimetres.clicked.connect(self.gestion_vers_perimetres)
        self.ui.ButtonZones.clicked.connect(self.gestion_vers_zones)
        self.ui.ButtonEntrer.clicked.connect(self.Envoie_Donne)
    #    self.ui.ButtonSupprimer.clicked.connect(self.Suppression_Donne)


    def Envoie_Donne(self):

        print("Bonjour")
        connection = mysql.connector.connect(
        host="192.168.1.213",
        user="root",
        password="root",
        database="test_proje_entremont"
    )
        self.conn = connection
        cursor = self.conn.cursor()
        valeur_colonne1 = self.ui.lineEditNom.text()
        valeur_colonne2 = self.ui.lineEditPrenom.text()
        valeur_colonne3 = self.ui.lineEditMail.text()
        valeur_colonne4 = self.ui.lineEditAcces.text()
        valeur_colonne5 = self.ui.lineEditBatiment.text()

        # Requête d'insertion avec spécification des colonnes
        sql = "INSERT INTO Liste_acces (Nom, Prénom, Mail, Accès, Bâtiment) VALUES (%s, %s, %s, %s, %s)"
        values = (valeur_colonne1, valeur_colonne2, valeur_colonne3, valeur_colonne4, valeur_colonne5)
        cursor.execute(sql, values)

        # Valider la transaction
        self.conn.commit()

        # Fermer la connexion
        cursor.close()
        self.conn.close()

        self.populate_table()

    #    def vider_les_LineEdit(self):
        for widget in self.ui.findChildren(QLineEdit):
            widget.clear()
        print("Aurevoir")
        
    def populate_table(self):

        connection = self.Import_BDD.Connection_BDD()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Liste_acces")
        data = cursor.fetchall()

        # Définir le nombre de lignes et de colonnes du tableau
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))

        # Remplir le tableau avec les données
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_widget.setItem(row_idx, col_idx, item)

#    def Suppression_Donne(self):

#        self.

    def gestion_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def gestion_vers_perimetres(self):

        self.accueilOrigine.perimetres_page.show()
        self.hide()

    def gestion_vers_zones(self):

        self.perimetre.zones_page.show()
        self.hide()

