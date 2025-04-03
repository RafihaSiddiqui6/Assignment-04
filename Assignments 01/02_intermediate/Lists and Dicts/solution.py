# Index Game Solution

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

# List Practice Solution

def main():
    # Create a list called `fruit_list` that contains the following fruits:
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    print("List length:", len(fruit_lst))

    # Add 'mango' at the end of the list.
    fruit_lst.append('mango')

    # Print the updated list.
    print("Updated fruit list:")
    for fruit in fruit_lst:
        print(fruit)

if __name__ == '__main__':
    print("Choose a program to run:")
    print("1. Index Game")
    print("2. List Practice")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        index_game()
    elif choice == "2":
        main()
    else:
        print("Invalid choice. Please enter 1 or 2.")
