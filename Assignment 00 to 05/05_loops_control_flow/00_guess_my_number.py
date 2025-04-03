import random
def guess():
    random_mumber = random.randint(1,99)
    guess = 0
    print("I am thinking of a number between 1 and 99...")
    while guess != random_mumber:
        guess =int(input(f'Guess a new number: '))
        if guess < random_mumber:
            print("Soory guess again. It's too low")
        elif guess > random_mumber:
            print ("Soory guess again. It's too high")

    print (f'Congrats! you have guessed the number {random_mumber} correctly')
guess()
