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

# Exécuter la requête pour calculer la capacité totale des salles
query = "SELECT SUM(capacite) AS capacite_totale FROM salle"
cursor.execute(query)

# Récupérer le résultat
result = cursor.fetchone()

# Afficher le résultat
capacite_totale = result[0]
print(f"La capacité totale des salles est de {capacite_totale}")

# Fermer le curseur et la connexion
cursor.close()
conn.close()
