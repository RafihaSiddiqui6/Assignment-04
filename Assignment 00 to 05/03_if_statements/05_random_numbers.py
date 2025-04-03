# A program that Print 10 random numbers in the range 1 to 100.
import random

numbers : int = 10
min_val : int = 1
max_val : int = 100

def main():
   for num in range(numbers):
         print(random.randint(min_val,max_val))
    

if __name__ == '__main__':
    main()