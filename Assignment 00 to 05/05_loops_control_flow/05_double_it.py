# User enters a number
curr_value = int(input("Enter a number: "))

# Loop until the value reaches 100 or more
while curr_value < 100:
    curr_value *= 2  # Double the number
    print(curr_value, end=" ")  # Print on the same line
