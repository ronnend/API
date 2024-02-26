def sum(a, b):
    return a + b 

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division not possible by 0"
    else:
        return a / b

def calculate(operation, a, b):
    if operation == '+':
        return sum(a, b)
    elif operation == '-':
        return sub(a, b)
    elif operation == '*':
        return multi(a, b)
    elif operation == '/':
        return divide(a, b)
    else:
        return "Invalid operation"

number1 = float(input("Please enter your first number: "))
number2 = float(input("Please enter your second number: "))

operation = input("Please enter the operation (+, -, *, /): ")

result = calculate(operation, number1, number2)
print(f"Result of {number1} {operation} {number2} =", result)

