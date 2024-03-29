from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
import mysql.connector

class Page:
    def __init__(self, ui_file):
        self.loader = QUiLoader()
        self.ui = self.loader.load(ui_file, None)
        self.setup_ui_connections()

    def setup_ui_connections(self):
        raise NotImplementedError("La méthode setup_ui_connections doit être implémentée dans les sous-classes.")

    def show(self):
        self.ui.show()

    def hide(self):
        self.ui.hide()

class MainWindow(Page):
    def __init__(self, data):
        super(Page, self).__init__()
        # Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("TableauB.ui")

        # Récupérer le widget de tableau depuis le fichier .ui
        self.table_widget = self.ui.findChild(QTableWidget, "tableWidget")
        self.line_edit = self.ui.findChild(QLineEdit, "lineEdit1")
        self.line_edit2 = self.ui.findChild(QLineEdit, "lineEdit2")

        # Remplir le tableau avec les données
        self.populate_table(data)

        self.table_widget.cellClicked.connect(self.update_line_edit)

    def populate_table(self, data):
        # Définir le nombre de lignes et de colonnes du tableau
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))

        # Remplir le tableau avec les données
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_widget.setItem(row_idx, col_idx, item)
                

    def update_line_edit(self, row):
        # Récupérer la valeur de la cellule sélectionnée et l'afficher dans le QLineEdit

        item_2 = self.table_widget.item(row, 1)
        self.line_edit2.setText(item_2.text())
        if item_2 is not None:
         self.line_edit2.setText(item_2.text())
    
        item = self.table_widget.item(row, 0)
        self.line_edit.setText(item.text())
        if item is not None:
            self.line_edit.setText(item.text())




def fetch_data_from_mysql():
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="192.168.1.213",
        user="root",
        password="root",
        database="test_proje_entremont"
    )
    #cursor = connection.cursor()

    return connection

def fetch_data_from_mysql2(connection, i):
    cursor = connection.cursor()
    if i == 0 :
    # Execute SQL query
        cursor.execute("SELECT * FROM Feuil1")
        rows = cursor.fetchall()
    else: 
        cursor.execute("SELECT * FROM Feuil1 WHERE Origine = 'Plan actions général'")
        rows = cursor.fetchall()


    # Close connection
    #connection.close()

    return rows

