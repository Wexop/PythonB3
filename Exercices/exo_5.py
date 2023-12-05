def nbChar(nb, phrase):
    if (nb == len(phrase)):
        print('nb de caratère : ', nb)
    else:
        nbChar(nb + 1, phrase)


nbChar(0, "Salut ça va moi ça va bien oui")
