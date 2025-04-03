affirmation = '"Nothing can hold me back from achieving greatness."'
def main():
    print("please type the follwoing affirmation: "+ affirmation)
    user_input = input()
    while user_input != affirmation:
        print("You have failed the affirmation.")
       
    #Ask the user to write again
        print("❌ Kindly write the correct affirmation." + affirmation)
        user_input = input()
    print("You have succesfully completed the affirmation🥳.")

main()
        

