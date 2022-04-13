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
* lancement des tests avec Pytest et du linting avec Flake8
* conteneurisation par CircleCI de l'application Docker (construction et téléversement sur dockerhub)
* mise en production sur heroku ([adresse actuelle du projet](https://oc-lettings-site.herokuapp.com/))

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

* Un compte GitHub
* Un compte CircleCI relié au compte Github
* Un compte Docker/DockerHub
* Un compte Heroku
* Un compte Sentry

#### CircleCI

Le projet CircleCI se trouve à cette [adresse](https://app.circleci.com/pipelines/github/YoannDeb/OC-Lettings).

Si nécessité d'utiliser un autre compte, il faut :
* relier le compte GitHub hébergeant le projet au compte au compte CircleCI
* dans l'onglet projet cliquer sur 'Set Up Project'
* Sélectionner : `Fastest: Use the .circleci/config.yml in my repo`

Toute la configuration sera importée du fichier `.circleci/config.yml`

L'environnement CircleCI doit contenir les clés suivantes, à renseigner dans les paramètres du projet, sous l'onglet "Environment variables" :

| Clé             | Description                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------|
| DOCKER_TOKEN    | Token généré sur le compte DockerHUB (voir section Docker et DockerHub)                                        |
| DOCKER_USER     | nom du user Docker                                                                                             |
| HEROKU_API_KEY  | Clé API Heroku dans l'onglet API de l'app heroku                                                               |
| HEROKU_APP_NAME | nom de l'application heroku                                                                                    |
| SECRET_KEY      | Clé secrète                                                                                                    |
| SENTRY_DSN      | adresse du dsn de sentry, que l'on trouve dans les paramètres du projet sur Sentry.io, onglet ClientKeys (DSN) |

#### Docker et DockerHub

##### Principe de fonctionnement

La configuration de la conteneurisation se trouve dans le fichier `Dockerfile` à la racine du projet

##### Générer la clé 

* Se connecter ou créer un compte sur [DockerHub](https://hub.docker.com/).
* Aller dans `Account Settings`, onglet `Security`
* Cliquer sur `New Access Token`
* Rentrer une description et sélectionner `Read, Write, Delete`
* Copier le token qui s'affiche, car il ne sera pas possible de le récupérer plus tard
* Le renseigner dans le compte Sentry (voir la section CircleCI)


##### Lancer l'image Docker à partir de DockerHub

##### Installation locale et configuration de Docker Desktop

Il faut d'abord installer localement et configurer docker pour sa machine :
* Télécharger l'installeur [ici](https://www.docker.com/get-started/)
* Consulter les instructions d'installation selon l'OS de la machine [ici](https://docs.docker.com/get-docker/)

##### Lancement de l'image la plus récente stockée sur DockerHub
On peut ensuite lancer dans un terminal la dernière image stockée sur DockerHub (tag latest) avec cette unique commande :

`docker run --pull always -p 8000:8000 --name OC-Lettings yoanndeb/oc-lettings-site:latest`

Ici `OC-Lettings` est le nom du conteneur local, `yoanndeb` est le nom du compte docker et `oc-lettings-site` est le nom du dépôt DockerHub. À remplacer si besoin par les paramètres du compte utilisé si différent.

À noter qu'on ne peut pas utiliser le nom d'un conteneur qui existe déjà, pour lancer une deuxième fois la commande, il faut soit changer le nom du conteneur, soit supprimer l'ancien (voir section `Suppression du conteneur et de l'image docker stockés localement`).


##### Construction de l'image Docker et lancement en local (sans passer par CircleCI ni DockerHub)

Dans certains cas, il peut être préférable de construire et de lancer l'image localement (par exemple pour gagner du temps ou pour tester sans déployer)

Dans un terminal à la racine du projet, on peut utiliser les commandes suivantes :
* Construction et conteneurisation de l'image Docker : `docker build -t Test/oc-lettings-site:test .`
* Lancement de l'image docker : `docker run -p 8000:8000 oc-lettings-site:test`
``

##### Suppression du conteneur et de l'image docker stockés localement

Pour supprimer le conteneur et l'image docker qui sont stockées sur la machine, on peut utiliser l'interface graphique, mais il est également possible de le faire en ligne de commande.

Pour le compte et le nom de conteneur utilisé dans le premier exemple :
* Suppression du conteneur : `docker rm OC-Lettings`
* Suppression de l'image : `docker rmi yoanndeb/oc-lettings-site:latest`

##### Consultation du site

Le site lancé localement sera disponible à l'adresse http://127.0.0.1:8000 avec cette configuration de ports.

#### Heroku



#### Sentry






