class Main :
    """ La main d'un joueur.
    """
    def __init__(self, deck, nb_cartes) :
        self.cartes = None
        self.selected = 0 #à partir de 1
        #self.show_selected = False
        self.piocher(deck, nb_cartes)

    def __str__(self) :
        affichage = ""
        for i in range(len(self.cartes)) :
            if (i+1) == self.selected : #self.show_selected and
                affichage += self.cartes[i].montrer().__str__()+" "
            else :
                affichage += self.cartes[i].__str__()+" "
        return affichage

    def __len__(self) :
        return len(self.cartes)

    def piocher(self, deck, nb_cartes) :
        if len(deck.cartes) < nb_cartes :
            raise ValueError(f"Pas assez de cartes dans le deck ({len(deck.cartes)} cartes au lieu de {nb_cartes}.).")
        self.cartes = [deck.tirer() for _ in range(nb_cartes)]

    def select(self,i) :
        if i < 1 or i > len(self.cartes) :
            raise ValueError(f"Indice {i} invalide.")
        self.selected = i
        return self.cartes[i-1]

    def deselect(self) :
        self.selected = None
        #self.show_selected = False

    def show_all(self) :
        for c in self.cartes :
            c.montrer()
        return self

    def hide_all(self) :
        for c in self.cartes :
            c.cacher()
        return self