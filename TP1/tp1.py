player1 = input("saisir le pseudo du joueur 1 : ")
player2 = input("saisir le pseudo du joueur 2 : ")

jeu = True
dic = {"x1":"x1","x2":"x2","x3":"x3","x4":"x4","x5":"x5","x6":"x6","x7":"x7","x8":"x8","x9":"x9" }

gagnant = ""
perdant = ""

print(dic["x1"],dic["x2"],dic["x3"])
print(dic["x4"],dic["x5"],dic["x6"])
print(dic["x7"],dic["x8"],dic["x9"])

def getChoix(player):
    choix = input(player + " choisissez votre case : ")
    try:
        test = dic[choix]
        return choix
    except:
        return getChoix(player)

tour = 0
while jeu:

    if tour %2 == 0:

        can = False
        while not can:
            choix = getChoix(player1)
            if dic[choix] !="o" and dic[choix] != "x":
                can = True
        dic[choix] = "o"

        print(dic["x1"], dic["x2"], dic["x3"])
        print(dic["x4"], dic["x5"], dic["x6"])
        print(dic["x7"], dic["x8"], dic["x9"])

    else:
        can = False
        while not can:
            choix = getChoix(player2)
            if dic[choix] != "o" and dic[choix] != "x":
                can = True
        dic[choix] = "x"

        print(dic["x1"], dic["x2"], dic["x3"])
        print(dic["x4"], dic["x5"], dic["x6"])
        print(dic["x7"], dic["x8"], dic["x9"])

    if (dic["x1"] == "x" and dic["x2"] == "x" ) and dic["x3"] == "x":
        gagnant = player2
        jeu = False
    elif (dic["x1"] == "x" and dic["x5"] == "x" ) and dic["x9"] == "x":
        gagnant = player2
        jeu = False
    elif (dic["x1"] == "x" and dic["x4"] == "x" ) and dic["x7"] == "x":
        gagnant = player2
        jeu = False
    elif (dic["x2"] == "x" and dic["x5"] == "x" ) and dic["x8"] == "x":
        gagnant = player2
        jeu = False
    elif(dic["x3"] == "x" and dic["x6"] == "x" ) and dic["x9"] == "x":
        gagnant = player2
        jeu = False
    elif (dic["x4"] == "x" and dic["x5"] == "x" ) and dic["x6"] == "x":
        gagnant = player2
        jeu = False
    elif (dic["x7"] == "x" and dic["x8"] == "x" ) and dic["x9"] == "x":
        gagnant = player2
        jeu = False
    elif (dic["x7"] == "x" and dic["x5"] == "x" ) and dic["x3"] == "x":
        gagnant = player2
        jeu = False
    elif (dic["x1"] == "o" and dic["x2"] == "o" ) and dic["x3"] == "o":
        gagnant = player1
        jeu = False
    elif (dic["x1"] == "o" and dic["x5"] == "o" ) and dic["x9"] == "o":
        gagnant = player1
        jeu = False
    elif (dic["x1"] == "o" and dic["x4"] == "o") and dic["x7"] == "o":
        gagnant = player1
        jeu = False
    elif (dic["x2"] == "o" and dic["x5"] == "o" ) and dic["x8"] == "o":
        gagnant = player1
        jeu = False
    elif (dic["x3"] == "o" and dic["x6"] == "o" ) and dic["x9"] == "o":
        gagnant = player1
        jeu = False
    elif (dic["x4"] == "o" and dic["x5"] == "o") and dic["x6"] == "o":
        gagnant = player1
        jeu = False
    elif (dic["x7"] == "o" and dic["x8"] == "o") and dic["x9"] == "o":
        gagnant = player1
        jeu = False
    elif (dic["x7"] == "o" and dic["x5"] == "o") and dic["x3"] == "o":
        gagnant = player1
        jeu = False
    tour += 1

    if tour == 9:
        jeu = False




if gagnant == player1:
    perdant = player2
elif gagnant == player2:
    perdant = player1
else:
    gagnant = "="
    perdant = "="

if gagnant == "=":
    print("personne n'a gagné")
else:
    print(gagnant, " a gagner !!", perdant," est un looser")

f = open("resultats.txt" ,"a")
if gagnant == "=":
    f.write("Egalité entre " + player1 + " et "+player2+" !\n")
else:
    f.write(gagnant + " à gagner contre " + perdant + "\n")
f.close()


