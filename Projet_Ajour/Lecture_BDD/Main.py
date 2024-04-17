from PySide6 import QtWidgets
import sys

from MainWindow import MainWindow
from Import_Base import Import_Base

if __name__ == "__main__":
    i = 4

    app = QtWidgets.QApplication(sys.argv)
    import_base = Import_Base()
    #connect = Import_Base.fetch_data_from_mysql()
    data = import_base.fetch_data_from_mysql2(i)
    window = MainWindow(data, import_base)
    window.show()
    sys.exit(app.exec())



