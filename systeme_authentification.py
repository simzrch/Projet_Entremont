from Niv1 import Niv1
from Niv3 import Niv3
from Niv2 import Niv2
import mysql.connector



class systemeAuthentification:
    def __init__(self):
        self.conn = mysql.connector.connect(host="192.168.1.213", user="root", password="root", database="test_proje_entremont")
        self.cursor = self.conn.cursor()
        

    def verifier_authentification(self, username, password):
        query = "SELECT * FROM mdp WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        resultat = "coucou"

        print(id)
        if id == Niv1:
            resultat == "Bienvenue, {username} ! Niveau d'accès : Niv1"
        elif id== Niv2:
            resultat =="Bienvenue, {username} ! Niveau d'accès : Niv2"
        elif id == Niv3:
            resultat =="Bienvenue, {username} ! Niveau d'accès : Niv3"
        else:
            resultat =="Nom d'utilisateur ou mot de passe incorrect."

        return resultat