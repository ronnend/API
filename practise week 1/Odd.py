def remove_odd_values(original_list):
    
    manipulated_list = [num for num in original_list if num % 2 == 0]
    return manipulated_list

def main():
    
    values = input("Enter a list of values separated by spaces: ").split()
    values = [int(num) for num in values]  
    manipulated_list = remove_odd_values(values)

    print("Original List:", values)
    print("Manipulated List (without odd values):", manipulated_list)

if __name__ == "__main__":
    main()
