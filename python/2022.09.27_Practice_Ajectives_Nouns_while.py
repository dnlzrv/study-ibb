adjectives = ["beste", "liebenswuerdigste", "schoenste", "groesste"]
nouns = ["Mensch", "Hecht", "Freund", "Kumpel", "Programmierer"]

numberOfCombinations = 0

adjectiveIndex = 0

while adjectiveIndex < len(adjectives) :
    nounIndex = 0
    while nounIndex < len(nouns) :
        numberOfCombinations += 1
        print(f"Du bist der {adjectives[adjectiveIndex]} {nouns[nounIndex]}!")
        nounIndex += 1    
    adjectiveIndex += 1

print(f"\nNumber of combinations: {numberOfCombinations}")
