import random
import matplotlib.pyplot as plt

def scrysort(cardsindeck):
    scrys = 0
    decklist = [i for i in range(cardsindeck)]
    random.shuffle(decklist)

    for targetcard in range(1,cardsindeck):
        while decklist[0] != targetcard:
            if decklist[1] != targetcard:
                decklist.append(decklist.pop(1))
            decklist.append(decklist.pop(0))
            scrys += 1
        while decklist[1] != targetcard - 1:
            decklist.append(decklist.pop(1))
            scrys += 1
        decklist.append(decklist.pop(1))
        decklist.append(decklist.pop(0))
        scrys += 1
    return scrys


decksize = [i for i in range(0,101,10)]
avgscry = []

for n in decksize:
    scrysum = 0
    for count in range(10):
        scrysum += scrysort(n)
    avgscry.append(scrysum/10)

plt.plot(decksize,avgscry)
plt.xlabel("Deck Size, no I said DECK size")
plt.ylabel("Average Number of 'Scry 2s' to Sort")
plt.show()
