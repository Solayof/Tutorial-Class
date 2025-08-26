def return_list(n):
    list_ = []
    for i in range(n + 1): # 0 to n
        list_.append(i) # [0, 1, 2, ..., n]
    return list_ # 0(n) time complexity, O(n) space complexity


def countdown(n):
    """A generator that counts down from n to 0."""
    while n >= 0: # O(1) space complexity
        yield n
        n -= 1

for number in return_list(5):
    print(number)