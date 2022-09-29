
adjektive = ["beste", "liebenswuerdigste", "schoenste", "groesste"]
nomen = ["Mensch", "Hecht", "Freund", "Kumpel", "Programmierer"]

import random

zufahlzahl = int(input("Geben sie bite eine ganze zahl:"))

totalCombin =0
while totalCombin < zufahlzahl:
    adjIndex = random.randint(0,3)
    nomIndex = random.randint(0,4)
    total = adjektive[adjIndex] + " " + nomen[nomIndex]
    print("Du bist der", total)
    totalCombin += 1


       