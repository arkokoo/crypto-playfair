import os
from dotenv import load_dotenv
import random
from utils.utils_cipher import *

# Script de chiffrement en playfair

def playfair(unformatted_string: str, grid: list[list[str]], action: str) -> str:
    """
    Chiffre ou déchiffre les bigrammes du texte avec la grille de chiffrement.

    :param bigrams: Liste des bigrammes à chiffrer ou déchiffrer.
    :param grid: Grille de chiffrement.
    :param action: 'chiffrer' pour le chiffrement, 'dechiffrer' pour le déchiffrement.
    :return: Texte chiffré ou déchiffré.
    """
    texte_resultat = ''
    bigrams = input_playfair_format(unformatted_string)
    for bg in bigrams:
        coord = get_coordinates(bg, grid)
        if coord[0][0] == coord[1][0]:  # Si sur la même ligne :
            if action == 'chiffrer':
                texte_resultat += grid[coord[0][0]][(coord[0][1] + 1) % 5]
                texte_resultat += grid[coord[1][0]][(coord[1][1] + 1) % 5]
            elif action == 'dechiffrer':
                texte_resultat += grid[coord[0][0]][(coord[0][1] - 1) % 5]
                texte_resultat += grid[coord[1][0]][(coord[1][1] - 1) % 5]
        elif coord[0][1] == coord[1][1]:  # Si dans la même colonne :
            if action == 'chiffrer':
                texte_resultat += grid[(coord[0][0] + 1) % 5][coord[0][1]]
                texte_resultat += grid[(coord[1][0] + 1) % 5][coord[1][1]]
            elif action == 'dechiffrer':
                texte_resultat += grid[(coord[0][0] - 1) % 5][coord[0][1]]
                texte_resultat += grid[(coord[1][0] - 1) % 5][coord[1][1]]
        else:  # Sinon :
            if action == 'chiffrer':
                texte_resultat += grid[coord[0][0]][coord[1][1]]
                texte_resultat += grid[coord[1][0]][coord[0][1]]
            elif action == 'dechiffrer':
                texte_resultat += grid[coord[0][0]][coord[1][1]]
                texte_resultat += grid[coord[1][0]][coord[0][1]]
    return texte_resultat

def get_coordinates(bigram, grid):
    """
    Remplacement de chaque lettre du message codé par ses coordonnées dans la grille sous cette forme :
    "[[ligne_lettre0, colonne_lettre0] , [ligne_lettre1, colonne_lettre1]]"

    :param bigrams: Bigramme comparé à la grille.
    :param grid: Grille de chiffrement.
    :return: Coordonnées des deux lettres du bigramme dans la grille.
    """
    coord = []
    for i in range(2):
        for j in range(5):
            for k in range(5):
                if bigram[i] == grid[j][k]:
                    coord.append([j, k])
    return coord