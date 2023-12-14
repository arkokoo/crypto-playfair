from utils.utils_cipher import *
from utils.cipher import *

grid = get_grid()
# print(grid)

texte_clair = input("Entrez une chaîne à chiffrer.\n--> ")
# way_move_line = input("Si les paires sont sur la même ligne, dans quel sens faire le décalage?\nChoisis entre : Z | Q | S | D\n--> ")
# way_move_column = input("Si les paires sont sur la même colonne, dans quel sens faire le décalage?\nChoisis entre : Z | Q | S | D\n--> ")
# way_move_other = input("Si on n'est dans aucun de ces cas, dans quel ordre le faire?\nChoisis entre : L (ligne) | C (colonne)\n--> ")

texte_chiffre = playfair(unformatted_string=texte_clair, grid=grid, action='chiffrer')
print(f"Texte chiffré :\n{texte_chiffre}")

texte_dechiffre = playfair(unformatted_string=texte_chiffre, grid=grid, action='dechiffrer')
print(f"Texte déchiffré :\n{texte_dechiffre}")