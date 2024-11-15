import matplotlib.pyplot as plt

def plot_group_participation(taux_participation):
    """Affiche un diagramme à barres des taux de participation par groupe."""
    groupes = list(taux_participation.keys())
    valeurs = list(taux_participation.values())

    plt.figure(figsize=(8, 6))
    plt.bar(groupes, valeurs)
    plt.title("Taux de Participation par Groupe", fontsize=16)
    plt.xlabel("Groupes", fontsize=12)
    plt.ylabel("Taux de Participation (%)", fontsize=12)
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()
