class Carte :
    """
    Une carte à jouer (pour un jeu classique de 52 cartes, sans joker).
    (j'ai mis couleur pour voir, on peut s'en servir pour identifier les cartes pendant le jeu, après on en a pas vraiment besoin mais je pose ça là)
    """
    VALEURS = {1:"A ", 2:"2 ", 3:"3 ", 4:"4 ", 5:"5 ", 6:"6 ", 7:"7 ", 8:"8 ", 9:"9 ", 10:"10", 11:"J ", 12:"Q ", 13:"K "}
    COULEURS = {"carreau" : "♦", "coeur" : "♥", "pique" : "♠", "trefle" : "♣"}

    def __init__(self, valeur, couleur, custom_val=False, custom_col=False) :
        if not custom_val and valeur not in self.VALEURS :
            raise ValueError(f"Valeur {valeur} invalide.")
        if not custom_col and couleur not in self.COULEURS :
            raise ValueError(f"Couleur {couleur} invalide.")

        self.valeur = valeur
        self.couleur = couleur
        self.custom_val = custom_val
        self.custom_col = custom_col
        self.visible = True

    def __str__(self):
        if self.visible :
            if self.custom_val :
                val = str(self.valeur) + " " if self.valeur < 10 else str(self.valeur)
            else :
                val = self.VALEURS[self.valeur]
            return f"[{val}{self.couleur if self.custom_col else self.COULEURS[self.couleur]}]"
        else :
            return "[ x ]"

    def montrer(self) :
        self.visible = True
        return self

    def cacher(self) :
        self.visible = False
        return self

    def montrer_une_fois(self) :
        c = copy(self.montrer())
        self.cacher()
        return c

    def same_value(self, carte) :
        return self.valeur == carte.valeur