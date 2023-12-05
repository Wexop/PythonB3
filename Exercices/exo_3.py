longueur = int(input('Longueur du rectangle : '))
largeur = int(input('Largeur du rectangle : '))

air = longueur * largeur
perimetre = (largeur * 2) + (longueur * 2)

print('air : ', air)
print('perimetre : ', perimetre)
if longueur > 0 and largeur > 0:
    print('Carré de', longueur, 'x', largeur)
    for i in range(longueur):
        print('- ' * largeur)
