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
    #    self.perimetres_page = PerimetresPage(self)
        

    def setup_ui_connections(self):

        self.ui.ButtonAccueil.clicked.connect(self.gestion_vers_accueil)
        self.ui.ButtonPerimetres.clicked.connect(self.gestion_vers_perimetres)
        self.ui.ButtonZones.clicked.connect(self.gestion_vers_zones)
        self.ui.ButtonEntrer.clicked.connect(self.Envoie_Donne)
        self.ui.ButtonSupprimer.clicked.connect(self.ligne_selectionnee)


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
    #    valeur_colonne4 = self.ui.lineEditAcces.text()
    #    valeur_colonne5 = self.ui.lineEditBatiment.text()
        valeur_colonne4 = self.ui.comboBoxAcces.currentText()
        valeur_colonne5 = self.ui.comboBoxBatiment.currentText()

        # Requête d'insertion avec spécification des colonnes
        sql = "INSERT INTO Liste_acces (Nom, Prenom, Mail, Acces, Batiment) VALUES (%s, %s, %s, %s, %s)"
        values = (valeur_colonne1, valeur_colonne2, valeur_colonne3, valeur_colonne4, valeur_colonne5)
        cursor.execute(sql, values)

        # Valider la transaction
        self.conn.commit()

        # Fermer la connexion
        cursor.close()
        self.conn.close()

        self.populate_table()

        # vider_les_LineEdit(self):
        for widget in self.ui.findChildren(QLineEdit):
            widget.clear()
        print("Aurevoir")
        

    def Implementation_ComboBox(self):

        self.clear_all(0)

        self.populate_combobox("Acces", self.ui.comboBoxAcces)
        self.populate_combobox("Batiment", self.ui.comboBoxBatiment)


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

#==============================================================================================================
#Suppression
#============

    def ligne_selectionnee(self):
        selected_items = self.table_widget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.Recuperation_donne(row)

    def Recuperation_donne(self, row):
        Nom = self.table_widget.item(row, 0).text() if self.table_widget.item(row, 0) else ""
        Prenom = self.table_widget.item(row, 1).text() if self.table_widget.item(row, 1) else ""
        Mail = self.table_widget.item(row, 2).text() if self.table_widget.item(row, 2) else ""
        Acces = self.table_widget.item(row, 3).text() if self.table_widget.item(row, 3) else ""
        Batiment = self.table_widget.item(row, 4).text() if self.table_widget.item(row, 4) else ""
        print(Nom, Prenom, Mail, Acces, Batiment)

        self.Suppression_Donne(Nom, Prenom, Mail, Acces, Batiment)
         

    def Suppression_Donne(self, Nom, Prenom, Mail, Acces, Batiment):
        # Connect to the database
        self.conn = self.Import_BDD.Connection_BDD()
        cursor = self.conn.cursor()

        # Print column names to verify
        cursor.execute("SHOW COLUMNS FROM Liste_acces")
        columns = cursor.fetchall()
        print("Columns in Liste_acces:", [column[0] for column in columns])

        # Check if the entry exists
        cursor.execute("""
            SELECT COUNT(*) 
            FROM Liste_acces 
            WHERE Nom = %s AND Prenom = %s AND Mail = %s AND Acces = %s AND Batiment = %s
        """, (Nom, Prenom, Mail, Acces, Batiment))
        result = cursor.fetchone()

        if result[0] > 0:
            # Entry exists, delete the data
            sql = """
            DELETE FROM Liste_acces 
            WHERE Nom = %s AND Prenom = %s AND Mail = %s AND Acces = %s AND Batiment = %s
            """
            cursor.execute(sql, (Nom, Prenom, Mail, Acces, Batiment))
            self.conn.commit()
        else:
            # Entry does not exist, show a message or handle accordingly
            print("Entry does not exist.")

        cursor.close()
        self.conn.close()

        # Comment out the clear_all call if it does not exist
        # self.clear_all(1)
        self.populate_table()

    def clear_all(self, flag):
        # Implémente la logique de nettoyage ici
        # Par exemple, nettoyer certains champs de l'interface utilisateur
        self.ui.Nom.clear()
        self.ui.Prenom.clear()
        self.ui.Mail.clear()
        self.ui.Acces.clear()
        self.ui.Batiment.clear()
        # Ajoute d'autres champs si nécessaire
        print(f"clear_all called with flag: {flag}")

#=====================================================================================================================

    def gestion_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def gestion_vers_perimetres(self):

        self.accueilOrigine.perimetres_page.show()
        self.hide()

    def gestion_vers_zones(self):

        self.perimetre.zones_page.show()
        self.hide()
