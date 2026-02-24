from collections import Counter

class Texte:
    def __init__(self, titre: str, auteur: str, contenu: str):
        self._titre = titre
        self.auteur = auteur
        self.contenu = contenu

    @property
    def titre(self) -> str:
        return self._titre
    @titre.setter
    def titre(self, nouveau: str) -> None:
        if not nouveau.strip():
            raise ValueError("Le titre est vide, ou il y a des espace au début/à la fin")
        self._titre = nouveau.strip()


    def nombre_mots(self) -> int:
        return sum(len(texte.split()) for texte in self.contenu)

    def mots_uniques(self) -> set[str]: #set -> que les éléments uniques
        cnt = Counter(self.contenu.split())
        mots_unic = []
        for word in cnt:
            if cnt[word] == 1:
                mots_unic.append(word)
        return set(mots_unic)
    
    def frequences(self) -> dict[str, int]:
        cnt = Counter(self.contenu.split())
        return cnt
    

if __name__ == "__main__":
    texte_test = Texte("Titre", "Moi", "Un texte quelconque oui oui")
    print(texte_test.titre)
    #texte_test.titre = ""
    #print(texte_test.mots_uniques())

    print(texte_test.frequences())