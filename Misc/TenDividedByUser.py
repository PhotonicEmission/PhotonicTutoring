#take user input, 10 divided by user input, and not crash 
try:
    x=10/int(input())
    print(x)
except(ValueError):
    print("you fucked up, try an integer plz")
except(ZeroDivisionError):
    print("zeros won't work, try something with a value < zero")