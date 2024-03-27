from PySide6.QtWidgets import QApplication

from Recuperation_BDD_Tableau import MainWindow
from Recuperation_BDD_Tableau import fetch_data_from_mysql

if __name__ == "__main__":
    app = QApplication([])
    data = fetch_data_from_mysql()
    window = MainWindow(data)
    window.show()
    app.exec()