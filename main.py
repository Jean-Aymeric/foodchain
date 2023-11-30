import foodchain

animalsIndex, indexAnimals = foodchain.getAnimalAndIndexFromFile("chaine.txt")
whoEatWho = foodchain.getWhoEatWhoFromFile("chaine.txt")
print(whoEatWho)