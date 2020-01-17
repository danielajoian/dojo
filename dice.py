import random
from random import randint


Attacker = 3
ad1 = randint(1,6)
ad2 = randint(1,6)
ad3 = randint(1,6)

Deffender = 2
dd1 = randint(1,6)
dd2 = randint(1,6)

i = 0
while i < 10:
    i +=1
    print("Round: ", i)
    ad1 = randint(1,6)
    ad2 = randint(1,6)
    ad3 = randint(1,6)
    print("Attacker :", ad1, "-", ad2, "-", ad3)
    dd1 = randint(1,6)
    dd2 = randint(1,6)
    print("Deffender :", dd1, "-", dd2)
    print("\n")
    
