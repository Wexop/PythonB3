longueur = int(input('Longueur du rectangle : '))
largeur = int(input('Largeur du rectangle : '))


def getAir(long, larg):
    air = long * larg
    print('air : ', air)
    return air


def getPerimetre(long, larg):
    perimetre = (long * 2) + (larg * 2)
    print('perimetre : ', perimetre)
    return perimetre


def forme(long, larg):
    if long > 0 and larg > 0:
        print('Carré de', long, 'x', larg)
        for i in range(long):
            print('- ' * larg)
    else:
        print('carré trop petit')


getAir(longueur, largeur)
getPerimetre(longueur, largeur)
forme(longueur, largeur)
