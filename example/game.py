import time, os, random
from yourfile import * 



class Starter(object):
    def __init__(self):
        name = str(input("What is your name? "))

        self.name = name
        self.health = 100



    def questionasker(self):

        choice = str(input('A, B, C, D, E, Make your choice. ')).upper()

        if choice == "A":
            print("You chose A")
            return q1   
        if choice == "B":
            print("You chose B")
            return q2
        if choice == "C":
            print("You chose C")
            return q3
        if choice == "D":
            print("You chose D")
            return q4 
        if choice == "E":
            print("You chose E")
            return q5 
        else:
            print("Please try again, ABCDE. ")
            self.questionasker()






def main():
    print("")
    print(star.questionasker())
    print("")
    print("Your name is:",star.name)







star = Starter()
main()





