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
    if auth_system.verifier_authentification(username, password):
        while True:
            action = input("Que voulez-vous faire? (1. Déconnexion / 2. Vérifier autorisation) : ")
            if action == "1":
                auth_system.logout()
                break
            elif action == "2":
                required_role = input("Quel niveau d'autorisation voulez-vous vérifier? (admin/moderateur/basic) : ")
                if auth_system.is_authorized(required_role):
                    print(f"autorisation du niveau {required_role}.")
                else:
                    print("Vous n'avez pas le niveau d'autorisation requis.")
            else:
                print("Commande non reconnue.")
    else:
        print("L'authentification a échoué. Veuillez réessayer.")

    

auth_system.conn.close()

