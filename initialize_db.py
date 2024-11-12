import sqlite3

# Chemin de la nouvelle base de données
db_path = 'traceforum.db'

# Lecture du fichier SQL
with open('./config/traceforum.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

# Création de la base de données et exécution du script SQL
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Exécute toutes les commandes du fichier SQL
cursor.executescript(sql_script)

# Ferme la connexion
conn.commit()
conn.close()

print(f"Base de données créée avec succès à {db_path}")
