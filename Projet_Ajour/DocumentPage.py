import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QWidget
from PySide6.QtUiTools import QUiLoader

from Page import Page
import os
import mysql.connector
from Import_Base import Import_Base
from systeme_authentification import systemeAuthentification

class DocumentPage(Page, QWidget):
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

        self.button_name2 = None
        
        boutons = self.recuperer_donnees_bouton()
        # Mettre à jour chaque bouton avec le nom récupéré
        for id, nom_bouton in boutons.items():
            button_name = f"Button_{id}_Doc"
            button_widget = self.ui.findChild(QPushButton, button_name)
            if button_widget:
                button_widget.setText(nom_bouton)
            else:
                print(f"Erreur: Widget {button_name} introuvable.")
        

             
    def setup_ui_connections(self):
        loader = QUiLoader()
        self.form_ui = loader.load("Formulaire_document.ui")
        self.form_ui.setWindowTitle("Formulaire_document")
        self.form_ui.Bt_valider.clicked.connect(self.handle_bt_valider_click)
        self.form_ui.Bt_fichier.clicked.connect(self.open_file_explorer)
        #self.ui.pushButton_20.clicked.connect(self.vers_formulaire_document)
        
        #self.ui.Button_20_Doc.clicked.connect(self.ouverture_fichier)
        self.ui.ButtonAccueil.clicked.connect(self.domaine_accueil)
        #self.ui.Button_restriction.clicked.connect(self.affiche)

        for i in range(1, 31):
            button_name = f"Button_{i}_Doc"
            button_widget = self.ui.findChild(QPushButton, button_name)
            if button_widget:
                button_widget.clicked.connect(self.ouverture_fichier)
            else:
                print(f"Erreur: Widget {button_name} introuvable.")


        for i in range(1, 31):
            button_name1 = f"pushButton_{i}"
            self.button_widget1 = self.ui.findChild(QPushButton, button_name1)
            if  self.button_widget1:
                 self.button_widget1.clicked.connect(self.vers_formulaire_document)
            else:
                print(f"Erreur: Widget {button_name1} introuvable.")
            


    def affiche_niveau(self):
        authorization_level = self.auth_system.is_authorized("")
        print("je suis", authorization_level)

        button_restriction = self.ui.button_restriction 
        if button_restriction:
            button_restriction.setText(f"Niveau: {authorization_level}")  # Sinon, affiche le niveau actuel
        else:
            print("Erreur: Widget button_restriction introuvable.") 


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
        boutton = self.button_name2.split('_')[1]
        new_boutton = f"Button_{boutton}_Doc"
        button_widget = self.ui.findChild(QPushButton, new_boutton)
        if button_widget:
            button_widget.setText(new_button_name)
        else:
            print("Erreur: Widget Button_Doc introuvable.")
        print(new_button_name)
        self.form_ui.close()
         


    def authent_modif(self):
        print("début")
        authorization_level = self.auth_system.is_authorized("")
        print(f"Autorisation de l'utilisateur de niveau {authorization_level}")

        for i in range(1, 31):
            button_name = f"pushButton_{i}"
            button_widget = self.ui.findChild(QPushButton, button_name)

            if button_widget is not None:
                if authorization_level == 1 or authorization_level == 2:
                    button_widget.setEnabled(False)
                    print(f"{button_name} désactivé pour tous")
                elif authorization_level == 3:
                    button_widget.setEnabled(True)
                    print(f"{button_name} activé pour administrateur")
                else:
                    button_widget.setEnabled(False)
                    print(f"{button_name} désactivé (condition par défaut)")
            else:
                print(f"Erreur: Widget {button_name} introuvable.")

        print("fin") 




    def afficher_bouton(self):
        affichage_dict = self.recuperer_donnees_affichage()
        if affichage_dict is None:
            print("Erreur lors de la récupération des droits d'affichage.")
            return
        # Obtenir le niveau d'autorisation actuel de l'utilisateur
        authorization_level = self.auth_system.is_authorized("")
        print(f"Autorisation de l'utilisateur: {authorization_level}")
        # Parcourir tous les boutons et mettre à jour leur état en fonction des droits d'affichage
        for i in range(1, 31):
            button_name = f"Button_{i}_Doc"
            button_widget = self.ui.findChild(QPushButton, button_name)
            if button_widget is not None:
                id_ = str(i)
                valeur_afficher = affichage_dict.get(id_, "non_autorisé")

                if valeur_afficher == "tous":
                    button_widget.setEnabled(True)
                    print(f"{button_name}: tous")
                elif authorization_level == 2 and valeur_afficher == "Niv2_Niv3":
                    button_widget.setEnabled(True)
                    print(f"{button_name}: Niv2")
                elif authorization_level == 3 and valeur_afficher == "Niv2_Niv3":
                    button_widget.setEnabled(True)
                    print(f"{button_name}: Niv3")
                elif authorization_level == 1 and valeur_afficher != "tous":
                    button_widget.setEnabled(False)
                    print(f"{button_name}: Non autorisé")
                else:
                    button_widget.setEnabled(False)
                    print(f"{button_name}: Aucune condition satisfaite")
            else:
                print(f"Erreur: Widget {button_name} introuvable.")
        


    def ouverture_fichier(self):
        # Récupérer le chemin du fichier à partir de la base de données
        chemin_fichier = self.recuperer_donnees()
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
        
        sender = self.sender()
        if sender:
            self.button_name2 = sender.objectName()
            print(f"Le bouton {self.button_name2} a été cliqué.")


        self.form_ui.lineEdit_2.clear()
        self.form_ui.lineEdit.clear()
        self.form_ui.checkBox_3.setChecked(False)
        self.form_ui.checkBox.setChecked(False)
        self.form_ui.show()


    def recuperer_donnees(self):
        # Exécution de la requête SQL pour récupérer le chemin du fichier à partir de la base de données
        self.conn = self.Import_Base.Connection_BDD()
        cursor = self.conn.cursor()


        sender = self.sender()
        if sender:
            button_name3 = sender.objectName()
            print(f"Le bouton {button_name3} a été cliqué.")

        id_ = button_name3.split('_')[1]
        print(id_)
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
        self.conn = self.Import_Base.Connection_BDD()
        cursor = self.conn.cursor()

        # Exécution de la requête SQL pour récupérer tous les noms de boutons
        cursor.execute("SELECT id, Nom_bouton FROM chemin_fichier")

        # Récupération des résultats
        resultats = cursor.fetchall()

        # Fermeture de la connexion à la base de données
        cursor.close()
        self.conn.close()

        # Retourner les résultats sous forme de dictionnaire {id: nom_bouton}
        boutons = {resultat[0]: resultat[1] for resultat in resultats}
        return boutons


    def recuperer_donnees_affichage(self):
        # Exécution de la requête SQL pour récupérer les droits d'affichage de tous les boutons
        self.conn = self.Import_Base.Connection_BDD()
        cursor = self.conn.cursor()

        # Récupérer les droits d'affichage de tous les boutons
        cursor.execute("SELECT id, affichage FROM chemin_fichier")

        # Récupération des résultats
        resultats = cursor.fetchall()
        if resultats:
            affichage_dict = {str(resultat[0]): resultat[1] for resultat in resultats}
            return affichage_dict
        else:
            print("Les valeurs d'affichage n'ont pas été trouvées.")
            return None


    def fermer_connexion(self):
        # Fermeture du curseur et de la connexion à la base de données
        self.cursor.close()
        self.conn.close()

    def changeBDD_chemin(self):
        print(self.button_name2)
        new_path = self.form_ui.lineEdit_2.text()
        

        try:
            self.conn = self.Import_Base.Connection_BDD()
            cursor = self.conn.cursor()
            
            
            
            # Exemple de mise à jour du chemin de la base de données
            id_ = self.button_name2.split('_')[1]
            print(id_)
            cursor.execute("UPDATE chemin_fichier SET chemin = %s WHERE id = %s", (new_path,id_,))
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
            
            id_ = self.button_name2.split('_')[1]
            # Exemple de mise à jour du chemin de la base de données
            cursor.execute("UPDATE chemin_fichier SET Nom_bouton = %s WHERE id = %s", (new_pathi,id_,))
            self.conn.commit()

            print("Bouton de la base de données mis à jour avec succès.")
        except mysql.connector.Error as err:
            print("Erreur MySQL:", err)
       
        self.conn.close()

    def changeBDD_affichage(self):

        if self.form_ui.checkBox.isChecked() == True:
            new_aff = "Niv2_Niv3"
        elif self.form_ui.checkBox_3.isChecked() == True:
            new_aff = "tous"
        elif self.form_ui.checkBox.isChecked() == True and self.form_ui.checkBox_3.isChecked() == True :
            new_aff = "tous"
        else:
            new_aff = "rien"


        try:
            self.conn = self.Import_Base.Connection_BDD()
            cursor = self.conn.cursor()
        
            id_ = self.button_name2.split('_')[1]
            # Exemple de mise à jour du chemin de la base de données
            cursor.execute("UPDATE chemin_fichier SET affichage = %s WHERE id = %s", (new_aff,id_,))
            self.conn.commit()

            print("Bouton de la base de données mis à jour avec succès.")
        except mysql.connector.Error as err:
            print("Erreur MySQL:", err)
    
        self.conn.close()
        
    
            


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

