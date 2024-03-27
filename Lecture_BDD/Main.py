from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
import mysql.connector

from Recuperation_BDD_Tableau import MainWindow
from Recuperation_BDD_Tableau import fetch_data_from_mysql

if __name__ == "__main__":
    app = QApplication([])
    data = fetch_data_from_mysql()
    window = MainWindow(data)
    window.show()
    app.exec()
