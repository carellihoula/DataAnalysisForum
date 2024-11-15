import mysql.connector

def connect_to_database():
    """Établit une connexion à la base de données MySQL."""
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Remplacez par votre utilisateur MySQL
        password="",   # Remplacez par votre mot de passe MySQL
        database="traceforum",
        port=3308
    )

def get_table_data(table_name):
    """Récupère les données d'une table spécifique."""
    try:
        conn = connect_to_database()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print(f"Erreur lors de la récupération des données de la table {table_name} : {e}")
        return []
