import json
import pandas as pd
from to_json import export_table_to_json, export_all_tables_to_single_json
from calculs import exclude_users, assign_random_groups, calculate_weighted_scores, \
    calculate_group_scores, normalize_scores_to_percentage
from visualization import plot_group_participation
from weights import ACTION_WEIGHTS

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
group_names = ["Groupe1", "Groupe2", "Groupe3"]
etudiants_df = assign_random_groups(etudiants_df, group_names)

# Vérifiez que chaque utilisateur appartient à un seul groupe
print("Vérification des affectations des groupes :")
print(etudiants_df.groupby('Utilisateur')['Groupe'].nunique().value_counts())

# Étape 7 : Calculer le taux de participation par groupe
# taux_participation = calculate_group_participation(etudiants_df)

# Étape 6 : Calculer les scores pondérés pour chaque utilisateur
etudiants_df = calculate_weighted_scores(etudiants_df, ACTION_WEIGHTS)

# Étape 7 : Calculer les scores totaux par groupe
group_scores = calculate_group_scores(etudiants_df)

# Étape 8 : Normaliser les scores pour que la somme soit égale à 100%
normalized_scores = normalize_scores_to_percentage(group_scores)

# Étape 8 : Sauvegarder les résultats dans un fichier JSON
resultats = {"scores_totaux_par_groupe": normalized_scores}
with open("resultats.json", "w", encoding="utf-8") as result_file:
    json.dump(resultats, result_file, indent=4, ensure_ascii=False)

# Étape 9 : Visualiser les résultats
plot_group_participation(normalized_scores)

print("Analyse terminée. Résultats enregistrés dans resultats.json et visualisés.")
