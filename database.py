import mysql.connector
import pandas as pd


def get_data_from_database():
    # Connexion à la base de données MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Remplacez par votre nom d'utilisateur MySQL
        password="",  # Remplacez par votre mot de passe MySQL
        database="traceforum",
        port=3306
    )

    # Extraction des données
    query = """
    SELECT Utilisateur, Titre, Date, Heure
    FROM transition
    """
    data = pd.read_sql(query, conn)
    conn.close()
    return data
