from systeme_authentification import systemeAuthentification

# Création d'une instance du système d'authentification
auth_system = systemeAuthentification()
print("Bienvenue dans le système d'authentification.")
while True:
    username = input("Nom d'utilisateur (ou 'q' pour quitter) : ")
    if username.lower() == 'q':
        print("Merci d'avoir utilisé le système d'authentification.")
        break
    
    password = input("Mot de passe : ")
    resultat = auth_system.verifier_authentification(username, password)
    print(resultat)

    auth_system.conn.close()