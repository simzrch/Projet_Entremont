from Page import Page
from Import_Base import Import_Base
from PySide6.QtUiTools import QUiLoader


class GestionPage(Page):
    def __init__(self, perimetre, accueil_origine):

        super(Page, self).__init__()
    #    Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("gestion.ui")

        self.ui.setWindowTitle("Gestion des acces")
        self.accueilOrigine = accueil_origine
        self.perimetre = perimetre
        self.setup_ui_connections()
    #    self.perimetres_page = PerimetresPage(self)
        self.Import_BDD = Import_Base()

    def setup_ui_connections(self):

        self.ui.ButtonAccueil.clicked.connect(self.gestion_vers_accueil)
        self.ui.ButtonPerimetres.clicked.connect(self.gestion_vers_perimetres)
        self.ui.ButtonZones.clicked.connect(self.gestion_vers_zones)
        self.ui.ButtonEntrer.clicked.connect(self.Envoie_Donne)

    def Envoie_Donne(self):

        Nom = self.ui.lineEditNom.text()
        connection = self.Import_BDD.Connection_BDD()
        cursor = connection.cursor()
            
        sql = "INSERT INTO Liste_acces (Nom) VALUES (%s)"
        user = (Nom) #Contien les valeurs a rentré
        cursor.execute(sql, user) #Execute les 2 fonctions 
        connection.commit() #Active la commande d'envoie
        

    def gestion_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def gestion_vers_perimetres(self):

        self.accueilOrigine.perimetres_page.show()
        self.hide()

    def gestion_vers_zones(self):

        self.perimetre.zones_page.show()
        self.hide()
