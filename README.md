# Superblog

Superblog est une application Django permettant aux utilisateurs de s'enregistrer comme lecteurs pour lire, aimer et commenter les articles, ou comme rédacteurs pour rédiger des articles.

## Caractéristiques

- Inscription et authentification des utilisateurs.
- Rôles des utilisateurs : 
  - Lecteur (INTERNAUTE) : peut lire, aimer et commenter les articles.
  - Rédacteur (BLOGGEUR) : peut également rédiger des articles.
- Gestion des profils avec photo de profil.

## Installation

Suivez les étapes ci-dessous pour installer et exécuter l'application Superblog localement.

### Prérequis

- Python 3.x
- Django 3.x
- pip (Python package installer)

### Étapes d'installation

1. Clonez le dépôt depuis GitHub, activez l'environnement virtuel et démarrez le serveur de développement :
  * git clone https://github.com/deuxevi/Superblog.git
  * cd Superblog
  * source env/bin/activate  # Sur Windows, utilisez `env\\Scripts\\activate`
  * python manage.py runserver

2. Ouvrez votre navigateur web et accédez à l'URL http://127.0.0.1/8000