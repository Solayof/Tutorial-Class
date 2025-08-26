# decorators provide a way to modify or enhance functions or methods in Python.
# They are often used for logging, access control, instrumentation, and caching.

def my(func):
    def dan(name):
        print("demo backend training.")
        print(name)
        result = func(name)
        print(f"Thanks for attensing the training. {name}")
        print(func.__name__)
        print(result)
        # return result
    return dan

@my # my(say_hello)
def say_hello(names):
    for name in names:
        print(f"Hello, {name}!")
    return "All names have been greeted."

names = []
for _ in range(3):
    name = input("Enter your name: ")
    names.append(name)


return_val = say_hello(names)

print(return_val)