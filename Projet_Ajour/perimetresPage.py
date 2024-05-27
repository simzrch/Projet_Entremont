from Page import Page
from Import_Base import Import_Base
from PySide6.QtWidgets import QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from gestionPage import GestionPage
from zonesPage import ZonesPage
import mysql.connector


class PerimetresPage(Page):
    def __init__(self, accueil_origine):

        super(Page, self).__init__()
        # Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("perimetres.ui")

        self.ui.setWindowTitle("Perimetres")
        self.accueilOrigine = accueil_origine
        self.Import_BDD = Import_Base()
        self.table_widget = self.ui.tableWidgetAcces
        self.setup_ui_connections()
        self.gestion_page = GestionPage(self, accueil_origine)
        self.zones_page = ZonesPage(self, accueil_origine)

    def setup_ui_connections(self):

        self.accueilOrigine
        self.ui.ButtonAccueil.clicked.connect(self.perimetres_vers_accueil)
        self.ui.ButtonGestion.clicked.connect(self.perimetres_vers_gestion)
        self.ui.ButtonZones.clicked.connect(self.perimetres_vers_zones)

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

    def perimetres_vers_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def perimetres_vers_gestion(self):

        self.gestion_page.show()
        self.hide()

    def perimetres_vers_zones(self):

        self.zones_page.show()
        self.hide()
