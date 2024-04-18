from Page import Page
from PySide6.QtUiTools import QUiLoader

class PAG(Page):
    def __init__(self, hygiene):

        super(Page, self).__init__()
        # Charger le fichier .ui
        loader = QUiLoader()
        self.ui = loader.load("PAG.ui")
        self.hygiene = hygiene

    def Affichage(self):
        
        self.hygiene.stackedWidget.addWidget(self.ui)
        self.hygiene.stackedWidget.setCurrentWidget(self.ui)