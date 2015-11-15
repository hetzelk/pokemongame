import time, os, random
from pokedex import * 


os.system("cls")

def showpokemonascii():
    print("                                ,.::;                            ")
    print("                              .;****'                            ")
    print("  .:XHHHHk.              db.   .;;.     dH  MX                  ")
    print("oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN       ")
    print("QMMMMMb  'MMX       MMMMMMP !MX' :M~   MMM MMM  .oo. XMMM 'MMM  ")
    print("  `MMMM.  )M> :X!Hk. MMMM   XMM.o'  .  MMMMMMM X?XMMM MMM>!MMP  ")
    print("   'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `' MX MMXXMM   ")
    print("    ~MMMMM~ XMM. .XM XM`'MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP   ")
    print("     ?MMM>  YMMMMMM! MM   `?MMRb.    `'''   !L'MMMMM XM IMMM    ")
    print("      MMMX   'MMMM'  MM       ~%:           !Mh.''' dMI IMMP    ")
    print("      'MMM.                                             IMX     ")
    print("       ~M!M                                             IMP     ")
    print("")

showpokemonascii()

def multiplayer():
    print("Would you like to play against the computer or a rival?")
    print("[1] - Vs. Computer")
    print("[2] - Vs. Rival")
    multiplayerchoice = int(input("Select: "))
    if multiplayerchoice == 1:
        return 1
    elif multiplayerchoice ==2:
        return 2
    else:
        print("Please enter the right option. 1 or 2? ")
        print("")
        return difficulty()

def difficulty():
    print("Please select a difficulty.")
    print("[1]00, Health")
    print("[2]00, Health")
    print("[3]00, Health")
    difchoice = int(input("Level 1, 2, or 3? "))

    if difchoice == 1:
        return difficulty1   
    elif difchoice == 2:
        return difficulty2
    elif difchoice == 3:
        return difficulty3
        """
    elif difchoice == 4:
        return difficulty2
    elif difchoice == 5:
        return difficulty3
    elif difchoice == 10:
        return difficulty2
    elif difchoice == 100:
        return difficulty3"""

    else:
        print("Please enter the right option. 1, 2, or 3? ")
        print("")
        return difficulty()

multiplayer = multiplayer()
difficulty = difficulty()

class Character:
    def __init__(self, health):
        self.battlehealth = 0

    def attack(self, other):
        raise NotImplementedError

class Player(Character):
    def __init__(self, multiplayer, difficulty):
        self.playername = 0
        self.multiplayer = multiplayer
        self.difficulty = difficulty #difficulty1, 2, 3
        self.pokemon = 0 #set this to another variable so the computer can't select the same pokemon as the player.
        self.name1 = 0
        self.name2 = 0
        self.name3 = 0
        self.pokedict = 0
        self.pokechoice = 0
        self.health = 0
        self.battlehealth = 0
        self.move1 = 0
        self.move2 = 0
        self.move3 = 0
        self.move1amount = 0
        self.move2amount = 0
        self.move3amount = 0

    def getplayername(self):
        self.playername = input("Please enter your name. ")

    def getnamechoices(self):
        chardict = self.difficulty
        pokemon1 = chardict[1]
        pokemon2 = chardict[2]
        pokemon3 = chardict[3]

        self.name1 = pokemon1['Pokemon']
        self.name2 = pokemon2['Pokemon']
        self.name3 = pokemon3['Pokemon']

    def pokemonchoice(self):
        chardict = self.difficulty
        pokechoice = 0
        print(self.playername,"make your choice of Pokemon. ")
        print("[1]", self.name1, "- Leaf-Type")
        print("[2]", self.name2, "- Fire-Type")
        print("[3]", self.name3, "- Water-Type")
        pokechoice = str(input("Pokemon 1, 2 or 3. "))

        if pokechoice == "1":
            print("")
            print(self.playername, "picked", self.name1)
            self.pokedict = chardict[1]
            self.pokemon = self.name1
        elif pokechoice == "2":
            print("")
            print(self.playername, "picked", self.name2)
            self.pokedict = chardict[2]
            self.pokemon = self.name2
        elif pokechoice == "3":
            print("")
            print(self.playername, "picked", self.name3)
            self.pokedict = chardict[3]
            self.pokemon = self.name3
        elif pokechoice != "1" or "2" or "3":
            print("Please enter the right option. 1, 2, or 3? ")
            print("")
            return self.pokemonchoice()


    def gethealth(self):
        pokemon = self.pokedict
        self.health = pokemon['health']
        self.battlehealth = pokemon['health']
    def getmove1(self):
        pokemon = self.pokedict
        self.move1 = pokemon['move1name']
    def getmove2(self):
        pokemon = self.pokedict
        self.move2 = pokemon['move2name']
    def getmove3(self):
        pokemon = self.pokedict
        self.move3 = pokemon['move3name']


    def attack(self, other):
        pokemon = self.pokedict
        
        print("Your current health is:", self.battlehealth)
        print("[1]", self.move1)
        print("[2]", self.move2)
        print("[3]", self.move3)
        attacks = int(input("Select a move: "))

        if attacks == 1:
            print(self.playername, "used", self.move1)
            damage = pokemon['move1']
            movename = pokemon['move1name']
            other.battlehealth -= damage
            print(self.playername,"attacked with",movename,"dealing",damage,"damage.")

        elif attacks == 2:
            print(self.playername, "used", self.move2)
            damage = pokemon['move2']
            movename = pokemon['move2name']
            other.battlehealth -= damage
            print(self.playername,"attacked with",movename,"dealing",damage,"damage.")

        elif attacks == 3:
            print(self.playername, "used", self.move3)
            health = pokemon['move3']
            movename = pokemon['move3name']
            self.battlehealth += health
            print(self.playername,"used",movename,"adding",health,"health.")

        else:
            print("Please enter a correct choice.")
            return self.attack()


