# This program converts feet to inches. The user enters a number of feet, and the program shows how many inches
# that is. For example, 3 feet is 36 inches.
Inches_In_Foot: int = 12  

def main():
    feet: float = float(input("Enter number of feet: ")) # Ask user for feet
    inches: float = feet *Inches_In_Foot  # Perform the conversion
    print("The equivalent measurement is", inches, "inches!")
    
if __name__ == '__main__':
    main()