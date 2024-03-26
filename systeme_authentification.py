from User import User
from Niv3 import Niv3
from Niv2 import Niv2
import mysql.connector
import hashlib


class systemeAuthentification:
    def __init__(self):
        self.conn = mysql.connector.connect(host="192.168.1.213", user="root", password="root", database="test_proje_entremont")
        self.cursor = self.conn.cursor()
        self.logged_in_user = None



    def hash_password(self, password):
        # Convertir le mot de passe en octect
        password_bytes = password.encode('utf-8')
        
        # Calculer le hachage SHA-256
        hashed_password = hashlib.sha256(password_bytes).hexdigest()
        
        return hashed_password




    def verifier_authentification(self, username, password):
        hashed_password = self.hash_password(password)
        query = "SELECT * FROM mdp WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, hashed_password))
        rows = self.cursor.fetchall()
        #for row in rows:
            #print('{0} : {1} - {2}'.format(row[0], row[1], row[2])) #Affiche les données
        #print("Nombre de lignes dans le tableau rows :", len(rows))
        if len(rows) == 0 :
            print("identifiant invalide")
            print (len(rows))
            return False
        else :
            print(("Authentification reussie test"))
            print(rows)
            print (len(rows))
            user_data = rows[0]
            self.logged_in_user = User(username=user_data[0], role=user_data[0])
            print(f"Bienvenue, {username}! Vous êtes connecté en tant que {self.logged_in_user.role}")
            return True

    
    def logout(self):
        if self.logged_in_user:
            print(f"Déconnexion de l'utilisateur {self.logged_in_user.username}")
            self.logged_in_user = None
        else:
            print("Aucun utilisateur connecté")

    def is_authorized(self, required_role):
        if self.logged_in_user.role == "Niv1" and required_role.lower() == "basic":
                return True
        elif self.logged_in_user.role == "Niv2" and required_role.lower() != "admin":
                return True
        elif self.logged_in_user.role == "Niv3":
                return True
        return False
        
        



