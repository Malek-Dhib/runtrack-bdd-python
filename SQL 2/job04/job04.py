import mysql.connector

# Remplacez les valeurs suivantes par les informations de votre base de données
host = "localhost"
user = "root"
password = "Malek2004"
database = "LaPlateforme"

# Créer une connexion à la base de données
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Créer un objet curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exécuter la requête pour récupérer les noms et les capacités de la table "salle"
query = "SELECT nom, capacite FROM salle"
cursor.execute(query)

# Récupérer tous les résultats
salles = cursor.fetchall()

# Afficher le résultat en console
for salle in salles:
    print(f"Nom: {salle[0]}, Capacité: {salle[1]}")

# Fermer le curseur et la connexion
cursor.close()
conn.close()
