# import random
from random import choice, randint, shuffle

for i in range(100):
    coin = choice(["heads", "tails"])
    print(coin)
    



p = randint(1,10)
print(p)



cards = ["Jack", "Queen", "King"]
shuffle(cards)
for card in cards:
    print(card)
    




import statistics
print(statistics.mean([2.2,6.2]))



