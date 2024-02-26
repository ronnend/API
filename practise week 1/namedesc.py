def main():
    names = []

   
    while True:
        name = input("Enter a name (press Enter to finish): ")
        if name == "":
            break  
        names.append(name)

    print("Names in the same order:")
    for name in names:
        print(name)

    print("Names in descending order:")
    names.sort(reverse=True)  
    for name in names:
        print(name)

if __name__ == "__main__":
    main()
