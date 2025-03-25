from Carte import Carte
from Deck import Deck
#from Hand import Main
from Joueur import Joueur, JoueurRandom, JoueurPresqueRandom, AdversaireIA
#from Pyramide import Pyramide
from Game import Game

import matplotlib.pyplot as plt
#import numpy as np


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


def stats_rand_ia(n_parties=1000, nb_val=100, taille_pyramide=27, nb_cartes_par_joueur=4, afficher_score=False, ui=False) :

    j1_wins = 0; ia_wins = 0
    for  _ in range(n_parties) :
        cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, nb_val) for couleur in Carte.COULEURS]  # 4 cartes par valeur
        custom_deck = Deck(custom_cards=cards)

        j1 = JoueurRandom("Bertrand")
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
x = range(5, 27)

for i in x :

    j1_wins, ia_wins, n_parties, j1, j2 = stats_bot_ia(n_parties=1000, nb_val=100, taille_pyramide=i, nb_cartes_par_joueur=4)

    liste_j1_wins.append(j1_wins)
    liste_ia_wins.append(ia_wins)

#print(f'liste_j1_wins : {liste_j1_wins}')
#print(f'liste_ia_wins : {liste_ia_wins}')



plt.plot(x, liste_j1_wins, label='Bot avec stratégie fixe')
plt.plot(x, liste_ia_wins, label='IA')
plt.xlabel('Nombre d\'étages dans la pyramide')
plt.ylabel('Nombre de victoires')
plt.title('Performances en fonction de la taille de la pyramide\navec un grand deck (400 cartes)')
plt.legend()


plt.savefig('figures/perf_bot_ia-taille_pyramide.png')
plt.show()



##### Bot Random vs IA : Graphiques

liste_j1_wins = []
liste_ia_wins = []
x = range(5, 27)

for i in x :
    j1_wins, ia_wins, n_parties, j1, j2 = stats_rand_ia(n_parties=1000, nb_val=100, taille_pyramide=i, nb_cartes_par_joueur=4)
    liste_j1_wins.append(j1_wins)
    liste_ia_wins.append(ia_wins)

plt.plot(x, liste_j1_wins, label='Bot aléatoire')
plt.plot(x, liste_ia_wins, label='IA')
plt.xlabel('Nombre d\'étages dans la pyramide')
plt.ylabel('Nombre de victoires')
plt.title('Performances en fonction de la taille de la pyramide\navec un grand deck (400 cartes)')
plt.legend()

plt.savefig('figures/perf_rand_ia-taille_pyramide.png')
plt.show()


##### Bot Random vs IA : Graphiques

liste_j1_wins = []
liste_ia_wins = []
x = range(1,100)

for i in x :
    j1_wins, ia_wins, n_parties, j1, j2 = stats_rand_ia(n_parties=100, nb_val=100, taille_pyramide=15, nb_cartes_par_joueur=i)
    liste_j1_wins.append(j1_wins)
    liste_ia_wins.append(ia_wins)

plt.plot(x, liste_j1_wins, label='Bot aléatoire')
plt.plot(x, liste_ia_wins, label='IA')
plt.xlabel('Taille de la main')
plt.ylabel('Nombre de victoires')
plt.title('Performances en fonction du nombre de cartes en main')
plt.legend()

plt.savefig('figures/perf_rand_ia-taille_main.png')
plt.show()
