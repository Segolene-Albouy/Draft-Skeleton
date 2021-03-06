# Draft Skeleton

Ce repository contient le squelette d'un application web utilisant la librairie Flask de Python

__Description de l'arborescence des dossiers__ :

```
__init__.py			fichier initialisant le dossier en package
db.sqlite			base de données utilisée par l'application
run.py				appel de l'application pour son lancement

app/				Package application
–– __init__.py				fichier initialisant le dossier en package
–– app.py				module principal de l'application (initialisation et configuration)
–– constantes.py			défintion des constantes utilisées dans l'application
–– test_db.sqlite			base de données utilisée par la version test de l'application
–– __pycache__/				fichiers cache python (pré-compilation pour exécution plus rapide des fichiers .py)
–– modeles/				fichiers de modélisation de la base de donnée
–––––– __init__.py				fichier initialisant le dossier en package
–––––– donnees.py				mise en place des classes de la BDD
–––––– utilisateurs.py				classe User + fonctionnalités de création et identification
–––––– __pycache__/				fichiers cache python
–– routes/				fichiers définissant les routes d'accès aux pages de l'application
–––––– __init__.py				fichier initialisant le dossier en package
–––––– api.py					définition des url de l'API et du contenu JSON de réponse
–––––– routes.py				définition des url et des fonctions définissant le contenu des pages associées
–––––– __pycache__/				fichiers cache python
–– static/				fichiers statiques
–––––– css/					fichiers css (bootstrap, font-awesome, etc.)
–––––– fonts/					fichiers de police de caractères
–––––– img/					fichiers images
–––––– js/					fichiers javascript (bootstrap, jquery, popper)
–– templates/				templates constituant les différentes pages de l'application
–––––– conteneur.html				page de base à compléter
–––––– pages/					pages du site (accueil, connexion, recherche, etc.)
–––––– partials/				blocs à intégrer aux pages du site
––––––––––– css.html				balise lien vers les fichiers bootstrap
––––––––––– metadata.html			balises <meta> détaillant les métadonnées
––––––––––– recherche.html			module de recherche réduit

tests/				tests relatifs à la vérification du fonctionnement de l'application	
–– __init__.py				fichier initialisant le dossier en package
–– base.py				duplication de la BDD et configuration de l'app à utiliser pour les tests
–– test_1.py				définition d'un premier test

venv/				fichiers relatifs à l'environnement virtuel
					à activer avec "source venv/bin/activate"
```

