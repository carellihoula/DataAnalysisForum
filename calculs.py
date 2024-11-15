import pandas as pd
import numpy as np

def exclude_users(data, exclusion_list):
    """Exclut les utilisateurs spécifiques."""
    return data[~data['Utilisateur'].isin(exclusion_list)]

def assign_random_groups(data, group_names):
    """Assigne chaque utilisateur à un groupe aléatoire."""
    # Créer une affectation aléatoire unique pour chaque utilisateur
    unique_users = data['Utilisateur'].unique()
    user_to_group = {user: np.random.choice(group_names) for user in unique_users}

    # Ajouter une colonne 'Groupe' en mappant les utilisateurs à leurs groupes
    data['Groupe'] = data['Utilisateur'].map(user_to_group)
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
