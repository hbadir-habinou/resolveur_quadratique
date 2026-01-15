# Résolveur d'Équations Quadratiques avec Visualisation (Django)

[![Construit avec Django](https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Langage Principal](https://img.shields.io/badge/Langage-Python-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)

## Description du Projet

Ce dépôt contient une application web complète, développée avec le framework **Django** en Python, conçue pour résoudre les équations quadratiques de la forme :

$$ax^2 + bx + c = 0$$

L'application ne se contente pas de fournir les racines de l'équation ; elle offre également une **visualisation graphique** de la parabole associée :

$$f(x) = ax^2 + bx + c$$

Le tracé est généré dynamiquement en utilisant la bibliothèque `Matplotlib`.

## Fonctionnalités

*   **Résolution Complète :** Calcule les racines réelles distinctes, la racine double, ou les racines complexes conjuguées en fonction du discriminant :
    $$\Delta = b^2 - 4ac$$
*   **Gestion des Cas Limites :** Gère correctement les cas où $a = 0$ (équation linéaire ou indéterminée).
*   **Visualisation Graphique :** Génère et affiche le graphique de la parabole, incluant le marquage des racines réelles sur l'axe des abscisses.
*   **Interface Utilisateur Intuitive :** Une interface web simple et claire pour la saisie des coefficients $a$, $b$ et $c$.
*   **Rendu Mathématique :** Utilisation de **MathJax** pour un affichage clair et professionnel des formules mathématiques sur l'interface web.

## Technologies Utilisées

| Catégorie | Technologie | Description |
| :--- | :--- | :--- |
| **Backend** | Python | Langage de programmation principal. |
| **Web Framework** | Django | Framework web pour la logique du serveur et le routage. |
| **Calcul Scientifique** | NumPy, cmath | Bibliothèques pour les calculs mathématiques complexes. |
| **Visualisation** | Matplotlib | Utilisé pour générer le graphique de la parabole. |
| **Frontend** | HTML, CSS (Bootstrap) | Structure de l'interface utilisateur et style réactif. |
| **Rendu Math.** | MathJax | Pour un affichage de qualité des équations. |

## Installation et Démarrage

Suivez ces étapes pour configurer et exécuter le projet localement.

### Prérequis

*   Python 3.x
*   `pip` (gestionnaire de paquets Python)

### 1. Cloner le Dépôt

```bash
git clone https://github.com/hbadir-habinou/resolveur_quadratique.git
cd resolveur_quadratique
```

### 2. Créer et Activer l'Environnement Virtuel

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel (Linux/macOS)
source venv/bin/activate

# Activer l'environnement virtuel (Windows)
# venv\Scripts\activate
```

### 3. Installer les Dépendances

```bash
pip install django matplotlib numpy
```

### 4. Exécuter le Serveur de Développement

```bash
python manage.py runserver
```

Le serveur sera lancé à l'adresse `http://127.0.0.1:8000/`.

## Utilisation

1.  Ouvrez votre navigateur et naviguez vers `http://127.0.0.1:8000/`.
2.  Entrez les coefficients $a$, $b$, et $c$ de votre équation.
3.  Cliquez sur le bouton **Calculer**.
4.  L'application affichera les résultats détaillés (racines, discriminant) et le graphique de la parabole.

---
