import random

n = random.randrange(1,10)
guess = 0
while guess != n:
    guess = int(input('Gess a number'))
    if guess<n:
        print('Guess is smaller')
    elif guess>n:
        print('Guess is larger')
    else:print('Currect guess')
        