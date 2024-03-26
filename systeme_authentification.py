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
        rows = self.cursor.fetchall()
        #for row in rows:
            #print('{0} : {1} - {2}'.format(row[0], row[1], row[2])) #Affiche les données
        #print("Nombre de lignes dans le tableau rows :", len(rows))
        if len(rows) == 0 :
            print("identifiant invalide")
        else :
            print(("Authentification reussie test"))
            print(rows)
        
        
        
        
    




#user = self.cursor.fetchone()

        #print(password)

        #if user:
            #id = user[0]
            #query = "SELECT * FROM mdp WHERE id = %s"
            #self.cursor.execute(query, (id,))
            #id = self.cursor.fetchone()
            #print("zef")
            #print(id)
        #if id == Niv1:
            #resultat == "Bienvenue, {username} ! Niveau d'accès : Niv1"
        #elif id== Niv2:
            #resultat =="Bienvenue, {username} ! Niveau d'accès : Niv2"
        #elif id == Niv3:
            #resultat =="Bienvenue, {username} ! Niveau d'accès : Niv3"
        #else:
            #resultat =="Nom d'utilisateur ou mot de passe incorrect."

        #return resultat