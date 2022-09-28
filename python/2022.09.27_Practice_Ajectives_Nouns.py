adjectives = ["beste", "liebenswuerdigste", "schoenste", "groesste"]  # Bsp - kann beliebig erweitert werden
nouns = ["Mensch", "Hecht", "Freund", "Kumpel", "Programmierer"]  # Bsp - kann beliebig erweitert werden

# Bsp-Ausgabe für die Eingabe 2
# Du bist der beste Freund
# Du bist der groesste Kumpel

numberOfCombinations = 0

for adjective in adjectives:
    for noun in nouns:
        numberOfCombinations += 1
        print(f"Du bist der {adjective} {noun}!")

print(f"\nNumber of combinations: {numberOfCombinations}")
