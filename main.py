"""Ce code permet de trouver les palindrome"""

def ispalindrome(s):
    """voici le code :
    j'utilise la fonction .issalnum gardée
    uniquement les lettres et les chifres
    (suprime ponctuation etc...) """

    change_accent = str.maketrans("éèêëàâäôöîïùûç", "eeeeaaaooiiuuc")
    s = s.lower()
    texte_sans_accent = ''.join(c for c in s.translate(change_accent).lower() if c.isalnum())

    return texte_sans_accent == texte_sans_accent[::-1] # Je vérifie si il est palindrome

def main():

    """Ma fonction qui va executer la 1er"""

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
