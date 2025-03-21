from Carte import Carte
from Deck import Deck
from Pyramide import Pyramide

cartes = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
d = Deck(custom_cards=cartes)
d.melanger()
pyramide = Pyramide(20, d)
print(pyramide)

pyramide.montrer_prochaine_carte()
print(pyramide)
pyramide.montrer_prochaine_carte()
print(pyramide)
print(pyramide.montrer_tout())