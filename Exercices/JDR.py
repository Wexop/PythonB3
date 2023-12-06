class Personnage:

    def __init__(self, nom, hp, hpMax, dmg, defense, cacthPhrase):
        self.__name = nom
        self.__hp = hp
        self.__hpMax = hpMax
        self.__dmg = dmg
        self.__defense = defense
        self.__cacthPhrase = cacthPhrase

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value
        if self.__hp > self.hpMax:
            self.__hp = self.hpMax
        elif self.__hp < 0:
            self.__hp = 0
            print(f'{self.name} est mort !')

    @property
    def hpMax(self):
        return self.__hpMax

    @property
    def dmg(self):
        return self.__dmg

    @property
    def defense(self):
        return self.__defense

    @property
    def cacthPhrase(self):
        return self.__cacthPhrase

    def attaquer(self, perso):
        if self.hp <= 0:
            print(f"{self.name} ne peut pas attaquer, il est mort")
            return
        perso.hp = self.__dmg - perso.defense
        print(f"{self.name} attaque {perso.name}, il lui reste {perso.hp} hp !")

    def sePresenter(self):
        print(f"{self.__name} : {self.cacthPhrase}")


class Guerrier(Personnage):

    def __init__(self, name):
        Personnage.__init__(self, name, 100, 100, 30, 20, "KAAAAAAAAAARMINE COOOOOOOOORP")

    def crieDeGuerre(self):
        print(f"{self.__name} : {self.cacthPhrase}")


class Clerc(Personnage):

    def __init__(self, name):
        Personnage.__init__(self, name, 200, 200, 10, 15, "JE SUIS LE SOIGNEUR")
        self.__heal = 30

    def soigner(self, perso):
        perso.hp += self.__heal
        if (perso.hp > perso.hpMax):
            perso.hp = perso.hpMax
        print(f"{self.name} soigne {perso.name}, il est maintenant à {perso.hp} hp !")


class Paladin(Clerc, Guerrier):

    def __init__(self, name):
        Personnage.__init__(self, name, 250, 250, 20, 40, "DEMACIAAAA")


class Mage(Personnage):

    def __init__(self, name):
        Personnage.__init__(self, name, 75, 75, 70, 20, "BOMBARDATION")
        self.__mana = 200
        self.__manaCost = 20

    @property
    def mana(self):
        return self.__mana

    @property
    def manaCost(self):
        return self.__manaCost

    def jeterSort(self, perso):
        if self.mana - self.manaCost >= 0:
            perso.hp -= self.dmg
            self.hp += self.dmg
            if self.hp <= 0:
                print(f"{self.name} ne peut pas attaquer, il est mort")
                return
            print(f"{self.name} lance un sort sur {perso.name}, il lui reste {perso.hp} hp !")
        else:
            print(f"{self.name} n'a plus de mana !")


class Archer(Guerrier):

    def __init__(self, name):
        Personnage.__init__(self, name, 60, 60, 75, 15, "JE SAPPELLE GROOT")


guerrier = Guerrier("Salope")
mage = Mage("Ziggs")
clerc = Clerc("Soraka")

mage.jeterSort(guerrier)
guerrier.attaquer(mage)
clerc.soigner(mage)
mage.jeterSort(guerrier)
clerc.attaquer(guerrier)
guerrier.attaquer(clerc)
mage.jeterSort(guerrier)
