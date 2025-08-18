def greet(name):
    print(f"Your name is {name}.")
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def add(*args):
    print(type(args))
    print(f"Arguments received: {args}")
    total = 0
    for number in args:
        total += number
    return total


nums = (1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89)

total = add(*nums)
print(f"The total is {total}.")

def greets(name = "Guest", lastName = "Johnson"):
    print(f"Hello, {name} {lastName}!")


details = {}
greets(**details) # list, dictionary, set, tuple


def calculate_area(width, length = 8):
    area = length * width
    return area

tuple_values = (7, 10)
size = {"lengths": 10, "widths": 7}
result = calculate_area(**size) # result = calculate_area(length=10, width=7)
calculate_area(*tuple_values) # calculate_area(7, 10)
# result = calculate_area(5, 10)

print(f"The area is {result}.")


