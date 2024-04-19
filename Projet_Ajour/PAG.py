import mysql.connector
from Page import Page
from Import_Base import Import_Base
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets


class PAG(Page):
    def __init__(self, hygiene):

        super(Page, self).__init__()
        # Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("PAG.ui")
        self.hygiene = hygiene
        self.ui.ButtonValide.clicked.connect(self.Envoie_Données)
        self.Import_Base = Import_Base()

    def Envoie_Données(self):
            print("Bonjour")
            connection = mysql.connector.connect(
            host="192.168.1.213",
            user="root",
            password="root",
            database="test_proje_entremont"
        )
            self.conn = connection
            cursor = self.conn.cursor()
            valeur_colonne1 = "valeur1"
            valeur_colonne2 = "valeur2"
            valeur_colonne3 = "valeur3"

            # Requête d'insertion avec spécification des colonnes
            sql = "INSERT INTO Feuil1 (BU, Origine, Heure) VALUES (%s, %s, %s)"
            values = (valeur_colonne1, valeur_colonne2, valeur_colonne3)
            cursor.execute(sql, values)

            # Valider la transaction
            self.conn.commit()

            # Fermer la connexion
            cursor.close()
            self.conn.close()
            print("Ovoir")

    def Affichage(self):
        
        self.hygiene.stackedWidget.addWidget(self.ui)
        self.hygiene.stackedWidget.setCurrentWidget(self.ui)

    def Implementation_ComboBox(self):

        connection = self.Import_Base.Connection_BDD()

        self.conn = connection
        cursor = self.conn.cursor()

        cursor.execute("SELECT Origine FROM Information")
        rows = cursor.fetchall()
        #self.ui.comboBox.clear()
        self.clear_all_comboboxes()
        self.ui.comboBox.addItems([row[0] for row in rows])
        
        cursor.close()
        self.conn.close()

    def clear_all_comboboxes(self):
        for widget in self.ui.findChildren(QtWidgets.QComboBox):
            widget.clear()