class Enemy(Character):
    def __init__(self, multiplayer, difficulty):
        self.playername = 0
        self.multiplayer = multiplayer
        self.difficulty = difficulty #difficulty1, 2, 3
        self.pokemon = 0
        self.name1 = 0
        self.name2 = 0
        self.name3 = 0
        self.pokedict = 0
        self.pokechoice = 0
        self.health = 0
        self.battlehealth = 0
        self.move1 = 0
        self.move2 = 0
        self.move3 = 0
        self.move1amount = 0
        self.move2amount = 0
        self.move3amount = 0

    def getplayername(self):
        if multiplayer == 1:
            self.playername = "Computer"
        else:
            self.playername = input("Please enter your name. ")

    def getnamechoices(self):
        chardict = self.difficulty
        pokemon1 = chardict[1]
        pokemon2 = chardict[2]
        pokemon3 = chardict[3]

        self.name1 = pokemon1['Pokemon']
        self.name2 = pokemon2['Pokemon']
        self.name3 = pokemon3['Pokemon']

    def pokemonchoice(self):
        chardict = self.difficulty

        pokechoice = random.randint(1,3)

        if pokechoice == 1:
            print("")
            print(self.playername, "picked", self.name1)
            self.pokedict = chardict[1]   
            self.pokemon = self.name1
        elif pokechoice == 2:
            print("")
            print(self.playername, "picked", self.name2)
            self.pokedict = chardict[2]
            self.pokemon = self.name2
        elif pokechoice == 3:
            print("")
            print(self.playername, "picked", self.name3)
            self.pokedict = chardict[3]
            self.pokemon = self.name3


    def gethealth(self):
        pokemon = self.pokedict
        self.health = pokemon['health']
        self.battlehealth = pokemon['health']
    def getmove1(self):
        pokemon = self.pokedict
        self.move1 = pokemon['move1name']
        self.move1amount = pokemon['move1']
    def getmove2(self):
        pokemon = self.pokedict
        self.move2 = pokemon['move2name']
        self.move2amount = pokemon['move2']
    def getmove3(self):
        pokemon = self.pokedict
        self.move3 = pokemon['move3name']
        self.move3amount = pokemon['move3']


    def attack(self, other):
        pokemon = self.pokedict
        print(self.playername, "current health is:", self.battlehealth)

        attacks = random.randint(1,100)
        healpercent = self.health * .25

        if self.battlehealth <= healpercent:
            if attacks >= 65:
                print(self.playername, "used", self.move3)
                health = pokemon['move3']
                movename = pokemon['move3name']
                self.battlehealth += health
                print(self.playername,"used",movename,"adding",health,"health.")
            elif attacks >= 25:
                print(self.playername, "used", self.move2)
                damage = pokemon['move2']
                movename = pokemon['move2name']
                other.battlehealth -= damage
                print(self.playername,"attacked with",movename,"dealing",damage,"damage.")
            elif attacks >= 1:
                print(self.playername, "used", self.move1)
                damage = pokemon['move1']
                movename = pokemon['move1name']
                other.battlehealth -= damage
                print(self.playername,"attacked with",movename,"dealing",damage,"damage.")
        else:
            if attacks >= 85:
                print(self.playername, "used", self.move3)
                health = pokemon['move3']
                movename = pokemon['move3name']
                self.battlehealth += health
                print(self.playername,"used",movename,"adding",health,"health.")
            elif attacks >= 50:
                print(self.playername, "used", self.move2)
                damage = pokemon['move2']
                movename = pokemon['move2name']
                other.battlehealth -= damage
                print(self.playername,"attacked with",movename,"dealing",damage,"damage.")
            elif attacks >= 1:
                print(self.playername, "used", self.move1)
                damage = pokemon['move1']
                movename = pokemon['move1name']
                other.battlehealth -= damage
                print(self.playername,"attacked with",movename,"dealing",damage,"damage.")









