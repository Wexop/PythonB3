f = open('exo6.txt', 'a')


def write():
    try:
        sentence = input('Ecrit quelque chose : ')

        f.writelines(str(sentence) + '\n')
        print('Enregistré !')
        res = input('Continuer ? (OUI, NON)')
        if (res == 'OUI'):
            write()
        else:
            f.close()
            print('Terminé')
    except:
        print('Erreur')


write()
