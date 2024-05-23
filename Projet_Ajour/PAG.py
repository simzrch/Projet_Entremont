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
        self.ui.BouttonModifier.clicked.connect(self.Envoie_Données2)
        self.ui.BouttonModifier.hide()
        self.Import_Base = Import_Base()

    def Affichage(self):
        
        self.hygiene.stackedWidget.addWidget(self.ui)
        self.hygiene.stackedWidget.setCurrentWidget(self.ui)   

    def Implemente_info(self, ID, Datedebut, Fonction, Origine, Redacteur, Secteur, LignePoste, Fonction2, Constat, Tâche, Commentaire, Responsablesecteur, Heure, Datefin, Groupe):

        # self.ui.Date.setText(item_2.text())
        # self.ui.DelaieRealisation.setText(item.text())

        self.ui.ID.setText(ID.text())
        self.ui.Date.setText(Datedebut.text())
        self.ui.TypeAudit.setCurrentText(Fonction.text())
        self.ui.OrigineAction.setCurrentText(Origine.text())
        self.ui.Redacteur.setCurrentText(Redacteur.text())
        self.ui.Secteur.setCurrentText(Secteur.text())
        self.ui.LignePoste.setPlainText(LignePoste.text())
        self.ui.Type.setCurrentText(Fonction2.text())
        self.ui.Constat.setPlainText(Constat.text())
        self.ui.Mesure.setPlainText(Tâche.text())
        self.ui.Commentaire.setPlainText(Commentaire.text())
        self.ui.ResponsableAction.setCurrentText(Responsablesecteur.text())
        self.ui.DelaieRealisation.setText(Heure.text())
        self.ui.DateRealisation.setText(Datefin.text())
        self.ui.EvaluationEfficacite.setText(Groupe.text())

        self.ui.BouttonModifier.show()
        self.ui.BouttonModifier.setStyleSheet("background-color: red; color: white; border: 2px solid black;")

        self.ID = ID

    def Envoie_Données(self):
          
            self.conn = self.Import_Base.Connection_BDD()
            cursor = self.conn.cursor()

            Datedebut = self.ui.Date.text()
            Fonction = self.ui.TypeAudit.currentText()
            Origine = self.ui.OrigineAction.currentText()
            Redacteur = self.ui.Redacteur.currentText()
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
            values = (Datedebut, Fonction, Origine, Redacteur, Secteur, LignePoste, Fonction2, Constat, Tâche, Commentaire, Responsablesecteur, Heure, Datefin, Groupe)
            cursor.execute(sql, values)

            # Valider la transaction
            self.conn.commit()

            # Fermer la connexion
            cursor.close()
            self.conn.close()

            self.clear_all(1)

    
    def Envoie_Données2(self):
          
        
            Datedebut = '2024-01-01'
            Fonction = 'Engineer'
            Origine = 'Internal'
            Redacteur = 'John Doe'
            Secteur = 'IT'
            LignePoste = 'Developer'
            Fonction2 = 'Lead'
            Constat = 'All good'
            Tâche = 'Coding'
            Commentaire = 'No comments'
            Responsablesecteur = 'Jane Smith'
            Heure = '12:00'
            Datefin = '2024-01-02'
            Groupe = 'Group A'

            # Convert QTableWidgetItem to string (or int if applicable)
            id_value = self.ui.ID.text()

            # Connect to the database
            self.conn = self.Import_Base.Connection_BDD()
            cursor = self.conn.cursor()

            # Check if the ID exists
            cursor.execute("SELECT COUNT(*) FROM Feuil1 WHERE ID = %s", (id_value,))
            result = cursor.fetchone()

            if result[0] > 0:
                # ID exists, update the data
                sql = """
                UPDATE Feuil1
                SET Datedebut = %s, Fonction = %s, Origine = %s, Rédacteur_Rédactrice = %s, Secteur = %s, Ligne_Poste = %s, Fonction2 = %s, Constat = %s, Tâche = %s, Commentaires = %s, Responsablesecteur = %s, Heure = %s, Datefin = %s, Groupe = %s
                WHERE ID = %s
                """
                values = (Datedebut, Fonction, Origine, Redacteur, Secteur, LignePoste, Fonction2, Constat, Tâche, Commentaire, Responsablesecteur, Heure, Datefin, Groupe, id_value)
            else:
                # ID does not exist, insert the data
                sql = """
                INSERT INTO Feuil1 (Datedebut, Fonction, Origine, Rédacteur_Rédactrice, Secteur, Ligne_Poste, Fonction2, Constat, Tâche, Commentaires, Responsablesecteur, Heure, Datefin, Groupe)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (Datedebut, Fonction, Origine, Redacteur, Secteur, LignePoste, Fonction2, Constat, Tâche, Commentaire, Responsablesecteur, Heure, Datefin, Groupe)

            cursor.execute(sql, values)
            self.conn.commit()

            cursor.close()
            self.conn.close()

            self.clear_all(1)

            self.hygiene.populate_table()

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