import matplotlib.pyplot as plt

def plot_participation_rates(participation_df):
    plt.figure(figsize=(12, 8))
    for group in participation_df['Groupe'].unique():
        subset = participation_df[participation_df['Groupe'] == group]
        plt.bar(subset['Utilisateur'], subset['TauxParticipation'], label=group)

    plt.title("Taux de Participation par Groupe et Utilisateur")
    plt.xlabel("Utilisateur")
    plt.ylabel("Taux de Participation (%)")
    plt.legend(title="Groupe")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
