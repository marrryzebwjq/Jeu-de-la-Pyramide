from Carte import Carte
import random

class Deck :
    def __init__(self, taille=52, custom_cards=False, ui=False) :
        self.ui = ui
        self.taille = taille #52 ou 32 ou jspquoi
        self.custom_cards = custom_cards
        self.cartes = []
        self.creer()#(t)

    def __str__(self):
        affichage = ""
        for i in range(len(self.cartes)):
            affichage += self.cartes[i].__str__() + ("\n" if (i+1)%(self.taille//4) == 0 else " ")
        return f"{len(self.cartes)} cartes :\n{affichage}"

    def creer(self) : #52 cartes
        if self.custom_cards :
            self.taille = len(self.custom_cards)
            for c in self.custom_cards :
                if not isinstance(c, Carte) :
                    raise ValueError(f"Carte {c} invalide.")
            self.cartes = self.custom_cards
        else :
            self.cartes = []
            for couleur in Carte.COULEURS :
                for valeur in Carte.VALEURS :
                    self.cartes.append(Carte(valeur, couleur).cacher())


    def melanger(self) :
        if self.ui : print("Mélange du deck")
        random.shuffle(self.cartes)

    def montrer(self) :
        for c in self.cartes :
            c.montrer()
        return self

    def cacher(self) :
        for c in self.cartes :
            c.cacher()
        return self

    def tirer(self) : #top
        if self.ui : print("Pioche d'une carte du deck")
        return self.cartes.pop(0) if self.cartes else None

    def ajouter(self, carte) : #bottom
        if self.ui : print("Ajout d'une carte au fond du deck")
        self.cartes.append(carte)

    #def regarder le top, reposer une carte en top ou bottom ou autre, ......
