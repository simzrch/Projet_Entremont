from Page import Page
from Import_Base import Import_Base
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets
from PySide6 import QtCore, QtWidgets


class RDR(Page):
    def __init__(self, hygiene):

        super(Page, self).__init__()
        # Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("RDR.ui")
        self.hygiene = hygiene
        self.ui.BouttonValide.clicked.connect(self.Envoie_Données)
        #self.ui.BouttonModifier.clicked.connect(self.Envoie_Données2)
        #self.ui.BouttonModifier.hide()
        self.Import_Base = Import_Base()

    def Affichage(self):
        
        self.hygiene.stackedWidget.addWidget(self.ui)
        self.hygiene.stackedWidget.setCurrentWidget(self.ui)   

    def Implemente_info(self, ID, Groupe, Datedebut, Fonction, Origine, Redacteur, Secteur, LignePoste, Fonction2, Constat, Tâche, Commentaire, Responsablesecteur, Heure, Datefin):

        pass

    def Envoie_Données(self):
          
        pass

    def get_last_id_from_database(self):

        pass
        
    def Envoie_Données2(self):
          
        pass
    
    def Implementation_ComboBox(self):

        self.clear_all(0)

        self.populate_combobox("Origine", "Feuil1", self.ui.Redacteur)
        self.populate_combobox("Origine2", "Feuil1", self.ui.Secteur)
        self.populate_combobox("Poste", "Information", self.ui.TypologieRisque)
        self.populate_combobox("Secteur", "Feuil1", self.ui.NivPyramide)
        self.populate_combobox("Datedebut", "Feuil1", self.ui.ResponsableAction)
        self.populate_combobox("Datedebut", "Feuil1", self.ui.ContributaurAction)


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