def main():
    for i in range(10, 20):  # 10 se 19 tak loop chalega
        if i % 2 == 0:  # Agar even hai
            print(i, "even" ,end="   ")
        else:  # Agar odd hai
            print(i, "odd")

if __name__ == "__main__":
    main()
