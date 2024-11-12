from database import get_data_from_database
from analytics import prepare_data, group_users_by_activity
from visualization import plot_participation_rates

# Chemin vers votre nouvelle base de données SQLite
db_path = 'traceforum.db'

# Extraction des données depuis la base de données
try:
    data = get_data_from_database()
    print("Données extraites avec succès de la base de données.")
except Exception as e:
    print(f"Erreur lors de l'extraction des données : {e}")
    exit(1)

# Préparation et analyse des données
data = prepare_data(data)
participation_df = group_users_by_activity(data)

# Affichage des résultats dans le terminal
print("Taux de participation par groupe et utilisateur:")
print(participation_df)

# Visualisation des résultats
try:
    plot_participation_rates(participation_df)
    print("Visualisation terminée avec succès.")
except Exception as e:
    print(f"Erreur lors de la visualisation des résultats : {e}")
