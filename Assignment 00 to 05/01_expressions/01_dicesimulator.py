import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and returns their total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    return die1 + die2

def main():
    die1 = 10  # Local variable in main, unaffected by roll_dice()
    print("die1 in main() starts as:", die1)
    
    # Asking user how many times to roll
    rolls = int(input("Enter number of rolls: "))
    for i in range(rolls):
        print(f"Roll {i+1}: {roll_dice()}")
    
    print("die1 in main() is:", die1)

if __name__ == '__main__':
    main()