def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True
    
def print_primes_up_to(limit):
    print(f"Prime numbers up to {limit}:")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=" ")


limit = int(input("Please enter a number to find prime numbers up to: "))
print_primes_up_to(limit)
