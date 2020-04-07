m=range(1, 51)
for n in m:
    if (n % 3 == 0) & (n % 5 == 0):
        print("FizzBuzz")
    elif (n % 3 == 0) & (n % 5 != 0):
        print("Fizz")
    elif (n % 3 != 0) & (n % 5 == 0):
        print("Buzz")
    else:
        print(str(n))
