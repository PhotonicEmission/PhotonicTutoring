# if (bacon = 5)
# !=


# 10 % 2
# test if divisible by 3
# x = 17
# if(x %3 == 0):

# # write a loop that prints every third number starting at 1
# for x in range (1, 22, 3):
#     print(x)

# print out what version of Python you are using.
# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)

# Write a program that outputs the area and perimeter of a square based on a side length entered by the user.

# Get length from user, calculate area, and calculate perimeter:
def inputLength():
    x = int(input("Enter length to be evaluated: "))
    # print(x)
    return x

length = inputLength()

def calcArea(length):
    x = length**2
    return x

def calcPerimeter(length):
    x = length*4
    return x

# area = calcArea(length)
# perimeter = calcPerimeter(length)

print("Area: " + str( calcArea(length) ))
print("Perimeter: "+str(calcPerimeter(length)))