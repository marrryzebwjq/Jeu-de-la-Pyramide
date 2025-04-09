from Carte import Carte
from Deck import Deck
#from Hand import Main
from Joueur import Joueur, JoueurRandom, JoueurPresqueRandom, AdversaireIA
#from Pyramide import Pyramide
from Game import Game

import matplotlib.pyplot as plt
from copy import deepcopy
#import numpy as np


def stats(j1, j2, n_parties=1000, nb_val=100, taille_pyramide=27, nb_cartes_par_joueur=4, savej1=False, savej2=False) :
    if not savej1 : j1_reset = deepcopy(j1)
    if not savej2 : j2_reset = deepcopy(j2)
    j1_wins = 0; j2_wins = 0
    
    for  _ in range(n_parties) :
        # reset
        cards   = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, nb_val+1) for couleur in Carte.COULEURS]  # 4 cartes par valeur
        custom_deck = Deck(custom_cards=cards)
        if not savej1 : j1 = deepcopy(j1_reset)
        if not savej2 : j2 = deepcopy(j2_reset)
        
        # lancement de la partie
        game = Game(joueurs=[j1, j2], custom_deck=custom_deck, taille_pyramide=taille_pyramide, nb_cartes_par_joueur=nb_cartes_par_joueur, ui=False)
        winner = game.jouer()
        
        # points
        if winner == j1 :
            j1_wins += 1
        elif winner == j2 :
            j2_wins += 1

    return j1_wins, j2_wins, n_parties, j1, j2


j1rand = JoueurRandom("Richard")
bot1 = JoueurPresqueRandom("Patrick")
bot2 = JoueurPresqueRandom("Pascale")
ia1 = AdversaireIA("Igor")
ia2 = AdversaireIA("Isabelle")

##### Bot Simple vs IA : 400 cartes, 120 tours (27 étages), 4 cartes par joueur, pas d'affichage, 1000 parties

"""
n_parties = 1000

j1_wins, ia_wins, n_parties, j1, j2 = stats(bot1, ia2, n_parties=n_parties, nb_val=100)

print(f'j1_wins : {j1_wins}/{n_parties}')
print(f'ia_wins : {ia_wins}/{n_parties}')
"""


##### IA vs IA : Graphiques

liste_j1_wins = []
liste_ia_wins = []
x = range(5, 28)

for i in x :
    j1_wins, ia_wins, n_parties, j1, j2 = stats(ia1, ia2, n_parties=1000, nb_val=int(2+i*(i+1)/8)+1, taille_pyramide=i, nb_cartes_par_joueur=4)
    liste_j1_wins.append(j1_wins)
    liste_ia_wins.append(ia_wins)

plt.plot(x, liste_j1_wins, label='IA 1')
plt.plot(x, liste_ia_wins, label='IA 2')
plt.xlabel('Nombre d\'étages dans la pyramide')
plt.ylabel('Nombre de victoires')
plt.ylim([0, 1000])
plt.title('Performances en fonction de la taille de la pyramide\n(main de 4 cartes)')
plt.legend()

#plt.savefig('figures/perf_ia_ia-taille_pyramide.png')
plt.show()


##### Bot Random vs IA : Graphiques

liste_j1_wins = []
liste_ia_wins = []
x = range(5, 28)

for i in x :
    j1_wins, ia_wins, n_parties, j1, j2 = stats(j1rand, ia2, n_parties=1000, nb_val=int(2+i*(i+1)/8)+1, taille_pyramide=i, nb_cartes_par_joueur=4)
    liste_j1_wins.append(j1_wins)
    liste_ia_wins.append(ia_wins)

plt.plot(x, liste_j1_wins, label='Bot aléatoire')
plt.plot(x, liste_ia_wins, label='IA')
plt.xlabel('Nombre d\'étages dans la pyramide')
plt.ylabel('Nombre de victoires')
plt.title('Performances en fonction de la taille de la pyramide\navec un grand deck (400 cartes)')
plt.legend()

#plt.savefig('figures/perf_rand_ia-taille_pyramide.png')
plt.show()


##### Bot Random vs IA : Graphiques

# 1. si on vide le deck dans la pyramide alors ça change rien qu'il soit grand ou petit (en faisant varier la taille de la main).
# 2. on peut se demander si laisser bcp de cartes dans la pioche influence les perf de l'ia
#    ---> etages fixe et pas trop grand, taille de main petit (4) ou grand (20) : resultat ça change rien

etages = 10

liste_j1_wins = []
liste_ia_wins = []
x = range(100, 400, 5)
for i in x :
    j1_wins, ia_wins, n_parties, j1, j2 = stats(j1rand, ia2, n_parties=500, nb_val=i, taille_pyramide=etages, nb_cartes_par_joueur=20)
    liste_j1_wins.append(j1_wins)
    liste_ia_wins.append(ia_wins)

plt.plot(x, liste_j1_wins, label='Bot aléatoire')
plt.plot(x, liste_ia_wins, label='IA')
plt.xlabel(f'Nombre de cartes laissées de côté pour une pyramide à {etages} étages')
plt.ylabel('Nombre de victoires')
plt.title('Performances en fonction de la quantité de cartes laissées dans le deck')
plt.legend()
plt.ylim([0,500])

#plt.savefig('figures/perf_rand_ia-deck-pas_ouf.png')
plt.show()


##### Bot Simple vs IA : Graphiques

liste_j1_wins = []
liste_ia_wins = []
x = range(5, 27)

for i in x :

    j1_wins, ia_wins, n_parties, j1, j2 = stats(bot1, ia2, n_parties=1000, nb_val=100, taille_pyramide=i, nb_cartes_par_joueur=1)
    liste_j1_wins.append(j1_wins)
    liste_ia_wins.append(ia_wins)

#print(f'liste_j1_wins : {liste_j1_wins}')
#print(f'liste_ia_wins : {liste_ia_wins}')

plt.plot(x, liste_j1_wins, label='Bot avec stratégie fixe')
plt.plot(x, liste_ia_wins, label='IA')
plt.xlabel('Nombre d\'étages dans la pyramide')
plt.ylabel('Nombre de victoires')
plt.title('Performances en fonction de la taille de la pyramide\n(main de 4 cartes)')
plt.legend()

#plt.savefig('figures/perf_bot_ia-taille_pyramide-petite_main.png')
plt.show()

