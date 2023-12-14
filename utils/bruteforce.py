from utils.cipher import playfair, get_coordinates
from utils.utils_bruteforce import generate_playfair_grid, get_score

def bruteforce_playfair(unformatted_string: str, target_frequencies: dict) -> (str, str):
    """
    Déchiffre les bigrammes du texte avec toutes les combinaisons possibles de la grille de chiffrement.

    :param unformatted_string: Texte à déchiffrer.
    :param target_frequencies: Fréquences cibles des lettres de la langue française.
    :return: Texte déchiffré.
    """
    best_grid = None
    best_score = 0

    for key in range(25):
        grid = generate_playfair_grid(key)
        decrypted_text = playfair(unformatted_string, grid, action='dechiffrer')
        current_score = get_score(decrypted_text, target_frequencies)

        if current_score > best_score:
            best_score = current_score
            best_grid = grid
        
        current_decrypted_text = playfair(unformatted_string=unformatted_string, grid=grid, action='dechiffrer')
        current_key = ""
        for line in grid:
            for character in line:
                current_key += character

        print(f"Clé utilisée: {current_key}\n\n{current_decrypted_text}\n\n=====\n")

    if best_grid is not None:
        decrypted_text = playfair(unformatted_string, best_grid, action='dechiffrer')
        return best_grid, decrypted_text
    else:
        return "Échec de déchiffrement."