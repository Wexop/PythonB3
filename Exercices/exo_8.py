import random

nb = 0
find = False

res = random.randint(1, 50)

while not find:
    number = int(input('Choisir un chiffre entre 1 et 50 :'))
    nb += 1
    if number > res:
        print("C'est moins !")
    elif number < res:
        print("C'est plus !")
    elif number == res:
        find = True

print("Gagné !!")
print("Nombre de tentatives : ", nb)
