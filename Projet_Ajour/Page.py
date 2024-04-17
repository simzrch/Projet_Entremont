from PySide6.QtUiTools import QUiLoader

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
