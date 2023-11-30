import foodchain

animalsIndex, indexAnimals = foodchain.getAnimalAndIndexFromFile("chaine.txt")
whoEatWho = []
foodchain.getWhoEatWhoFromFile(whoEatWho, "chaine.txt")
animalsEatWho = foodchain.getAnimalsEatWho(whoEatWho, animalsIndex, indexAnimals)
print(animalsEatWho)
animalsEatenByWho = foodchain.getAnimalsEatenByWho(whoEatWho, animalsIndex, indexAnimals)
print(animalsEatenByWho)
