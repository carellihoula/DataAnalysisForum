import pandas as pd


def prepare_data(data):
    # Convertir `Date` et `Heure` en chaînes et les combiner, puis les convertir en datetime
    data['Date'] = data['Date'].astype(str)
    data['Heure'] = data['Heure'].astype(str)
    data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Heure'], errors='coerce')

    # Supprimer les colonnes `Date` et `Heure` originales
    data = data.drop(columns=['Date', 'Heure'])
    return data


def group_users_by_activity(data):
    # Groupement par type d'activité et calcul du taux de participation
    groups = data.groupby('Titre')
    participation_data = []

    for group_name, group_data in groups:
        user_counts = group_data['Utilisateur'].value_counts()
        total_actions = len(group_data)

        # Calcul du taux de participation de chaque utilisateur dans le groupe
        participation_rates = (user_counts / total_actions) * 100
        for user, rate in participation_rates.items():
            participation_data.append({
                'Groupe': group_name,
                'Utilisateur': user,
                'TauxParticipation': rate
            })

    return pd.DataFrame(participation_data)
