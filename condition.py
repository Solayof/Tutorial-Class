age =10

if age > 18 and age < 60:
    print("You are an adult.")
elif age >= 60: #else if
    print("You are a senior citizen.")
else:
    print("You are a minor.")


for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")
