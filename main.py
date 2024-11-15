import json
import pandas as pd
from to_json import export_table_to_json, export_all_tables_to_single_json
from calculs import exclude_users, assign_random_groups, calculate_weighted_scores, \
    calculate_group_scores, normalize_scores_to_percentage
from visualization import plot_group_participation
from weights import ACTION_WEIGHTS

# Nom du dossier pour stocker les JSON
output_directory = "sql_to_json_data"

# Étape 1 : Exporter les données de la table transition vers un fichier JSON
export_table_to_json("transition", "transition_data.json", output_directory)

# Étape 2 : Exporter toutes les tables dans un seul fichier JSON
export_all_tables_to_single_json("all_tables_data.json", output_directory )

# Étape 3 : Charger les données depuis le fichier JSON
with open(f"{output_directory}/transition_data.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Étape 4 : Convertir les données en DataFrame
df = pd.DataFrame(data)

# Étape 5 : Exclure les utilisateurs spécifiques
exclusion_list = ["mmay", "madeth", "admin"]
etudiants_df = exclude_users(df, exclusion_list)

# Étape 6 : Assigner les étudiants à trois groupes aléatoires
group_names = ["Groupe1", "Groupe2", "Groupe3"]
etudiants_df = assign_random_groups(etudiants_df, group_names)

# Étape 6.1 : Compter le nombre d'utilisateurs par groupe
group_user_counts = etudiants_df.groupby('Groupe')['Utilisateur'].nunique()

# Étape 6.2 : Compter le nombre total d'utilisateurs uniques
total_users = etudiants_df['Utilisateur'].nunique()

# Étape 7 : Calculer les scores pondérés pour chaque utilisateur
etudiants_df = calculate_weighted_scores(etudiants_df, ACTION_WEIGHTS)

# Étape 8 : Calculer les scores totaux par groupe
group_scores = calculate_group_scores(etudiants_df)

# Étape 9 : Normaliser les scores pour que la somme soit égale à 100%
normalized_scores = normalize_scores_to_percentage(group_scores)

# Regrouper toutes les informations dans un seul JSON
final_results = {
    "nombre_utilisateurs_par_groupe": group_user_counts.to_dict(),
    "nombre_total_utilisateurs": total_users,
    "scores_pondérés_normalisés": normalized_scores
}

# Sauvegarder les résultats dans un fichier JSON unique
with open("final_results.json", "w", encoding="utf-8") as result_file:
    json.dump(final_results, result_file, indent=4, ensure_ascii=False)

print("Analyse terminée. Tous les résultats sont enregistrés dans final_results.json et visualisés.")

# Étape 10 : Visualiser les résultats
plot_group_participation(normalized_scores)

