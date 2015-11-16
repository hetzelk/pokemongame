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
    multiplayerchoice = str(input("Select: "))
    if multiplayerchoice == "1":
        return 1
    elif multiplayerchoice == "2":
        return 2
    else:
        print("Please enter the right option. 1 or 2? ")
        print("")
        return multiplayer()

def difficulty():
    print("Please select a difficulty.")
    print("[1]00, Health")
    print("[2]00, Health")
    print("[3]00, Health")
    difchoice = str(input("Level 1, 2, or 3? "))

    if difchoice == "1":
        return difficulty1   
    elif difchoice == "2":
        return difficulty2
    elif difchoice == "3":
        return difficulty3
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
        self.difficulty = difficulty
        self.pokemon = 0
        self.name1 = 0
        self.name2 = 0
        self.name3 = 0
        self.pokedict = 0
        self.pokechoice = 0
        self.health = 0
        self.battlehealth = 0
        self.move1name = 0
        self.move2name = 0
        self.move3name = 0

    def getplayername(self):
        if multiplayer == 1:
            self.playername = input("Please enter your name. ").title()
        else:
            self.playername = input("Player 1 enter your name. ").title()

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
        self.move1name = pokemon['move1name']
    def getmove2(self):
        pokemon = self.pokedict
        self.move2name = pokemon['move2name']
    def getmove3(self):
        pokemon = self.pokedict
        self.move3name = pokemon['move3name']


    def attack(self, other):
        pokemon = self.pokedict
        
        print(self.playername, "current health is:", self.battlehealth)
        print("[1]", self.move1name)
        print("[2]", self.move2name)
        print("[3]", self.move3name)
        attacks = str(input("Select a move: "))

        if attacks == "1":
            print(self.playername, "used", self.move1name)
            damage1 = pokemon['move11']
            damage2 = pokemon['move12']
            damage = random.randint(damage1, damage2)
            movename = pokemon['move1name']
            other.battlehealth -= damage
            print(self.playername,"attacked with",movename,"dealing",damage,"damage.")

        elif attacks == "2":
            print(self.playername, "used", self.move2name)
            damage1 = pokemon['move21']
            damage2 = pokemon['move22']
            damage = random.randint(damage1, damage2)
            movename = pokemon['move2name']
            other.battlehealth -= damage
            print(self.playername,"attacked with",movename,"dealing",damage,"damage.")

        elif attacks == "3":
            print(self.playername, "used", self.move3name)
            health1 = pokemon['move31']
            health2 = pokemon['move32']
            health = random.randint(health1, health2)
            movename = pokemon['move3name']
            self.battlehealth += health
            print(self.playername,"used",movename,"adding",health,"health.")

        elif attacks != "1" or "2" or "3":
            print("Please enter a correct choice.")
            return self.attack(other)

