from Carte import Carte
from Deck import Deck
#from Hand import Main
from Joueur import Joueur, JoueurPresqueRandom, AdversaireIA
#from Pyramide import Pyramide
from Game import Game

import matplotlib.pyplot as plt
import numpy as np


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



##### Bot Simple vs IA : 400 cartes, 120 tours (27 étages), 4 cartes par joueur, pas d'affichage, 1000 parties

"""
n_parties = 1000
afficher = False

j1_wins, ia_wins, n_parties, j1, j2 = stats_bot_ia(n_parties=n_parties, nb_val=100, taille_pyramide=27, nb_cartes_par_joueur=4, afficher_score=afficher)

print(f'j1_wins : {j1_wins}/{n_parties}')
print(f'ia_wins : {ia_wins}/{n_parties}')
"""



##### Bot Simple vs IA : Graphiques

liste_j1_wins = []
liste_ia_wins = []

for i in range(5,25) :

    j1_wins, ia_wins, n_parties, j1, j2 = stats_bot_ia(n_parties=100, nb_val=100, taille_pyramide=i, nb_cartes_par_joueur=4)

    liste_j1_wins.append(j1_wins)
    liste_ia_wins.append(ia_wins)

#print(f'liste_j1_wins : {liste_j1_wins}')
#print(f'liste_ia_wins : {liste_ia_wins}')


x = np.arange(1, 21)
plt.plot(x, liste_j1_wins, label='Bot avec proba fixe')
plt.plot(x, liste_ia_wins, label='IA')
plt.xlabel('Nombre d\'étages dans la pyramide')
plt.ylabel('Nombre de victoires')
plt.title('Victoires Joueur vs IA (deck de 400 cartes)')
plt.legend()
plt.show()