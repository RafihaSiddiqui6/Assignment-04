# Write a program which prompts the user for a temperature in Fahrenheit 
# (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
def main():
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celcius = (Fahrenheit - 32) * 5.0/9.0
    print(f"Temperature: {Fahrenheit}F = {Celcius}C")

if __name__ == '__main__':
    main()   
