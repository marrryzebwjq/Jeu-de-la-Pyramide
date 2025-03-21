from Carte import Carte
from Deck import Deck
from Hand import Main
from Joueur import Joueur, JoueurPresqueRandom, AdversaireIA

class Pyramide :
    def __init__(self, hauteur, deck) :
        if hauteur < 1 :
            raise ValueError(f"Hauteur {hauteur} invalide.")
        if len(deck.cartes) < (hauteur*(hauteur+1)//2) :
            raise ValueError(f"Pas assez de cartes dans le deck ({len(deck.cartes)} cartes).")

        self.hauteur = hauteur #nb cartes = h(h+1)/2
        self.cartes = []
        self.piocher(deck)
        self.icartesamontrer = []
        self.icartesacacher = []
        self.cacher_tout()

    def __str__(self):
        affichage = ""; k=0
        for etage in range(self.hauteur+1) :
            affichage += "   " * (self.hauteur-etage)
            for j in range(k, k+etage) :
                affichage += self.cartes[j].__str__()+" "
            k += etage
            affichage += "\n"
        return affichage

    def piocher(self, deck) : #private
        for i in range(self.hauteur*(self.hauteur+1)//2) :
            c = deck.tirer()
            self.cartes.append(c)

    def generer_indices_ordre(self) : #private
        """ordre des cartes à retourner pendant une  partie"""
        self.icartesamontrer, self.icartesacacher = [], []

        for etage in range(self.hauteur) :
            i = (etage*(etage+1))//2
            self.icartesamontrer[:0] = range(i,i+etage+1)#[0] [1,2] [3,4,5]...



    def montrer_prochaine_carte(self) :
        i = self.icartesamontrer.pop(0) #enleve le premier elmt
        self.icartesacacher.append(i)   #l'ajoute ici à la fin
        self.cartes[i].montrer()
        return self.cartes[i]

    def montrer_tout(self) :
        self.generer_indices_ordre()
        self.icartesamontrer, self.icartesacacher = self.icartesacacher, self.icartesamontrer

        for c in self.cartes :
            c.montrer()
        return self

    def cacher_tout(self) :
        self.generer_indices_ordre()
        for c in self.cartes :
            c.cacher()
        return self