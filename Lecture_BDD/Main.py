from PySide6.QtWidgets import QApplication,  QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets
import sys

from Recuperation_BDD_Tableau import MainWindow
from Recuperation_BDD_Tableau import fetch_data_from_mysql
from Recuperation_BDD_Tableau import fetch_data_from_mysql2

if __name__ == "__main__":
    i = 0

    app = QtWidgets.QApplication(sys.argv)
    data1 = fetch_data_from_mysql()
    data = fetch_data_from_mysql2(data1, i)
    window = MainWindow(data)
    window.show()
    sys.exit(app.exec())

