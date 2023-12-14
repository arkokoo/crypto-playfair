import os
from dotenv import load_dotenv
import random

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupération des variables d'environnement
grid_file_path = os.getenv("GRID_5x5_FILE_PATH")

def generate_random_letter() -> str:

    # Fonction de génération d'une lettre aléatoire parmi les 25 lettres de la grille
    # Permet d'ajouter une nulle dans la string chiffrée

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
    #string_param = string_splitter(string_param)
    return string_param


def input_playfair_format(string_unsplitted: str) -> list[str]:

    # Fonction de parsing de la chaîne d'entrée en paires de caractères
    # Fournit une entrée valide pour le chiffrement en playfair

    buffer_string = string_formatter(string_unsplitted)
    updated_string_splitted = []

    i = 0
    while i < len(buffer_string):
        pair = buffer_string[i:i+2]
        
        # Si le bigramme contient deux fois la même lettre, alors on ajoute une lettre entre les 2
        if len(pair) == 2 and pair[0] == pair[1]:
            random_letter = generate_random_letter()
            updated_string_splitted.append(pair[0] + random_letter)
            buffer_string = buffer_string[:i + 1] + random_letter + buffer_string[i + 1:]
        else:
            updated_string_splitted.append(pair)

        i += 2

    # Si le dernier bigramme contient une seule lettre, ajouter une lettre aléatoire
    if len(updated_string_splitted[-1]) == 1:
        updated_string_splitted[-1] += generate_random_letter()

    return updated_string_splitted