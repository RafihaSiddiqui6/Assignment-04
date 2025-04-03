# Roll two dice and print out the results.
import random

# Number of sides on each die to roll
Num_sides: int = 6

def main():
    # Roll die
    die1: int = random.randint(1, Num_sides)
    die2: int = random.randint(1,Num_sides)
    
    # Get their total
    total: int = die1 + die2
    
    # Print out the results
    print("Dice have", Num_sides, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()
