from Carte import Carte
import random

for c in Carte.COULEURS :
    print(c)
    print(Carte.COULEURS[c])


for i in range(1, 14) :
    c = random.choice(list(Carte.COULEURS.keys()))
    print(Carte(i, c))

print("---")
c = Carte(1, "coeur")
print(c.montrer())
print(c)
c2 = Carte(1, "trefle")
print(c2)
print(c2.same_value(c))
print(c2.same_value(Carte(2,"trefle")))

print(c.cacher())

print(c.montrer_une_fois())
print(c)