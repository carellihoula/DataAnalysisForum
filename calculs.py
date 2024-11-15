import pandas as pd
import numpy as np

def exclude_users(data, exclusion_list):
    """Exclut les utilisateurs spécifiques."""
    return data[~data['Utilisateur'].isin(exclusion_list)]

def assign_random_groups(data, group_names):
    """Assigne chaque utilisateur à un groupe aléatoire."""
    data['Groupe'] = np.random.choice(group_names, size=len(data))
    return data

def calculate_group_participation(data):
    """Calcule le taux de participation par groupe."""
    actions_par_groupe = data.groupby('Groupe').size()
    total_actions = len(data)
    return (actions_par_groupe / total_actions * 100).to_dict()