def battle(player, enemy):
    print("Rival wants to battle!")
    print("Rival sent", enemy.pokemon, "!")


    while player.battlehealth > 0 and enemy.battlehealth > 0:
        time.sleep(2.0)
        os.system("cls")
        showpokemonascii()
        
        print("")
        #displaygba()
        player.attack(enemy)
        if enemy.battlehealth <= 0:
            print(enemy.playername, "you have 0 health!")
            break
            winner()

        print("")
        enemy.attack(player)
        if player.battlehealth <= 0:
            print(player.playername, "you have 0 health!")
            break
            winner()
    



def winner():
    player = Player(multiplayer, difficulty)
    enemy = Enemy(multiplayer, difficulty)

    if player.battlehealth > 0:
        print(player.playername,"you were defeated by",enemy.playername,"!")
        print("")
    if enemy.battlehealth > 0:
        print(enemy.playername,"you were defeated by",player.playername,"!")
        print("")


def intro():
    print("Welcome to the pokemon world.")
    print("There are 3 difficulty levels.")
    print("You can face the computer or a rival.")
    print("You take turns with your opponent.")
    print("You have 3 different moves you can choose from.")
    print("")
    print("")



def main():
    os.system("cls")
    showpokemonascii()
    intro()

    player = Player(multiplayer, difficulty)
    enemy = Enemy(multiplayer, difficulty)

    player.getplayername()
    print("")
    print("")
    player.getnamechoices(),player.pokemonchoice(),player.gethealth(),player.getmove1(),player.getmove2(),player.getmove3()
    print("Starting Health: ",player.health, player.battlehealth)
    print(player.playername,"Move 1:",player.move1,"- Move 2:",player.move2,"- Move 3:",player.move3)
    print("")

    enemy.getplayername(),enemy.getnamechoices(),enemy.pokemonchoice(),enemy.gethealth(),enemy.getmove1(),enemy.getmove2(),enemy.getmove3()
    print("Computer starting Health: ",enemy.health)
    print(enemy.playername,"Move 1:",enemy.move1,"- Move 2:",enemy.move2,"- Move 3:",enemy.move3)
    print("")
    print("")
    print("")
    battle(player, enemy)
    winner()

def displaygba():
    player = Player(multiplayer, difficulty)
    enemy = Enemy(multiplayer, difficulty)
    print(" __________________________________________")
    print("| RIVAL {0}                                |".format(enemy.playername))#rival name
    print("| {0}   Lv5                                |".format(enemy.pokemon))#rival pokemon
    print("|      HP {0}/{1}                          |".format(enemy.battlehealth, enemy.health))#hp of starting hp
    print("|                                          |")
    print("|                                          |")
    print("|                            {0}         |".format(player.playername))#name
    print("|                           {0}   Lv5 |".format(player.pokemon))#pokemon
    print("|                               HP {0}/{1} |".format(player.battlehealth, player.health))#hp of starting hp
    print("|                                          |")
    print("| [1] {0}   [2] {1} | PP     35/35|".format(player.move1name, player.move2name))#move1 move2
    print("| [3] {0}                   |  type/NORMAL|".format(player.move3name))#move3
    print("|__________________________________________|")




if __name__ == '__main__':
    os.system("cls")
    main()




