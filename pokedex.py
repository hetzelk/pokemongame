import random
difficulty1 = {
1:{'Pokemon': 'Balbasaur', 'move1name': 'Tackle', 'move2name': 'Razor', 'move3name': 'Heal', 'health':100, 'move1':random.randint(15,25),'move2':random.randint(5,35),'move3':random.randint(10,20)},
2:{'Pokemon': 'Charmander', 'move1name': 'Scratch', 'move2name': 'Ember', 'move3name': 'Heal', 'health':100, 'move1':random.randint(15,25),'move2':random.randint(5,35),'move3':random.randint(10,20)},
3:{'Pokemon': 'Squirtle', 'move1name': 'Tackle', 'move2name': 'Bubble', 'move3name': 'Heal', 'health':100, 'move1':random.randint(15,25),'move2':random.randint(5,35),'move3':random.randint(10,20)}}

difficulty2 = {
1:{'Pokemon': 'Ivysaur', 'move1name': 'Tackle', 'move2name': 'Razor', 'move3name': 'Heal', 'health':200, 'move1':random.randint(30,50),'move2':random.randint(10,70),'move3':random.randint(20,40)},
2:{'Pokemon': 'Charmeleon', 'move1name': 'Scratch', 'move2name': 'Ember', 'move3name': 'Heal', 'health':200, 'move1':random.randint(30,50),'move2':random.randint(10,70),'move3':random.randint(20,240)},
3:{'Pokemon': 'Wartortle', 'move1name': 'Tackle', 'move2name': 'Bubble', 'move3name': 'Heal', 'health':200, 'move1':random.randint(30,50),'move2':random.randint(10,70),'move3':random.randint(20,40)}}

difficulty3 = {
1:{'Pokemon': 'Venusaur', 'move1name': 'Tackle', 'move2name': 'Razor', 'move3name': 'Heal', 'health':300, 'move1':random.randint(40,75),'move2':random.randint(20,85),'move3':random.randint(30,60)},
2:{'Pokemon': 'Charizard', 'move1name': 'Scratch', 'move2name': 'Ember', 'move3name': 'Heal', 'health':300, 'move1':random.randint(40,75),'move2':random.randint(20,85),'move3':random.randint(30,60)},
3:{'Pokemon': 'Blastoise', 'move1name': 'Tackle', 'move2name': 'Bubble', 'move3name': 'Heal', 'health':300, 'move1':random.randint(40,75),'move2':random.randint(20,85),'move3':random.randint(30,60)}}



"""
balbasaur = {'Pokemon': 'Balbasaur', 'move1': 'Tackle', 'move2': 'Razor', 'move3': 'Heal', 'health':100}
ivysaur =   {'Pokemon': 'Ivysaur', 'move1': 'Tackle', 'move2': 'Razor', 'move3': 'Heal', 'health':200}
venusaur =  {'Pokemon': 'Venusaur', 'move1': 'Tackle', 'move2': 'Razor', 'move3': 'Heal', 'health':300}

charmander = {'Pokemon': 'Charmander', 'move1': 'Scratch', 'move2': 'Ember', 'move3': 'Heal', 'health':100}
charmeleon = {'Pokemon': 'Charmeleon', 'move1': 'Scratch', 'move2': 'Ember', 'move3': 'Heal', 'health':200}
charizard =  {'Pokemon': 'Charizard', 'move1': 'Scratch', 'move2': 'Ember', 'move3': 'Heal', 'health':300}

squirtle =  {'Pokemon': 'Squirtle', 'move1': 'Tackle', 'move2': 'Bubble', 'move3': 'Heal', 'health':100}
wartortle = {'Pokemon': 'Wartortle', 'move1': 'Tackle', 'move2': 'Bubble', 'move3': 'Heal', 'health':200}
blastoise = {'Pokemon': 'Blastoise', 'move1': 'Tackle', 'move2': 'Bubble', 'move3': 'Heal', 'health':300}


in battle messages

 __________________________________________
| RIVAL WILLIAM                            |
| Bulbasaur   Lv5                          |
|      HP 100/100                          |
|                                          |
|                                          |
|                            KEITH         |
|                           SQUIRTLE   Lv5 |
|                               HP 100/100 |
|                                          |
| What will            |   FIGHT       BAG |    -very first
| SQUIRTLE do?         |   POKeMON     RUN |   game screen
|__________________________________________|

----
| RIVAL ____name
| would like to battle!
----
| What will
| SQUIRTLE do?
----
| [1] TACKLE   [2] TAIL WHIP  |PP    35/35       -in game screen
| [3] HEAL                    | type/NORMAL



-A critical hit!


WILD RATTATA
fainted!






print("                                .::;                            ")
print("                              .;:**'                            ")
print("                                                                ")
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



    print(" ____       _                              ")
    print("|  _ \ ___ | | _____ _ __ ___   ___  _ __  ")
    print("| |_) / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ ")
    print("|  __/ (_) |   <  __/ | | | | | (_) | | | |")
    print("|_|   \___/|_|\_\___|_| |_| |_|\___/|_| |_|")
    print("")



"""
