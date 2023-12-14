def generate_playfair_grid(key: int) -> list[list[str]]:
    """
    Génère une grille représentant l'alphabet (sans le J), décalé en fonction du paramètre

    :param key: Entier représentant le décalage réalisé dans la grille retournée.
    :return: Grille décalée.
    """
    # Créer un alphabet sans 'J' (car Playfair exclut généralement 'J')
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1) if chr(i) != 'J']

    # Mélanger l'alphabet en fonction de la clé
    key = key % 25
    shuffled_alphabet = alphabet[key:] + alphabet[:key]

    # Remplir la grille 5x5 avec l'alphabet mélangé
    grid = [shuffled_alphabet[i:i + 5] for i in range(0, 25, 5)]

    return grid

def get_score(text: str, target_frequencies: dict) -> float:
    """
    Donne un score de correspondance au dictionnaire des fréquences passé en paramètre.

    :param text: Chaîne déchiffrée.
    :param target_frequencies: Dictionnaire des fréquences des lettres de l'alphabet
    :return: Score de correspondance entre text et target_frequencies
    """
    # Convertir le texte en majuscules pour la comparaison
    text = text.upper()

    # Calculer les fréquences des lettres dans le texte déchiffré
    text_frequencies = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            total_letters += 1
            text_frequencies[char] = text_frequencies.get(char, 0) + 1

    # Calculer les pourcentages de fréquence dans le texte déchiffré
    text_percentages = {char: (count / total_letters) * 100 for char, count in text_frequencies.items()}

    # Calculer le score de similarité (somme des carrés des différences)
    score = sum((text_percentages.get(char, 0) - target_frequencies.get(char, 0))**2 for char in target_frequencies)

    return score