def print_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * i
        print(spaces + stars)

height = 10
print_triangle(height)
