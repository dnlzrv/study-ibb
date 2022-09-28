adjectives = ["beste", "liebenswuerdigste", "schoenste", "groesste"]
nouns = ["Mensch", "Hecht", "Freund", "Kumpel", "Programmierer"]

numberOfCombinations = 0

for adjective in adjectives:
    for noun in nouns:
        numberOfCombinations += 1
        print(f"Du bist der {adjective} {noun}!")

print(f"\nNumber of combinations: {numberOfCombinations}")
