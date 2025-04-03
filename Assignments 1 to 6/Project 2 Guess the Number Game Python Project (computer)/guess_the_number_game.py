import random
def guess():
    random_mumber = random.randint(1,10)
    guess = 0
    while guess != random_mumber:
        guess =int(input(f'Guess a number between 1 and 10: '))
        if guess < random_mumber:
            print("Soory guess again. It's too low")
        elif guess > random_mumber:
            print ("Soory guess again. It,s too high")

    print (f'Congrats! you have guessed the number {random_mumber} correctly')
guess()