class Enemy(Character):
    def __init__(self, multiplayer, difficulty):
        self.playername = 0
        self.multiplayer = multiplayer
        self.difficulty = difficulty
        self.pokemon = 0
        self.name1 = 0
        self.name2 = 0
        self.name3 = 0
        self.pokedict = 0
        self.pokechoice = 0
        self.health = 0
        self.battlehealth = 0
        self.move1name = 0
        self.move2name = 0
        self.move3name = 0

    def getplayername(self):
        if multiplayer == 1:
            self.playername = "Computer"
        else:
            self.playername = input("Player 2 enter your name. ").title()

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

        if self.multiplayer ==2:
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
        else:
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
        self.move1name = pokemon['move1name']
    def getmove2(self):
        pokemon = self.pokedict
        self.move2name = pokemon['move2name']
    def getmove3(self):
        pokemon = self.pokedict
        self.move3name = pokemon['move3name']


    def attack(self, other):
        pokemon = self.pokedict
        if self.multiplayer == 1:
            print(self.playername, "current health is:", self.battlehealth)

            attacks = random.randint(1,100)
            healpercent = self.health * .25

            if self.battlehealth <= healpercent:
                if attacks >= 65:
                    print(self.playername, "used", self.move3name)
                    health1 = pokemon['move31']
                    health2 = pokemon['move32']
                    health = random.randint(health1, health2)
                    movename = pokemon['move3name']
                    self.battlehealth += health
                    print(self.playername,"used",movename,"adding",health,"health.")
                elif attacks >= 25:
                    print(self.playername, "used", self.move2name)
                    damage1 = pokemon['move21']
                    damage2 = pokemon['move22']
                    damage = random.randint(damage1, damage2)
                    movename = pokemon['move2name']
                    other.battlehealth -= damage
                    print(self.playername,"attacked with",movename,"dealing",damage,"damage.")
                elif attacks >= 1:
                    print(self.playername, "used", self.move1name)
                    damage1 = pokemon['move11']
                    damage2 = pokemon['move12']
                    damage = random.randint(damage1, damage2)
                    movename = pokemon['move1name']
                    other.battlehealth -= damage
                    print(self.playername,"attacked with",movename,"dealing",damage,"damage.")
            else:
                if attacks >= 85:
                    print(self.playername, "used", self.move3name)
                    health1 = pokemon['move31']
                    health2 = pokemon['move32']
                    health = random.randint(health1, health2)
                    movename = pokemon['move3name']
                    self.battlehealth += health
                    print(self.playername,"used",movename,"adding",health,"health.")
                elif attacks >= 50:
                    print(self.playername, "used", self.move2name)
                    damage1 = pokemon['move21']
                    damage2 = pokemon['move22']
                    damage = random.randint(damage1, damage2)
                    movename = pokemon['move2name']
                    other.battlehealth -= damage
                    print(self.playername,"attacked with",movename,"dealing",damage,"damage.")
                elif attacks >= 1:
                    print(self.playername, "used", self.move1name)
                    damage1 = pokemon['move11']
                    damage2 = pokemon['move12']
                    damage = random.randint(damage1, damage2)
                    movename = pokemon['move1name']
                    other.battlehealth -= damage
                    print(self.playername,"attacked with",movename,"dealing",damage,"damage.")

        else:
            print(self.playername, "current health is:", self.battlehealth)
            print("[1]", self.move1name)
            print("[2]", self.move2name)
            print("[3]", self.move3name)
            attacks = str(input("Select a move: "))

            if attacks == "1":
                print(self.playername, "used", self.move1name)
                damage1 = pokemon['move11']
                damage2 = pokemon['move12']
                damage = random.randint(damage1, damage2)
                movename = pokemon['move1name']
                other.battlehealth -= damage
                print(self.playername,"attacked with",movename,"dealing",damage,"damage.")

            elif attacks == "2":
                print(self.playername, "used", self.move2name)
                damage1 = pokemon['move11']
                damage2 = pokemon['move12']
                damage = random.randint(damage1, damage2)
                movename = pokemon['move2name']
                other.battlehealth -= damage
                print(self.playername,"attacked with",movename,"dealing",damage,"damage.")

            elif attacks == "3":
                print(self.playername, "used", self.move3name)
                health1 = pokemon['move31']
                health2 = pokemon['move32']
                health = random.randint(health1, health2)
                movename = pokemon['move3name']
                self.battlehealth += health
                print(self.playername,"used",movename,"adding",health,"health.")

            elif attacks != "1" or "2" or "3":
                print("Please enter a correct choice.")
                return self.attack(other)







def startbattle(player, enemy):
    print("Rival wants to battle!")
    print("Rival sent", enemy.pokemon, "!")


    while player.battlehealth > 0 and enemy.battlehealth > 0:
        input("Hit enter to Continue. ")
        os.system("cls")
        showpokemonascii()
        print(player.pokemon, "                     ", enemy.pokemon)
        print("{0}, {1}/{2} Health - {3}, {4}/{5} Health".format(player.playername,player.battlehealth,player.health,enemy.playername,enemy.battlehealth,enemy.health))

        print("")
        player.attack(enemy)
        if enemy.battlehealth <= 0:
            print("")
            print(enemy.playername, "you have 0 health!")
            break
            

        print("")
        enemy.attack(player)
        if player.battlehealth <= 0:
            print("")
            print(player.playername, "you have 0 health!")
            break

    if player.battlehealth > 0:
        print("")
        print("{0} you were defeated by {1}!".format(enemy.playername,player.playername))
        print("")
    if enemy.battlehealth > 0:
        print("")
        print("{0} you were defeated by {1}!".format(player.playername,enemy.playername))
        print("")


def showintro():
    print("Welcome to the pokemon world.")
    print("There are multiple difficulty levels.")
    print("You can face the computer or a rival.")
    print("You take turns with your opponent.")
    print("You have 3 different moves you can choose from.")
    print("There's 3 moves, 2 attacks and 1 heal.")
    print("Every time you call a move, the value changes.")
    print("")



def main():
    os.system("cls")
    showpokemonascii()
    showintro()

    player = Player(multiplayer, difficulty)
    enemy = Enemy(multiplayer, difficulty)

    player.getplayername()

    player.getnamechoices(),player.pokemonchoice(),player.gethealth(),player.getmove1(),player.getmove2(),player.getmove3()
    print(player.playername,"starting Health: ",player.health)
    print(player.playername,"Move 1:",player.move1name,"- Move 2:",player.move2name,"- Move 3:",player.move3name)
    print("")

    enemy.getplayername(),enemy.getnamechoices(),enemy.pokemonchoice(),enemy.gethealth(),enemy.getmove1(),enemy.getmove2(),enemy.getmove3()
    print(enemy.playername,"starting Health: ",enemy.health)
    print(enemy.playername,"Move 1:",enemy.move1name,"- Move 2:",enemy.move2name,"- Move 3:",enemy.move3name)
    print("")
    print("")
    print("")
    startbattle(player, enemy)


if __name__ == '__main__':
    os.system("cls")
    main()




