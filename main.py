#from Carte import Carte
#from Deck import Deck
#from Hand import Main
from Joueur import Joueur, JoueurPresqueRandom, AdversaireIA
#from Pyramide import Pyramide
from Game import Game



##### Joueur vs Joueur : Partie classique

"""
j1, j2 = Joueur("Bob"), Joueur("Michel")
game = Game([j1, j2])
winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom, '\n')
"""



##### Joueur vs IA avancée : Partie Classique

nom = input("Entrez votre nom : ")
game = Game(joueurs=[Joueur(nom), AdversaireIA("Isabella")])
winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom)
else :
    print("Egalité.")