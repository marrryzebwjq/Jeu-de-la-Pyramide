import Game



##### Joueur vs Joueur : Partie classique

"""
#main
j1, j2 = Joueur("Bob"), Joueur("Michel")
game = Game([j1, j2])
#game = Game(joueurs, ui=False, desactiver_questions_h=True)
winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom, '\n')

j1.show_stats(); print()
j2.show_stats()
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

"""
#main
cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
custom_deck = Deck(custom_cards=cards)

j1 = JoueurPresqueRandom("Bertrand")
j2 = JoueurPresqueRandom("Caroline")

game = Game(joueurs=[j1, j2], custom_deck=custom_deck, taille_pyramide=15, nb_cartes_par_joueur=20, ui=False)
#game = Game(joueurs, ui=False, desactiver_questions_h=True)

winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom, '\n')
else :
    print("Personne n'a gagné.")

print(j1)
print(j2, '\n')

j1.show_stats(); print()
j2.show_stats()
"""


##### Bot Simple vs IA : 400 cartes, 120 tours (15 étages), 20 cartes par joueur, pas d'affichage, 1 partie

#main
cards = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
custom_deck = Deck(custom_cards=cards)

j1 = JoueurPresqueRandom("Bertrand")
j2 = AdversaireIA("Caroline")

game = Game(joueurs=[j1, j2], custom_deck=custom_deck, taille_pyramide=15, nb_cartes_par_joueur=20, ui=False)
#game = Game(joueurs, ui=False, desactiver_questions_h=True)

winner = game.jouer()

if winner :
    print('Gagnant :')
    print(winner.nom, '\n')
else :
    print("Personne n'a gagné.")

print(j1)
print(j2, '\n')

j1.show_stats(); print()
j2.show_stats()