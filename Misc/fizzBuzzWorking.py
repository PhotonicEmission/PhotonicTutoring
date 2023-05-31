for val in range (1,101):
    if val % (3*5) == 0:
        print("Fizzbuzz")
    elif val % 3 == 0 :
        print("Fizz")
    elif val % 5 == 0:
        print("Buzz")
    else: print(val)