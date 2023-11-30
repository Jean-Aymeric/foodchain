def getAnimalAndIndexFromFile(fileName: str) -> (dict, dict):
    with open(fileName, "r") as file:
        animalsIndex = {}
        indexAnimals = {}
        nbAnimals = int(file.readline())
        animalsList = file.readline().split()
        for i in range(nbAnimals):
            animalsIndex[animalsList[i]] = i
            indexAnimals[i] = animalsList[i]
        file.close()
        return animalsIndex, indexAnimals


def listCharToListInt(listChar: list[str]) -> list[int]:
    listInt = []
    for i in range(len(listChar)):
        listInt.append(int(listChar[i]))
    return listInt


def getWhoEatWhoFromFile(whoEatWho: list[list[int]], fileName: str) -> list[list[int]]:
    with open(fileName, "r") as file:
        nbAnimals = int(file.readline())
        file.readline()
        for i in range(nbAnimals):
            whoEatWho.append(listCharToListInt(file.readline().split()))
        file.close()
        return whoEatWho


def getAnimalsEatWho(whoEatWho: list[list[int]], animalsIndex: dict, indexAnimals: dict) -> dict:
    animalsEatWho = {}
    for animalIndex in animalsIndex.values():
        animalsEaten = []
        for index, value in enumerate(whoEatWho[animalIndex]):
            if value == 1:
                animalsEaten.append(indexAnimals[index])
        animalsEatWho[indexAnimals[animalIndex]] = animalsEaten
    return animalsEatWho


def getAnimalsEatenByWho(whoEatWho: list[list[int]], animalsIndex: dict, indexAnimals: dict) -> dict:
    animalsEatWho = {}
    for animalIndex in animalsIndex.values():
        animalsEaten = []
        for index, value in enumerate(whoEatWho[animalIndex]):
            if value == -1:
                animalsEaten.append(indexAnimals[index])
        animalsEatWho[indexAnimals[animalIndex]] = animalsEaten
    return animalsEatWho
