import mysql.connector
from mysql.connector import errorcode

class Employe:
    def __init__(self, user, password, host, database):
        self.conn = None
        self.cursor = None
        try:
            self.conn = mysql.connector.connect(
                user=user,
                password=password,
                host=host,
                database=database
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Accès refusé. Vérifiez votre nom d'utilisateur et votre mot de passe.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de données non existante. Créez la base de données.")
            else:
                print(err)
            exit()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s);"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Employé ajouté avec succès.")

    def read_employes(self):
        query = "SELECT * FROM employe;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("Liste des employés:")
        for row in result:
            print(row)

    def update_employe(self, employe_id, new_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s;"
        values = (new_salaire, employe_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Salaire de l'employé mis à jour avec succès.")

    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s;"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Employé supprimé avec succès.")

    def __del__(self):
        if self.conn:
            self.conn.close()

# Exemple d'utilisation de la classe Employe
if __name__ == "__main__":
    # Remplacez ces valeurs par vos informations de connexion
    employe_manager = Employe(user='root', password='Malek2004', host='localhost', database='entreprise')

    # Exemples d'opérations CRUD
    employe_manager.create_employe(nom='Smith', prenom='John', salaire=50000.00, id_service=1)
    employe_manager.read_employes()
    employe_manager.update_employe(employe_id=1, new_salaire=55000.00)
    employe_manager.read_employes()
    employe_manager.delete_employe(employe_id=1)
    employe_manager.read_employes()
