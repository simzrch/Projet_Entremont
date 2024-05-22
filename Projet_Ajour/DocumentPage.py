import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PySide6.QtUiTools import QUiLoader
from Page import Page
import os
import mysql.connector

class DocumentPage(Page):
    def __init__(self, ui_file, db_host, db_user, db_password, db_database):
        super().__init__(ui_file)
        self.conn = mysql.connector.connect(host="192.168.1.213", user="root", password="root", database="test_proje_entremont")
        self.cursor = self.conn.cursor()

        loader = QUiLoader()
        self.ui = loader.load("document.ui")
        self.ui.setWindowTitle("document")
        
        self.setup_ui_connections()
        
             
    def setup_ui_connections(self):
        loader = QUiLoader()
        self.form_ui = loader.load("Formulaire_document.ui")
        self.form_ui.setWindowTitle("Formulaire_document")
        self.form_ui.Bt_valider.clicked.connect(self.update_button_text)
        self.form_ui.Bt_valider.clicked.connect(self.changeBDD_chemin)
        self.form_ui.Bt_valider.clicked.connect(self.changeBDD_bouton)
        self.form_ui.Bt_fichier.clicked.connect(self.open_file_explorer)
        self.ui.pushButton_23.clicked.connect(self.vers_formulaire_document)
        self.form_ui.radioButton.clicked.connect(self.afficher_personne)
        self.ui.Button_9_Doc.clicked.connect(self.ouverture_fichier)
        


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
        button_widget = self.ui.findChild(QPushButton, "Button_9_Doc")
        if button_widget:
            button_widget.setText(new_button_name)
        else:
            print("Erreur: Widget Button_9_Doc introuvable.")
        self.form_ui.lineEdit.clear()
        self.form_ui.checkBox.setChecked(False)
        self.form_ui.checkBox_2.setChecked(False)
        self.form_ui.checkBox_3.setChecked(False)
        self.form_ui.radioButton.setChecked(False)
        self.form_ui.close()
        #print("Chemin du fichier sélectionné :", file_path)  # Afficher le chemin dans la console



    def afficher_personne(self):
        if self.form_ui.radioButton.isChecked():
            self.form_ui.checkBox_2.setChecked(True)
            self.form_ui.checkBox_3.setChecked(True)
            self.form_ui.checkBox.setChecked(True)


    def ouverture_fichier(self):
        # Récupérer le chemin du fichier à partir de la base de données
        chemin_fichier = self.recuperer_donnees()

        if chemin_fichier:
            try:
                # Ouvrir le fichier avec le programme par défaut associé à son extension de fichier
                os.startfile(chemin_fichier)
            except FileNotFoundError:
                # Gérer le cas où le fichier spécifié n'est pas trouvé
                print("Le fichier n'a pas été trouvé.")
            except Exception as e:
                # Gérer toutes les autres exceptions qui pourraient survenir pendant l'ouverture du fichier
                print("Une erreur s'est produite lors de l'ouverture du fichier :", e)
        else:
            print("Le chemin du fichier n'a pas été trouvé.")



    def vers_formulaire_document(self):
        self.form_ui.lineEdit_2.clear()
        self.form_ui.show()


    def recuperer_donnees(self):
        # Exécution de la requête SQL pour récupérer le chemin du fichier à partir de la base de données
        id_ = 1  # ID de la ligne à récupérer
        self.cursor.execute("SELECT * FROM chemin_fichier WHERE id = %s", (id_,))
    
        # Récupération du chemin du fichier
        resultat = self.cursor.fetchone()
        if resultat:
            chemin_fichier = resultat[1]
            return chemin_fichier
        else:
            print("Le chemin du fichier n'a pas été trouvé.")
            return None


    def fermer_connexion(self):
        # Fermeture du curseur et de la connexion à la base de données
        self.cursor.close()
        self.conn.close()

    def changeBDD_chemin(self):
        new_path = self.form_ui.lineEdit_2.text()

        try:
            # Connexion à la base de données
            conn = mysql.connector.connect(host="192.168.1.213", user="root", password="root", database="test_proje_entremont")
            cursor = conn.cursor()
            
            # Exemple de mise à jour du chemin de la base de données
            cursor.execute("UPDATE chemin_fichier SET chemin = %s WHERE id = 1", (new_path,))
            conn.commit()

            print("Chemin de la base de données mis à jour avec succès.")
        except mysql.connector.Error as err:
            print("Erreur MySQL:", err)
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def changeBDD_bouton(self):
        new_pathi = self.form_ui.lineEdit.text()

        try:
            # Connexion à la base de données
            conn = mysql.connector.connect(host="192.168.1.213", user="root", password="root", database="test_proje_entremont")
            cursor = conn.cursor()
            
            # Exemple de mise à jour du chemin de la base de données
            cursor.execute("UPDATE chemin_fichier SET Nom_bouton = %s WHERE id = 1", (new_pathi,))
            conn.commit()

            print("Chemin de la base de données mis à jour avec succès.")
        except mysql.connector.Error as err:
            print("Erreur MySQL:", err)
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
        
if __name__ == "__main__":
    # Informations de connexion à la base de données
    db_host = "192.168.1.213"
    db_user = "root"
    db_password = "root"
    db_database = "test_proje_entremont"

    # Création de l'application Qt
    app = QApplication(sys.argv)
    
    # Création de la page de document en passant les informations de connexion à la base de données
    document_page = DocumentPage("document.ui", db_host, db_user, db_password, db_database)

    # Afficher la fenêtre
    document_page.ui.show()

    # Exécution de l'application
    sys.exit(app.exec())

