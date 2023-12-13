class Carte :

    def __init__(self,manaCout):

        self.__manaCout = manaCout

    def getManacout(self):
        return self.__manaCout
    
class Mage:
    
    def __init__(self,nom,pv,mana,main,defausse):

        self.__nom = nom
        self.__pv = pv
        self.__mana = mana
        self.__main = main
        self.__defausse = defausse

    def getNom(self):
        return self.__nom
    def getPv(self):
        return self.__pv
    def getMana(self):
        return self.__mana
    def getMain(self):
        return self.__main
    def getDefausse(self):
        return self.__defausse
    def Stats(self):
        print(self.__nom)
        print(self.__pv,"PV", self.__mana,"MANA\n", "vous avez", self.__main, "carte en main et", self.__defausse,"carte dans votre defausse")
    def regenMana(self):
        self.getMana += 5
        print(self.__mana,"MANA")
    
class Cristal(Carte):

    def __init__(self, nom, valeur,manaCout):

        self.__nom = nom
        self.__valeur = valeur
        self.__manaCout = manaCout


    def getValeur(self):
        return self.__valeur
    def getNom(self):
        return self.__nom
    def getManacout(self):
        return self.__manaCout
    def activeCristal(self,terrain):
        terrain = True 
        while terrain == True : 
            Mage.getMana += self.getValeur
            print("vous recupéré ",self.getValeur ,"point de mana")

class Creature(Carte):

    def __init__(self,nom,pv,atk,manaCout):

        self.__nom = nom
        self.__pv = pv
        self.__atk = atk
        self.__manaCout = manaCout

    def getPv(self):
        return self.__pv
    def getAtk(self):
        return self.__atk
    def getNom(self):
        return self.__nom
    def getManacout(self):
        return self.__manaCout
    def activeCreature(self,terrain):
        terrain = True
    
class Blast(Carte):

    def __init__(self,nom,atk, manaCout):

        self.__nom = nom
        self.__atk = atk
        self.__manaCout = manaCout

    def getAtk(self):
        return self.__atk
    def getNom(self):
        return self.__nom
    def getManacout(self):
        return self.__manaCout
    def ativeBlast(self):
        Mage.getPv -= self.getAtk
        # print("vous avez fait", self.getAtk "point de degat au mage")
    
choixNom = input("comment voulez vous nommer votre mage ?\n")


monMage = Mage(choixNom,100,10,3,0)
monCristal = Cristal("cristal",5,0)
maCreature = Creature("Creature", 20, 25,10)
monBlast = Blast("Blast", 40,15)

monMage.Stats()

choixJeu = int(input("que faire :\n - jouer une carte ? [1]\n - récuperé ses points de mana ? [2]\n - Ataquer ? [3]\n"))

if choixJeu == 1 :
    choixCarte = int(input("quel carte vouler vous jouer :\n - mon Cristal ? [1]\n - ma Creature ? [2]\n - mon Blast ? [3]\n"))
    if choixCarte == 1 :
        monCristal.activeCristal()
    elif choixCarte == 2 : 
        maCreature.activeCreature()
    else : 
        monBlast.ativeBlast()
elif choixJeu == 2 : 
    monMage.regenMana
    
else : 
    ChoixAtk = int(input("qui attaquer ? :\n"))
