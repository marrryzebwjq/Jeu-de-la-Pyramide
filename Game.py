from Carte import Carte
from Deck import Deck
from Hand import Main
from Joueur import Joueur, JoueurPresqueRandom, AdversaireIA
from Pyramide import Pyramide

#from IPython.display import clear_output   # pour clear l'output dans un notebook (.pynb)
import os                                   # pour clear le terminal (.py)

class Game:
    POINTS = {"claim" : 1, "denoncer_success" : 2, "denoncer_failed" : 3}

    def __init__(self, joueurs, nb_cartes_par_joueur=5, taille_pyramide=7, custom_deck=False, ui=True, desactiver_questions_h=False, desactiver_questions_ia=True, clear_between_rounds=True):
        self.ui = ui #affichage pyramide, mains etc
        self.desactiver_questions_h = desactiver_questions_h
        self.desactiver_questions_ia = desactiver_questions_ia
        self.clear_between_rounds = clear_between_rounds

        self.joueurs = joueurs
        self.nb_cartes_par_joueur = nb_cartes_par_joueur
        self.deck = custom_deck if custom_deck else self.new_deck()
        self.deck.melanger()

        self.pyramide = Pyramide(taille_pyramide, self.deck)
        self.tour = 1
        self.inputs = {joueur.nom : False for joueur in self.joueurs}

        self.setUI()

    def __str__(self):
        affichage = ""
        affichage += self.pyramide.__str__()
        affichage += "\n"
        for joueur in self.joueurs :
            affichage += f"{joueur.__str__()}\n"
        return affichage

    def setUI(self) :
        if not self.ui :
            self.desactiver_questions_h = True
            self.desactiver_questions_ia = True
        if self.desactiver_questions_h and self.desactiver_questions_ia :
            self.ui=False

        for joueur in self.joueurs :
            if self.desactiver_questions_h and joueur.human :
                joueur.ui=False
            if self.desactiver_questions_ia and not joueur.human :
                joueur.ui=False

    def clearUI(self) :
        if self.clear_between_rounds :
            #clear_output()
            os.system('cls||clear')

    def new_deck(self) :
        deck = Deck()
        return deck

    def adversaire(self, joueur) :
        if joueur not in self.joueurs :
            return None
        for j2 in self.joueurs :
            if j2 != joueur :
                return j2

    def winner(self) :
        """Le gagnant est celui qui a le moins de points"""
        jminpoints = 1000000000000
        jmin = None
        for joueur in self.joueurs :
            if joueur.points < jminpoints :
                jminpoints = joueur.points
                jmin = joueur
            elif joueur.points == jminpoints :
                jmin = None
        return jmin

    def not_denoncer(self, joueur, bluff) :
        p = self.POINTS["claim"]
        if self.ui : print(f"{joueur.nom} ne dénonce pas. {joueur.nom} prends {p} points")
        joueur.not_denoncer(p)                                          # not denounce
        self.adversaire(joueur).claimed(p, success=True, bluff=bluff, accused=False, manche=self.tour, adv_p_denonce=1) #claimed success (avec ou sans bluff)

    def denoncer_success(self, joueur, carte_pyr) :
        p = self.POINTS["denoncer_success"]
        if self.ui : print(f"{self.adversaire(joueur).nom} a bluffé ! {self.adversaire(joueur).nom} prends {p} points")
        joueur.denoncer(p, success=True, card=carte_pyr, manche=self.tour, adv_p_denonce=1)                             #denoncer success
        self.adversaire(joueur).claimed(p, success=False, bluff=True, accused=True, manche=self.tour, adv_p_denonce=1)  #claimed failed (bluff raté)

    def denoncer_failed(self, joueur, carte_pyr) :
        p = self.POINTS["denoncer_failed"]
        self.adversaire(joueur).main.select(self.adversaire(joueur).possede_carte(carte_pyr))
        if self.ui :
            print(self.adversaire(joueur))
            print(f"{self.adversaire(joueur).nom} possédait la carte... {joueur.nom} prends {p} points")
        joueur.denoncer(p, success=False, card=carte_pyr, manche=self.tour, adv_p_denonce=1)                             #denoncer failed
        self.adversaire(joueur).claimed(p, success=True, bluff=False, accused=True, manche=self.tour, adv_p_denonce=1)   #claim success (pas bluff)



    # ---- jeu ---- #

    def jouer(self) : #loop jusque pyramide vide
        #-- début de partie : distribution --#
        for joueur in self.joueurs :
            joueur.recevoir_main(self.deck, self.nb_cartes_par_joueur)
            #afficher main de maniere super discrete
            if joueur.ui :
                joueur.main.show_all()
                input(f"Appuyez sur entrée pour voir la main de {joueur.nom}")
                print(joueur)
                input("Appuyez sur entrée pour continuer.")
                self.clearUI()
            joueur.main.hide_all()


        #-- tours : --#
        stop_game = False
        while self.pyramide.icartesamontrer and not stop_game :
            if self.ui : self.clearUI()
            # phase de début : une carte de la pyramide est retournée #

            carte_pyr = self.pyramide.montrer_prochaine_carte()
            if self.ui :
                print(self)
                print(f"\nVoici la nouvelle carte : {carte_pyr}\n")

            # phase d'action 1 : les joueurs choisissent s'ils jouent #

            for joueur in self.joueurs:
                self.inputs[joueur.nom]=False
            hastoplay=[]

            for joueur in self.joueurs :
                if joueur.ui :
                    print(f"----- {joueur.nom} -----")
                    print("Jouer une carte ?\n[ o ] [ n ]") #[print(f"[ {a} ] : {joueur.ACTIONS[a]}") for a in joueur.ACTIONS]
                i = joueur.choose_action1(carte_pyr)

                if not i :
                    stop_game = True
                    break #un joueur a demandé à arrêter la partie

                elif i=="o":
                    self.inputs[joueur.nom] = True
                    hastoplay.append(self.adversaire(joueur))

            if stop_game : break

            if self.ui :
                played=False;
                for joueur in self.joueurs :
                    if self.inputs[joueur.nom] :
                        print(f"Joueur {joueur.nom} a réclamé la carte."); played=True
                if not played :
                    print("Personne n'a joué. Tour suivant.")

            for joueur in self.joueurs:
                self.inputs[joueur.nom]=False

            # phase d'action 2 : les joueurs dénoncent éventuellement #

            for joueur in hastoplay :
                # dénoncer ?
                if joueur.ui :
                    print(f"----- {joueur.nom} -----")
                    print(f"Dénoncer l'adversaire {self.adversaire(joueur).nom} ?\n[ o ] [ n ]")

                i = joueur.choose_action2(carte_pyr)
                hascard = self.adversaire(joueur).possede_carte(carte_pyr)

                if not i :
                    stop_game = True
                    break

                elif i=="o": # a dénoncé
                    if self.ui : print(f"{joueur.nom} dénonce {self.adversaire(joueur).nom} !!!")

                    if hascard :
                        self.denoncer_failed(joueur, carte_pyr)  # POINT MALUS POUR joueur + révéler la carte dans la main
                    else :
                        self.denoncer_success(joueur, carte_pyr) # POINT MALUS POUR self.adversaire(joueur)

                elif i=="n" : # n'a pas dénoncé : POINT MALUS POUR joueur
                    if hascard :
                        self.not_denoncer(joueur, True) #bluff
                    else :
                        self.not_denoncer(joueur, False)


            # phase finale : tour suivant #

            if self.ui : input("Appuyez sur entrée pour continuer.")
            self.tour += 1

        #-- fin de partie : return points --#
        if self.ui :
            print("Toutes les cartes ont été retournées.") if not stop_game else print("Fin de la partie.")
            [print(joueur) for joueur in self.joueurs]
        return self.winner()