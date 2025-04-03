def in_range(n, low, high):
    if n >= low and n <= high:
        return True

    return False

def main():
    num = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    result = in_range(num, low, high)  # Calling the function
    print(f"Is {num} in range [{low}, {high}]? {result}")  # Printing the result

if __name__ == "__main__":
    main()
