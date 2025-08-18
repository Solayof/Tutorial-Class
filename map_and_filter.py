
# Map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_sub_by_10 = map(lambda x: x - 10, numbers)
print(list(numbers_sub_by_10))

# Filter
even_numbers = filter(lambda x: x % 3 == 0, numbers)
bool_values = map(lambda x: x % 3 == 0, numbers)
print(list(bool_values))
print(list(even_numbers))

