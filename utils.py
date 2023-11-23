import os
from dotenv import load_dotenv
import random

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupération des variables d'environnement
grid_file_path = os.getenv("GRID_FILE_PATH")

def generate_random_letter() -> str:

    # Fonction de génération d'une lettre aléatoire parmi les 25 lettres de la grille

    grid_letters = get_grid_letters()
    random_int = random.randint(0,24)
    return grid_letters[random_int]

def get_grid_letters() -> str:

    # Fonction de récupération de la grille sous forme de string

    grid_file = open(grid_file_path, "r")
    lines = grid_file.readlines()
    grid_file.close()
    grid_letters = ""
    for line in lines:
        grid_letters = grid_letters + line.replace("\n", "")
    return grid_letters

def get_grid() -> list[list[str]]:

    # Fonction de récupération de la grille sous forme de liste de liste

    grid_file = open(grid_file_path, "r")
    lines = grid_file.readlines()
    grid_file.close()
    grid = []
    for line in lines:
        char_list = []
        line = line.replace("\n", "")
        for char in line:
            char_list.append(char)
        grid.append(char_list)
    return grid

def string_formatter(string_param: str) -> str:

    # Fonction de formatage de la string à chiffrer
    # - Mise en majuscules
    # - Suppression des espaces
    # - séparation en couples de lettres
    
    string_param = string_param.upper()
    string_param = string_param.replace(" ", "")
    string_param = string_splitter(string_param)
    return string_param


def input_playfair_format(string_unsplitted: str) -> list[str]:

    # Fonction de parsing de la chaîne d'entrée en paires de caractères
    # Fournit une entrée valide pour le chiffrement en playfair

    string_splitted = []
    for i in range(0, len(string_unsplitted), 2):
        string_splitted.append(string_unsplitted[i:i+2])
    last_index = len(string_splitted) - 1
    if len(string_splitted[last_index]) == 1:
        string_splitted[last_index] += generate_random_letter()
    print(string_splitted)