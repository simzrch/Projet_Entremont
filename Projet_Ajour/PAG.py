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
          
            self.conn = self.Import_Base.Connection_BDD()
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

    def Affichage(self):
        
        self.hygiene.stackedWidget.addWidget(self.ui)
        self.hygiene.stackedWidget.setCurrentWidget(self.ui)

    def Implementation_ComboBox(self):

        self.clear_all_comboboxes()
        self.populate_combobox("Origine", "Feuil1", self.ui.comboBox)
        self.populate_combobox("Origine2", "Feuil1", self.ui.comboBox_2)
        self.populate_combobox("Poste", "Information", self.ui.comboBox_3)
        self.populate_combobox("Secteur", "Feuil1", self.ui.comboBox_4)
        self.populate_combobox("Datedebut", "Feuil1", self.ui.comboBox_6)

    def populate_combobox(self, column_name, table_name, combo_box):

        self.conn = self.Import_Base.Connection_BDD()
        cursor = self.conn.cursor()

        query = f"SELECT DISTINCT {column_name} FROM {table_name} WHERE {column_name} != ''"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            if row[0]:
                combo_box.addItem(row[0])
        cursor.close()
        self.conn.close()

    def clear_all_comboboxes(self):

        for widget in self.ui.findChildren(QtWidgets.QComboBox):
            widget.clear()