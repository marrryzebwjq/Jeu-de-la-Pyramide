import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Carte import Carte
from Deck import Deck
#from Hand import Main
from Joueur import Joueur, JoueurPresqueRandom, AdversaireIA
#from Pyramide import Pyramide
from Game import Game


##### Joueur vs Joueur : 400 cartes, pyramide de 15 étages (120 tours), 20 cartes par joueurs

"""
cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
custom_deck = Deck(custom_cards=cards)

joueurs = [Joueur("Bertrand"), Joueur("Caroline")]
game = Game(joueurs, custom_deck=custom_deck, taille_pyramide=15, nb_cartes_par_joueur=20)

winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom)
"""


##### Joueur vs Bot Simple : 400 cartes, 120 tours (15 étages), 20 cartes par joueur

"""
cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
custom_deck = Deck(custom_cards=cards)

game = Game(joueurs=[Joueur("Bertrand"), JoueurPresqueRandom("Caroline")], custom_deck=custom_deck, taille_pyramide=15, nb_cartes_par_joueur=20)
winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom)
"""


def stats_bot_bot(n_parties=1000, nb_val=100, taille_pyramide=27, nb_cartes_par_joueur=4, afficher_score=False, ui=False) :

    j1_wins = 0; ia_wins = 0
    for  _ in range(n_parties) :
        cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, nb_val) for couleur in Carte.COULEURS]  # 4 cartes par valeur
        custom_deck = Deck(custom_cards=cards)

        j1 = JoueurPresqueRandom("Bertrand")
        j2 = JoueurPresqueRandom("Brigitte")

        game = Game(joueurs=[j1, j2], custom_deck=custom_deck, taille_pyramide=taille_pyramide, nb_cartes_par_joueur=nb_cartes_par_joueur, ui=ui)
        winner = game.jouer()

        if winner == j1 :
            j1_wins += 1
        elif winner == j2 :
            ia_wins += 1
        if afficher_score :
            #print(j1)
            print(j2, '\n')
            j1.show_stats(); print()
            j2.show_stats()

    return j1_wins, ia_wins, n_parties, j1, j2


def stats_bot_ia(n_parties=1000, nb_val=100, taille_pyramide=27, nb_cartes_par_joueur=4, afficher_score=False, ui=False) :

    j1_wins = 0; ia_wins = 0
    for  _ in range(n_parties) :
        cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, nb_val) for couleur in Carte.COULEURS]  # 4 cartes par valeur
        custom_deck = Deck(custom_cards=cards)

        j1 = JoueurPresqueRandom("Bertrand")
        j2 = AdversaireIA("Isabelle")

        game = Game(joueurs=[j1, j2], custom_deck=custom_deck, taille_pyramide=taille_pyramide, nb_cartes_par_joueur=nb_cartes_par_joueur, ui=ui)
        winner = game.jouer()

        if winner == j1 :
            j1_wins += 1
        elif winner == j2 :
            ia_wins += 1
        if afficher_score :
            #print(j1)
            print(j2, '\n')
            j1.show_stats(); print()
            j2.show_stats()

    return j1_wins, ia_wins, n_parties, j1, j2



##### Bot Simple vs Bot Simple : 400 cartes, 120 tours (15 étages), 20 cartes par joueur

"""
j1_wins, ia_wins, n_parties, j1, j2 = stats_bot_bot(n_parties=1, nb_val=100, taille_pyramide=15, nb_cartes_par_joueur=20, ui=True)

if j1_wins :
    print('Gagnant :')
    print(j1.nom, '\n')
elif ia_wins :
    print('Gagnant :')
    print(j2.nom, '\n')
else :
    print("Personne n'a gagné.")

print(j1)
print(j2, '\n')

j1.show_stats(); print()
j2.show_stats()
"""

##### Bot Simple vs IA : 400 cartes, 120 tours (15 étages), 20 cartes par joueur, pas d'affichage, 1 partie


j1_wins, ia_wins, n_parties, j1, j2 = stats_bot_ia(n_parties=1, nb_val=100, taille_pyramide=15, nb_cartes_par_joueur=20, afficher_score=False, ui=False)

if j1_wins :
    print('Gagnant :')
    print(j1.nom, '\n')
elif ia_wins :
    print('Gagnant :')
    print(j2.nom, '\n')
else :
    print("Personne n'a gagné.")

print(j1)
print(j2, '\n')

j1.show_stats(); print()
j2.show_stats()


