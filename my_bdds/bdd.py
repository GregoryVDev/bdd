# Création de la base de donnée

import sqlite3

# Créer une variable pour mettre le chemin en spécifiant la base de donnée avec l'extension
bdd = "my_bdds/ma_base-de_donnees.sq3"

# On se connecte à la base de données avec la variable "bdd"
connexion = sqlite3.connect(bdd)
