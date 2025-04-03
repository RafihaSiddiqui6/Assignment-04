def main():
    Amir : int = 21  # Amir  is 21 years old
    Saim : int = 6 + Amir # Saim is 6 years older than Amir
    Iqra : int = 20 + Saim  # Iqra is 20 years older than Saim, 
    Umer : int= Amir + Iqra  # Umer's age is the combo of Amir's age plus Iqra's age,
    Urwa : int = Iqra  # Urwa is the same age as Iqra

   # Print out all of the ages!
    print("Amir is " + str(Amir))
    print("Saim is " + str(Saim))
    print("Iqra is " + str(Iqra))
    print("Umer is " + str(Umer))
    print("Urwa is " + str(Urwa))


if __name__ == '__main__':
    main()