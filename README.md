# Api_Book_Flask
 A Flaks API about books and their categories



## DÉMARRAGE

### INSTALLATION DES DÉPENDANCES

#### Python 3.10.2

#### pip 22.0.4 from /usr/lib/python3/dist-packages/pip (python 3.10)

Suivez les instructions pour installer la dernière version de python pour votre système dans le [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### ENVIRONNEMENT VIRTUEL

Nous vous recommandons de travailler dans un environnement virtuel lorsque vous utilisez Python pour vos projets.Cela vous permet de séparer et d'organiser vos dépendances pour chaque projet. Vous pourez trouver toutes les instructions vous permettant de mettre en place un environnement virtuel pour votre système dans [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### DÉPENDANCES PIP

Maintenant que vous avez configurer et lancer votre environnement virtuel, Installez les dépendances en vous rendant sur le repectoire `Api_Book_Flask`, ensuite exécutez les commandes suivantes :

```bash
pip install -r requirements.txt
ou
pip3 install -r requirements.txt
```

Ceci installera toutes les pacquets requis dans le fichier `requirements.txt`.

##### DÉPENDANCES CLÉS

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## CONFIGURATION DE LA BASE DE DONNÉES

Avec Postgres en marche, restaurez une base de données en utilisant le fichier livre.sql fourni. Depuis le dossier databases, dans le terminal, exécutez :

```bash
psql  livre< livre.sql
```

## DÉMARER LE SERVEUR

Depuis le répertoire `Api_Book_Flask`, assurez-vous d'abord que vous travaillez dans l'environnement virtuel que vous avez créé.

Pour exécuter le serveur sur Linux ou Mac, exécutez :

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Pour exécuter le serveur sur Windows, exécutez :

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

Mettre la variable `FLASK_ENV` à `development` va détecter les changements de fichiers et redémarrer le serveur automatiquement.

En mettant la variable `FLASK_APP` à `flaskr`, flask utilisera le répertoire `flaskr` et le fichier `__init__.py` pour trouver l'application.

Vous pouvez aussi exécutez

```
python app.py
```

## RÉFÉRENCE API

Démarrer

URL de base : Actuellement, cette application ne peut être exécutée que localement et n'est pas hébergée comme une URL de base. L'application backend est hébergée par défaut à l'adresse http://localhost:5000, qui est définie comme un proxy dans la configuration du frontend.

## GESTION D'ERREURS

Les erreurs sont retournées sous forme d'objets JSON au format suivant :

```
    {
    "success":False
    "error": 400
    "message":"Bad request
    }
```

L'API retournera cinq types d'erreurs quand les requêtes échouent :

```
    . 400: Bad request
    . 404: Not found
    . 405: Method not allowed
    . 422: Unprocessable
    . 500: Internal server error
    
    
    
```

## TERMINAISON

##### CATEGORIE

. ## GET/categories

GENERAL:
Cette terminaison retourne une liste d'objets Categorie, une valeur 'success', nombre total de categories.

    SAMPLE: curl http://localhost:5000/categories
    [
        {
        "Nombres de categories": 2,
        "success": "True"
        },
    [
        {
            "id": 1,
            "lib_categorie": "Fiction"
        },
        {
            "id": 2,
            "lib_categorie": "Drame"
        }
    ]
    ]
. ## GET/livres

GENERAL:
Cette terminaison retourne une liste d'objets livre, une valeur 'success', nombre total de livres.

    SAMPLE: curl http://localhost:5000/livres
    [
       {
        "Nombres de livres": 2,
        "success": "True"
       },
    [
        {
            "auteur": "Georges Lucas",
            "categorie_id": 1,
            "dateSortie": "1997-01-01",
            "editeur": "Yoda",
            "id": 2,
            "isbn": 124589635,
            "titre": "Star Wars"
        },
        {
            "auteur": "Joël Dicker",
            "categorie_id": 2,
            "dateSortie": "2015-09-30",
            "editeur": "Dicker",
            "id": 1,
            "isbn": 215489637,
            "titre": "Le livre des Baltimores"
        }
    ]
    ]

. ## DELETE/Categories/(categorie_id)

GENERAL:
Supprime la catégorie avec l'ID donneé s'il existe. Retourne la valeur du success, et le nombre total de catégories

        SAMPLE: curl -X DELETE http://localhost:5000/categories/1

    {
        "nombre_categories": 2,
        "success": true,
        "supprimer ":1
    }

. ## DELETE/livres/(livre_id)

GENERAL:
Supprime le livre avec l'ID donneé s'il existe. Retourne  la valeur du success, et le nombre total de livres

        SAMPLE: curl -X DELETE http://localhost:5000/livres/2

    {
        "success": true,
        "supprimer ":2,
        "total_livres":2
    }

```



```

. ##PUT/categories(categorie_id)

GENERAL:
Cette terminaison est utilisé pour modifier une catégorie
Nous retournons la valeur du success et un message de confirmation
    SAMPLE.....For Patch

    curl -X PUT http://localhost:5000/categories/2 -H "Content-Type:application/json" -d " {
    "lib_categorie":"Drame"
     }
    [ 
      {
        "message": "Modification effectuer a succes",
        "success": "True"
      },
    ]

. ##PUT/livres(livre_id)

GENERAL:
Cette terminaison est utilisé pour modifier un livre
Nous retournons  la valeur du success et un message de confirmation

    SAMPLE.....For PUT

    curl -X PATCH http://localhost:5000/livres/1 -H "Content-Type:application/json" -d "{"isbn":"215489637",
    "titre":"Le livre des Baltimores"}
    [ 
      {
        "message": "Modification effectuer a succes",
        "success": "True"
      },
    ]

. ##POST/categories

GENERAL:
Cette terminaison est utilisé pour créer une nouvelle categorie.
Dans le cas de la création d'une categorie :
Nous retournons lavaleur success et un message de confirmation

    SAMPLE.....For create

    curl -X POST http://localhost:5000/categories -H "Content-Type:application/json" -d "{
    "lib_categorie":"Fiction"}
    [
        { 
        "message": "Ajout effectuer avec succes",
        "success": "True"
       },
       {
        "id": 2,
        "lib_categorie": "Fiction"
       }
    ]


    

. ## POST/livres

GENERAL:
Cette terminaison est utilisé pour créer un nouveau livre.
Dans le cas de la création d'un livre :
Nous retournons l'ID du nouveau livre créé, le livre créé, la liste des livres et le nombre de livres.

    SAMPLE.....For create

    curl -X POST http://localhost:5000/livres -H "Content-Type:application/json" -d "{
    "isbn":"124589635",
    "titre":"Star Wars",
    "auteur":"Georges Lucas",
    "editeur":"Yoda",
    "dateSortie":"1997-01-01",
    "categorie_id":1
    
}

    [  
        {
        "message": "Ajout effectuer avec succes",
        "success": "True"
       },   
       {
            "auteur": "Georges Lucas",
            "categorie_id": 1,
            "dateSortie": "1997-01-01",
            "editeur": "Yoda",
            "id": 2,
            "isbn": 124589635,
            "titre": "Star Wars"
        },
    ]#
