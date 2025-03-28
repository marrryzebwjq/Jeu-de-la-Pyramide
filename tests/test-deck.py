import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Carte import Carte
from Deck import Deck

cartes = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
d = Deck(custom_cards=cartes)
print(d)
d.melanger()
print(d)
print(d.tirer())
print(d)
print(d.tirer())
print(d)