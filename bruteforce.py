from cipher import playfair, get_coordinates

french_letters_frequencies = {
    'E': 17.3, 'P': 3.0, 'A': 8.4, 'G': 1.3, 'S': 8.1, 'V': 1.3,
    'I': 7.3, 'B': 1.1, 'N': 7.1, 'F': 1.1, 'T': 7.1, 'Q': 1.0,
    'R': 6.6, 'H': 0.9, 'L': 6.0, 'X': 0.4, 'U': 5.7, 'J': 0.3,
    'O': 5.3, 'Y': 0.3, 'D': 4.2, 'K': 0.1, 'C': 3.0, 'W': 0.1,
    'M': 3.0, 'Z': 0.1
}

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
        current_score = score_text(decrypted_text, target_frequencies)

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

def score_text(text: str, target_frequencies: dict) -> float:
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

texte_clair = "EllesappelleAngelicaSummerelleadouzeansetelleestcanadienneIlyacinqansmafamilleetmoiavonsdemenagedanslesuddelaFranceMonpereFrankSummerestmecanicieniladorelesvoituresanciennesetcollectionnelesvoituresminiaturesMameresappelleEmilieSummerelleestinfirmieredansunhopitalnonloindenotremaisonNousavonsdemenageenFranceparcequelleaimelaculturedecepaysLavieenFranceesttresdifferentedecelleauCanadaIciilfaitsouventchaudChaquedimanchenousallonsalamagnifiqueplagedeBiarritzetnousachetonsdesglacesapresavoirnagedanslamerLesFrancaissonttressympathiquesetaccueillantsNousparlonsfrancaislorsquenoussommesdehorsalecoleouaumarcheCependantnouscontinuonsdeparleranglaisalamaisoncarmesparentsneveulentpasquelleperdemalanguenatale"
texte_clair = "DansunevalleeverdoyantelesrivieresserpententdoucemententrelescollinesrecouvertesdherbeLesarbressetirentverslecielleursfeuillesdansantaugreduventlegerLesoiseauxchantentmelodieusementcreantunesymphonienaturellequiresonneatraverslacampagneLesmontagnesgeantessedressentalhorizonleurssommetsenneigesbrillantsouslalumieredusoleilUnruisseaumurmureentraversantlaforetdenseoulesanimauxcurieuxobserventsilencieusementlesvisiteursdepassageDeschampsdefleurscoloreessetendentapertedevuecreantuntableaueclatantdecouleursvivesLespapillonsvoltigentgracieusementdunefleuralautreintegrantunetouchedegraceacepaysagefortbienenchanteurLecrepusculeapprocheteintantlecieldenuanceschaudesetpastelLesetoilesemergenttimidementeclairantlanuitdeleureclatscintillantLalunerondeetlumineuseveillesilencieusementsurlaterreendormieCestdanscedecoridylliquequelanaturedevoilesabeautesansfinunesymphoniedeformesetdecouleursquicaptiventlessensetnourrissentlameChaqueinstantchaquebrisechaquerayondesoleilcontribuealharmonieintemporelledecelieumagique"
# texte_clair = "EPEPEPEAEAEAEAEAEAEAEAEGESESESESESVSISISIBININININFNTNTNTQTRTRTRTRHRLRLULULULULUOUODODODODCMCMCM"
random_grid = [['W', 'X', 'Y', 'Z', 'A'], ['B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'K', 'L'], ['M', 'N', 'O', 'P', 'Q'], ['R', 'S', 'T', 'U', 'V']]
text_chiffre = playfair(unformatted_string=texte_clair, grid=random_grid, action="chiffrer")
discovered_key, decrypted_text = bruteforce_playfair(text_chiffre, french_letters_frequencies)
print(f"La clé utilisée est : {discovered_key} et le texte déchiffré donne : {decrypted_text}")