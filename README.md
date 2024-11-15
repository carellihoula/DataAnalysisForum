Voici le contenu généré en **Markdown** pour votre fichier **`README.md`** :

---

# Taux de Participation - Analyse et Visualisation

Ce projet permet d'analyser et de visualiser la participation des utilisateurs dans une base de données relationnelle. Les données SQL sont transformées en JSON, puis traitées et visualisées.


## 📋 Pré-requis

Avant de lancer ce projet, assurez-vous d'avoir installé les outils suivants :

- **Python** (version 3.8 ou plus récente)
- **pip** (installé avec Python)
- **Git** (optionnel, pour cloner le projet)

---

## 🚀 Instructions pour lancer le projet

### 1. Cloner le dépôt

Clonez le projet depuis GitHub (ou votre plateforme de gestion de code) :

```bash
git clone https://github.com/carellihoula/DataAnalysisForum.git
cd DataAnalysisForum
```
```bash
cd DataAnalysisForum
```

### 2. Créer un environnement virtuel

Créez un environnement virtuel pour éviter les problèmes d'incompatibilité avec d'autres projets :

```bash
python -m venv .venv
```

### 3. Activer l'environnement virtuel

- Sur **Windows** :
  ```bash
  .venv\Scripts\activate
  ```

- Sur **Linux/MacOS** :
  ```bash
  source .venv/bin/activate
  ```

### 4. Installer les dépendances

Installez les bibliothèques nécessaires en utilisant le fichier **`requirements.txt`** :

```bash
pip install -r requirements.txt
```

---

## 📂 Structure du projet

- **`main.py`** : Point d'entrée principal du projet.
- **`to_json.py`** : Contient les fonctions pour transformer les tables SQL en fichiers JSON.
- **`calculs.py`** : Implémente les fonctions pour exclure des utilisateurs, attribuer des groupes et calculer les scores.
- **`visualization.py`** : Génère les visualisations des résultats.
- **`database.py`** : Gère les connexions et les requêtes à la base de données.
- **`weights.py`** : Définit les poids pour chaque action.

### Dossier **`sql_to_json_data`**

Ce dossier contient les fichiers JSON exportés :
- **`transition_data.json`** : Contient les données de la table `transition`.
- **`all_tables_data.json`** : Contient toutes les tables de la base de données exportées.
- **`final_results.json`** : Résultats finaux des analyses.

---

## 🏃‍♂️ Lancer le projet

Exécutez le script principal :

```bash
python main.py
```

### Résultats

- Les JSON générés seront sauvegardés dans le dossier **`sql_to_json_data`**.
- Les visualisations seront affichées automatiquement.
- Les fichiers JSON des résultats seront disponibles pour inspection ou réutilisation.

---

## 🛠️ Résolution de problèmes

- Si des bibliothèques sont manquantes, vérifiez que vous avez bien activé l'environnement virtuel avant d'installer les dépendances.
- Si un fichier JSON ou un dossier attendu est manquant, assurez-vous que les droits d'écriture sont activés sur le répertoire.

---