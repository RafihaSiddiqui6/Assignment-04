def get_last_element(lst):
    """Prints the last element of the provided list."""
    if lst:  # Check if the list is not empty
        print("Last element:", lst[-1])
    else:
        print("List is empty.")

def get_lst():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    lst = []
    while True:
        elem = input("Please enter an element of the list or press Enter to stop: ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == "__main__":
    main()
