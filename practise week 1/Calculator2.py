def sub(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multi(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Division not possible by 0"
        else:
            result /= num
    return result

def calculate(operation, numbers):
    if operation == '+':
        return sum(numbers)
    elif operation == '-':
        return sub(numbers)
    elif operation == '*':
        return multi(numbers)
    elif operation == '/':
        return divide(numbers)
    else:
        return "Invalid operation"

numbers = input("Please enter your numbers separated by commas: ").split(',')
numbers = [float(num) for num in numbers]

operation = input("Please enter the operation (+, -, *, /): ")

result = calculate(operation, numbers)
print("Result:", result)
