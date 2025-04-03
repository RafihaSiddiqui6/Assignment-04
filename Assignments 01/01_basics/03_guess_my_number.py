import random
def guess():
    secret_mumber = random.randint(1,10)
    guess = 0
    while guess != secret_mumber:
        guess =int(input(f'Guess a number between 1 and 10: '))
        if guess < secret_mumber:
            print("Soory guess again. It's too low")
        elif guess > secret_mumber:
            print ("Soory guess again. It,s too high")

    print (f'Congrats! you have guessed the number {secret_mumber} correctly')
guess()