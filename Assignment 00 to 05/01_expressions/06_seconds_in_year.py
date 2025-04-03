Days_per_year: int = 365
Hours_per_day: int = 24
Minutes_per_hour: int =60
Seconds_per_minute: int =60
 
def main():
    #calculate the number of seconds in a year
    print("There are " + str(Days_per_year * Hours_per_day *Minutes_per_hour *Seconds_per_minute) + " seconds in a year!")

if __name__ == '__main__':
    main()   