
# Unpack - Python allows for unpacking.

# first, last = input("What's your name? ").split(" ")
# print(f"hello, {first}")

def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = [100,50,25]
print(total(coins[0],coins[1],coins[2]), "Knuts")

galleons, sickles, knuts = [100,50,25]
print(total(galleons, sickles, knuts), "Knuts")

# Power of unpacking lists
coins = [100,50,25]
print(total(*coins), "Knuts")

# Power of unpacking dictionary
coins = {"galleons": 100,"sickles": 50,"knuts": 25}
print(total(**coins), "Knuts")



def f(*args, **kwargs):
    print("Positional:", kwargs)
    
f(galleons=100,sickles= 50,knuts=25)