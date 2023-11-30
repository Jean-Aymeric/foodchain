def getAnimalAndIndexFromFile(fileName: str) -> (dict, dict):
    with open(fileName, "r") as file:
        animalIndex = {}
        indexAnimal = {}
        nbAnimals = int(file.readline())
        animalsList = file.readline().split()
        for i in range(nbAnimals):
            animalIndex[animalsList[i]] = i
            indexAnimal[i] = animalsList[i]
        file.close()
        return animalIndex, indexAnimal


def listCharToListInt(listChar: list[str]) -> list[int]:
    listInt = []
    for i in range(len(listChar)):
        listInt.append(int(listChar[i]))
    return listInt


def getWhoEatWhoFromFile(fileName: str) -> list[list[int]]:
    with open(fileName, "r") as file:
        whoEatWho = []
        nbAnimals = int(file.readline())
        file.readline()
        for i in range(nbAnimals):
            whoEatWho.append(listCharToListInt(file.readline().split()))
        file.close()
        return whoEatWho
