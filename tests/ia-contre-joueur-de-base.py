import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Carte import Carte
from Deck import Deck
from Joueur import JoueurRandom, JoueurPresqueRandom, AdversaireIA
from Game import Game

from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # noqa: F401



# idée :
# faire un joueur qui s'améliore en fonction de la partie en cours
# ce sera "AdversaireIA", un joueur meilleur que JoueurPresqueRandom


def stats(j1, j2, n_parties=1000, nb_val=100, taille_pyramide=27, nb_cartes_par_joueur=4, savej1=False, savej2=False) :
    if not savej1 : j1_reset = deepcopy(j1)
    if not savej2 : j2_reset = deepcopy(j2)
    j1_wins = 0; j2_wins = 0
    
    for  x in range(n_parties) :
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

##### Parties identiques

j1rand = JoueurRandom("Richard")
bot1 = JoueurPresqueRandom("Bernard")
ia2  = AdversaireIA("Igor")

j1_wins, j2_wins, n_parties, j1, j2 = stats(j1rand, ia2, nb_val=int(2+5*(5+1)/8)+1, taille_pyramide=5, nb_cartes_par_joueur=4)

print("Partie courte: random vs ia")
print(f'j1_wins : {j1_wins/(j1_wins+j2_wins):.2f}%')
print(f'j2_wins : {j2_wins/(j1_wins+j2_wins):.2f}%')

j1_wins, j2_wins, n_parties, j1, j2 = stats(bot1, ia2, nb_val=int(2+5*(5+1)/8)+1, taille_pyramide=5, nb_cartes_par_joueur=4)

print("Partie courte : probas(bluff=0.2, denonce=0.2) vs ia")
print(f'j1_wins : {j1_wins/(j1_wins+j2_wins):.2f}%')
print(f'j2_wins : {j2_wins/(j1_wins+j2_wins):.2f}%')


##### Plein de parties avec des variables qui évoluent (les deux probas)

taille_pyramide = 20
nb_cartes_par_joueur = 4
nb_val = int(nb_cartes_par_joueur/2+taille_pyramide*(taille_pyramide+1)/8)+1


liste_j1_wins = []
liste_j2_wins = []
x = np.linspace(0, 1, 16)
y = np.linspace(0, 1, 16)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)
#Z2 = np.zeros_like(X)

for i in range(len(x)):
    for j in range(len(y)):
        p1, p2 = X[j, i], Y[j, i]
        
        bot1 = JoueurPresqueRandom("Bernard", probaBluff=p1, probaDenonce=p2)
        j1_wins, j2_wins, n_parties, j1, j2 = stats(bot1, ia2, n_parties=500, nb_val=nb_val, taille_pyramide=taille_pyramide, nb_cartes_par_joueur=nb_cartes_par_joueur)
        
        Z[j, i] = j1_wins
        #Z2[j, i] = j2_wins

milieu = np.abs(Z - 250) < 50  # Seuil de tolérance



### graphe en 3D

fig = plt.figure(figsize=(10, 7), dpi=100)
ax = fig.add_subplot(111, projection='3d')

s = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, label='Nombre de victoires')
#ax.plot_surface(X, Y, Z2, cmap='plasma', alpha=0.7, label='Z2')
ax.scatter(X[milieu], Y[milieu], Z[milieu], c='red', s=10, label='Intersection') # milieu
ax.view_init(elev=31, azim=-171)

plt.colorbar(s)
plt.xlabel('Probabilité de bluff')
plt.ylabel('Probabilité de dénoncer')
plt.title('Nombre de victoires en variant les probabilités\nde bluff et de dénonciation sur une partie longue')

#plt.savefig('../figures/rand_vs_rand-probas_variees.png')
plt.show()



### graphe en 2D

fig = plt.figure(figsize=(10, 7), dpi=100)
plt.contourf(X,Y,Z, cmap='viridis', vmin=0, vmax=500)

plt.clim(0, 500)
plt.colorbar()
plt.grid(color='gray')
plt.xlabel('Probabilité de bluff')
plt.ylabel('Probabilité de dénoncer')
plt.title('Nombre de victoires en variant les probabilités\nde bluff et de dénonciation sur une partie longue')

#plt.savefig('../figures/rand_vs_rand-probas_variees-2D.png')
plt.show()
