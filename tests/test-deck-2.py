import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Deck import Deck

deck = Deck()
print(deck)
deck.montrer()
print(deck)
deck.melanger()
#print(deck)
print(deck.tirer())
print(deck)
print(deck.tirer())
print(deck)