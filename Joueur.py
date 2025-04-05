from Hand import Main
import random

class Joueur:
    """ Un joueur HUMAIN.
    """
    ACTIONS = {"o" : "oui", "n" : "non"}
    STOP = ["stop", "quit", "q", "exit"]

    def __init__(self, nom, human=True, ui=True):
        self.nom = nom
        self.human = human
        self.ui = ui #affichage des questions

        self.stop_game = False
        self.main = None
        self.points = 0

    def __str__(self):
        """ Affichage """
        return f"{self.nom} ({self.points} pts) : {self.main.__str__()}"

    def show_stats(self):
        """ Affichage """
        print(f"{self.nom} (Human) : {self.points} pts")


    # actions de début de jeu
    def recevoir_main(self, deck, nb_cartes):
        self.main = Main(deck, nb_cartes)

    # actions pendant un tour
    def choose_action1(self, carte) :
        """ Choisir entre jouer une carte ou passer son tour."""
        i=None
        while i not in self.ACTIONS :
            i = input()
            if i in self.STOP :
                self.stop_game = True
                return False
        return i

    def choose_action2(self, carte) :
        """ Choisir entre dénoncer l'adversaire ou le laisser."""
        i=None
        while i not in self.ACTIONS :
            i = input()
            if i in self.STOP :
                self.stop_game = True
                return False
        return i

    def possede_carte(self, carte):
        """ return indice de la carte si elle est dans la main
        [ 1 ] [ 2 ] [ 3 ] [ 4 ].... ou False (0)"""
        i=1
        for c in self.main.cartes :
            if c.same_value(carte) :
                return i
            i+=1
        return False

    # actions de fin de tour
    def ajouter_points(self, points) :
        self.points += points
        return self.points

    def claimed(self, points, success, bluff, accused, manche) : #le joueur a claim une carte...
        if not success :       #...et il n'a pas gagné
            self.ajouter_points(points)

    def denoncer(self, points, success, card, manche) : #le joueur a dénoncé l'adversaire
        if not success :       #...et l'adversaire n'avait pas bluffé
            self.ajouter_points(points)

    def not_denoncer(self, points, manche) :  #le joueur n'a pas dénoncé l'adversaire
        self.ajouter_points(points)




class JoueurRandom(Joueur):
    """ Joueur qui joue au hasard avec une proba uniforme à chaque action possible.
    """
    def __init__(self, nom):
        super().__init__(nom, human=False, ui=False)    #attributs parent : nom, human, ui, stop_game, main, points

    def show_stats(self):
        """ Affichage """
        print(f"{self.nom} (Random) : {self.points} pts")

    def choose_action1(self, carte) :
        """ Choisir entre jouer une carte ou passer son tour."""
        return "o" if random.random() < 0.5 else "n"

    def choose_action2(self, carte) :
        """ Choisir entre dénoncer l'adversaire ou le laisser."""
        return "o" if random.random() < 0.5 else "n"




class JoueurPresqueRandom(Joueur):
    """ Joueur qui joue avec des probas fixées.
    """
    def __init__(self, nom, probaBluff=0.2, probaDenonce=0.5):
        super().__init__(nom, human=False, ui=False)    #attributs parent : nom, human, ui, stop_game, main, points
        self.probaBluff = probaBluff                    # Probabilité de bluff du joueur
        self.probaDenonce = probaDenonce                # Probabilité de dénonciation du joueur

    # méthodes parent :
    # recevoir_main(self, deck, nb_cartes) - show_stats()
    # choose_action1(self) - choose_action2(self)
    # possede_carte(self, carte) - ajouter_points(self, points)
    # claimed(self, points, success, bluff, accused, manche) - denoncer(self, points, success, card, manche) - not_denoncer(self, points, manche)

    def show_stats(self):
        """ Affichage """
        print(f"{self.nom} (IA Simple) : {self.points} pts")
        print(f"Proba de bluffer     : {self.probaBluff}")
        print(f"Proba de dénoncement : {self.probaDenonce}")


    def choose_action1(self, carte) : # Le joueur bluffe s'il a une probabilité de bluff > une valeur aléatoire ou s'il possède la carte
        """ Choisir entre jouer une carte ou passer son tour."""
        return "o" if random.random() < self.probaBluff or self.possede_carte(carte) else "n"

    def choose_action2(self, carte) :
        """ Choisir entre dénoncer l'adversaire ou le laisser."""
        return "o" if random.random() < self.probaDenonce else "n"




