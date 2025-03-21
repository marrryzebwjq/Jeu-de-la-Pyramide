##### Joueur vs Joueur : Partie classique

"""
#main
joueurs = [Joueur("Bob"), Joueur("Michel")]
game = Game(joueurs)
#game = Game(joueurs, ui=False, desactiver_questions_h=True)
game.jouer()
"""


##### Joueur vs Joueur : 400 cartes, pyramide de 15 étages (120 tours), 20 cartes par joueurs

"""
#main
cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
custom_deck = Deck(custom_cards=cards)

joueurs = [Joueur("Bertrand"), Joueur("Caroline")]
game = Game(joueurs, custom_deck=custom_deck, taille_pyramide=15, nb_cartes_par_joueur=20)
#game = Game(joueurs, ui=False, desactiver_questions_h=True)

winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom)
"""


##### Joueur vs Bot Simple : 400 cartes, 120 tours (15 étages), 20 cartes par joueur

"""
#main

cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
custom_deck = Deck(custom_cards=cards)

joueurs = [Joueur("Bertrand"), JoueurPresqueRandom("Caroline")]
game = Game(joueurs, custom_deck=custom_deck, taille_pyramide=15, nb_cartes_par_joueur=20)
#game = Game(joueurs, ui=False, desactiver_questions_h=True)

winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom)
"""
    
##### Bot Simple vs Bot Simple : 400 cartes, 120 tours (15 étages), 20 cartes par joueur

#main

cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
custom_deck = Deck(custom_cards=cards)

joueurs = [JoueurPresqueRandom("Bertrand"), JoueurPresqueRandom("Caroline")]
game = Game(joueurs, custom_deck=custom_deck, taille_pyramide=15, nb_cartes_par_joueur=20, ui=False)
#game = Game(joueurs, ui=False, desactiver_questions_h=True)

winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner)