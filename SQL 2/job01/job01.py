import mysql.connector

# Créer une connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Malek2004",
    database="LaPlateforme"
)

# Créer un objet curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exécuter la requête pour récupérer l'ensemble des étudiants
query = "SELECT * FROM etudiant"
cursor.execute(query)

# Récupérer tous les résultats
etudiants = cursor.fetchall()

# Afficher le résultat en console
for etudiant in etudiants:
    print(etudiant)

# Fermer le curseur et la connexion
cursor.close()
conn.close()
