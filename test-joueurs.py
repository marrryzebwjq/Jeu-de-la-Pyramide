from Deck import Deck
from Joueur import *

d = Deck()
d.melanger()
print(d)
j = Joueur("Bob")
print(j.nom)
j.recevoir_main(d, 5)
print(j.main)
print("aaaaaaa",j.main.show_all())
print(j.main)
print(j)
j.main.hide_all()
j.main.select(2)
print(j.main)