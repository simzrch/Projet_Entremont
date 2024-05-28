import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox
from PySide6.QtUiTools import QUiLoader
from Page import Page
import os
import mysql.connector
from Import_Base import Import_Base
from systeme_authentification import systemeAuthentification

class DocumentPage(Page):
    def __init__(self, accueil_origine):
        super(Page, self).__init__()
        self.auth_system = accueil_origine.auth_system
        self.accueilOrigine = accueil_origine

        #authorization_level = self.auth_system.is_authorized("")
        #authorization_level == 1
        

        loader = QUiLoader()
        self.ui = loader.load("document.ui")
        self.ui.setWindowTitle("document")
        self.Import_Base = Import_Base()
        
        self.setup_ui_connections()

        chemin_bouton = self.recuperer_donnees_bouton()
        button_widget = self.ui.findChild(QPushButton, "Button_20_Doc")
        if button_widget:
            button_widget.setText(chemin_bouton)
        else:
            print("Erreur: Widget Button_20_Doc introuvable.")
        
             
    def setup_ui_connections(self):
        loader = QUiLoader()
        self.form_ui = loader.load("Formulaire_document.ui")
        self.form_ui.setWindowTitle("Formulaire_document")
        self.form_ui.Bt_valider.clicked.connect(self.handle_bt_valider_click)
        self.form_ui.Bt_fichier.clicked.connect(self.open_file_explorer)
        self.ui.pushButton_20.clicked.connect(self.vers_formulaire_document)
        self.form_ui.radioButton.clicked.connect(self.afficher_personne)
        self.ui.Button_20_Doc.clicked.connect(self.ouverture_fichier)
        self.ui.ButtonAccueil.clicked.connect(self.domaine_accueil)
        #self.ui.Button_restriction.clicked.connect(self.affiche)
       
    def handle_bt_valider_click(self):
        self.update_button_text()
        self.changeBDD_chemin()
        self.changeBDD_bouton()
        self.changeBDD_affichage()
        self.afficher_bouton()
        
    def domaine_accueil(self):

        self.accueilOrigine.show()
        self.hide()

    def open_file_explorer(self):       
        file_dialog = QFileDialog(self.ui)  # Utiliser self.ui comme parent
        file_dialog.setWindowTitle("Ouvrir un fichier")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            file_path = selected_files[0]  # Récupérer le chemin du fichier sélectionné
            self.form_ui.lineEdit_2.setText(file_path)  # Mettre à jour le texte du QLineEdit avec le chemin du fichier sélectionné
            print("Chemin du fichier sélectionné :", file_path)  # Afficher le chemin dans la console

    def update_button_text(self):
        new_button_name = self.form_ui.lineEdit.text()
        button_widget = self.ui.findChild(QPushButton, "Button_20_Doc")
        if button_widget:
            button_widget.setText(new_button_name)
        else:
            print("Erreur: Widget Button_20_Doc introuvable.")
        print(new_button_name)
        self.form_ui.close()
         




    def authent_modif(self):
        print("début")
        authorization_level = self.auth_system.is_authorized("")
        print(f"Autorisation de l'utilisateur de niveau {authorization_level}")

        if authorization_level == 1:
            self.ui.pushButton_20.setEnabled(False)
            print("tous")
        elif authorization_level == 2:
            self.ui.pushButton_20.setEnabled(False)
            print("Niv2")
        elif authorization_level == 3:
            self.ui.pushButton_20.setEnabled(True)
        else:
            ("marche pas ")
            self.ui.pushButton_20.setEnabled(False)

        print("fin") 




    def afficher_bouton(self):
        valeur_afficher = self.recuperer_donnees_affichage()

        # Obtenir le niveau d'autorisation actuel de l'utilisateur
        authorization_level = self.auth_system.is_authorized("")

        print(f"Valeur à afficher: {valeur_afficher}")
        print(f"Autorisation de l'utilisateur: {authorization_level}")
        
        print(authorization_level == 2)
        print(valeur_afficher == "Niv2")

        if valeur_afficher == "tous":
            self.ui.Button_20_Doc.setEnabled(True)
            print("tous")
        elif authorization_level == 2 and valeur_afficher == "Niv2":
            self.ui.Button_20_Doc.setEnabled(True)
            print("Niv2",)
        elif authorization_level == 2 and valeur_afficher == "Niv3":
            self.ui.Button_20_Doc.setEnabled(False)
            print("Niv3 mais désactivé pour Niv2")
        elif authorization_level == 3 and valeur_afficher == "Niv3":
            self.ui.Button_20_Doc.setEnabled(True)
            print("Niv3")
        elif authorization_level == 3 and valeur_afficher == "Niv2":
            self.ui.Button_20_Doc.setEnabled(False)
            print("Niv2 mais désactivé pour Niv3")
        elif authorization_level == 1 and valeur_afficher != "tous":
            self.ui.Button_20_Doc.setEnabled(False)
            print("Non autorisé")
        else:
            self.ui.Button_20_Doc.setEnabled(False)
            print("Aucune condition satisfaite")


    def afficher_personne(self):
        if self.form_ui.radioButton.isChecked():
            self.form_ui.checkBox_2.setChecked(True)
            self.form_ui.checkBox_3.setChecked(True)
            self.form_ui.checkBox.setChecked(True)
        else:
            self.form_ui.checkBox_2.setChecked(False)
            self.form_ui.checkBox_3.setChecked(False)
            self.form_ui.checkBox.setChecked(False)
        


    def ouverture_fichier(self):
        # Récupérer le chemin du fichier à partir de la base de données
        chemin_fichier = self.recuperer_donnees()

        print("d")

        try:
            # Ouvrir le fichier avec le 
            # programme par défaut associé à son extension de fichier
            
            print(chemin_fichier)

            print(type(chemin_fichier))
            chemin_fichier = chemin_fichier.replace('/', '\\')
            os.startfile(chemin_fichier)
            #os.startfile("\\\\serveur-SNIR\\Public\\intro_methode.PNG")
            print("Fin ouverture")
        except FileNotFoundError:
            # Gérer le cas où le fichier spécifié n'est pas trouvé
            print("Le fichier n'a pas été trouvé.")
        except Exception as e:
            # Gérer toutes les autres exceptions qui pourraient survenir pendant l'ouverture du fichier
            print("Une erreur s'est produite lors de l'ouverture du fichier :", e)
        



    def vers_formulaire_document(self):
        self.form_ui.lineEdit_2.clear()
        self.form_ui.lineEdit.clear()
        self.form_ui.checkBox_2.setChecked(False)
        self.form_ui.checkBox_3.setChecked(False)
        self.form_ui.checkBox.setChecked(False)
        self.form_ui.radioButton.setChecked(False)
        self.form_ui.show()


    def recuperer_donnees(self):
        # Exécution de la requête SQL pour récupérer le chemin du fichier à partir de la base de données
        self.conn = self.Import_Base.Connection_BDD()
        cursor = self.conn.cursor()


        id_ = 1  # ID de la ligne à récupérer
        cursor.execute("SELECT * FROM chemin_fichier WHERE id = %s", (id_,))

        # Récupération du chemin du fichier
        resultat = cursor.fetchone()
        if resultat:
            chemin_fichier = resultat[1]
            
            return chemin_fichier
        else:
            print("Le chemin du fichier n'a pas été trouvé.")
            return None
        
    def recuperer_donnees_bouton(self):
        # Exécution de la requête SQL pour récupérer le chemin du fichier à partir de la base de données
        self.conn = self.Import_Base.Connection_BDD()
        cursor = self.conn.cursor()


        id_ = 1  # ID de la ligne à récupérer
        cursor.execute("SELECT * FROM chemin_fichier WHERE id = %s", (id_,))

        # Récupération du chemin du fichier
        resultat = cursor.fetchone()
        if resultat:
            chemin_bouton = resultat[2]
            
            return chemin_bouton
        else:
            print("Le chemin du bouton n'a pas été trouvé.")
            return None
        
    def recuperer_donnees_affichage(self):
        # Exécution de la requête SQL pour récupérer le chemin du fichier à partir de la base de données
        self.conn = self.Import_Base.Connection_BDD()
        cursor = self.conn.cursor()


        id_ = 1  # ID de la ligne à récupérer
        cursor.execute("SELECT * FROM chemin_fichier WHERE id = %s", (id_,))

        # Récupération du chemin du fichier
        resultat = cursor.fetchone()
        if resultat:
            valeur_affichage = resultat[3]
            
            return valeur_affichage
        else:
            print("La valeur de l'affichage n'a pas été trouvé.")
            return None


    def fermer_connexion(self):
        # Fermeture du curseur et de la connexion à la base de données
        self.cursor.close()
        self.conn.close()

    def changeBDD_chemin(self):
        new_path = self.form_ui.lineEdit_2.text()

        try:
            self.conn = self.Import_Base.Connection_BDD()
            cursor = self.conn.cursor()
            
            
            # Exemple de mise à jour du chemin de la base de données
            cursor.execute("UPDATE chemin_fichier SET chemin = %s WHERE id = 1", (new_path,))
            self.conn.commit()

            print("Chemin de la base de données mis à jour avec succès.")
        except mysql.connector.Error as err:
            print("Erreur MySQL:", err)

        self.conn.close()

    def changeBDD_bouton(self):
        new_pathi = self.form_ui.lineEdit.text()

        try:
            self.conn = self.Import_Base.Connection_BDD()
            cursor = self.conn.cursor()
            
            # Exemple de mise à jour du chemin de la base de données
            cursor.execute("UPDATE chemin_fichier SET Nom_bouton = %s WHERE id = 1", (new_pathi,))
            self.conn.commit()

            print("Bouton de la base de données mis à jour avec succès.")
        except mysql.connector.Error as err:
            print("Erreur MySQL:", err)
       
        self.conn.close()

    def changeBDD_affichage(self):

        if self.form_ui.checkBox.isChecked() == True:
            new_aff = "Niv2"
        elif self.form_ui.checkBox_2.isChecked() == True:
            new_aff = "Niv3"
        elif self.form_ui.checkBox_3.isChecked() == True:
            new_aff = "tous"
        elif self.form_ui.checkBox.isChecked() == True and self.form_ui.checkBox_2.isChecked() == True :
            new_aff = "Niv2_Niv3"
        else:
            new_aff = "rien"


        try:
            self.conn = self.Import_Base.Connection_BDD()
            cursor = self.conn.cursor()
        
            # Exemple de mise à jour du chemin de la base de données
            cursor.execute("UPDATE chemin_fichier SET affichage = %s WHERE id = 1", (new_aff,))
            self.conn.commit()

            print("Bouton de la base de données mis à jour avec succès.")
        except mysql.connector.Error as err:
            print("Erreur MySQL:", err)
    
        self.conn.close()
        
    #def affiche(self):
        #self.auth_system.affichage_niveau()
            


if __name__ == "__main__":
    # Informations de connexion à la base de données
    

    # Création de l'application Qt
    app = QApplication(sys.argv)
    
    # Création de la page de document en passant les informations de connexion à la base de données
    document_page = DocumentPage("document.ui")

    # Afficher la fenêtre
    document_page.ui.show()

    # Exécution de l'application
    sys.exit(app.exec())

