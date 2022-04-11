## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## CI/CD (Intégration continue et déploiement continu) :

### Principe de fonctionnement :

Le process CI/CD pour cette application permet à chaque commit sur la branche master, de déclencher un pipeline sur CircleCI.
Chaque étape doit être complétée avec succès pour passer à la suivante.

#### Le pipeline est constitué de ces étapes (après un commit sur la branche master) : 
* lancement des tests
* conteneurisation par CircleCI de l'app (construction et téléversement sur dockerhub)
* mise en production sur heroku (https://oc-lettings-site.herokuapp.com/)

À noter qu'un commit sur une branche autre que master déclenchera un autre pipeline avec une seule étape : le lancement des tests.

### Configuration requise pour que le déploiement fonctionne :

#### Prérequis en local

Un fichier .env à la racine du projet, pour le fonctionnement en local, contenant :
```
SECRET_KEY=[Clé secrète django (commande pour générer une nouvelle secrète key : python -c "import secrets; print(secrets.token_urlsafe())")]
SENTRY_DSN=[adresse du dsn de sentry, que l'on trouve dans les paramètres du projet sur Sentry.io, onglet ClientKeys (DSN)]
DEBUG=True
```

#### Prérequis du CI/CD

##### CircleCI

Adresse du projet sur CircleCI : https://app.circleci.com/pipelines/github/YoannDeb/OC-Lettings

L'environnement CircleCI doit contenir les clés suivantes, à renseigner dans les paramètres du projet, sous l'onglet "Environment variables" :
DOCKER_TOKEN : Token généré sur le compte DockerHUB
DOCKER_USER : nom du user Docker
HEROKU_API_KEY : Clé API Heroku dans l'onglet API de l'app heroku
HEROKU_APP_NAME : nom de l'application heroku
SECRET_KEY : Clé secrète
SENTRY_DSN : adresse du dsn de sentry, que l'on trouve dans les paramètres du projet sur Sentry.io, onglet ClientKeys (DSN)

##### Docker et DockerHub

##### Heroku


### Étapes nécessaires pour effectuer le déploiement :




### Lancer l'image Docker à partir de DockerHub:

docker run --pull always -p 8000:8000 --name OC-Lettings yoanndeb/oc-lettings-site:latest

