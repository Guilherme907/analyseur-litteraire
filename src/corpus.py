from texte import Texte

class Corpus:
    def __init__(self, nom: str):
        self.nom = nom
        self.textes: list[Texte] = []

    def ajouter(self, texte: Texte) -> None:
        self.textes.append(texte)
    
    def total_mots(self) -> int:
        return sum(l.nombre_mots() for l in self.textes)

    def rechercher(self, mot_cle: str) -> list[Texte]:
        return [l for l in self.textes if mot_cle in l.titre]
    
texte_test1 = Texte("Titre", "Moi", "Un texte quelconque oui oui")
texte_test2 = Texte("Titre", "Moi", "Un texte quelconque oui oui")

corpus = Corpus("Corpus")
corpus.ajouter(texte_test1)
corpus.ajouter(texte_test2)

print(corpus.nom) 
print(corpus.textes)