import mysql.connector

class Import_Base():
    

    def __init__(self):
        
        connection = mysql.connector.connect(
            host="192.168.1.213",
            user="root",
            password="root",
            database="test_proje_entremont"
        )

        self.conn = connection
    
    def Connection_BDD(self):
        connection = mysql.connector.connect(
            host="192.168.1.213",
            user="root",
            password="root",
            database="test_proje_entremont"
        )

        return connection
        

    def fetch_data_from_mysql2(self, i):
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM visiteurs")
        rows = cursor.fetchall()
        # if i == 0 :
        # # Execute SQL query
        #     cursor.execute("SELECT * FROM Feuil1")
        #     rows = cursor.fetchall()
        # else: 
        #     cursor.execute("SELECT * FROM Feuil1 WHERE Origine = 'Plan actions général'")
        #     rows = cursor.fetchall()


        # Close connection
        #cursor.close()
        
        return rows


    def ajoute_donne(self):

        cursor = self.conn.cursor()
            
        sql = "INSERT INTO visiteurs (id, name, age) VALUES (NULL, %s, %s)"
        user = ("Pêche", str(5)) #Contien les valeurs a rentré
        cursor.execute(sql, user) #Execute les 2 fonctions 
        self.conn.commit() #Active la commande d'envoie