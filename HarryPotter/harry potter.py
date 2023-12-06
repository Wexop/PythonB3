import requests

maisons = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]


class Personnage:

    def __init__(self, name, birthday, wand):
        self.name = name
        self.birthday = birthday
        self.wand = wand


def getCharactersFromHouse(house):
    characters = requests.get(f"https://hp-api.onrender.com/api/characters/house/{house.lower()}").json()
    f = open(house, 'w')

    for i in range(len(characters)):
        char = characters[i]
        newChar = Personnage(char['name'], char['dateOfBirth'], char['wand'])
        f.write(f'{newChar.name} / {newChar.birthday} / {newChar.wand} \n')

    f.close()


for i in range(len(maisons)):
    house = maisons[i]
    getCharactersFromHouse(house)
