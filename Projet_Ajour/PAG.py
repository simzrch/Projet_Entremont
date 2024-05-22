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

            Datedebut = self.ui.Date.text()
            Fonction = self.ui.TypeAudit.currentText()
            Origine = self.ui.OrigineAction.currentText()
            Rédacteur = self.ui.Redacteur.currentText()
            Secteur = self.ui.Secteur.currentText()
            LignePoste = self.ui.LignePoste.toPlainText()
            Fonction2 = self.ui.Type.currentText()
            Constat = self.ui.Constat.toPlainText()
            Tâche = self.ui.Mesure.toPlainText()
            Commentaire = self.ui.Commentaire.toPlainText()
            Responsablesecteur = self.ui.ResponsableAction.currentText()
            Heure = self.ui.DelaieRealisation.text()
            Datefin = self.ui.DateRealisation.text()
            Groupe = self.ui.EvaluationEfficacite.text()
            

            # Requête d'insertion avec spécification des colonnes
            sql = "INSERT INTO Feuil1 (Datedebut, Fonction, Origine, Rédacteur_Rédactrice, Secteur, Ligne_Poste, Fonction2, Constat, Tâche, Commentaires, Responsablesecteur, Heure, Datefin, Groupe) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Datedebut, Fonction, Origine, Rédacteur, Secteur, LignePoste, Fonction2, Constat, Tâche, Commentaire, Responsablesecteur, Heure, Datefin, Groupe)
            cursor.execute(sql, values)

            # Valider la transaction
            self.conn.commit()

            # Fermer la connexion
            cursor.close()
            self.conn.close()

            self.clear_all(1)

    def Affichage(self):
        
        self.hygiene.stackedWidget.addWidget(self.ui)
        self.hygiene.stackedWidget.setCurrentWidget(self.ui)

    def Implementation_ComboBox(self):

        self.clear_all(0)

        self.populate_combobox("Origine", "Feuil1", self.ui.TypeAudit)
        self.populate_combobox("Origine2", "Feuil1", self.ui.OrigineAction)
        self.populate_combobox("Poste", "Information", self.ui.Redacteur)
        self.populate_combobox("Secteur", "Feuil1", self.ui.Secteur)
        self.populate_combobox("Datedebut", "Feuil1", self.ui.Type)

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

    def clear_all(self, i):

        if (i == 0):

            for combo_box in self.ui.findChildren(QtWidgets.QComboBox):
                combo_box.clear()
        

        for text_edit in self.ui.findChildren(QtWidgets.QTextEdit):
             text_edit.clear()
        
        for line_edit in self.ui.findChildren(QtWidgets.QLineEdit):
            line_edit.clear()