from Carte import Carte

cartes = [Carte(valeur, couleur, custom_val=True) for valeur in range(1, 100) for couleur in Carte.COULEURS]  # 4 cartes par valeur
print(cartes[0])
print(cartes[395])