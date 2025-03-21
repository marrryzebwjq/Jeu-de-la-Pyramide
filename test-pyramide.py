from Deck import Deck
from Pyramide import Pyramide

deck = Deck()
deck.melanger()
print(deck.montrer())
pyramide = Pyramide(5, deck)
print(pyramide)

pyramide.montrer_prochaine_carte()
print(pyramide)
pyramide.montrer_prochaine_carte()
print(pyramide)