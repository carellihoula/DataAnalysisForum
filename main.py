import json
import pandas as pd
from to_json import export_table_to_json, export_all_tables_to_single_json
from calculs import exclude_users, assign_random_groups, calculate_group_participation
from visualization import plot_group_participation

# Étape 1 : Exporter les données de la table transition vers un fichier JSON
export_table_to_json("transition", "transition_data.json")

# Étape 2 : Exporter toutes les tables dans un seul fichier JSON
export_all_tables_to_single_json("all_tables_data.json")

# Étape 3 : Charger les données depuis le fichier JSON
with open("transition_data.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Étape 4 : Convertir les données en DataFrame
df = pd.DataFrame(data)

# Étape 5 : Exclure les utilisateurs spécifiques
exclusion_list = ["mmay", "madeth", "admin"]
etudiants_df = exclude_users(df, exclusion_list)

# Étape 6 : Assigner les étudiants à trois groupes aléatoires
group_names = ["Groupe 1", "Groupe 2", "Groupe 3"]
etudiants_df = assign_random_groups(etudiants_df, group_names)

# Étape 7 : Calculer le taux de participation par groupe
taux_participation = calculate_group_participation(etudiants_df)

# Étape 8 : Sauvegarder les résultats dans un fichier JSON
with open("resultats.json", "w", encoding="utf-8") as result_file:
    json.dump({"taux_participation": taux_participation}, result_file, indent=4, ensure_ascii=False)

# Étape 9 : Visualiser les résultats
plot_group_participation(taux_participation)

print("Analyse terminée. Résultats enregistrés dans resultats.json et visualisés.")
