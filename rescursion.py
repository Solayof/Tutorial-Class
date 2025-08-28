# 5! = 5*4*3*2*1 = 120
# 4! = 4*3*2*1 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# 1! = 1
# 5! = 5*4! = n * (n-1)!
# 5! = 5*4*3!
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # 5 * 4 * 3 * 2 * 1 = 120
 
 # is_even(10) -> is_odd(9) -> is_even(8) -> is_odd(7) -> is_even(6) -> is_odd(5) -> is_even(4) -> is_odd(3) -> is_even(2) -> is_odd(1) -> is_even(0) -> True
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)


print(is_even(10)) # True
print(is_odd(10))  # False

def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

print(is_prime(2)) # True