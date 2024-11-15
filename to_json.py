import json
import datetime
import os


def serialize_data(data):
    """Transforme les données en un format JSON sérialisable."""
    for row in data:
        for key, value in row.items():
            if isinstance(value, (datetime.date, datetime.datetime)):
                row[key] = value.isoformat()
            elif isinstance(value, datetime.timedelta):
                row[key] = str(value)
    return data

def ensure_directory(directory_name):
    """
    Vérifie si un dossier existe, sinon le crée.

    Parameters:
        directory_name (str): Nom du dossier à vérifier/créer.
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def export_table_to_json(table_name, file_name,output_directory="sql_to_json_data"):
    """Exporte une table spécifique vers un fichier JSON."""
    ensure_directory(output_directory)
    try:
        from database import get_table_data  # Import local pour éviter les circular imports
        data = get_table_data(table_name)
        if data:
            serialized_data = serialize_data(data)
            with open(os.path.join(output_directory, file_name), "w", encoding="utf-8") as json_file:
                json.dump(serialized_data, json_file, indent=4, ensure_ascii=False)
            print(f"Table {table_name} exportée vers {file_name}")
        else:
            print(f"Aucune donnée trouvée pour la table {table_name}")
    except Exception as e:
        print(f"Erreur lors de l'exportation de la table {table_name} : {e}")

def export_all_tables_to_single_json(output_file, output_directory="sql_to_json_data"):
    """Exporte toutes les tables de la base de données vers un fichier JSON."""
    ensure_directory(output_directory)
    try:
        from database import connect_to_database  # Import local
        conn = connect_to_database()
        cursor = conn.cursor()

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        all_tables_data = {}
        for (table_name,) in tables:
            cursor.execute(f"SELECT * FROM {table_name}")
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            table_data = [dict(zip(columns, row)) for row in rows]
            all_tables_data[table_name] = serialize_data(table_data)

        with open(os.path.join(output_directory, output_file), "w", encoding="utf-8") as json_file:
            json.dump(all_tables_data, json_file, indent=4, ensure_ascii=False)
        print(f"Toutes les tables exportées vers {output_file}")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erreur lors de l'exportation de toutes les tables : {e}")
