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

# Exécuter la requête pour calculer la superficie totale des étages
query = "SELECT SUM(superficie) AS superficie_totale FROM etage"
cursor.execute(query)

# Récupérer le résultat
result = cursor.fetchone()

# Afficher le résultat
superficie_totale = result[0]
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermer le curseur et la connexion
cursor.close()
conn.close()
