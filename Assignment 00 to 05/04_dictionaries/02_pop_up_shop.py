# A simple fruit shop program that calculates the total cost based on user input for fruit quantities.
def main():
    fruits = {'apple': 2, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 3, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        quantity_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * quantity_bought)
    
    print("Your total is Rs." + str(total_cost))

if __name__ == '__main__':
    main()