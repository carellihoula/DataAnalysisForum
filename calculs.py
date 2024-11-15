import random

import pandas as pd
import numpy as np

def exclude_users(data, exclusion_list):
    """Exclut les utilisateurs spécifiques."""
    return data[~data['Utilisateur'].isin(exclusion_list)]

def assign_random_groups(data, group_names):
    """
    Assigne chaque utilisateur à un groupe aléatoire avec un nombre équilibré d'utilisateurs par groupe.

    Parameters:
        data (DataFrame): Les données contenant les utilisateurs.
        group_names (list): Liste des noms des groupes.

    Returns:
        DataFrame: Les données avec une nouvelle colonne 'Groupe'.
    """
    # Récupérer les utilisateurs uniques
    unique_users = data['Utilisateur'].unique()

    # Mélanger les utilisateurs aléatoirement
    random.shuffle(unique_users)

    # Calculer la répartition aléatoire mais équilibrée
    num_users = len(unique_users)
    num_groups = len(group_names)
    base_size = num_users // num_groups  # Taille de base pour chaque groupe
    extra_users = num_users % num_groups  # Reste à répartir aléatoirement

    # Créer les groupes avec des tailles équilibrées
    group_sizes = [base_size + 1 if i < extra_users else base_size for i in range(num_groups)]
    random.shuffle(group_sizes)  # Mélanger les tailles des groupes pour plus de variabilité

    # Répartir les utilisateurs dans les groupes
    group_assignments = []
    start_idx = 0
    for group_name, group_size in zip(group_names, group_sizes):
        end_idx = start_idx + group_size
        for user in unique_users[start_idx:end_idx]:
            group_assignments.append((user, group_name))
        start_idx = end_idx

    # Convertir en DataFrame pour le mappage
    group_df = pd.DataFrame(group_assignments, columns=['Utilisateur', 'Groupe'])

    # Fusionner les groupes dans les données originales
    data = data.merge(group_df, on='Utilisateur', how='left')
    return data

def calculate_weighted_scores(data, weights):
    data['ScorePondere'] = data['Titre'].map(weights).fillna(0)
    return data

def calculate_group_scores(data):
    group_scores = data.groupby('Groupe')['ScorePondere'].sum()
    return group_scores.to_dict()

def normalize_scores_to_percentage(scores):
    total_score = sum(scores.values())
    if total_score == 0:
        return {group: 0 for group in scores}  # Évite la division par zéro
    return {group: (score / total_score) * 100 for group, score in scores.items()}

def calculate_group_participation(data):
    actions_par_groupe = data.groupby('Groupe').size()
    total_actions = len(data)
    return (actions_par_groupe / total_actions * 100).to_dict()
