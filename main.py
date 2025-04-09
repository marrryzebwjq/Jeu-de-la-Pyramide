from Carte import Carte
from Deck import Deck
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
"""
nom = input("Entrez votre nom : ")
game = Game(joueurs=[Joueur(nom), AdversaireIA("Isabella")], taille_pyramide=5, nb_cartes_par_joueur=5)
winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom)
else :
    print("Egalité.")
    """
    
    
cards   = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 65) for couleur in Carte.COULEURS]  # 4 cartes par valeur
custom_deck = Deck(custom_cards=cards)
j2 =  AdversaireIA("Isabella")
game = Game(joueurs=[JoueurPresqueRandom("nom"),j2], custom_deck=custom_deck, taille_pyramide=10, nb_cartes_par_joueur=10, ui=False)
winner = game.jouer()
j2.show_stats()