import os
from dotenv import load_dotenv
import random
from utils import *

# Script de chiffrement en playfair

# def playfair_encrypt(string_param: str, key: str) -> str:

print(get_grid())

texte_clair = input("Entrez une chaîne à chiffrer.\n--> ")

input_playfair_format(texte_clair)