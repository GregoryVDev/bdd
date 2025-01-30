# Création de la base de donnée
import os
import sqlite3

# Créer une variable pour mettre le chemin en spécifiant la base de donnée avec l'extension et on se connecte à la base de données avec la variable "database"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Récupère le dossier où se trouve votre script
database = os.path.join(BASE_DIR, "my_database.sq3")  # Crée un chemin relatif vers la base de données à partir de ce dossier

connexion = sqlite3.connect(database)

