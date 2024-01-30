import mysql.connector
from mysql.connector import errorcode

# Connexion à la base de données MySQL
try:
    conn = mysql.connector.connect(
        user='root',
        password='Malek2004',
        host='localhost',
        database='zoo'
    )
    cursor = conn.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Accès refusé. Vérifiez votre nom d'utilisateur et votre mot de passe.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Base de données non existante. Créez la base de données 'zoo'.")
    else:
        print(err)
    exit()

# Fonction pour afficher tous les animaux
def afficher_animaux():
    query = "SELECT * FROM animal;"
    cursor.execute(query)
    result = cursor.fetchall()
    print("Liste des animaux dans le zoo:")
    for row in result:
        print(row)

# Fonction pour afficher les animaux dans les cages
def afficher_animaux_dans_cages():
    query = "SELECT a.id_animal, a.nom, a.race, c.id_cage FROM animal a LEFT JOIN cage c ON a.id_cage = c.id_cage;"
    cursor.execute(query)
    result = cursor.fetchall()
    print("Liste des animaux dans les cages:")
    for row in result:
        print(row)

# Fonction pour calculer la superficie totale des cages
def calculer_superficie_totale():
    query = "SELECT SUM(superficie) FROM cage;"
    cursor.execute(query)
    result = cursor.fetchone()
    superficie_totale = result[0] if result[0] is not None else 0
    print("Superficie totale de toutes les cages:", superficie_totale, "m²")

# Fonction pour demander au directeur d'ajouter, de supprimer ou de modifier des animaux ou des cages
def demander_action_directeur():
    print("\nQue souhaitez-vous faire ?")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    print("4. Afficher tous les animaux")
    print("5. Afficher les animaux dans les cages")
    print("6. Calculer la superficie totale de toutes les cages")
    print("7. Quitter")
    choix = input("Entrez le numéro de l'action souhaitée : ")
    return choix

# Boucle principale du programme
while True:
    choix = demander_action_directeur()

    if choix == "1":
        # Ajouter un animal
        nom = input("Entrez le nom de l'animal : ")
        race = input("Entrez la race de l'animal : ")
        id_cage = input("Entrez l'ID de la cage de l'animal : ")
        date_naissance = input("Entrez la date de naissance de l'animal (YYYY-MM-DD) : ")
        pays_origine = input("Entrez le pays d'origine de l'animal : ")

        query = f"INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES ('{nom}', '{race}', {id_cage}, '{date_naissance}', '{pays_origine}');"
        cursor.execute(query)
        conn.commit()
        print("Animal ajouté avec succès.")

    elif choix == "2":
        # Supprimer un animal
        id_animal = input("Entrez l'ID de l'animal à supprimer : ")
        query = f"DELETE FROM animal WHERE id_animal = {id_animal};"
        cursor.execute(query)
        conn.commit()
        print("Animal supprimé avec succès.")

    elif choix == "3":
        # Modifier un animal
        id_animal = input("Entrez l'ID de l'animal à modifier : ")
        nom = input("Entrez le nouveau nom de l'animal (appuyez sur Entrée pour ne pas modifier) : ")
        race = input("Entrez la nouvelle race de l'animal (appuyez sur Entrée pour ne pas modifier) : ")
        id_cage = input("Entrez le nouvel ID de la cage de l'animal (appuyez sur Entrée pour ne pas modifier) : ")
        date_naissance = input("Entrez la nouvelle date de naissance de l'animal (appuyez sur Entrée pour ne pas modifier) : ")
        pays_origine = input("Entrez le nouveau pays d'origine de l'animal (appuyez sur Entrée pour ne pas modifier) : ")

        update_query = "UPDATE animal SET"
        if nom:
            update_query += f" nom = '{nom}',"
        if race:
            update_query += f" race = '{race}',"
        if id_cage:
            update_query += f" id_cage = {id_cage},"
        if date_naissance:
            update_query += f" date_naissance = '{date_naissance}',"
        if pays_origine:
            update_query += f" pays_origine = '{pays_origine}',"

        # Supprimer la virgule finale si nécessaire
        update_query = update_query.rstrip(',')

        update_query += f" WHERE id_animal = {id_animal};"

        cursor.execute(update_query)
        conn.commit()
        print("Animal modifié avec succès.")

    elif choix == "4":
        afficher_animaux()

    elif choix == "5":
        afficher_animaux_dans_cages()

    elif choix == "6":
        calculer_superficie_totale()

    elif choix == "7":
        # Quitter le programme
        break

# Fermer la connexion à la base de données MySQL
conn.close()
