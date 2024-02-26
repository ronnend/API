def main():
    
    while True:
        try:
            number = int(input("Enter an integer number: "))
            break  
        except ValueError:
            print("Invalid input. Please enter an integer.")


    squares = [i ** 2 for i in range(number + 1)]


    print("Squares from 0 to", number, "are:")
    print(squares)

if __name__ == "__main__":
    main()
