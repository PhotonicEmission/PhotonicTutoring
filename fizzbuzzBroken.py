for val in range (1,101):
    if val % 3 == True:
        print("Fizz")
    elif val % 5 == True:
        print("Buzz")
    elif val % (3*5) == True:
        print("Fizzbuzz")
    else: print(val)