class AdversaireIA(JoueurPresqueRandom):
    """ Joueur qui s'adapte en fonction des actions de l'adversaire.
    """
    def __init__(self, nom="IA", probaBluff=0.2, probaDenonce=0.2):
        super().__init__(nom, probaBluff, probaDenonce)  #attributs parent : nom, human, ui, stop_game, main, points - probaBluff, probaDenonce

        self.cartesAdversaire = []  # Mémorise les cartes de l'adversaire
        self.bluffReussis = 0
        self.bluffRate = 0
        self.denonceReussi = 0
        self.denonceRate = 0
        #self.cartesRetournees = []
        #self.cartesInterditesBluff = []
        self.cptAdvClaim  = 0       # Le nombre de fois que l'adversaire a joué une carte
        self.advBluffeur = False
        self.cptAccuse = 0          # Le nombre de fois que l'adversaire a accusé
        self.stopMentir = False

    # méthodes parent :
    # recevoir_main(self, deck, nb_cartes) - show_stats()
    # choose_action1(self) - choose_action2(self)
    # possede_carte(self, carte) - ajouter_points(self, points)
    # claimed(self, points, success, bluff, accused, manche) - denoncer(self, points, success, card, manche) - not_denoncer(self, points, manche)

    def show_stats(self):
        print(f"{self.nom} (IA Améliorée) : {self.points} pts")
        print(f"Proba de bluffer              : {self.probaBluff}")
        print(f"Proba de dénoncement          : {self.probaDenonce}")
        print(f"Bluff réussis/ratés           : {self.bluffReussis} | {self.bluffRate}")
        print(f"Dénonciations reussies/ratées : {self.denonceReussi} | {self.denonceRate}")
        print(f"Détection bluff abusif        : {self.advBluffeur} - {self.cptAdvClaim}")
        print(f"Nombre d'accusations reçues   : {self.cptAccuse}")
        print("Cartes mémorisées : ", end=' ')
        for c in self.cartesAdversaire : print(c, end=' ')
        print('\n')
        

    # actions pendant un tour
    def choose_action2(self, carte):
        """ Choisir entre dénoncer l'adversaire ou le laisser."""
        for c in self.cartesAdversaire :                    # Si la carte est connue comme appartenant au joueur, ne pas accuser
            if c.same_value(carte) :
                return "n"
        if len(self.cartesAdversaire) >= len(self.main) :   # Si l'IA connaît toutes les cartes du joueur, elle accuse systématiquement un bluff
            return "o"
        return super().choose_action2(carte)                # Sinon, comportement normal avec probabilité



    # actions de fin de tour :
    # répartition des points et recalculs en fonction de si le joueur a joué une carte/dénoncé/pas dénoncé
    def claimed(self, points, success, bluff, accused, manche) : #le joueur a claim une carte...
        if success :    #...et il a gagné
            if bluff :
                self.bluffReussis += 1          # L'adversaire n'a pas dénoncé
                self.recalcul_proba(manche)
                return
            else :                              # Le joueur dit la vérité, l'adversaire a dénoncé ou n'a pas dénoncé
                if accused :
                    self.cptAccuse += 1
                return
        else :          #...et il n'a pas gagné
            self.cptAccuse += 1
            self.ajouter_points(points)         # Le bluffeur est puni (2 points)
            self.bluffRate += 1                 # L'IA enregistre une bluff ratée
            self.recalcul_proba(manche)               # on pourrait décider de moins bluffer ici
            return

    def denoncer(self, points, success, card, manche) : #le joueur a dénoncé l'adversaire
        self.cptAdvClaim += 1
        if success :    #...et l'adversaire avait bluffé
            self.denonceReussi += 1             # L'IA enregistre une dénonciation réussie
            self.recalcul_proba(manche)
            return
        else :          #...et l'adversaire n'avait pas bluffé
            self.ajouter_points(points)         # L'IA est punie fortement pour une accusation erronée (3 points)

            self.denonceRate += 1               # L'IA enregistre une dénonciation ratée
            self.recalcul_proba(manche)               # on pourrait décider de moins dénoncer ici
            self.cartesAdversaire.append(card)  # L'IA mémorise la carte correcte du joueur
            return

    def not_denoncer(self, points, manche) : #le joueur n'a pas dénoncé l'adversaire
        self.ajouter_points(points)             # Pas contesté (1 point)
        self.cptAdvClaim += 1
        self.recalcul_proba(manche)
        return




    def recalcul_proba(self, manche):
        """ Recalcul des probabilités en fonction des actions de la manche en cours
        """
        # -- v3 -- #
        # Si l'adversaire joue plus de cartes différentes qu'il n'a en main (c'est qu'il bluff sûrement), l'IA va plus souvent le dénoncer
        if self.cptAdvClaim >= len(self.main) and not self.advBluffeur :
            self.probaDenonce = min(self.probaDenonce+0.5, 0.9)
            self.advBluffeur = True
        # Si l'adversaire dénonce souvent (>= 0.6), l'IA cesse presque totalement de bluffer
        if self.cptAccuse >= 10 and manche == 15 :
            self.stopMentir = True
            self.probaBluff = 0.01
        
        # Par défaut, l'IA adapte sa proba de dénoncer en fonction du nombre d'accusations réussies
        if not self.advBluffeur :
            self.probaDenonce = min(0.5, 0.2 + (self.denonceReussi - self.denonceRate) * 0.05)
        
        # et adapte sa proba de bluffer en fonction du nombre de bluff réussis
        if not self.stopMentir :
            self.probaBluff = max(0.01, self.probaBluff + (self.bluffReussis - self.bluffRate) * 0.05)
    
    
    """
    def recalcul_proba_v2(self, manche):
        # -- v2 -- #
        # Si l'adversaire dénonce souvent (>= 0.3), l'IA cesse presque totalement de bluffer
        if (self.cptAccuse >= 1 and manche == 20):
            self.stopMentir = True
            self.probaBluff = 0.01
        elif(self.stopMentir):
            self.probaBluff = 0.01
        else:
            self.probaBluff = max(0.01, self.probaBluff + (self.bluffReussis - self.bluffRate) * 0.05)

            self.probaDenonce = min(0.5, 0.2 + (self.denonceReussi - self.denonceRate) * 0.05)
    """
    
    
    """
    def recalcul_proba_v1(self, manche, adv_p_denonce):
        # -- v1 -- #
        # Si l'adversaire dénonce souvent (>= 0.3), l'IA cesse presque totalement de bluffer
        if adv_p_denonce >= 0.30:
            self.probaBluff = 0.01
        else:
            self.probaBluff = max(0.01, self.probaBluff + (self.bluffReussis - self.bluffRate) * 0.05)
        self.probaDenonce = min(0.5, 0.2 + (self.denonceReussi - self.denonceRate) * 0.05)
    """
